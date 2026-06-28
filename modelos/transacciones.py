from pydantic import BaseModel
from .clientes import Cliente

#crear modelo de datos para la transaccion(id, cantidad, vr_unitario, id_factura)

class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
   

class transaccionCrear(TransaccionBase):
    pass

class transaccionEditar(TransaccionBase):
    pass

class transaccion(TransaccionBase):
    id: int | None = None
    factura_id : int | None = None

class transaccionEliminar(BaseModel):
    id: int

class eliminarTransaccion(BaseModel):
    id: int 
    