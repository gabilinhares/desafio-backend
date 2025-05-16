# Readme with instructions

# 💳 API de Carteiras Digitais

Projeto de backend desenvolvido com Django REST Framework para gerenciamento de carteiras digitais e transações financeiras, com autenticação via JWT e documentação Swagger.

---

## 🚀 Tecnologias utilizadas

- Python 3.11
- Django 5.2
- Django REST Framework
- Django REST Framework SimpleJWT
- drf-yasg (Swagger)
- SQLite (banco de dados local)

---

## 📂 Funcionalidades

- Cadastro e autenticação de usuários
- Criação e listagem de carteiras digitais
- Registro de transações entre carteiras
- Proteção de rotas com autenticação JWT
- Documentação interativa com Swagger

---

## 🔐 Autenticação JWT

Use os endpoints abaixo para obter e renovar tokens JWT:

```http
POST /token/          → obter token de acesso e refresh  
POST /token/refresh/  → renovar token de acesso
