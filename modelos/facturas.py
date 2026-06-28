from pydantic import BaseModel
from .clientes import Cliente

#crear modelo de datos para la factura(id, fecha, total, cliente_id)
class FacturaBase(BaseModel):
    fecha: str
    vr_total: float
    cliente: Cliente


#crear modulo crear factura
class facturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    pass

#crear modulo editar factura
class facturaEditar(FacturaBase):
    pass

class facturaEliminar(BaseModel):
    id: int