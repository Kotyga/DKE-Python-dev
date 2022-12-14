import fastapi
from fastapi.templating import Jinja2Templates
import pyodbc
connstr = (r'DRIVER={Microsoft Access Driver (.mdb,.accdb)};'r'DBQ=C:\Users\aobus\Downloads\online-productstore.accdb;')
cnxn = pyodbc.connect(connstr)

app = fastapi.FastAPI()
templates = Jinja2Templates(directory="./templates")

@app.get("/")
def read_root(request: fastapi.Request):
    crsr = cnxn.cursor()
    tables = [ x for x in crsr.tables(tableType='TABLE')]
    return templates.TemplateResponse("all_db.html", {"request": request, "databases": tables })
