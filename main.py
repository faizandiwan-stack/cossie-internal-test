from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Ok 🚀"}

@app.get("/health")
def root():
    return {"status": "FastAPI running on Azure 🚀"}

@app.get("/git-deploy")
def root():
    return {"status": "FastAPI running on Azure Using GitHub Action 🚀"}

