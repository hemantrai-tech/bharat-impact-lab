# HaqSaathi

Organize questions and documents before contacting an official scheme service or community support team.

## Run locally

On Windows, double-click `run.bat`; it starts this project’s backend and opens the app. Or install Python 3.9+, run `python server.py`, and open http://127.0.0.1:8019.

The app uses only Python’s standard library. Its JSON API is `GET /api/health`, `GET /api/records`, and `POST /api/records`. Records are stored in `data.sqlite3` in this project folder. The database is created automatically on first run.

Use fictional or non-sensitive information. This is a local prototype; it does not connect to public agencies, clinics, employers, emergency services, or verified live data.
