
############################################################    VARIABLES
#var1 = "ola"
#var2 = 'ola'
#var3 = 'ola "kiara"' #para esto se pueden combinar " i '

#var4 = 4

#print(var1) #imprime el contenido de la variable
#print(var2)
#print(var3)


#print(type(var1)) #imprime el tipo de variable
#print(type(var2))

#if(var4==4): # el if no va con {} si no que se tiene que idementar
   # print("hola")
#else:
    #print("nose")





############################################################## FOR



#for i in var1: #aqui solo se pueden recorrer objetos, no int
#    print(i)

#for i in range(2, 10, 2): #esto seria un for como en java, el primer numero es donde empieza
#    print(i)              #el segundo numero es hasta donde llega
                          # y el tercero son los saltos, aqui omite el 10, o sea que acaba en el 8

#for i in range(100) # empieza desde el 0 y acaba en el 99





###################################### POSICIONES?NOSE



#name = "kiara"
#print(name[3]) #imprimira la letra de la posición 3, teniendo en cuenta que empieza con 0
#print(name[-1]) #se puede empezar desde atras tambien
#print(name[3], name[0]) #aqui imprime las dos letras que pongas, puedes poner varias

#print(name[:2]) #aqui imprime del inicio, al 2, pero sin contar el 2
#print(name[2:]) #aqui lo mismo, solo que del dos al final
#print(name[1:5]) #aqui se incluye el 1, pero el 5 no

#print(name.replace('ar', 'nose')) # de kiara --> kinosea




############################################## LISTAS




#llista = [1, 2, 3, "hola", 3.4, [3,4,5]] #esto es una lista, haya lo que haya dentro
#print(type(llista)) # aqui nos indica que ES una lista
#print(type(llista[3])) # aqui si podemos saber el tipo de algo que haya dentro de la lista

#llista.append("olaola") #añadimos cosas a la lista
#print(llista)

#print(27 in llista) # aqui queremos mirar si dentro de lista esta el numero 27, dira FALSE
#print(3 in llista) # aqui TRUE

#llista.pop() # borra lo ultimo de la lista
#print(llista)

#llista2 = llista.pop() #borra lo ultimo de la lista pero lo estamos guardando en llista2
#print(llista2)




###################################################### TUPLA




#tupla = (1, 2, 3, "hola", 3.4, [3,4,5]) # es lo mismo que una lista pero en vez de [] se usa ()

#tupla1 = tupla() #para hacerla vacia

# length --> len

#tupla[3] = "juan"  # aqui estamos diciendo que se añada "juan" en la posicion 3 de la tupla





#################################### SET Y DICCIONARIO




#set1 = set("value1") #hay que poner el set pq si no es una tupla, segun roger no sirve de mucho
#print(set1)

#dict1 = {"key1":"value1"}
#print(dict1)

#dict1["travel"] = "Europa"

#dict2 = dict1.popitem()
#print(dict1)
#print(dict2)

#print(dict1.value()) #para sacar el valor







#########################################################3   FUNCIONES




#def nom_funcio():
#    return "ola"

#print(nom_funcio())


##### SABER QUE ES UNA     -->      LISTA, DICCIONARIO {"key":"mensaje"}, TUPLA, SET {"ola"}













##################################################################### otro dia y creo que es api


#from fastapi import FastAPI

#app = FastAPI()

#@app.get("/lacarpeta")   aqui podemos poner --> @app.get("/lacarpeta", response_model=str)   para asegurar el tipo de valor que te devuelve
#async def ola():
#    return "ola"

