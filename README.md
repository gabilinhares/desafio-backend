# 💰 Desafio Backend - Carteiras Digitais

Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework, com autenticação via JWT, para gerenciamento de carteiras digitais e transações financeiras entre usuários.

## 🔧 Tecnologias Utilizadas

- Python 3.11
- Django 5.2.1
- Django REST Framework
- Simple JWT (autenticação)
- drf-yasg (Swagger)
- SQLite (padrão para testes locais)
- Git + GitHub

## 🚀 Funcionalidades

- ✅ Cadastro de usuários com senha criptografada
- ✅ Criação e gerenciamento de carteiras por usuário
- ✅ Realização de transações entre carteiras (débito/crédito)
- ✅ Listagem de transações
- ✅ Autenticação via JWT (token/refresh)
- ✅ Documentação Swagger disponível na rota `/swagger/`

## 🔐 Autenticação

A autenticação é feita com JWT. Use as rotas:

- `POST /token/` – para obter o token
- `POST /token/refresh/` – para atualizar o token

Inclua o token no cabeçalho das requisições autenticadas:

```http
Authorization: Bearer <seu_token_aqui>

# Clone o projeto
git clone git@github.com:gabilinhares/desafio-backend.git
cd desafio-backend

# Crie o ambiente virtual
python -m venv venv
source venv/Scripts/activate  # no Windows
# ou
source venv/bin/activate  # no Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Rode o servidor
python manage.py runserver

📄 Documentação
Swagger UI: /swagger/

Redoc: /redoc/

⚙️ Como rodar localmente

# Clone o projeto
git clone git@github.com:gabilinhares/desafio-backend.git
cd desafio-backend

# Crie o ambiente virtual
python -m venv venv
source venv/Scripts/activate  # no Windows
# ou
source venv/bin/activate  # no Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Rode o servidor
python manage.py runserver
Acesse em: http://127.0.0.1:8000

🚀 Deploy no Render
1. Crie o projeto no Render
Vá em New → Web Service

Conecte seu GitHub e selecione o repositório

2. Configure os campos:
Name: desafio-backend

Build Command: pip install -r requirements.txt

Start Command: gunicorn wallet_api.wsgi:application

Environment: Python 3

Runtime: Docker (ou use ambiente padrão)

Environment Variables:

DJANGO_SETTINGS_MODULE=wallet_api.settings

PYTHON_VERSION=3.11

SECRET_KEY=<sua_secret_key>

DEBUG=False

ALLOWED_HOSTS=*

3. Faça o deploy
O Render cuidará do build e do deploy automático a cada git push.

✅ Status do Projeto
🚧 Em desenvolvimento – funcionalidades principais implementadas, testes e deploy em progresso.

✨ Autora
Desenvolvido por Gabi Linhares 💜
github.com/gabilinhares


