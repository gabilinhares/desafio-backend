# 💰 Desafio Backend - Carteiras Digitais

Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework, com autenticação via JWT, para gerenciamento de carteiras digitais e transações financeiras entre usuários.

---

## 🔧 Tecnologias Utilizadas

- Python 3.11  
- Django 5.2.1  
- Django REST Framework  
- Simple JWT (autenticação)  
- drf-yasg (Swagger UI)  
- PostgreSQL (produção) / SQLite (teste local)  
- Git + GitHub  

---

## 🚀 Funcionalidades

- ✅ Cadastro de usuários com senha criptografada  
- ✅ Criação e gerenciamento de carteiras por usuário  
- ✅ Realização de transações entre carteiras (débito/crédito)  
- ✅ Listagem de transações  
- ✅ Autenticação via JWT (token/refresh) com login por email  
- ✅ Documentação Swagger disponível na rota `/swagger/`  

---

## ⚙️ Como rodar localmente

```bash
# Clone o projeto
git clone git@github.com:gabilinhares/desafio-backend.git
cd desafio-backend

# Crie e ative o ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Rode o servidor
python manage.py runserver

Acesse em: http://127.0.0.1:8000

Autenticação via JWT com login por email
A API utiliza autenticação JWT e permite login usando email e senha, com emissão de tokens de acesso e refresh.

Endpoints para autenticação
POST /api/token/
Solicitação para obter tokens JWT. Envie JSON no corpo com email e senha:

{
  "email": "usuario@example.com",
  "password": "sua_senha"
}

POST /api/token/refresh/
Atualiza o token de acesso enviando o token de refresh:

{
  "refresh": "seu_token_refresh"
}

Usando o token nas requisições autenticadas
Inclua o token JWT no cabeçalho Authorization:

Authorization: Bearer <seu_token_aqui>

 Documentação da API
Swagger UI: /swagger/

Redoc: /redoc/

🚀 Deploy no Render
Crie o Web Service no Render acessando New → Web Service

Conecte seu repositório GitHub e selecione o repositório do projeto

Configure os campos:

Name: desafio-backend

Build Command: pip install -r requirements.txt

Start Command: gunicorn wallet_api.wsgi:application

Environment: Python 3

Runtime: Docker (ou ambiente padrão)

Configure as variáveis de ambiente no painel do Render:
DJANGO_SETTINGS_MODULE=wallet_api.settings
PYTHON_VERSION=3.11
SECRET_KEY=<sua_secret_key>
DEBUG=False
ALLOWED_HOSTS=*
DATABASE_URL=<sua_database_url>


Faça o deploy. O Render cuidará do build e deploy automático a cada push no GitHub.

✅ Status do Projeto
🚧 Em desenvolvimento – funcionalidades principais implementadas, testes e deploy em progresso.

✨ Autora
Desenvolvido por Gabi Linhares 💜
github.com/gabilinhares
