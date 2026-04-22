import hashlib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Req(BaseModel):
    a:int
    b:int

@app.post("/compute")
def compute(req:Req):
    s=req.a+req.b
    p=req.a*req.b
    v=hashlib.sha256(f"sum:{s}:product:{p}".encode()).hexdigest()[:10]
    return {"sum":s,"product":p,"verify":v}
