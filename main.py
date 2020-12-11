# modulos locales
from db import clientes_db
from models import cliente_model

#modulos api
from fastapi import FastAPI
from fastapi import HTTPException


app = FastAPI() 

@app.get("/get_cliente/")
async def read_cliente(username: str):
    status = clientes_db.get_cliente(username)

    if status == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        return True #clientes_db.get_cliente(username)

@app.post("/post_cliente")
async def add_cliente(data: cliente_model.new_registro):
    if data.username in clientes_db.database_clientes.keys():
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        clientes_db.post_cliente(data.username, data)
        return {"out": "Registro exitoso"}
