import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, update

#from product import *
from pydantic import BaseModel
app = FastAPI()
#app.add_middleware(
 #   CORSMiddleware,
  #  allow_origins=["*"],
   # allow_credentials=True,
    #allow_methods=["*"],
    #allow_headers=["*"],
#)
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

#@app.post("/api/users", response_model=dict)
#async def newUser(User: user, db: Session = Depends(get_db)):












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