# modulos locales
from db import clientes_db
from models import cliente_model

#modulos api
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI() 

#politicas cors
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    'https://hotelappe2.herokuapp.com'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_cliente/{username}")
async def read_cliente(username: str):
    status = clientes_db.get_cliente(username)

    if status == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        #resul = cliente_model.get_registro(tatus["nombre"]) 
        return {"out": True}

@app.post("/post_cliente")
async def add_cliente(data: cliente_model.new_registro):
    if data.username in clientes_db.database_clientes.keys():
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        clientes_db.post_cliente(data.username, data)
        return {"out": True}
