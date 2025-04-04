# 📌 Link Manager - Django App

![Django](https://img.shields.io/badge/Django-4.0%2B-success)  
Um aplicativo web desenvolvido com Django para gerenciar links.

---
## ✨ Funcionalidades

- Adicionar, editar e excluir links
- Compartilhar links por e-mail
- Interface responsiva
- Banco de dados integrado

---

## 🛠 Tecnologias Utilizadas  
- **Python** 🐍  
- **Django** 🎯  
- **Bootstrap** 🎨  
- **SQLite** (banco de dados padrão)  
- **SMTP** (para envio de e-mails)  

---

## 🔧 Como Rodar o Projeto Localmente  

### 1️⃣ Obter o Projeto

**Você pode obter o código-fonte de duas formas:**

#### 🔁 Opção 1: Clonando com Git
```
git clone https://github.com/gabrielgasperig/link-manager
cd link-manager
```
#### 📦 Opção 2: Baixando o ZIP
- Acesse o repositório: https://github.com/gabrielgasperig/link-manager

- Clique no botão verde "Code" e selecione "Download ZIP"

- Extraia o arquivo em seu computador

- Acesse a pasta extraída com seu terminal:
```
cd link-manager-main  # ou o nome da pasta descompactada
```
### 2️⃣ Criar e Ativar um Ambiente Virtual
```
python -m venv venv
```
#### 🐧 Ativa ambiente no Linux/macOS
```
source venv/bin/activate
```
#### 🪟 Ativa ambiente no Windows
```
venv\Scripts\activate  
```
### 3️⃣ Instalar as Dependências
```
pip install -r requirements.txt
```
### 4️⃣ Criar o Banco de Dados e Aplicar Migrações
```
python manage.py makemigrations
python manage.py migrate  
```
### 5️⃣ Criar um Superusuário (Opcional)
```
python manage.py createsuperuser
```
### 6️⃣ Rodar o Servidor
```
python manage.py runserver
```
---

## 🌍 Acesse o App Localmente

🔗 http://127.0.0.1:8000/

---

## 🧪 Testando como PWA

-  Acesse a aplicação pelo navegador (Chrome, Edge ou Vivaldi).

- Você verá um botão "Instalar App" no canto superior direito do cabeçalho.

- Ou instale via navegador: Menu → "Instalar Link Manager" ou "Criar atalho".
