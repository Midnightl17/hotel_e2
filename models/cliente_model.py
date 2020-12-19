from pydantic import BaseModel

class new_registro(BaseModel):
    username: str
    nombre: str
    apellido: str
    email: str
    telefono: int
    edad: int
    idioma: str
    password: str

class get_registro(BaseModel):
    nombre: str
    apellido: str
    edad: int
    telefono: int

class login(BaseModel):
    username: str
    password: str