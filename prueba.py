
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

    


def recursividad(numero):
    if numero==0:
        return 1
    
    else:
        return numero*recursividad(numero-1)
    

"""        aux2=0
        indice2=0
        no_terminal=""
        terminal2=""
        for elemento2 in lista_aux:
            if elemento2==nombre_gram:
                while aux2 < len(lista_aux):  #cambiar datos para que no se confunda
                    elemento2=lista_aux[aux2]
                    if elemento2==nombre_gram:
                        indice2=0
                    elif elemento2==0:
                        no_terminal=elemento
                        indice2+=1
                    elif elemento2 ==1:
                        terminal2=elemento

                        tabla1.insert("", 'end',text = no_terminal, values=(terminal2))
                        indice2=0
                   # elif indice2==2:
                    #    no_terminal=elemento
                     #   indice+=1
                      #  if indice2==2:
                       #     terminal2=elemento
                        #    indice2+=1
                        #if no_terminal !="" and terminal2 !="":
                         #   tabla1.insert("", 'end',text = no_terminal, values=(terminal2))
                         #   indice2=0
                    elif elemento2== "$":
                        break
                    aux2+=1
            else:   
                    aux2+=1

        tabla1.place(x=50,y=245)"""