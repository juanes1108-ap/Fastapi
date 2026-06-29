from pydantic import BaseModel
from sqlmodel import SQLModel,Field, Relationship



#crear modelo de datos para el cliente(id, nombre, edad, descripcion)

class ClienteBase(SQLModel):
    nombre: str = Field(default=None)
    edad: int = Field(default=None)
    email: str = Field(default=None)
    descripcion: str | None = Field(default=None)

class clientecrear(ClienteBase):
    pass

class clienteEditar(ClienteBase):
    pass

class clienteEliminar(BaseModel):
    id: int

class Cliente(ClienteBase, table = True ):
    id: int | None = Field(default=None, primary_key=True)
    #relacion virtual
    factura : list["Factura"] = Relationship(back_populates="cliente")


class clienteleer(ClienteBase):
    id: int