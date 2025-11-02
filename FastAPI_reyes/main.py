import os
from sqlmodel import SQLModel, create_engine, Session, Field, select, update
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, update
from pydantic import BaseModel
from product import *
from fastapi.middleware.cors import CORSMiddleware
#IMPORTS


# CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()

# connexió amb la bd
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

# Iniciar/Apagar la sessió de la BDD
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

################################### 1 ####################################
@app.post("/api/prod", response_model=dict, tags=["AFEGIR"])
async def newProd(prod: createProduct, db: Session = Depends(get_db)):
    afegir = product.model_validate(prod)
    # validar l'informació amb el nostre model

    db.add(afegir)  # afegir
    db.commit()     # comentari
    return {"msg":"Inserció exitosa"}

################################### 2 ####################################
@app.get("/api/prod/{id}", responde_model=product, tags=["CONSULTA"])
async def getProd(id: int, db: Session = Depends(get_db)):
    trobar = SELECT(product).WHERE(product.id==id)
    # consulta sql
    mostrar = db.exec(trobar).first()
    # el first() es per a que només retorni el primer que trobi
    return mostrar

################################### 3 ####################################
@app.get("/api/product", response_model=list, tags=["CONSULTA"])
async def registres(db: Session = Depends(get_db)):
    trobar = select(product)
    mostrar = db.exec(trobar).all() # all per a trobar tots
    llista = [] # llista

    #bucle
    for i in mostrar:
        llista.append(createProduct.model_validate(i))
    return llista

################################### 4 ####################################
@app.get("/api/product/{nom_camp}", response_model=list[product], tags=["CONSULTA"])
async def buscaCamp(nom_camp: str, db: Session = Depends(get_db)):
    trobar = select(product).where(nom_camp==product.name)
    #consulta de sql
    mostrar = db.exec(trobar).all()
    return mostrar

################################### 5 ####################################
@app.delete("/api/product/delete/{id}", response_model=dict, tags=["REMOVE"])
async def borrarRegistre(id: int, db: Session = Depends(get_db)):
    trobar = select(product).where(product.id==id)
    mostrar = db.exec(trobar).first()
    db.delete(mostrar) # LO BORRAMOS
    db.commit()
    return{"msg":"Eliminat exitosament"}

################################### 6 ####################################
@app.get("/api/prodAux", response_model=list, tags=["CONSULTA"])
async def dadesProd(db: Session = Depends(get_db)):
    trobar = select(product)
    mostrar = db.exec(trobar).all()
    lista=[]
    for i in mostrar:
        lista.append(productPublic.model_validate(i))
    return lista

################################### 7 ####################################
@app.put("/api/actualizar/{id}", response_model=dict, tags=["UPDATE"])
async def actualitzarProd(id: int, prod: productPublic, db: Session = Depends(get_db)):
    act = prod.model_dump()
    # PASA ELS PARAMETRES COM AL MODEL DEMANAT
    up=update(product).where(roduct.id==id).values(act)
    db.exec(up)
    db.commit()
    return {"msg":"Actualització exitosa"}

################################### 8 ####################################
@app.patch("/api/actualizarNombre/{id}", response_model=dict, tags=["UPDATE"])
async def actualizarNom(id:int, nouNom: str, db: Session = Depends(get_db)):
    act = update(product).where(product.id==id).values(name=nouNom)
    db.exec(act)
    db.commit()
    return {"msg":"Modificació exitosa"}

################################### 9 ####################################
@app.patch("/api/upTwo/{id}", response_model=dict, tags=["UPDATE"])
async def updateTwo(id:int, nouNom:str, nouStock: int, db: Session = Depends(get_db)):
    act = (
        update(product)
        .where(product.id==id)
        .values(name=nouNom, stock=nowStock)
    )
    db.exec(act)
    db.commit()
    return {"msg":"Nom i Stock actualitzats exitosament"}










##########################################################################################################################

#from fastapi import FastAPI
#app = FastAPI()

#users = ["petunia", "vaca"]

################################### 1 #######################################

#@app.post("/api/users", response_model=dict)
#async def addUser():
    # print(users) # com es avans del canvi

#    newUser="pouka"
#    users.append(newUser)
    # print(users) # pero comprobar que s'ha afegit

#    id = range(len(users))
#    usersDict = dict(zip(id, users))

    # print(usersDict) # mirem el diccionari
#    return usersDict

################################### 2 #######################################

#@app.get("/api/users/{id}", response_model=dict)
#async def getUser(id: int):
    # el diccionari
#    usersDict = dict(zip(range(len(users)), users))
    # print(usersDict) # print del diccionari

    # busquem l'id
#    if id in usersDict:
        # print(id, usersDict[id])

        # retornem l'informació de l'id demanat
#        return{id: usersDict[id]}
#    else:
#        print("ERROR, usuari no trobat")
        # si no retornem un error ja que no s'ha trobat
#        return {"ERROR":"Usuari no trobat"}

################################### 3 #######################################

#@app.get("/api/users", response_model=dict)
#async def getUserList():
    #retorna la llista de
#    usersDict = dict(zip(range(len(users)), users))
#    return usersDict

################################### 4 #######################################

#@app.put("/api/users/{id}", response_model=dict)
#async def modifyUser(id: int, name: str):
#    usersDict = dict(zip(range(len(users)), users))
    # busquem
#    if id in usersDict:
        # actualitzem
#        users[id] = name
  #      usersDictAct = dict(zip(range(len(users)), users))
#        return usersDictAct
#    else:
#        print("ERROR, usuari no trobat")
#        return {"ERROR":"Usuari no trobat"}

################################### 5 #######################################

#@app.patch("/api/users/{id}", response_model=dict)
#async def modifyUserPartial(id: int, name: str):
#    usersDict = dict(zip(range(len(users)), users))
#    if id in usersDict:
#        users[id] = name
#        usersDictAct = dict(zip(range(len(users)), users))
#        return usersDictAct
#    else:
#        print("ERROR, usuari no trobat")
#        return {"ERROR":"Usuari no trobat"}

################################### 6 #######################################

#@app.delete("/api/users/{id}", response_model=dict)
#async def deleteUser(id: int):
#    usersDict = dict(zip(range(len(users)), users))
#    if id in usersDict:
#        usersDict.pop(id)
#        return usersDict
#    else:
#        print("ERROR, usuari no trobat")
#        return {"ERROR":"Usuari no trobat"}