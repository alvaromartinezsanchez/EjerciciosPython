from io import open

archivo_texto=open("./Isla.txt","r")
texto=archivo_texto.readlines()
archivo_texto.close()
capitulos=[]
for i in range(len(texto)):
    if texto[i]=="\n" and texto[i-1]=="\n" and texto[i-2]=="\n":
        print(texto[i+1])
        capitulos.append(texto[i+1])
print(capitulos)


