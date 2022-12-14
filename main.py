import fastapi
from fastapi.templating import Jinja2Templates

app = fastapi.FastAPI()
templates = Jinja2Templates(directory="./templates")

@app.get("/")
def read_root(request: fastapi.Request):
    return templates.TemplateResponse("all_db.html", {"request": request, "databases": ["hello", "world"] })
