from fastapi import APIRouter, HTTPException, status
from app.modelos.clientes import Cliente, clientecrear,clienteEditar, clienteEliminar, ClienteBase

rutas_clientes = APIRouter()

#lista de clientes
lista_clientes: list[Cliente] = []


#endpoint para listar clientes

@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

#endpoint para obtener un cliente específico

@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorer la lista de clientes y buscar el cliente con el id especificado
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado") 

#endpoint para crear un cliente y agragar a la lista de clientes

@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: clientecrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

#endpoint para editar un cliente existente y agregar a la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: clienteEditar):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(status_code=404, detail=f"Cliente con {cliente_id} no fue encontrado")


#endpoint para eliminar un cliente existente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(status_code=404, detail=f"Cliente con {cliente_id} no fue encontrado")