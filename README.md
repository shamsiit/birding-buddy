# Birding Buddy Backend - README

**Birding Buddy** is a backend system for a birdwatching app that allows users to log bird sightings, identify species, share locations (hotspots), and contribute to community-driven ornithological data. Built using **Django**, **Django REST Framework**, and **SQLite**, it also supports JWT authentication and API documentation with Swagger.

---

## 📘 Project Background
Birding Buddy was inspired by the global citizen science movement for tracking bird biodiversity. Similar to eBird, it allows:
- **Bird sighting logs** with location and optional photos
- **User accounts** and profiles
- **Community hotspots** to find birding locations
- **API-first** architecture for frontend/mobile clients
- **Swagger UI** for interactive documentation

---

## ⚙️ Tech Stack
- Python 3.12+
- Django 5.x+
- Django REST Framework (DRF)
- SQLite (development)
- JWT Authentication (via SimpleJWT)
- Swagger documentation (via drf-yasg)

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/birding-buddy.git
cd birding-buddy/birding_buddy_backend
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, manually install:
```bash
pip install django djangorestframework djangorestframework-simplejwt drf-yasg Pillow
```

### 4. Apply migrations and create a superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the development server
```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users/register/` | POST | Register a new user |
| `/api/auth/token/` | POST | Obtain JWT access/refresh tokens |
| `/api/auth/token/refresh/` | POST | Refresh JWT access token |
| `/api/users/<id>/` | GET, PUT | Retrieve or update user profile |
| `/api/sightings/` | GET, POST | List or create bird sightings |
| `/api/sightings/<id>/` | GET, PUT, DELETE | View/update/delete specific sighting |
| `/api/hotspots/` | GET, POST | List or create hotspots |
| `/api/hotspots/<id>/` | GET, PUT, DELETE | View/update/delete hotspot |

---
### 3. Run Tests
```bash
manage.py test users sightings hotspots
```


## 🧪 Testing the API (with bash)
Save the script below as `test_birding_buddy_api.sh`:

```bash
#!/bin/bash
BASE_URL="http://127.0.0.1:8000"
USERNAME="testuser"
EMAIL="testuser@example.com"
PASSWORD="Testpass123"

curl -X POST "$BASE_URL/api/users/register/" -H "Content-Type: application/json" -d "{"username": "$USERNAME", "email": "$EMAIL", "password": "$PASSWORD"}"

TOKENS=$(curl -s -X POST "$BASE_URL/api/auth/token/" -H "Content-Type: application/json" -d "{"username": "$USERNAME", "password": "$PASSWORD"}")
ACCESS_TOKEN=$(echo "$TOKENS" | python3 -c "import sys, json; print(json.load(sys.stdin)['access'])")

curl -X POST "$BASE_URL/api/sightings/" -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -d '{"species_name": "House Sparrow", "count": 5, "behavior_notes": "Feeding", "location_lat": 23.81, "location_long": 90.41}'

curl -X GET "$BASE_URL/api/sightings/" -H "Authorization: Bearer $ACCESS_TOKEN"
curl -X POST "$BASE_URL/api/hotspots/" -H "Content-Type: application/json" -d '{"name": "Lalbagh", "description": "Great for urban birds", "location_lat": 23.71, "location_long": 90.38}'
curl -X GET "$BASE_URL/api/hotspots/"
curl -X GET "$BASE_URL/api/users/1/" -H "Authorization: Bearer $ACCESS_TOKEN"
```

Make it executable:
```bash
chmod +x test_birding_buddy_api.sh
./test_birding_buddy_api.sh
```

---

## 📘 API Documentation
Once the server is running, access interactive docs at:
- [Swagger UI](http://127.0.0.1:8000/swagger/)
- [ReDoc UI](http://127.0.0.1:8000/redoc/)

---

## 📦 Deployment (Coming Soon)
Future versions will include:
- PostgreSQL configuration for production
- Docker & Docker Compose setup
- Deployment on platforms like Render or Railway

---

## 🐞 Issues
Please report bugs or feature requests via GitHub Issues.

---

## 👨‍💻 Maintainers
Made by Shahriar Mohammad (and contributors). Contributions welcome!
