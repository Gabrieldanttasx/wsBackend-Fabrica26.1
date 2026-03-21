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

## 🔗 Endpoints / Rotas da Aplicação

A seguir estão as principais rotas disponíveis no sistema:

### Home
- `/` → página inicial do GarageVIN

### Garagens
- `/garagens/` → listagem de garagens
- `/garagens/nova/` → cadastro de nova garagem
- `/garagens/<id>/editar/` → edição de garagem
- `/garagens/<id>/excluir/` → exclusão de garagem

### Veículos
- `/veiculos/` → listagem de veículos
- `/veiculos/novo/` → cadastro de novo veículo
- `/veiculos/<id>/editar/` → edição de veículo
- `/veiculos/<id>/excluir/` → exclusão de veículo

### Consulta por VIN
- `/consultar-vin/` → consulta de informações de veículos via VIN

---

## 🌐 API Utilizada

A aplicação utiliza a API pública:

👉 https://vpic.nhtsa.dot.gov/api/

Exemplo de endpoint utilizado: https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{VIN}?format=json


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
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/garage-vin.git
cd garage-vin
2️⃣ Criar ambiente virtual
python -m venv venv

Ativar no Windows:

venv\Scripts\activate
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Aplicar migrações
python manage.py migrate
5️⃣ Criar superusuário (opcional)
python manage.py createsuperuser
6️⃣ Executar o servidor
python manage.py runserver
7️⃣ Acessar o sistema
http://127.0.0.1:8000/
🧪 Dados para teste

Após iniciar o sistema, cadastre uma garagem para começar a utilizar as funcionalidades.

Para testar a consulta VIN, utilize um exemplo:

1HGCM82633A004352
🎨 Interface

O sistema utiliza Bootstrap 5 para:

Layout moderno

Formulários estilizados

Botões interativos

Responsividade

🧠 Diferenciais do Projeto

Integração com API real de veículos

Preenchimento automático de dados via VIN

Estrutura organizada (padrão Django)

Interface amigável e profissional

Código limpo e bem estruturado

📈 Possíveis Melhorias

Sistema de autenticação (login/logout)

Deploy em produção (Render)

Dashboard com estatísticas

Upload de imagens de veículos

Filtros e busca avançada

👨‍💻 Autor

Desenvolvido por:

Felipe Gabriel