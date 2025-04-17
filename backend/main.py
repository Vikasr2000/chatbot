from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can restrict this to specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Define a request model
class QueryRequest(BaseModel):
    query: str

# Define a POST endpoint
@app.post("/process-query/")
async def process_query(request: QueryRequest):
    return {"message": f"Your query is {request.query}"}

# Run the app using: uvicorn main:app --reload