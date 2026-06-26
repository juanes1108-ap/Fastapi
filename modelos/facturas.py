from pydantic import BaseModel

#crear modelo de datos para la factura(id, fecha, total, cliente_id)
class FacturaBase(BaseModel):
    id: int
    fecha: str
    total: float
    cliente_id: int