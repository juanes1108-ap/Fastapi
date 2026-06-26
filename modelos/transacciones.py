from pydantic import BaseModel
from clientes import Cliente

#crear modelo de datos para la transaccion(id, cantidad, vr_unitario, id_factura)

class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    id_factura: int
    cliente: Cliente #esta es la relacion con el objeto cliente

class transaccionCrear(TransaccionBase):
    pass

class transaccionEditar(TransaccionBase):
    pass

    