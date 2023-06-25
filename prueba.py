
from tkinter.filedialog import askopenfilename
lis_todo=[]
nueva_lista=[]
def buscar_archivo():

    try:
        file = askopenfilename(title="Cargar un archivo", filetypes=[("Archivos", f'*.glc')])
        text = file
        openfile = open(text, encoding="utf-8")
        archivo = openfile.read().split("\n")
            
        for lineas in archivo:  
            lis_todo.append(lineas)
        print(lis_todo)
        separar()
        
    except:
        print('Error, no se ha seleccionado ningún archivo')

def separar():
    aux=0
    indice=0
    lista_aux=[]
    while aux < len(lis_todo):
        elemento=lis_todo[aux]
        if indice>=0 and indice<=3:
            indice+=1
        elif indice>3 and elemento !="%":
            nueva_lista.append(elemento)
            indice +=1
        elif elemento== "%":
            nueva_lista.append("$")
            indice=0
       
        aux+=1
    for elemento2 in nueva_lista:
        lementos_separados = elemento2.replace("::=", ",").split(",")
            
        lista_aux.extend(lementos_separados)
        lista_aux.append("#")
    print(lista_aux)    

    
buscar_archivo()

def recursividad(numero):
    if numero==0:
        return 1
    
    else:
        return numero*recursividad(numero-1)

