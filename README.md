# Moto Log

A backend API for tracking motorcycle maintenance. Log service history, costs, and repair notes for your bikes. Built with FastAPI, SQLAlchemy, and JWT auth. Started this after realizing I had no actual record of what's been done on my own Duke 250.

## Features

- Register and log in with JWT auth
- Passwords hashed with bcrypt
- Add multiple vehicles per user
- Log service records under each vehicle (what was done, cost, date)
- You only ever see your own vehicles and service logs

## Built with

- FastAPI
- SQLAlchemy + SQLite
- Pydantic
- python-jose for JWT
- passlib + bcrypt for hashing

## Running it locally

Clone it:
git clone https://github.com/risky-lemonade/Moto-Service-Log.git
cd Moto-Service-Log

Set up a virtual environment and install dependencies:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Add a .env file:
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

Run it:
uvicorn main:app --reload

Then open http://127.0.0.1:8000/docs to try it out.

## Endpoints

**Auth**
- POST /register
- POST /login

**Vehicles**
- POST /vehicles
- GET /vehicles
- GET /vehicles/{vehicle_id}
- DELETE /vehicles/{vehicle_id}

**Service logs** (nested under a vehicle)
- POST /vehicles/{vehicle_id}/services
- GET /vehicles/{vehicle_id}/services
