from fastapi import FastAPI
from contracts import router as contracts_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI funciona"}

# Montar el router
app.include_router(contracts_router)
