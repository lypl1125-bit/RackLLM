from fastapi import FastAPI

from model.request import RequestModel


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/request")
async def process_request(request: RequestModel):
    query = request.message
    print(f"request: {query}")
    return {"request" : query}


    