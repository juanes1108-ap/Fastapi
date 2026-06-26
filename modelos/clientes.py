from pydantic import BaseModel

#crear modelo de datos para el cliente(id, nombre, edad, descripcion)

class ClienteBase(BaseModel):
    nombre: str
    edad: int
    email: str
    descripcion: str

class clientecrear(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int | None = None
