
#Diccionario con codigo de encriptacion Leet 
diccionarioLeet={
    0 : "4",
    1 : "6",
    2 : "3",
    3 : "|",
    4 : "1",
    5 : "(V)",
    6 : r"(\)",# "r"--> para que no tenga en cuenta " \ "
    7 : "0",
    8 : "5",
    9 : "7",
    10 : r"\/",
    11 : "`//",
}
#Diccionario con condigo de encriptacion Normal
diccionarioNormal={
    0 : "A",
    1 : "B",
    2 : "E",
    3 : "I",
    4 : "L",
    5 : "M",
    6 : "N",
    7 : "O",
    8 : "S",
    9 : "T",
    10 : "V",
    11 : "W",
}
#Funcion recibe cadena de texto,Diccionaro Lee y Diccionario Normal
def Transcribir_De_Normal_A_Leet(frase_Normal,dicLee,dicNor):
    
    frase_Leet={}#Diccionario que almacenará la frase traducida
    
    frase_leet=""#Cadena en la que almacenará el contenido del diccionario para despues mostrar por consola
    
    #Bucle para recorrer cada letra dependiendo de la longitud de la cadena introducida
    for i in range(len(frase_Normal)):#Variable " i " almacena el indice de la letra actual
        
        traducida=False#Si la letra se busca en el diccionario y no esta entra dentro de los casos excepcionales
        
        #Bucle para recorrer las distintas posiciones del diccionario de traducciones para comparar si la letra actual se encuentra en el diccionario
        for j in range(12):#Variable " j " almacena el indice del diccionario
            
            #Comprueba si la letra actual coincide con letras del diccionario Normal
            if frase_Normal[i]==dicNor[j]:#Si coinciden ya sabemos la posicion del indice del 
                
                traducida=True#Activamos variable traducido pra que almacene este valor y no entre en condicional de excepciones
                
                frase_Leet[i]=dicLee[j]#Almacena valor traducido en diccionario  
                
                frase_leet+=frase_Leet[i]#Almacenamos valor del diccionario anterior en cadena de texto para mostrar

        #Si la letra no se encuentra en el diccionario de traduccion la copiamos directamente en el diccionario con la frase traducida     
        if traducida==False:
            frase_Leet[i]=frase_Normal[i]
            frase_leet+=frase_Leet[i]
    return frase_leet        
    
def Transcribir_De_Leet_A_Normal(frase_Leet,dicLee,dicNor):
    
    frase_Normal={}
    frase_normal=""
    
    for i in range(len(frase_Leet)):
        
        traducida=False#Si la letra se busca en el diccionario y no esta se copia en la frase traducida
        
        for j in range(12):
            
            if frase_Leet[i]==dicLee[j]:
                
                traducida=True
                
                frase_Normal[i]=dicNor[j]#Almacenamos en diccinario
                
                frase_normal+=frase_Normal[i]#Almacenamos en string para mostrar
                
        if traducida==False:
            
            #Traducción para codigo" \/ " --> Letra " V "
            if frase_Leet[i]=="\\" and frase_Leet[i+1]=="/":#Comprueva la posicion actual " \ " y la siguiente " /"
                frase_Normal[i]=dicNor[10]#Almacenamos en la posicion de "\" la traduccion de " V " antes de enviar eliminaremos la "/" que aun sigue en su posicion
                frase_normal+=frase_Normal[i]#Almacenamos en cadena
            
            #Traduccion para "  `//  " --> Letra " W "
            elif frase_Leet[i]=="`" and frase_Leet[i+1]=="/":
                frase_Normal[i]=dicNor[11]
                frase_normal+=frase_Normal[i]
            
            #Traduccion para " (V) " --> Letra " M "
            elif frase_Leet[i]=="(" and frase_Leet[i+1]=="V":
                frase_Normal[i]=dicNor[5]
                frase_normal+=frase_Normal[i]
            
            #Traduccion para " (\) " --> Letra " N "
            elif frase_Leet[i]=="(" and frase_Leet[i+1]=="\\":
                frase_Normal[i]=dicNor[6]
                frase_normal+=frase_Normal[i]
            
            #Eliminamos las " V " que se quedaron al traducir " (V) " verificando que antes de la V se encuentre una letra "M" generada al realizar la traduccion de la " (V) "
            elif frase_Leet[i]=="V" and frase_Normal[i-1]=="M":
                frase_Normal[i]=""
                frase_normal+=frase_Normal[i]
            
            #Si es una letra normal que no se encuentra en el diccionario se copia
            else:
                frase_Normal[i]=frase_Leet[i]
                frase_normal+=frase_Normal[i]

    #Elimina los caracteres sobrantes de realizar la traduccion
    frase_normal=frase_normal.replace("/","")
    frase_normal=frase_normal.replace("\\","")
    frase_normal=frase_normal.replace("(","")
    frase_normal=frase_normal.replace(")","")

    #Envia la cadena que contiene la frase
    return frase_normal 

   
#Almacenamos frase introducida por el usuario
frase_Normal=input("Introduce una frase en escritura Normal: ")
frase_Normal=str.upper(frase_Normal)#Pasamos a Mayusculas para usar el diccionario
print("Frase Normal: ",frase_Normal)
print("Frase Leet: ",Transcribir_De_Normal_A_Leet(frase_Normal,diccionarioLeet,diccionarioNormal))

frase_Leet=input("Introduce una frase en escritura Leet: ")
print("Frase Leet: ",frase_Leet)
print("Frase Normal: ",Transcribir_De_Leet_A_Normal(frase_Leet,diccionarioLeet,diccionarioNormal))