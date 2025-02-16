import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request



# Initialize FastAPI and Jinja2 Templates
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home-page.html", 
                                      {"request": {"request": request}})

@app.get("/login-page", response_class=HTMLResponse)
async def getLoginPage(request:Request):   
    return templates.TemplateResponse("login-page.html", 
                                      {"request": {"request": request}})


@app.get("/write-page",response_class=HTMLResponse)
async def getWritePage(request:Request):
    print ("Here")
    return templates.TemplateResponse("write-page.html", 
                                    {"request": {"request": request}})





if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)