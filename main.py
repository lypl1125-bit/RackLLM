from fastapi import FastAPI

from model.request import RequestModel
from services.groq_client import get_response_from_groq


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/request")
async def process_request(request: RequestModel):
    query = request.message
    print(f"request: {query}")
    #return {"request" : query}
    response = get_response_from_groq(query)
    print(f"Response: {response}")
    return {"request": query, "response": response}



    