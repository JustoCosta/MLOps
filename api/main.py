from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from querys import Querys 
from predict import Predict

app = FastAPI()
templates = Jinja2Templates(directory="api/templates")

#Página principal

@app.get("/", response_class=HTMLResponse)
async def show_form1(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

#Consulta 1
@app.get("/query1", response_class=HTMLResponse)
async def show_form1(request: Request):
    return templates.TemplateResponse("form1.html", {"request": request})

#Respuesta 1
@app.post("/result1", response_class=HTMLResponse)
async def process_form1(request: Request, year: int = Form(...), platform: str = Form(...), durationtype: str = Form(...)):
    # Llama a la función importada y pasa las variables de entrada como argumentos
    result = Querys.get_max_duration(year, platform, durationtype)
    # Devuelve una plantilla de Jinja2 con el resultado
    return templates.TemplateResponse("result1.html", {"request": request, "result": result})

#Consulta 2
@app.get("/query2", response_class=HTMLResponse)
async def show_form2(request: Request):
    return templates.TemplateResponse("form2.html", {"request": request})

#Respuesta 2
@app.post("/result2", response_class=HTMLResponse)
async def process_form2(request: Request, platform: str = Form(...), score: float = Form(...), year: int = Form(...)):
    # Llama a la función importada y pasa las variables de entrada como argumentos
    result = Querys.get_score_count(platform , score , year)
    # Devuelve una plantilla de Jinja2 con el resultado
    return templates.TemplateResponse("result2.html", {"request": request, "result": result})

#Consulta 3
@app.get("/query3", response_class=HTMLResponse)
async def show_form3(request: Request):
    return templates.TemplateResponse("form3.html", {"request": request})

#Respuesta 3
@app.post("/result3", response_class=HTMLResponse)
async def process_form3(request: Request, platform: str = Form(...)):
    # Llama a la función importada y pasa las variables de entrada como argumentos
    result = Querys.get_count_platform(platform)
    # Devuelve una plantilla de Jinja2 con el resultado
    return templates.TemplateResponse("result3.html", {"request": request, "result": result})

#Consulta 4 
@app.get("/query4", response_class=HTMLResponse)
async def show_form4(request: Request):
    return templates.TemplateResponse("form4.html", {"request": request})

#Respuesta 4
@app.post("/result4", response_class=HTMLResponse)
async def process_form4(request: Request, platform: str = Form(...), year: int = Form(...)):
    # Llama a la función importada y pasa las variables de entrada como argumentos
    result = Querys.get_actor(platform, year)
    # Devuelve una plantilla de Jinja2 con el resultado
    return templates.TemplateResponse("result4.html", {"request": request, "result": result})

#Consulta 5 
@app.get("/query5", response_class=HTMLResponse)
async def show_form5(request: Request):
    return templates.TemplateResponse("form5.html", {"request": request})

#Respuesta 5
@app.post("/result5", response_class=HTMLResponse)
async def process_form5(request: Request, user: int = Form(...), movie: str = Form(...)):
    # Llama a la función importada y pasa las variables de entrada como argumentos
    p = Predict(user, movie)
    result = p.predict()
    

    # Devuelve una plantilla de Jinja2 con el resultado
    return templates.TemplateResponse("result5.html", {"request": request, "result": result})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002)
