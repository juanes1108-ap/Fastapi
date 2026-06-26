from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, clientecrear

app = FastAPI()



lista_clientes: list[Cliente] = []
 

#endpoint para listar clientes

@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_clientes

#endpoint para obtener un cliente específico

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def listar_cliente(cliente_id: int):
    #recorer la lista de clientes y buscar el cliente con el id especificado
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado") 

#endpoint para crear un cliente y agragar a la lista de clientes

@app.post("/clientes", response_model=Cliente)
def crear_cliente(datos_cliente: clientecrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val