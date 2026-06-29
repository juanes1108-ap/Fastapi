from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modelos.facturas import Factura


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

class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura: list["Factura"] = Relationship(back_populates="cliente")

class clienteleer(ClienteBase):
    id: int