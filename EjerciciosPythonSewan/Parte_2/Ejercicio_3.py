import json

def guardar(texto):
    contenido=open("./archivo.json","w")
    texto=json.dumps(texto)
    contenido.write(texto)
    contenido.close()
    
contenido=open("./archivo.json")
usuarios=json.load(contenido)
contenido.close()
print(usuarios)

mensajes=["Hola Alvaro","Aqui programando en python"]
usuarios["Alvaro"]=mensajes

print(usuarios)



guardar(usuarios)


contenido=open("./archivo.json")
usuarios=json.load(contenido)
contenido.close()
print(usuarios)



