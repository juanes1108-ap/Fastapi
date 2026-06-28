from fastapi import FastAPI, HTTPException, status
from app.modelos.clientes import Cliente, clientecrear,clienteEditar, clienteEliminar, ClienteBase
from app.modelos.transacciones import TransaccionBase, transaccionCrear, transaccionEditar, eliminarTransaccion, transaccion
from app.modelos.facturas import Factura, facturaCrear, facturaEditar, facturaEliminar
from app.enrutadores import clientes



app = FastAPI()



lista_clientes: list[Cliente] = []
lista_transacciones: list[TransaccionBase] = []
lista_facturas: list[Factura] = []
 
#incluir el enrutador de clientes
app.include_router(clientes.rutas_clientes, tags=["Clientes"])




#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#crear endpoint para Facturas

#listar todas las facturas
@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

#endpoint para obtener una factura específica
@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    for i, factura in enumerate(lista_facturas):
        if factura.id == factura_id:
            return factura
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con {factura_id} no fue encontrada")



#endpoint para crear una factura y agregar a la lista de facturas
@app.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: facturaCrear):
    #buscar el cliente con el id especificado
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente
            break
    #mensaje si el cliete no fue encontrado
    if not cliente_encontrado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Cliente con {cliente_id} no fue encontrado")
    #validar datos de la factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    #generar id de la factura
    factura_val.id = len(lista_facturas)+1
    lista_facturas.append(factura_val)
    return factura_val

#endpoint para editar una factura existente y agregar a la lista
@app.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: facturaEditar):
    for i, factura in enumerate(lista_facturas):
        if factura.id == factura_id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = factura_id
            lista_facturas[i] = factura_val
            return factura_val
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con {factura_id} no fue encontrada")


#endpoint para eliminar una factura existente
@app.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    for i, factura in enumerate(lista_facturas):
        if factura.id == factura_id:
            factura_eliminada = lista_facturas.pop(i)
            return factura_eliminada
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con {factura_id} no fue encontrada")



#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#ednpoint para transacciones
#listar todas las transacciones
@app.get("/transacciones", response_model=list[transaccion])
async def listar_transacciones():
    return lista_transacciones

#endpoint para obtener una transaccion específica   
@app.get("/transacciones/{transaccion_id}", response_model=transaccion)
async def listar_transaccion(transaccion_id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == transaccion_id:
            return transaccion
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaccion con {transaccion_id} no fue encontrada")

#endpoint para crear una transaccion y agregar a la lista de transacciones
@app.post("/transacciones/{factura_id}" , response_model=transaccion)
async def   crear_transaccion(factura_id: int, datos_transaccion: transaccionCrear):
     #buscar factura
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura
            break
    #mensaje si la factura no fue encontrada
    if not factura_encontrada:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Factura con {factura_id} no fue encontrada")
    
    #validar datos de la factura
    transaccion_val = transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.factura_id = factura_id
    transaccion_val.id = len(lista_transacciones) + 1
    lista_transacciones.append(transaccion_val)
    factura_encontrada.transacciones.append(transaccion_val)
    return transaccion_val





#endpoint para editar una transaccion existente y agregar a la lista
@app.patch("/transacciones/{transaccion_id}", response_model=transaccion)
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
@app.delete("/transacciones/{transaccion_id}", response_model=transaccion)
async def eliminar_transaccion(transaccion_id: int):
    for i, trans in enumerate(lista_transacciones):
        if trans.id == transaccion_id:
            transaccion_eliminada = lista_transacciones.pop(i)
            return transaccion_eliminada
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaccion con {transaccion_id} no fue encontrada")