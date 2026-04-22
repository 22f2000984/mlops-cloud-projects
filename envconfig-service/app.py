import os,hashlib
from fastapi import FastAPI

app=FastAPI()

@app.get("/config")
def config():
    t=os.getenv("THEME_COLOR")
    m=os.getenv("APP_MODE")
    b=os.getenv("BUILD_NUMBER")
    h=hashlib.sha256(f"{t}:{m}:{b}".encode()).hexdigest()[:12]
    return {"theme_color":t,"app_mode":m,"build_number":b,"config_hash":h}
