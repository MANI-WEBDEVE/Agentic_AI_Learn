from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from app import multi_agent_response  # Import the function
from fastapi.middleware.cors import CORSMiddleware
# Create FastAPI app instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post('/')
async def agent_request(request:Request):
    query = await request.json() 
    qu=query['query']
    result = multi_agent_response(qu)
    return JSONResponse({"data":result})
    
    
    
    
      
