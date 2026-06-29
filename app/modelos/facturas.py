from pydantic import BaseModel
from .clientes import Cliente
from datetime import datetime
from pydantic import computed_field
from .transacciones import transaccion
from sqlmodel import SQLModel, Field, Relationship


#crear modelo de datos para la factura(id, fecha, total, cliente_id)
class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())
    #cliente: Cliente
    #transacciones: list[transaccion] = []

    @computed_field
    @property
    def vr_total(self) -> float:
        ##consultar el id actal de la factura
        #factura_id_actual = getattr(self, 'id', None)
        #total_factura = 0.0
        #if not factura_id_actual or not self.transacciones:
           # return total_factura
        #recorer la lista de transacciones, segun el factura-id
        #for transaccion in self.transacciones:
            #if transaccion.factura_id == factura_id_actual:
                #total_factura += transaccion.vr_unitario * transaccion.cantidad
                
        return 0.0


#crear modulo crear factura
class facturaCrear(FacturaBase):
    pass

class Factura(FacturaBase, table= True):
    id: int | None = Field(default=None, primary_key= True)
    #transacciones: list[transaccion] = []
    cliente_id: int | None = Field(default=None, foreign_key="cliente.id")

#crear modulo editar factura
class facturaEditar(FacturaBase):
    pass

class facturaEliminar(BaseModel):
    id: int