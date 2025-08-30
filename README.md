# Healthcare Backend (Django + DRF + PostgreSQL)

## Overview
RESTful backend for managing Users (JWT), Patients, Doctors, and Patient–Doctor mappings.

## Tech
- Django
- Django REST Framework
- PostgreSQL
- JWT (djangorestframework-simplejwt)
- python-dotenv for configs
- CORS headers (for future frontend)

## Quick Start

```bash
# 1) Create and activate venv
python -m venv venv
# Windows
venv\Scripts\Activate.ps1
# Linux/Mac
# source venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Create .env from example and set DB credentials
cp .env.example .env  # Windows PowerShell: copy .env.example .env

# 4) Run migrations and dev server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## JWT Auth
- Register: `POST /api/auth/register/`
- Login: `POST /api/auth/login/` (fields: username, password) — we use email as username while creating the user.
- Refresh: `POST /api/auth/token/refresh/`

## Patients
- `POST /api/patients/`
- `GET /api/patients/` (only current user's patients)
- `GET /api/patients/<id>/`
- `PUT /api/patients/<id>/`
- `DELETE /api/patients/<id>/`

## Doctors
- `POST /api/doctors/`
- `GET /api/doctors/`
- `GET /api/doctors/<id>/`
- `PUT /api/doctors/<id>/`
- `DELETE /api/doctors/<id>/`

## Mappings
- `POST /api/mappings/` (assign doctor to patient; only for your own patients)
- `GET /api/mappings/`
- `GET /api/mappings/patient/<patient_id>/`
- `DELETE /api/mappings/<id>/`

## Notes
- Keep `.env` out of version control.
- For production, set `DEBUG=False` and configure proper `ALLOWED_HOSTS`.
