Backend prototype for Local Photo Search (FastAPI + CLIP + Qdrant)


Quick start:
1. Create and activate venv (see README in project root or VS Code instructions).
2. From backend/ install dependencies:
pip install -r requirements.txt
3. Ensure Qdrant is running locally at http://localhost:6333
4. Start the FastAPI app:
uvicorn app.main:app --reload --port 8000


Endpoints:
- GET /ping
- POST /index?folder=/absolute/path/to/images
- GET /search?q=your+query&limit=20


Notes:
- This is a minimal prototype for local dev only (no production hardening).