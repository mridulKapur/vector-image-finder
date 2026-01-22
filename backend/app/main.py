from fastapi import FastAPI
from ..api.routes.index import  router as index_router
from ..api.routes.search import router as search_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Photo indexing and searching")

origins = [
"*"
    # Add other localhost ports if necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allows cookies to be sent with requests
    allow_methods=["*"],     # Allows all standard methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],     # Allows all headers
)
# app.include_router(health_router)
app.include_router(index_router)
app.include_router(search_router)
app.include_router(thumbnail_router)

@app.get('/ping')
def ping():
    return {"OK":True}