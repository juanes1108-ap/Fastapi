from fastapi import APIRouter, HTTPException, status
from app.modelos.facturas import Factura, facturaCrear, facturaEditar, facturaEliminar
from app.modelos.clientes import Cliente, clientecrear,clienteEditar, clienteEliminar, ClienteBase

rutas_facturas = APIRouter()

#lista de facturas
lista_facturas: list[Factura] = []
lista_clientes: list[Cliente] = []





#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#crear endpoint para Facturas

#listar todas las facturas
@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas():
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

