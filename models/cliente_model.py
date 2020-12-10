from pydantic import BaseModel

class new_registro(BaseModel):
    password: str
    username: str
    nombre: str
    apellido: str
    edad: int
    telefono: int
    direccion: str
    idioma: str

class get_registro(BaseModel):
    nombre: str
    apellido: str
    edad: int
    telefono: int
