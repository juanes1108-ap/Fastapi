from pydantic import BaseModel

#crear modelo de datos para el cliente(id, nombre, edad, descripcion)

class ClienteBase(BaseModel):
    nombre: str
    edad: int
    email: str
    descripcion: str

class clientecrear(ClienteBase):
    pass

class clienteEditar(ClienteBase):
    pass

class clienteEliminar(BaseModel):
    id: int

class Cliente(ClienteBase):
    id: int | None = None



