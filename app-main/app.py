from fastapi import FastAPI
from pydantic import BaseModel
from src.run import run
from guvicorn_logger import Logger
from nltk.tokenize import sent_tokenize
from typing import Optional

## WEB SERVER
app = FastAPI()

# LOGGING
logger = Logger().configure()

class Request(BaseModel):
    input: str
    gen_params: Optional[dict] = None

@app.get(path="/health")
async def health():
    return {"status": "UP"}

@app.post("/run")
async def main(request: Request):
    logger.info("Running FastAPI Application..")

    # Parameters
    params = request.model_dump()
    gen_params = params['gen_params']
    input = params['input']
    
    generated_text = await run(input, gen_params)
        
    return generated_text