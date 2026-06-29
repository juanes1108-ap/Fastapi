from pydantic import BaseModel
from .clientes import Cliente
from sqlmodel import SQLModel, Field, Relationship


#crear modelo de datos para la transaccion(id, cantidad, vr_unitario, id_factura)

class TransaccionBase(SQLModel):
    cantidad: int = Field(default=0)
    vr_unitario: float = Field(default=0.0)
    descripcion: str | None = Field(default=None)
   

class transaccionCrear(TransaccionBase):
    pass

class transaccionEditar(TransaccionBase):
    pass

class transaccion(TransaccionBase, table = True):
    id: int | None = Field(default= None, primary_key=True)
    factura_id: int | None = Field(default=None, foreign_key="factura.id")

class transaccionEliminar(BaseModel):
    id: int

class eliminarTransaccion(BaseModel):
    id: int 
    