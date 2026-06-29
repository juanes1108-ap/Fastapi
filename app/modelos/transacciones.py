from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modelos.facturas import Factura


class TransaccionBase(SQLModel):
    cantidad: int = Field(default=0)
    vr_unitario: float = Field(default=0.0)
    descripcion: str | None = Field(default=None)


class transaccionCrear(TransaccionBase):
    pass

class transaccionEditar(TransaccionBase):
    pass

class transaccion(TransaccionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int | None = Field(default=None, foreign_key="factura.id")
    factura: "Factura" = Relationship(back_populates="transacciones")

class transaccionEliminar(BaseModel):
    id: int

class eliminarTransaccion(BaseModel):
    id: int

class transaccionleer(TransaccionBase):
    id: int
    