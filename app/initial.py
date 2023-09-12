from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Classe Produto para representar produtos
class Produto:
    def __init__(self, id, nome, preco, link_da_imagem, link_do_produto):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.link_da_imagem = link_da_imagem
        self.link_do_produto = link_do_produto

    def salvar_no_banco(self):
        try:
            connection = pymysql.connect(
                host='seu_host_mysql',
                user='seu_usuario_mysql',
                password='sua_senha_mysql',
                database='nome_do_banco_de_dados'
            )

            with connection.cursor() as cursor:
                # Verificar se o ID já existe no banco de dados
                cursor.execute("SELECT id FROM produtos WHERE id=%s", (self.id,))
                resultado = cursor.fetchone()

                if resultado:
                    return "ID já existe no banco de dados. Inserção não realizada."

                # Inserir o novo produto se o ID não existir
                sql = "INSERT INTO produtos (id, nome_do_produto, preco, link_da_imagem, link_do_produto) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (self.id, self.nome, self.preco, self.link_da_imagem, self.link_do_produto))
                connection.commit()

            return "Produto inserido com sucesso."

        except Exception as e:
            return "Erro: " + str(e)
        finally:
            connection.close()

# Rota para listar produtos
@app.route('/')
def listar_produtos():
    connection = pymysql.connect(
        host='seu_host_mysql',
        user='seu_usuario_mysql',
        password='sua_senha_mysql',
        database='nome_do_banco_de_dados'
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('initial.html', produtos=produtos)

# Rota para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        try:
            connection = pymysql.connect(
                host='seu_host_mysql',
                user='seu_usuario_mysql',
                password='sua_senha_mysql',
                database='nome_do_banco_de_dados'
            )

            senha_adm_confere = connection.cursor()
            senha_adm_confere.execute('SELECT * FROM usuario WHERE senha = %s AND email = %s AND tipo_usuario = %s',
                                      (senha, email, 'admin'))
            resultado_adm = senha_adm_confere.fetchone()

            senha_user_simples = connection.cursor()
            senha_user_simples.execute('SELECT * FROM usuario WHERE senha = %s AND email = %s AND tipo_usuario = %s',
                                       (senha, email, 'comum'))
            resultado_user = senha_user_simples.fetchone()

            if resultado_adm:
                return redirect(url_for('insert'))

            elif resultado_user:
                return redirect(url_for('listar_produtos'))

            else:
                flash('Credenciais inválidas. Tente novamente.', 'error')

        except Exception as e:
            flash('Erro ao processar o login. Tente novamente mais tarde.', 'error')

    return render_template('login.html')

# Rota para inserir produtos
@app.route('/inserir', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        id = request.form['id']
        nome = request.form['nome']
        preco = request.form['preco']
        link_da_imagem = request.form['link_da_imagem']
        link_do_produto = request.form['link_do_produto']

        novo_produto = Produto(id, nome, preco, link_da_imagem, link_do_produto)
        resultado = novo_produto.salvar_no_banco()

        return redirect(url_for('insert'))

    return render_template('add.html', titulo='Inserir')

if __name__ == '__main__':
    app.run(debug=True)
