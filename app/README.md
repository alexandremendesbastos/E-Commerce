# Documentação da Aplicação de E-Commerce:

Esta é a documentação básica para a aplicação de e-commerce, que permite adicionar produtos ao banco de dados e listar produtos existentes.

## Iniciando a Aplicação
Siga as etapas abaixo para iniciar a aplicação em seu ambiente local:

### Clone o Repositório
Comece clonando este repositório para o seu ambiente local. Use o comando abaixo no seu terminal:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Substitua `seu-usuario` e `nome-do-repositorio` pelo seu nome de usuário e nome do repositório no GitHub.

### Configuração do Ambiente Virtual (Opcional)
É recomendável criar um ambiente virtual Python para isolar as dependências da aplicação. Use os seguintes comandos:

```bash
cd nome-do-repositorio
python -m venv venv
source venv/bin/activate  # No Windows, use "venv\Scripts\activate"
```

### Instale as Dependências
Instale as dependências da aplicação usando o pip:

```bash
pip install -r requirements.txt
```

### Configuração do Banco de Dados
Você deve ter um servidor MySQL em execução. Certifique-se de configurar as informações de conexão com o banco de dados no arquivo `app.py`. Você deve modificar as seguintes linhas:

```python
connection = pymysql.connect(
    host='127.0.0.1',  # Host do seu servidor MySQL
    user='root',       # Seu usuário MySQL
    password='sua-senha',   # Sua senha MySQL
    database='ecommerce'   # Nome do banco de dados
)
```

Substitua `127.0.0.1`, `root`, `sua-senha` e `ecommerce` pelas suas próprias configurações.

### Execute a Aplicação
Agora, você pode iniciar a aplicação com o seguinte comando:

```bash
python app.py
```

A aplicação será executada localmente e estará acessível em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Usuário Admin Inicial
A aplicação inclui um usuário admin inicial com as seguintes credenciais:

- Email: `admin`
- Senha: `admin`

Este usuário admin possui privilégios administrativos e pode ser usado para acessar as funcionalidades administrativas da aplicação.

## Operações Básicas
Aqui estão as operações básicas que você pode realizar na aplicação:

### 1. Adicionar um Novo Produto
Para adicionar um novo produto ao banco de dados, siga estas etapas:

1. Acesse a página inicial da aplicação em [http://127.0.0.1:5000/](http://127.0.0.1:5000/) no seu navegador.

2. Clique na opção "Adicionar Produto" no menu de navegação.

3. Preencha o formulário com as informações do produto, incluindo ID, Nome, Preço, Link da Imagem e Link do Produto.

4. Clique no botão "Adicionar Produto" para salvar o novo produto no banco de dados.

5. Você receberá uma mensagem de confirmação informando que o produto foi inserido com sucesso.

### 2. Listar Produtos
Para listar todos os produtos existentes no banco de dados, siga estas etapas:

1. Acesse a página inicial da aplicação em [http://127.0.0.1:5000/](http://127.0.0.1:5000/) no seu navegador.

2. A lista de produtos será exibida na página inicial.

3. Você pode ver os detalhes de cada produto, incluindo nome, preço, imagem e link do produto.

Isso conclui a documentação básica da aplicação de e-commerce. Você agora pode iniciar a aplicação, adicionar produtos e listar produtos existentes no banco de dados. Certifique-se de personalizar esta documentação de acordo com as necessidades do seu projeto e das informações específicas do seu banco de dados.