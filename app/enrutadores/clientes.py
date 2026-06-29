from fastapi import APIRouter, HTTPException, status
from app.modelos.clientes import Cliente, clientecrear,clienteEditar, clienteEliminar, ClienteBase
from ..listas import lista_clientes
from ..conexion_bd import Sesion_dependancia
from sqlmodel import select


rutas_clientes = APIRouter()

#lista de clientes
#lista_clientes: list[Cliente] = []


#endpoint para listar clientes

@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes(sesion: Sesion_dependancia):
    lista_cli = sesion.exec(select(Cliente)).all()
    return lista_cli

#endpoint para obtener un cliente específico

@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int, mi_sesion: Sesion_dependancia): 
    cliente_bd = mi_sesion.get(Cliente, cliente_id) 
    if not cliente_bd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cliente no encontrado")
    return cliente_bd
        


     

#endpoint para crear un cliente y agragar a la lista de clientes

@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: clientecrear, mi_sesion: Sesion_dependancia):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    mi_sesion.add(cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_val)
    return cliente_val

#endpoint para editar un cliente existente y agregar a la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: clienteEditar, mi_sesion:Sesion_dependancia):
     
     cliente_bd = mi_sesion.get(Cliente, cliente_id) 
     if not cliente_bd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cliente no encontrado")
     cliente_dict = datos_cliente.model_dump(exclude_unset = True)
     cliente_bd.sqlmodel_update(cliente_dict)
     mi_sesion.add(cliente_bd)
     mi_sesion.commit()
     mi_sesion.refresh(cliente_bd)
     return cliente_bd


#endpoint para eliminar un cliente existente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int, mi_sesion: Sesion_dependancia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id) 
    if not cliente_bd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cliente no encontrado")
    
    mi_sesion.delete(cliente_bd)
    mi_sesion.commit()
    return cliente_bd