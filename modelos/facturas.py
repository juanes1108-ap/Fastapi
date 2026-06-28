from pydantic import BaseModel
from .clientes import Cliente
from datetime import datetime
from pydantic import computed_field
from .transacciones import transaccion


#crear modelo de datos para la factura(id, fecha, total, cliente_id)
class FacturaBase(BaseModel):
    fecha: str = datetime.now().strftime("%Y-%m-%d")
    cliente: Cliente
    transacciones: list[transaccion] = []

    @computed_field
    @property
    def vr_total(self) -> float:
        return 0


#crear modulo crear factura
class facturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None

#crear modulo editar factura
class facturaEditar(FacturaBase):
    pass

class facturaEliminar(BaseModel):
    id: int