# 🚗 GarageVIN

Sistema web desenvolvido em **Django** para gerenciamento de garagens e veículos, com integração a uma API pública para consulta de dados reais de veículos através do **VIN (Vehicle Identification Number)**.

---

## 📌 Sobre o Projeto

O **GarageVIN** foi criado com o objetivo de facilitar o controle de veículos e garagens, permitindo ao usuário:

- Cadastrar e gerenciar garagens
- Cadastrar e gerenciar veículos
- Consultar dados reais de veículos via API externa
- Preencher automaticamente informações a partir do VIN

O sistema possui uma interface moderna utilizando **Bootstrap**, proporcionando uma melhor experiência ao usuário.

---

## 🚀 Funcionalidades

### 🔹 Garagens
- Criar garagem
- Listar garagens
- Editar garagem
- Excluir garagem

### 🔹 Veículos
- Criar veículo
- Listar veículos
- Editar veículo
- Excluir veículo

### 🔹 Integração com API
- Consulta de veículo por VIN
- Retorno de dados reais:
  - Marca
  - Modelo
  - Ano
  - Fabricante
  - Tipo de veículo

### 🔹 Automação
- Preenchimento automático do formulário de veículo a partir da consulta VIN

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Django 5.x
- SQLite (banco de dados)
- Bootstrap 5 (interface)
- API pública vPIC (NHTSA)

---

## 🌐 API Utilizada

A aplicação utiliza a API pública:

👉 https://vpic.nhtsa.dot.gov/api/

Responsável por fornecer dados de veículos com base no VIN.

---

## 📂 Estrutura do Projeto

```bash
garage_vin/
│
├── config/              # Configurações do projeto Django
├── garagem/             # Aplicação principal
│   ├── models.py        # Modelos (Garagem e Veículo)
│   ├── views.py         # Lógica da aplicação
│   ├── forms.py         # Formulários com Bootstrap
│   ├── urls.py          # Rotas da aplicação
│   ├── services.py      # Integração com API VIN
│   └── templates/
│       └── garagem/
│           ├── base.html
│           ├── home.html
│           ├── consulta_vin.html
│           ├── garagens/
│           └── veiculos/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
⚙️ Como Executar o Projeto
 Clonar o repositório
git clone https://github.com/seu-usuario/garage-vin.git
cd garage-vin
 Criar ambiente virtual
python -m venv venv

Ativar no Windows:

venv\Scripts\activate
 Instalar dependências
pip install -r requirements.txt
Aplicar migrações
python manage.py migrate
 Criar superusuário (opcional)
python manage.py createsuperuser
 Executar o servidor
python manage.py runserver
 Acessar o sistema
http://127.0.0.1:8000/