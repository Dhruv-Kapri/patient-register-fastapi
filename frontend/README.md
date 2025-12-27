# Frontend – Patient Registry UI

This folder contains the **frontend client** for the Patient Register project.
The frontend is built using **Streamlit** and communicates with the FastAPI backend via HTTP APIs.

The goal of this frontend is to provide a **simple, lightweight UI** for demonstrating
patient CRUD operations and API integration.

<!-- --- -->

## Responsibilities

- Display backend status
- View all patients
- Create new patients
- View & edit existing patients
- Sort patients by height, weight, or BMI
- Delete patients by ID

<!-- --- -->

## Frontend Structure

  ```
  frontend/
  ├── app.py                 # Home / landing page
  ├── pages/                 # Streamlit pages (one workflow per page)
  │   ├── View_Patients.py
  │   ├── Create_Patient.py
  │   ├── Edit_Patient.py
  │   ├── Sort_Patients.py
  │   └── Delete_Patient.py
  ├── services/
  │   └── api.py             # API request wrapper (GET, POST, PUT, DELETE)
  ├── utils/
  │   └── config.py          # Environment config (.env loader)
  ├── requirements.txt
  └── README.md
```

<!-- --- -->

## Environment Configuration

The frontend reads the backend URL from a `.env` file.

Example `.env`:

  ```
  API_BASE_URL=http://localhost:8000
```

Make sure this file exists before running the frontend.

<!-- --- -->

## Running Frontend Locally

### 1. Create virtual environment

  ```
  python -m venv venv
  source venv/bin/activate
  ```

### 2. Install dependencies

  ```
  pip install -r requirements.txt
```

### 3. Start Streamlit app

  ```
  streamlit run app.py
```

The UI will be available at: [localhost:8501](http://localhost:8501)

<!-- --- -->

## Notes

- This frontend assumes the backend is already running
- No authentication is implemented
- State management is kept minimal for clarity
- Designed for demos, assignments, and learning purposes

<!-- --- -->

## Tech Stack

- Streamlit
- Python
- Requests
- python-dotenv

<!-- --- -->

## License

MIT License
