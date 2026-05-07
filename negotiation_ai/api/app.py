from fastapi import FastAPI
from pydantic import BaseModel
from services.negotiation_services import run_negotiation

app = FastAPI()

# Request schema
class NegotiationRequest(BaseModel):
    role: str
    experience: int
    company: str


@app.get("/")
def home():
    return {"message": "Negotiation API is running"}


@app.post("/negotiate")
def negotiate(data: NegotiationRequest):
    result = run_negotiation(
        role=data.role,
        experience=data.experience,
        company=data.company
    )
    return {"result": result}