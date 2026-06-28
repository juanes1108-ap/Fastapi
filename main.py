from fastapi import FastAPI, HTTPException, status
from modelos.clientes import Cliente, clientecrear,clienteEditar, clienteEliminar
from modelos.transacciones import TransaccionBase, transaccionCrear, transaccionEditar, eliminarTransaccion
from modelos.facturas import Factura, facturaCrear, facturaEditar, facturaEliminar

app = FastAPI()



lista_clientes: list[Cliente] = []
lista_transacciones: list[TransaccionBase] = []
lista_facturas: list[Factura] = []
 

#endpoint para listar clientes

@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

#endpoint para obtener un cliente específico

@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorer la lista de clientes y buscar el cliente con el id especificado
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado") 

#endpoint para crear un cliente y agragar a la lista de clientes

@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: clientecrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

#endpoint para editar un cliente existente y agregar a la lista
@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: clienteEditar):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(status_code=404, detail=f"Cliente con {cliente_id} no fue encontrado")


#endpoint para eliminar un cliente existente
@app.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(status_code=404, detail=f"Cliente con {cliente_id} no fue encontrado")



#|||||||||||||
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
    pass

#endpoint para eliminar una factura existente
@app.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    pass

#||||||||||||||||||||||||
#ednpoint para transacciones
#listar todas las transacciones
@app.get("/transacciones", response_model=list[TransaccionBase])
async def listar_transacciones():
    return lista_transacciones

#endpoint para obtener una transaccion específica   
@app.get("/transacciones/{transaccion_id}", response_model=TransaccionBase)
async def listar_transaccion(transaccion_id: int):
    pass

#endpoint para crear una transaccion y agregar a la lista de transacciones
@app.post("/transacciones", response_model=TransaccionBase )
async def   crear_transaccion(datos_transaccion: transaccionCrear):
    pass

#endpoint para editar una transaccion existente y agregar a la lista
@app.patch("/transacciones/{transaccion_id}", response_model=TransaccionBase)
async def editar_transaccion(transaccion_id: int, datos_transaccion: transaccionEditar):
    pass

#endpoint para eliminar una transaccion existente
@app.delete("/transacciones/{transaccion_id}", response_model=TransaccionBase)
async def eliminar_transaccion(transaccion_id: int):
    pass    
