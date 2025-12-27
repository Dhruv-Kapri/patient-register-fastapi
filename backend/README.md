# Backend – FastAPI Patient API

This folder contains the **FastAPI backend** responsible for handling all patient-related operations.

<!-- --- -->

## Responsibilities

- Expose REST APIs for patient management
- Validate input using Pydantic schemas
- Handle sorting and filtering logic
- Serve OpenAPI documentation

<!-- --- -->

## Backend Structure

  ```
  backend/
  ├── app/
  │   ├── main.py          # FastAPI app entry point
  │   ├── routes/          # API route definitions
  │   ├── schemas/         # Pydantic models
  │   └── utils/           # Helper & data utilities
  ├── Dockerfile
  ├── .dockerignore
  ├── requirements.txt
  └── README.md
  ```

<!-- --- -->

## Running Backend Locally

### 1. Create virtual environment

  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### 2. Install dependencies

  ```bash
  pip install -r requirements.txt
  ```

### 3. Start FastAPI server

  ```bash
  uvicorn app.main:app --reload
  ```

Server will start at: [localhost:8000](http://localhost:8000)

<!-- --- -->

## API Documentation

Once the server is running:

- Swagger UI: [localhost:8000/docs](http://localhost:8000/docs)
- OpenAPI JSON: [localhost:8000/openapi.json](http://localhost:8000/openapi.json)

<!-- --- -->

## Available API Routes

### General
- `GET /` – Health / hello route
- `GET /about/` – About the API

### Patient APIs
- `GET /view/` – View all patients
- `GET /patient/{patient_id}` – Get patient by ID
- `POST /create/` – Create a new patient
- `PUT /edit/{patient_id}` – Update patient
- `DELETE /delete/{patient_id}` – Delete patient
- `GET /sort/` – Sort patients

<!-- --- -->

## Data & Schemas

- Patient data schema defined in: `app/schemas/patient_schema.py`
- Sample patient data available in: `samples/patients.json`

<!-- --- -->

## Notes

- No database is used; data is managed via in-memory / JSON utilities
- Designed for learning and demos