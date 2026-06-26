from pydantic import BaseModel

#crear modelo de datos para la factura(id, cantidad, vr_unitario, id_factura)

class TransaccionBase(BaseModel):
    id: int
    cantidad: int
    vr_unitario: float
    id_factura: int
    