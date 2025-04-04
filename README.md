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

### **1️⃣ Clonar o Repositório**  
```
git clone https://github.com/gabrielgasperig/link-manager
cd link-manager
```
### 2️⃣ Criar e Ativar um Ambiente Virtual
```
python -m venv venv
```
#### Ativa ambiente no Linux/macOS
```
source venv/bin/activate
```
#### Ativa ambiente no Windows
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

**Acesse a aplicação em:**
🔗 http://127.0.0.1:8000/
