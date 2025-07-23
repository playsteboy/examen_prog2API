import json
from fastapi import FastAPI , Request
from starlette.responses import Response
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
