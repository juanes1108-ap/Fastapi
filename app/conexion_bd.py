from fastapi import FastAPI, Depends
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated


nombre_bd = "bd_proyecto.sqlite"
url_bd = f"sqlite:///{nombre_bd}"

#motor de bd
motor_bd = create_engine(url_bd)

#definir el metodo para crear las tablas

def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_bd)
    yield # no hay nada para retornar o ejecutar


#definir el metodo para la sesion

def obtener_sesion( ):
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion  #me retorna la sesion 


#denominado inyeccion de dependancias
#resgistrar la sesion como dependencia, utilizada en nustros endpoints

Sesion_dependancia = Annotated[Session, Depends(obtener_sesion)]