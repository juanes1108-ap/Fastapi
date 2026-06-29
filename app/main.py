from fastapi import FastAPI, HTTPException, status
from app.modelos.clientes import Cliente, clientecrear,clienteEditar, clienteEliminar, ClienteBase
from app.modelos.transacciones import TransaccionBase, transaccionCrear, transaccionEditar, eliminarTransaccion, transaccion
from app.modelos.facturas import Factura, facturaCrear, facturaEditar, facturaEliminar
from app.enrutadores import clientes
from app.enrutadores import facturas
from app.enrutadores import transacciones
from app.conexion_bd import crear_tablas


app = FastAPI(lifespan=crear_tablas)



lista_clientes: list[Cliente] = []
lista_transacciones: list[TransaccionBase] = []
lista_facturas: list[Factura] = []
 
#incluir el enrutador de clientes
app.include_router(clientes.rutas_clientes, tags=["Clientes"])

#incluir el enrutador de facturas
app.include_router(facturas.rutas_facturas, tags=["Facturas"])

#incluir el enrutador de transacciones
app.include_router(transacciones.rutas_transacciones, tags=["Transacciones"])






