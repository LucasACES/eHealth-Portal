# eHealth Portal

A clinical management system for organizing patients, reports, and appointments.

---
![Python](https://img.shields.io/badge/python-3.10-blue)
![Django](https://img.shields.io/badge/django-5.1.7-success)
![PostgreSQL](https://img.shields.io/badge/database-postgresql-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## 🌐 Technologies Used

- **Python 3.10**
- **Django 5.1.7**
- **PostgreSQL**
- **Bootstrap 5.3**
- **Docker (optional)**

---

## 🧰 Features

### 🙋 Access Profiles

- **Operational**: restricted access to basic functions
- **Supervisor**: full access (excluding Django admin)

### 🗂️ Modules

- **Patients**: register, list, and attach reports
- **Reports**:
  - Upload signed PDF files
  - Generate access code
  - Integration with ITI validator
- **Appointments**: (in progress)
- **Dashboard**:
  - Record counters
  - Recent reports list

---

## ⚙️ Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/youruser/ehealth-portal.git
cd ehealth-portal
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL database

Create your DB and user, then edit `settings.py`:

```python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'ehealth_db',
    'USER': 'ehealth_user',
    'PASSWORD': 'your_password',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}
```

### 5. Apply migrations and create superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

---

## 🐳 Docker Instructions

### 1. Build the Docker image

```bash
sudo docker build -t ehealth_portal .
```

### 2. Run the container

```bash
sudo docker run -p 8000:8000 ehealth_portal
```

> Make sure to configure the environment variables for PostgreSQL connection inside the container or via a `.env` file.

---

## 🧭 Navigation & Layout

### Sidebar menu includes:

- Dashboard
- Patients
- New Patient
- Reports
- Users (supervisor only)

### Visual Features:

- Collapsible sidebar
- Bootstrap styling
- Active item highlighting
- Custom login page
- Fun logout message screen

---

## 📦 QR Code & ITI Validator Integration

- Access via: `/laudo/?_secretCode=YOURCODE&_format=application/validador-iti+json`
- Returns JSON with file link

---

## 🚧 Roadmap

- Edit patient screen
- Search and filters by name, date, CPF
- Report generation in PDF/Excel
- Granular permission control

---

## 📄 License

This project is licensed under the MIT License.

---

## ❤️ Developed by Mr. Lucas

---
