from tkinter import *
from tkinter import ttk
from gramatica import Gramatica
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 

tiempo=10
lis_todo=[] #sirve al abrir el archivo
lista_nombres=[]    #sirve para los nombres y tenerlos en el combobox

lista_aux=[]        #tiene las producciones para luego llamarlas
lis_todoPila=[] #almacena todo lo de la pila
lista_nombresPila=[] #almacena los nombres de los automatas de pila


class Mi_ventan(Frame):
    

    def __init__(self, master=None):
        super().__init__(master, width=500,height=300,bg='#064663')
        self.master=master
        self.pack()
        self.bienvenida()


    def ventana_principal(self):
        self.ventana3.destroy()
       
        self.gramatica=Button(self,text="Módulo Gramáticas", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.ventana_gramaticas).place(x=150,y=50,width=200,height=40)
        self.automatas=Button(self,text="Módulo Autómatas", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=self.ventana_pila).place(x=150,y=100,width=200,height=40)
        self.salir=Button(self,text="Salir", bg="#0E8388", fg="white", font = ("Lemon Juice",14), command=self.despedida).place(x=150,y=150,width=200,height=40)
       
    def ventana_gramaticas(self):
        ventana2=Toplevel()
        ventana2.title("Gramáticas")
        ventana2.geometry("500x250")
        ventana2.config(bg='#064663')

        Carga=Button(ventana2,text="Carga Archivo", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.buscar_archivo)
        informacion=Button(ventana2,text="Informacion General", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=self.ventana_Infogeneral)
        arbol=Button(ventana2,text="Arbol de Derivación", bg="#0E8388", fg="white", font = ("Lemon Juice",14), command=self.ventana_arbol)
        boton_salir=Button(ventana2, text='Salir',bg="#ECB365", fg="white", font = ("Lemon Juice",14),command=ventana2.destroy)

        Carga.place(x=150,y=50,width=200,height=40)
        informacion.place(x=150,y=100,width=200,height=40)
        arbol.place(x=150,y=150,width=200,height=40)
        boton_salir.place(x=150,y=200,width=200,height=40)
    
    def ventana_pila(self):
        pila=Toplevel()
        pila.title("Gramáticas")
        pila.geometry("500x500")
        pila.config(bg='#064663')

        Carga=Button(pila,text="Carga Archivo", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.buscar_archivo2)
        informacion=Button(pila,text="Informacion Autómata", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=self.ventana_InfoAutomatas)
        validar=Button(pila,text="Validar Cadena", bg="#0E8388", fg="white", font = ("Lemon Juice",14))
        ruta=Button(pila, text='Ruta de Validacion',bg="#ECB365", fg="black", font = ("Lemon Juice",14))
        paso_paso=Button(pila,text="Recorrido paso a paso", bg="#0E8388", fg="white", font = ("Lemon Juice",12))
        una_pasada=Button(pila,text="Validar en una pasada", bg="#ECB365", fg="black", font = ("Lemon Juice",12))
        boton_salir=Button(pila, text='Salir',bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=pila.destroy)

        Carga.place(x=150,y=50,width=200,height=40)
        informacion.place(x=150,y=100,width=200,height=40)
        validar.place(x=150,y=150,width=200,height=40)
        ruta.place(x=150,y=200,width=200,height=40)
        paso_paso.place(x=150,y=250,width=200,height=40)
        una_pasada.place(x=150,y=300,width=200,height=40)
        boton_salir.place(x=150,y=350,width=200,height=40)

    def ventana_InfoAutomatas(self):
        automata=Toplevel()
        automata.title("Informacion General")
        automata.geometry("500x250")
        automata.config(bg='#064663')

        self.combo_automata=ttk.Combobox(automata)
        seleccionar=Button(automata,text="Seleccionar", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.transiciones_pila)
        boton_salir=Button(automata, text='Atras',bg="#ECB365", fg="white", font = ("Lemon Juice",14),command=automata.destroy)

        label_nombre=Label(automata,text="Autómata",bg="#064663", fg="white",font = ("Lemon Juice",14))
        label_nombre.place(x=50,y=50, width=100, height=30)
        self.combo_automata.place(x=160,y=50, width=200, height=30)
        seleccionar.place(x=150,y=150,width=200,height=40)
        boton_salir.place(x=150,y=200,width=200,height=40)
        
        aux=0
        indice=0
        while aux < len(lis_todoPila):
            elemento=lis_todoPila[aux]
            if indice==0:
                lista_nombresPila.append(elemento)
                indice+=1
            elif indice>0 and elemento !="%":
                indice +=1
            elif elemento== "%":
                indice=0
       
            aux+=1
        self.combo_automata["values"]=lista_nombresPila
        self.combo_automata.current(0)


    def transiciones_pila(self):
        nombre_autom=self.combo_automata.get()
        nueva_lista2=[]
        lista_elementosPila=[]
        aux2=0
        indice2=0
 
        self.nombrePila=""
        self.alfabetoTodo=""
        self.alfabetoPila=""
        self.estadosPila=""
        self.inicialPila=""
        self.aceptacionPila=""
        lista_estados=[]
        lista_estados2=[]
        lista_aceptacion=[]
    #----------------itero los elementos de la gramática y la muestro en los Label ------------
        for nombre in lis_todoPila:
            if nombre==nombre_autom:
                while aux2 < len(lis_todoPila):
                    elemento3=lis_todoPila[aux2]
                    if indice2==0:
                        self.nombrePila=elemento3
                        indice2+=1
                    elif indice2==1:
                        self.alfabetoTodo=elemento3
                        indice2+=1
                    elif indice2==2:
                        self.alfabetoPila=elemento3
                        indice2+=1
                    elif indice2==3:
                        self.estadosPila=elemento3
                        lista_estados.append(self.estadosPila)
                        indice2+=1
                    elif indice2==4:
                        self.inicialPila=elemento3
                        indice2+=1
                    elif indice2==5:
                        self.aceptacionPila=elemento3
                        lista_aceptacion.append(self.aceptacionPila)
                        indice2+=1
                    elif indice2>=6 and elemento3 !="%":
                        nueva_lista2.append(elemento3)
                        indice2+=1
                    elif elemento3=="%":
                        break
                        indice2=0
                    aux2+=1
            else:   
                aux2+=1
        #----separa los elementos de las transiciones y las mete en una lista
        for elementos in nueva_lista2:
            pila_separada=elementos.replace(";", ",").split(",")
             
            lista_elementosPila.extend(pila_separada)
            lista_elementosPila.append("&")
        
        for estados in lista_estados:
            esstados=estados.split(",")
            lista_estados2.extend(esstados)


         #itero, meto los elementos en la clase, luego a la pila

        
        dot = Digraph('AFD', filename='AFDPrueba2', format='png')
        dot.attr(rankdir='LR', size='8,5')
        dot.attr('node', shape='doublecircle')
        for i in lista_aceptacion:
            dot.node(i)

        dot.attr('node', shape='circle')
        for j in lista_estados2:
            dot.node(j)

        
        indice3=0
        aux3=0
        while aux3 <len(lista_elementosPila):
            elemento_aux=lista_elementosPila[aux3]
            if indice3==0:
                origen=elemento_aux
                indice3+=1
            elif indice3==1:
                lee=elemento_aux
                indice3+=1
            elif indice3==2:
                extrae=elemento_aux
                indice3+=1
            elif indice3==3:
                destino=elemento_aux
                indice3+=1
            elif indice3==4:
                inserta=elemento_aux
                indice3+=1
            elif elemento_aux=="&":
                dot.edge(origen, destino, label="{},{};{}".format(lee,extrae,inserta))
                indice3=0
            aux3+=1
        dot.render('AFDPrueba2', view=False)
 
        # print(lista_elementosPila)
        w, h = A4
        pdf = canvas.Canvas("ReporteAutómata.pdf", pagesize=A4)
        pdf.setTitle("Reporte de Autómata")
        text = pdf.beginText(50, h - 50)
        text.setFont("Times-Roman", 20)

        text.textLine("Nombre= "+self.nombrePila)                   
        text.textLine("Alfabeto= {"+self.alfabetoTodo+"}")                    
        text.textLine("Alfabeto de pila= {"+self.alfabetoPila+"}")                     
        text.textLine("Estados= {"+self.estadosPila+"}")                   
        text.textLine("Estado inicial= {"+self.inicialPila+"}")                      
        text.textLine("Estado de aceptacion= {"+self.aceptacionPila+"}")          
                       
        text.textLine()
        pdf.drawText(text)
        pdf.drawInlineImage("AFDPrueba2.png", 100, 50, width=450, height=450, preserveAspectRatio=True)
        pdf.save()
        webbrowser.open_new_tab('ReporteAutómata.pdf')

    def ventana_Infogeneral(self):
        info=Toplevel()
        info.title("Informacion General")
        info.geometry("500x250")
        info.config(bg='#064663')

        self.combo=ttk.Combobox(info)
        seleccionar=Button(info,text="Seleccionar", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.mostrar_info)
        boton_salir=Button(info, text='Atras',bg="#ECB365", fg="white", font = ("Lemon Juice",14),command=info.destroy)

        label_nombre=Label(info,text="Gramática",bg="#064663", fg="white",font = ("Lemon Juice",14))
        label_nombre.place(x=50,y=50, width=100, height=30)
        self.combo.place(x=160,y=50, width=200, height=30)
        seleccionar.place(x=150,y=150,width=200,height=40)
        boton_salir.place(x=150,y=200,width=200,height=40)
        
        aux=0
        indice=0
        while aux < len(lis_todo):
            elemento=lis_todo[aux]
            if indice==0:
                lista_nombres.append(elemento)
                indice+=1
            elif indice>0 and elemento !="%":
                indice +=1
            elif elemento== "%":
                indice=0
       
            aux+=1
        self.combo["values"]=lista_nombres
        self.combo.current(0)

    def ventana_arbol(self):
        arbol=Toplevel()
        arbol.title("Generar Arbol")
        arbol.geometry("500x250")
        arbol.config(bg='#064663')

        self.combo2=ttk.Combobox(arbol)
        seleccionar=Button(arbol,text="Seleccionar", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.mostrar_info)
        boton_salir=Button(arbol, text='Atras',bg="#ECB365", fg="white", font = ("Lemon Juice",14),command=arbol.destroy)

        label_nombre=Label(arbol,text="Gramática",bg="#064663", fg="white",font = ("Lemon Juice",14))
        label_nombre.place(x=50,y=50, width=100, height=30)
        self.combo2.place(x=160,y=50, width=200, height=30)
        seleccionar.place(x=150,y=150,width=200,height=40)
        boton_salir.place(x=150,y=200,width=200,height=40)
        
        aux=0
        indice=0
        while aux < len(lis_todo):
            elemento=lis_todo[aux]
            if indice==0:
                lista_nombres.append(elemento)
                indice+=1
            elif indice>0 and elemento !="%":
                indice +=1
            elif elemento== "%":
                indice=0
       
            aux+=1
        self.combo2["values"]=lista_nombres
        self.combo2.current(0)


