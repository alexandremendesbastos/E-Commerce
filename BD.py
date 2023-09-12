import pymysql
from flask import Flask, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Função para criar o banco de dados e tabelas, incluindo o usuário admin
def criar_banco_de_dados():
    try:
        connection = pymysql.connect(
            host='seu_host_mysql',
            user='seu_usuario_mysql',
            password='sua_senha_mysql'
        )

        with connection.cursor() as cursor:
            # Cria o banco de dados se não existir
            cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce")

            # Seleciona o banco de dados recém-criado
            cursor.execute("USE ecommerce")

            # Cria a tabela produtos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome_do_produto VARCHAR(255) NOT NULL,
                    preco DECIMAL(10, 2) NOT NULL,
                    link_da_imagem VARCHAR(255) NOT NULL,
                    link_do_produto VARCHAR(255) NOT NULL
                )
            """)

            # Cria a tabela usuario (se necessário)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    email VARCHAR(255) NOT NULL,
                    senha VARCHAR(255) NOT NULL,
                    tipo_usuario ENUM('admin', 'comum') NOT NULL
                )
            """)

            # Insere o usuário admin inicial
            cursor.execute("""
                INSERT INTO usuario (email, senha, tipo_usuario) VALUES ('admin', 'admin', 'admin')
            """)

        connection.commit()
        flash('Banco de dados criado com sucesso e usuário admin adicionado.', 'success')

    except Exception as e:
        flash('Erro ao criar o banco de dados: ' + str(e), 'error')

    finally:
        connection.close()

# Rota para criar o banco de dados e o usuário admin
@app.route('/criar_banco_de_dados', methods=['GET'])
def criar_db():
    criar_banco_de_dados()
    return 'Banco de dados criado com sucesso e usuário admin adicionado!'

if __name__ == '__main__':
    app.run(debug=True)
