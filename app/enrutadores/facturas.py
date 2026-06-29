from fastapi import APIRouter, HTTPException, status
from app.modelos.facturas import Factura, facturaCrear, facturaEditar, facturaEliminar, facturaleer
from app.modelos.clientes import Cliente, clientecrear,clienteEditar, clienteEliminar, ClienteBase
from app.modelos.transacciones import TransaccionBase, transaccionCrear, transaccionEditar, eliminarTransaccion, transaccion
from ..listas import lista_facturas, lista_clientes, lista_transacciones
from ..conexion_bd import Sesion_dependancia
from sqlmodel import select


rutas_facturas = APIRouter()

#lista de facturas
#lista_facturas: list[Factura] = []
#lista_clientes: list[Cliente] = []





#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#crear endpoint para Facturas

#listar todas las facturas
@rutas_facturas.get("/facturas", response_model=list[facturaleer])
async def listar_facturas(sesion: Sesion_dependancia):
    #select * from factura
    consulta = select(Factura)
    lista_facturas  =sesion.exec(consulta).all()
    return lista_facturas

#endpoint para obtener una factura específica
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    for i, factura in enumerate(lista_facturas):
        if factura.id == factura_id:
            return factura
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con {factura_id} no fue encontrada")



#endpoint para crear una factura y agregar a la lista de facturas
@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: facturaCrear, sesion: Sesion_dependancia):
    #buscar el cliente con el id especificado en bd

    cliente_encontrado = sesion.get(Cliente, cliente_id)

    #mensaje si el cliete no fue encontrado
    if not cliente_encontrado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Cliente con {cliente_id} no fue encontrado")
    #validar datos de la factura
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)
    #guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val

#endpoint para editar una factura existente y agregar a la lista
@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: facturaEditar):
    for i, factura in enumerate(lista_facturas):
        if factura.id == factura_id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = factura_id
            lista_facturas[i] = factura_val
            return factura_val
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con {factura_id} no fue encontrada")


#endpoint para eliminar una factura existente
@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    for i, factura in enumerate(lista_facturas):
        if factura.id == factura_id:
            factura_eliminada = lista_facturas.pop(i)
            return factura_eliminada
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con {factura_id} no fue encontrada")

