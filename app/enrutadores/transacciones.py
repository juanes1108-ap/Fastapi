from fastapi import APIRouter, HTTPException, status
from app.modelos.facturas import Factura, facturaCrear, facturaEditar, facturaEliminar
from app.modelos.clientes import Cliente, clientecrear,clienteEditar, clienteEliminar, ClienteBase
from app.modelos.transacciones import TransaccionBase, transaccionCrear, transaccionEditar, eliminarTransaccion, transaccion
from ..listas import lista_facturas, lista_clientes, lista_transacciones
from ..conexion_bd import Sesion_dependancia
from sqlmodel import select

rutas_transacciones = APIRouter()

#lista de transacciones
#lista_transacciones: list[TransaccionBase] = []
#lista_facturas: list[Factura] = []
#lista_clientes: list[Cliente] = []

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#ednpoint para transacciones


#listar todas las transacciones
@rutas_transacciones.get("/transacciones", response_model=list[transaccion])
async def listar_transacciones(sesion: Sesion_dependancia):
    #select * from factura
    consulta = select(transaccion)
    lista_transacciones =sesion.exec(consulta).all()
    return lista_transacciones



#endpoint para obtener una transaccion específica   
@rutas_transacciones.get("/transacciones/{transaccion_id}", response_model=transaccion)
async def listar_transaccion(transaccion_id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == transaccion_id:
            return transaccion
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaccion con {transaccion_id} no fue encontrada")

#endpoint para crear una transaccion y agregar a la lista de transacciones
@rutas_transacciones.post("/transacciones/{factura_id}" , response_model=transaccion)
async def   crear_transaccion(factura_id: int, datos_transaccion: transaccionCrear, sesion: Sesion_dependancia):
     #buscar factura
    factura_encontrada  = sesion.get(Factura, factura_id)
    #mensaje si la factura no fue encontrada
    if not factura_encontrada:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Factura con {factura_id} no fue encontrada")
    
    #validar datos de la factura
    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id
    transaccion_val = transaccion.model_validate(transaccion_dict)
    #guardar en la base de datos
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)
    return transaccion_val





#endpoint para editar una transaccion existente y agregar a la lista
@rutas_transacciones.patch("/transacciones/{transaccion_id}", response_model=transaccion)
async def editar_transaccion(transaccion_id: int, datos_transaccion: transaccionEditar):
    for i, trans in enumerate(lista_transacciones):
        if trans.id == transaccion_id:
            transaccion_val = transaccion.model_validate(datos_transaccion.model_dump())
            transaccion_val.id = transaccion_id
            transaccion_val.factura_id = trans.factura_id  # conserva la factura a la que pertenece
            lista_transacciones[i] = transaccion_val
            return transaccion_val
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaccion con {transaccion_id} no fue encontrada")


#endpoint para eliminar una transaccion 
@rutas_transacciones.delete("/transacciones/{transaccion_id}", response_model=transaccion)
async def eliminar_transaccion(transaccion_id: int):
    for i, trans in enumerate(lista_transacciones):
        if trans.id == transaccion_id:
            transaccion_eliminada = lista_transacciones.pop(i)
            return transaccion_eliminada
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaccion con {transaccion_id} no fue encontrada")
