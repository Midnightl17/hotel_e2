from typing import Dict
from pydantic import BaseModel

#modelo tipo de dato entrada
class registroCliente(BaseModel):
    password: str
    nombre: str
    apellido: str
    edad: int
    telefono: int
    direccion: str
    idioma: str

#definicion base de datos cliente
database_clientes = Dict[str, registroCliente]
database_clientes = {
    "fabra23": registroCliente(**{
        "password": "fabra2020",
        "nombre": "Daniel",
        "apellido": "Fabra",
        "edad": 23,
        "telefono": 3023018482,
        "direccion": "Algun lugar",
        "idioma": "Español"
    })
}

#funciones (querys) para base de datos
def get_cliente(nombre_usuario: str):
    if nombre_usuario in database_clientes.keys():
        return database_clientes[nombre_usuario]
    else:
        return None

def post_cliente(nombre_usuario: str, data_cliente: registroCliente):
    database_clientes[nombre_usuario] = data_cliente


