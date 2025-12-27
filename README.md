# Patient Register – FastAPI Project

A full-stack **Patient Registration and Management system** built using **FastAPI** for the backend and a lightweight **Python-based frontend**.  
The project supports CRUD operations, sorting, validation, and Docker-based deployment.

<!-- --- -->

## Repository Overview

This repository contains:

- **Backend**: FastAPI REST API
- **Frontend**: Simple UI client
- **Docker setup**: For local development & deployment
- **Sample data**: JSON file for testing

<!-- --- -->

## Tech Stack

- Backend: FastAPI, Python 3.12
- Frontend: Python (Streamlit-based)
- Validation: Pydantic
- Containerization: Docker, Docker Compose

<!-- --- -->

## Project Structure
  ```
  patient-register-fastapi/
  ├── backend/        # FastAPI backend
  ├── frontend/       # Frontend client
  ├── docker/         # Docker compose configuration
  ├── samples/        # Sample patient data
  ├── LICENSE
  └── README.md
  ```

<!-- --- -->

## How to Run

You can run the project in two ways:

### Option 1: Run using Docker (recommended)
  ```bash
  docker compose up --build
  ```

Backend will be available at: [localhost:8000](http://localhost:8000)

<!-- --- -->


### Option 2: Run Backend & Frontend Manually

Refer to:
- `backend/README.md`
- `frontend/README.md`

<!-- --- -->

## API Documentation

FastAPI automatically generates interactive docs:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

<!-- --- -->

## Features

- Create, read, update, delete patients
- Sort patients by height, weight, or BMI
- Request validation using Pydantic
- Modular route-based architecture
- Docker-ready setup

<!-- --- -->

## License

This project is licensed under the MIT License.