#---------------mostrar la informacion de las gramáticas en una tabla-------------
    def mostrar_info(self):
        nombre_gram=self.combo.get()
        
        aux=0
        indice=0
        nueva_lista=[]
        self.nombre=""
        self.nterminal=""
        self.terminal=""
        self.inicial=""

    #----------------itero los elementos de la gramática y la muestro en los Label ------------
        for elemento in lis_todo:
            if elemento==nombre_gram:
                while aux < len(lis_todo):
                    element=lis_todo[aux]
                    if indice==0:
                        self.nombre=element
                        indice+=1
                    elif indice==1:
                        self.nterminal=element
                        indice+=1
                    elif indice==2:
                        self.terminal=element
                        indice+=1
                    elif indice==3:
                        self.inicial=element
                        indice+=1
                    elif indice>3 and element !="%":
                        nueva_lista.append(element)
                        indice +=1
                    elif element== "%":
                        break
                    aux+=1
            else:   
                aux+=1

        nueva_lista2=[]
        for a in nueva_lista:
            lementos_separados2 = a.replace(" ", "").split(",")  
            nueva_lista2.extend(lementos_separados2)

        for elemento2 in nueva_lista2:
            
            lementos_separados = elemento2.replace("::=", ",").split(",")  
            lista_aux.extend(lementos_separados)
            lista_aux.extend("#")
            
        print(lista_aux)
         
        self.mostrar=Toplevel()
        self.mostrar.title("Informacion")
        self.mostrar.geometry("600x500")
        self.mostrar.config(bg='#064663')

        boton_salir=Button(self.mostrar, text='Atras',bg="#ECB365", fg="white", font = ("Lemon Juice",11),command=self.limpiar_tabla)

        label_nombre=Label(self.mostrar,text="Nombre",bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_noTerminal=Label(self.mostrar,text="No Terminales",bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_terminal=Label(self.mostrar,text="Terminales",bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_inicial=Label(self.mostrar,text="No Terminal inicial",bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_nombre1=Label(self.mostrar,text=self.nombre,bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_noTerminal1=Label(self.mostrar,text=self.nterminal,bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_terminal1=Label(self.mostrar,text=self.terminal,bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_inicial1=Label(self.mostrar,text=self.inicial,bg="#064663", fg="white",font = ("Lemon Juice",11))

        label_nombre.place(x=50,y=50, width=150, height=30)
        label_noTerminal.place(x=50,y=90, width=150, height=30)
        label_terminal.place(x=50,y=130, width=150, height=30)
        label_inicial.place(x=50,y=170, width=150, height=30)
        label_nombre1.place(x=300,y=50, width=150, height=30)
        label_noTerminal1.place(x=300,y=90, width=150, height=30)
        label_terminal1.place(x=300,y=130, width=150, height=30)
        label_inicial1.place(x=300,y=170, width=150, height=30)
        boton_salir.place(x=380,y=210,width=100,height=40)

        #------------------------Creo una tabla para las producciones------
        self.tabla1=ttk.Treeview(self.mostrar,columns="col1")
        self.tabla1.column('#0', width=100)
        self.tabla1.column('col1', width=100)

        self.tabla1.heading('#0',text="No terminales",anchor=CENTER)
        self.tabla1.heading('col1',text="Expresion",anchor=CENTER)

        aux2=0
        indice2=0

    #----------------itero los elementos de la gramática y la muestro en los Label ------------

        while aux2 < len(lista_aux):
            elemento3=lista_aux[aux2]
            if indice2==0:
                no_terminal=elemento3
                indice2+=1
            elif indice2==1:
                terminal2=elemento3
                indice2+=1
            elif elemento3=="#":
                if no_terminal==lista_aux[aux2-1]:
                      
                    self.tabla1.insert("",END,text="|".format(no_terminal),values=(terminal2))       
                else:
                    self.tabla1.insert("",END,text="{}>".format(no_terminal),values=(terminal2))
                        
                indice2=0
            aux2+=1
                

        self.tabla1.place(x=50,y=245)

    def limpiar_tabla(self):
    # Eliminar todos los elementos de la tabla
        self.tabla1.delete(*self.tabla1.get_children())
        self.mostrar.destroy()

    def buscar_archivo(self):
        try:
            self.file = askopenfilename(title="Cargar un archivo", filetypes=[("Archivos", f'*.glc')])
            self.text = self.file
            self.openfile = open(self.text, encoding="utf-8")
            self.archivo = self.openfile.read().split("\n")
            
            for lineas in self.archivo:  
                lis_todo.append(lineas)
            
            tkinter.messagebox.showinfo("Archivo","Se cargo el archivo")
        except:
            print('Error, no se ha seleccionado ningún archivo')

    def buscar_archivo2(self):
        try:
            self.file = askopenfilename(title="Cargar un archivo", filetypes=[("Archivos", f'*.ap')])
            self.text = self.file
            self.openfile = open(self.text, encoding="utf-8")
            self.archivo = self.openfile.read().split("\n")
            
            for lineas in self.archivo:  
                lis_todoPila.append(lineas)
            print(lis_todoPila)
            tkinter.messagebox.showinfo("Archivo","Se cargo el archivo")
        except:
            print('Error, no se ha seleccionado ningún archivo')
        
    def bienvenida(self):

        self.ventana3=Toplevel()
        self.ventana3.title("Gramáticas")
        self.ventana3.geometry("500x250")
        self.ventana3.config(bg='#064663')
        
        self.label =Label(self.ventana3, text="")
        self.label.pack()
        label1 =Label(self.ventana3, text="",background="#0E8388")
        label1.pack()
        curso=Label(self.ventana3,text="Lab. Lenguajes Formales y de Programacion P",font=22, background="#ffffff")
        curso.pack()
        label2 =Label(self.ventana3, text="",background="#0E8388")
        label2.pack()
        programa=Label(self.ventana3,text="Spark Stack",font=22, background="#ffffff")
        programa.pack()
        label3 =Label(self.ventana3, text="",background="#0E8388")
        label3.pack()
        Nombre=Label(self.ventana3,text="Fernando Misael Morales Ortíz",font=22, background="#ffffff")
        Nombre.pack()
        label4 =Label(self.ventana3, text="",background="#0E8388")
        label4.pack()
        carnet=Label(self.ventana3,text="202001950",font=22, background="#ffffff")
        carnet.pack()
        self.after(0, self.ventana_contador, tiempo)
  

    def ventana_contador(self,segundos):
        if segundos > 0:
            self.label.config(text=f"Espere {segundos} segundos...")
            segundos -= 1
            self.after(1000, self.ventana_contador, segundos)
            
        elif segundos==0:
            self.label.destroy()
            self.ventana_principal()

    def despedida(self):

        self.ventana3=Toplevel()
        self.ventana3.title("Gramáticas")
        self.ventana3.geometry("500x250")
        self.ventana3.config(bg='#064663')

        self.label2 =Label(self.ventana3, text="")
        self.label2.pack()
        label1 =Label(self.ventana3, text="",background="#0E8388")
        label1.pack()
        programa=Label(self.ventana3,text=" Cierre de Spark Stack",font=22, background="#ffffff")
        programa.pack()
        label3 =Label(self.ventana3, text="",background="#0E8388")
        label3.pack()
        Nombre=Label(self.ventana3,text="Fernando Misael Morales Ortíz",font=22, background="#ffffff")
        Nombre.pack()
        label4 =Label(self.ventana3, text="",background="#0E8388")
        label4.pack()
        carnet=Label(self.ventana3,text="202001950",font=22, background="#ffffff")
        carnet.pack()
        self.after(0, self.ventana_contador2, tiempo)
  
    def ventana_contador2(self,segundos):
        if segundos > 0:
            self.label2.config(text=f"Espere {segundos} segundos...")
            segundos -= 1
            self.after(1000, self.ventana_contador2, segundos)
            
        elif segundos==0:
            self.label.destroy()
            self.quit()

root=Tk()
app=Mi_ventan(root)
app.mainloop()
