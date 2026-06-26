from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

 #crear modelo de datos para el cliente(id, nombre, edad, descripcion)

class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    descripcion: str


lista_clientes: list[Cliente] = []
 

#endpoint para listar clientes

@app.get("/clientes")
def listar_clientes():
    return lista_clientes

#endpoint para obtener un cliente específico

@app.get("/clientes/{cliente_id}")
def listar_cliente(cliente_id: int):
    #recorer la lista de clientes y buscar el cliente con el id especificado
    for i, cliente in enumerate(lista_clientes):
        if cliente.get("id") == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado") 

#endpoint para crear un cliente y agragar a la lista de clientes

@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return datos_cliente