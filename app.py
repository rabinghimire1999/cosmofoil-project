from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.query_db import query_db
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, question: str = Form(...)):
    sql_query, results = query_db(question)
    return templates.TemplateResponse("result.html", {"request": request, "sql_query": sql_query, "results": results})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)