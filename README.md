events_backend

FastAPI backend ⚡ for event management — built with SQLAlchemy, Alembic, JWT auth, Pydantic models, and modular routing.

About

This is a backend REST API for managing events with secure authentication, database migrations, and clean architecture. Built using FastAPI and major Python tooling for scalable APIs.

🚀 Tech Stack

FastAPI – high‑perf Python web framework
SQLAlchemy – ORM for database modeling
Alembic – migration tool for schema management
Pydantic – request/response validation
JWT – JSON Web Token auth for secure access
APIRouter – modular route organization

🔑 Key Features

Register & login with JWT authentication
Protected routes with token verification
Structured routers for separate modules
SQLAlchemy models + Pydantic schemas
Alembic migrations for safe database evolution

🛠 Setup & Installation

Clone the repo:

git clone https://github.com/adhi896/events_backend.git
cd events_backend

Create virtual env & install deps:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
📦 Env Variables

Create a .env in the root:

DATABASE_URL=postgresql://user:pass@localhost/dbname
SECRET_KEY=some_super_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

Adjust to your setup (PostgreSQL/MySQL/SQLite).

🧠 Database Migrations

Initialize (if not done):

alembic init alembic

Run migrations:

alembic upgrade head
🚀 Running the App
uvicorn main:app --reload

Your controllers will be live at http://127.0.0.1:8000

🔗 Example Routes

POST /auth/register – create user

POST /auth/login – get JWT token

GET /events – list all events

POST /events/ – create event (auth needed)

Protected routes require the header:

Authorization: Bearer <your-jwt-token>
💡 Testing

Use Postman, Hoppscotch, or Insomnia to call endpoints and include tokens appropriately.

📁 Project Structure (example)
app/
  ├── core/          # configs, settings
  ├── db/            # models & migrations
  ├── routers/       # api routers
  ├── schemas/       # pydantic schemas
  ├── main.py
alembic.ini
.env
