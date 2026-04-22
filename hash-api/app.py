import hashlib
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Req(BaseModel):
    text:str
    salt:str

@app.post("/hash")
def hash_api(r:Req):
    t=r.text
    s=r.salt
    return {
        "sha256":hashlib.sha256(t.encode()).hexdigest()[:16],
        "salted_sha256":hashlib.sha256(f"{t}:{s}".encode()).hexdigest()[:16],
        "reversed":t[::-1],
        "length":len(t)
    }
