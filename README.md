markdown
Copy code
# E-Commerce Web App

Este é um projeto de aplicativo da web de e-commerce construído com Flask. Antes de iniciar o projeto, siga as instruções abaixo para configurar o banco de dados necessário.

## Configurando o Banco de Dados

Antes de iniciar o aplicativo, é necessário configurar o banco de dados que armazenará informações sobre produtos e usuários. Para fazer isso, siga estas etapas:

1. Certifique-se de ter o MySQL instalado em seu sistema. Se você ainda não o tiver instalado, você pode baixá-lo [aqui](https://dev.mysql.com/downloads/installer/).

2. Abra o terminal e navegue até a pasta raiz do projeto.

3. Execute o seguinte comando para criar o banco de dados e as tabelas necessárias:
python BD.py

Isso criará o banco de dados chamado `ecommerce` e as tabelas `produtos` e `usuario`. Certifique-se de que as configurações do MySQL em `BD.py` estejam corretas (host, usuário e senha).

4. Após a execução bem-sucedida do script `BD.py`, o banco de dados estará pronto para uso pelo aplicativo.

## Iniciando o Aplicativo

Agora que o banco de dados está configurado, você pode iniciar o aplicativo Flask. Certifique-se de ter todas as dependências instaladas (você pode instalá-las com `pip install -r requirements.txt`).

Para iniciar o aplicativo, execute o seguinte comando na pasta raiz do projeto:

python app.py

less
Copy code

O aplicativo estará disponível em `http://localhost:5000/` em seu navegador. Você pode acessar a interface da web para adicionar produtos, listar produtos e fazer login como administrador ou usuário comum.

## Contato

Se você tiver alguma dúvida ou encontrar algum problema, sinta-se à vontade para entrar em contato conosco no e-mail alexandrem.bastos2526@gmail.com.

Divirta-se usando o aplicativo!

