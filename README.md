GoIP - South African Graduate Opportunity Tracker API

A backend REST API built with FastAPI and PostgreSQL for tracking applications to South African graduate programmes, internships, and learnerships.

**Live API Docs:** https://goip-production-3e8c.up.railway.app/docs

## Tech Stack

- **Framework:** FastAPI (Python 3.11)
- **Database:** PostgreSQL & SQLAlchemy (ORM)
- **Authentication:** JWT (JSON Web Tokens) & bcrypt
- **Containerization:** Docker & Docker Compose
- **Deployment:** Railway

## Features

- Secure user registration and login with JWT
- Full CRUD operations for opportunities
- Advanced filtering by type, company, and deadline
- Application status tracking (Applied, Assessment, Interview, Offer, Rejected)

## Setup

1. Clone the repository: git clone https://github.com/denzel-builds/goip.git
cd goip
2. Create a `.env` file in the root directory:
```env
   DATABASE_URL=postgresql://username:password@localhost:5432/goip_db
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
```
3. Build and run: docker-compose up --build
4. API available at `http://localhost:8000/docs`
