from fastapi import FastAPI
from .router_index import router as index_router
from .router_search import router as search_router

app = FastAPI(title="Photo indexing and searching")


# app.include_router(health_router)
app.include_router(index_router)
app.include_router(search_router)

@app.get('/ping')
def ping():
    return {"OK":True}