import json
from fastapi import FastAPI , Request
from starlette.responses import Response
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def hello():
    return Response(content="Hello world",status_code=200)
