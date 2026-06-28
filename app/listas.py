from .modelos.facturas import Factura
from .modelos.clientes import Cliente
from .modelos.transacciones import TransaccionBase

lista_facturas: list[Factura] = []
lista_clientes: list[Cliente] = []
lista_transacciones: list[TransaccionBase] = []