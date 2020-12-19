from typing import Dict
from pydantic import BaseModel

#modelo tipo de dato entrada
class registroCliente(BaseModel):
    username: str
    nombre: str
    apellido: str
    email: str
    telefono: int
    edad: int
    idioma: str
    password: str

#definicion base de datos cliente
database_clientes = Dict[str, registroCliente]
database_clientes = {
    "fabra23": registroCliente(**{
        'username': 'fabra23',
        'nombre': 'Daniel',
        'apellido': 'Fabra',
        'email': 'daniel_fabra@outlook.com',
        'telefono': 3023018482,
        'edad': 23,
        'idioma': 'Español',
        'password': '1234',
    })
}

#funciones (querys) para base de datos
def get_cliente(username: str):
    if username in database_clientes.keys():
        return database_clientes[username]
    else:
        return None

def post_auth_cliente(username: str, password: str): 
    if username in database_clientes.keys():
        usuario_encontrado = database_clientes[username]
        return usuario_encontrado.password == password
    
    return "Las credenciales son incorrectas"

def post_cliente(nombre_usuario: str, data_cliente: registroCliente):
    database_clientes[nombre_usuario] = data_cliente


