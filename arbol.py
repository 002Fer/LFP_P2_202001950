import os
global lista 
lista = ["s","A","A","aAa","A","B","B","bBb","B","C"]


global graph 
graph = '''
    graph{
'''


global i
i=0
global numeronodo
global numeronodo1
global numeronodo2
numeronodo = 100
numeronodo1 = 200
numeronodo2=300


def grafo():
    #i = 0
    global i
    global numeronodo
    global numeronodo1
    global numeronodo2
    n1 =''
    n2 =''
    extras1=''
    operacion = ''
    extras2=''

    aux=0
    
    while True:
        if i>len(lista)-1:
            break
        char = lista[i]
        if char == 'Operacion':
            operacion = lista[i+1]
            nodo = f''' n{numeronodo}[label="{operacion}"]'''
            numeronodo+=1

        if char == 'Valor1':
            if lista[i+1]=='[':
                i+=1
                recursividad = grafo()
                n1 = recursividad[3]
                n1_1 = recursividad[0]
                extras1 = f'''{recursividad[1]}\n{recursividad[2]}\n{recursividad[3]}\n{recursividad[4]}'''
            else:
                n1 = float(lista[i+1])
                n1_1 = f''' n{numeronodo1}[label = "{n1}"] '''
                numeronodo1+=1



        if char == 'Valor2':
            if lista[i+1]=='[':
                i+=1
                recursividad2 = grafo()
                n2 = recursividad2[1]
                n2_2 = recursividad2[0]
                extras2 = f'''{recursividad2[1]}\n{recursividad2[2]}\n{recursividad2[3]}\n{recursividad2[4]}'''
            else:
                n2 = float(lista[i+1])
                n2_2=f''' n{numeronodo2}[label = "{n2}"] '''
                numeronodo2+=1




        if operacion and n1 and n2 !='':
            if extras1 == '' or extras1 or extras2=='' or extras2:
                relacion1 = f''' n{nodo[2:5]}--n{n1_1[2:5]} '''
                relacion2 = f''' n{nodo[2:5]}--n{n2_2[2:5]} '''
                return nodo, relacion1, relacion2, n1_1, n2_2, extras1, extras2
        i+=1
        


def crearArbol():
    n = 0
    graph = '''
    graph{
    '''
    while True:
        subgraph = grafo()
        subgrafo = f'''
            subgraph s{n}
        '''
        subgrafo+='{'
        nodoprincipal = subgraph[0]
        rela1 = subgraph[1]
        rela2 = subgraph[2]
        nodo1 = subgraph[3]
        nodo2 = subgraph[4]
        extras1 = subgraph[5]
        extras2 = subgraph[6]
        if nodoprincipal and rela1 and rela2 and nodo1 and nodo2:
            subgrafo+=nodoprincipal
            subgrafo+=rela1
            subgrafo+=rela2
            subgrafo+=nodo1
            subgrafo+=nodo2
            subgrafo+=extras1
            subgrafo+=extras2
            subgrafo+='}'
            graph+=subgrafo
            return graph
        if nodoprincipal=='' and rela1=='' and rela2=='' and nodo1=='' and nodo2=='':
            break
        n+=1
    

def fin():
        arbol = crearArbol()
        arbol+='}'
        with open("ejemplooo.dot", "w") as f:
            f.write(arbol)

        os.system('dot -Tpng ejemplooo.dot -o ejemplooo.png') 


fin()