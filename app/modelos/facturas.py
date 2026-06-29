from pydantic import BaseModel
from datetime import datetime
from pydantic import computed_field
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modelos.clientes import Cliente, clienteleer
    from app.modelos.transacciones import transaccion


class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)


class facturaCrear(FacturaBase):
    pass

class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int | None = Field(default=None, foreign_key="cliente.id")
    cliente: "Cliente" = Relationship(back_populates="factura")
    transacciones: list["transaccion"] = Relationship(back_populates="factura")

    @computed_field
    @property
    def vr_total(self) -> float:
        total_factura = 0.0
        for trans in self.transacciones:
            total_factura += trans.vr_unitario * trans.cantidad
        return total_factura

class facturaEditar(FacturaBase):
    pass

class facturaEliminar(BaseModel):
    id: int

class facturaleer(FacturaBase):
    id: int
    cliente: "clienteleer"

class facturaleercompuesta(facturaleer):
    transacciones: list["transaccion"] = []