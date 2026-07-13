# User Profile Management API

A resilient **User Profile Management API** built with **FastAPI**, **PostgreSQL**, and **Docker**. The application follows clean architecture principles using the **Repository Pattern**, **Unit of Work Pattern**, **Service Layer**, and integrates with an external mock enrichment service featuring **Retry** and **Circuit Breaker** mechanisms.

---

# Features

- User CRUD Operations
- PostgreSQL Database
- FastAPI REST API
- SQLAlchemy ORM
- Repository Pattern
- Unit of Work Pattern
- Service Layer
- Docker & Docker Compose
- External Mock Enrichment Service
- Retry Mechanism (Tenacity)
- Circuit Breaker Pattern
- Swagger API Documentation
- Unit Testing
- Integration Testing

---

# Tech Stack

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- Flask (Mock Service)
- Requests
- Tenacity
- Pytest

---

# Project Structure

```
user-profile-management-api/
│
├── initdb/
├── mock-service/
├── screenshots/
├── src/
│   ├── api/
│   ├── core/
│   ├── external/
│   ├── middleware/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── unit_of_work/
│   ├── utils/
│   └── main.py
│
├── tests/
│   ├── integration/
│   └── unit/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── pytest.ini
├── .env
└── README.md
```

---

# Architecture

```
                Client
                   │
                   ▼
             FastAPI Routes
                   │
                   ▼
            Service Layer
                   │
                   ▼
          Unit of Work Pattern
                   │
                   ▼
         Repository Pattern
                   │
                   ▼
              PostgreSQL

                   │
                   ▼
        External Enrichment Client
                   │
          Retry + Circuit Breaker
                   │
                   ▼
         Flask Mock Service
```

---

# API Endpoints

## Root

```
GET /
```

Returns application status.

---

## Health

```
GET /health
```

Returns health status.

---

## Create User

```
POST /api/users
```

---

## Get User

```
GET /api/users/{user_id}
```

---

## Get All Users

```
GET /api/users
```

---

## Update User

```
PUT /api/users/{user_id}
```

---

## Delete User

```
DELETE /api/users/{user_id}
```

---

## Get Enriched User

```
GET /api/users/{user_id}/enriched
```

Returns user information along with enrichment data from the external mock service.

---

# Environment Variables

```
PORT=8000

DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=user_profiles_db

EXTERNAL_SERVICE_URL=http://mock-service:8081/enrich

EXTERNAL_SERVICE_TIMEOUT_MS=1500

CIRCUIT_BREAKER_FAILURE_THRESHOLD=5
CIRCUIT_BREAKER_RESET_TIMEOUT_MS=30000
CIRCUIT_BREAKER_HALF_OPEN_SUCCESS_THRESHOLD=2

RETRY_MAX_ATTEMPTS=3
RETRY_BASE_DELAY_MS=100

MOCK_SERVICE_FAILURE_RATE=0.4
MOCK_SERVICE_DELAY_MS=200
```

> **Note**
>
> When running the application locally (outside Docker), update:
>
> ```
> DB_HOST=localhost
> EXTERNAL_SERVICE_URL=http://localhost:8081/enrich
> ```
>
> For Docker Compose, keep the service names (`db` and `mock-service`) as shown above.

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/Swetha-svvv/user-profile-management-api.git

cd user-profile-management-api
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Using Docker

```bash
docker compose up -d --build
```

---

## Verify Running Containers

```bash
docker ps
```

---

## Access Swagger

```
http://localhost:8000/docs
```

---

## Health Endpoint

```
http://localhost:8000/health
```

---

# Mock Service

Health

```
http://localhost:8081/health
```

Enrichment

```
http://localhost:8081/enrich?userId=user-1
```

---

# Running Tests

## Unit Tests

```bash
pytest tests/unit -v
```

Expected Result

```
5 passed
```

---

## Integration Tests

```bash
pytest tests/integration -v
```

Expected Result

```
3 passed
```

---

# Sample Enriched Response

```json
{
  "id": "user-1",
  "name": "Alice Wonderland",
  "email": "alice@example.com",
  "registration_date": "2026-07-12T17:44:38.691617",
  "recentActivity": [
    "Login",
    "Purchase",
    "Profile Update"
  ],
  "loyaltyScore": 49,
  "enrichedDataStatus": "available"
}
```

---

# Design Patterns Used

- Repository Pattern
- Unit of Work Pattern
- Service Layer Pattern
- Dependency Injection
- Retry Pattern
- Circuit Breaker Pattern

---

# Testing Summary

| Test Type | Status |
|-----------|--------|
| Unit Tests | ✅ Passed |
| Integration Tests | ✅ Passed |
| CRUD APIs | ✅ Passed |
| Docker Deployment | ✅ Passed |
| Swagger Testing | ✅ Passed |
| External Service Integration | ✅ Passed |

---

# Screenshots

The `screenshots/` folder contains:

- Swagger UI
- CRUD Operations
- Health Endpoint
- Docker Containers
- PostgreSQL Database
- Mock Service
- Enriched User API
- Unit Tests
- Integration Tests

---

# Author

**Siripurapu Veera Venkata Vishnu Swetha**

Computer Science & Engineering

Aditya College of Engineering and Technology