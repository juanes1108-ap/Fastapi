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
        #consultar el id actal de la factura
        factura_id_actual = getattr(self, 'id', None)
        total_factura = 0.0
        if not factura_id_actual or not self.transacciones:
            return total_factura
        #recorer la lista de transacciones, segun el factura-id
        for transaccion in self.transacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura += transaccion.vr_unitario * transaccion.cantidad
                
        return total_factura


#crear modulo crear factura
class facturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None
    transacciones: list[transaccion] = []

#crear modulo editar factura
class facturaEditar(FacturaBase):
    pass

class facturaEliminar(BaseModel):
    id: int