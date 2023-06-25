from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 

tiempo=5
lis_todo=[] #sirve al abrir el archivo
lista_nombres=[]    #sirve para los nombres y tenerlos en el combobox
lista_aux=[]        #tiene las producciones para luego llamarlas
class Mi_ventan(Frame):
    

    def __init__(self, master=None):
        super().__init__(master, width=500,height=300,bg='#064663')
        self.master=master
        self.pack()
        self.bienvenida()


    def ventana_principal(self):
        self.ventana3.destroy()
       
        self.gramatica=Button(self,text="Módulo Gramáticas", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.ventana_gramaticas).place(x=150,y=50,width=200,height=40)
        self.automatas=Button(self,text="Módulo Autómatas", bg="#ECB365", fg="black", font = ("Lemon Juice",14)).place(x=150,y=100,width=200,height=40)
        self.salir=Button(self,text="Salir", bg="#0E8388", fg="white", font = ("Lemon Juice",14), command=self.despedida).place(x=150,y=150,width=200,height=40)
       
    def ventana_gramaticas(self):
        ventana2=Toplevel()
        ventana2.title("Gramáticas")
        ventana2.geometry("500x250")
        ventana2.config(bg='#064663')

        Carga=Button(ventana2,text="Carga Archivo", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.buscar_archivo)
        informacion=Button(ventana2,text="Informacion General", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=self.ventana_Infogeneral)
        arbol=Button(ventana2,text="Arbol de Derivación", bg="#0E8388", fg="white", font = ("Lemon Juice",14))
        boton_salir=Button(ventana2, text='Salir',bg="#ECB365", fg="white", font = ("Lemon Juice",14),command=ventana2.destroy)

        Carga.place(x=150,y=50,width=200,height=40)
        informacion.place(x=150,y=100,width=200,height=40)
        arbol.place(x=150,y=150,width=200,height=40)
        boton_salir.place(x=150,y=200,width=200,height=40)

    def ventana_Infogeneral(self):
        info=Toplevel()
        info.title("Informacion General")
        info.geometry("500x250")
        info.config(bg='#064663')

        combo=ttk.Combobox(info)
        seleccionar=Button(info,text="Seleccionar", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.mostrar_info)
        boton_salir=Button(info, text='Atras',bg="#ECB365", fg="white", font = ("Lemon Juice",14),command=info.destroy)

        label_nombre=Label(info,text="Gramática",bg="#064663", fg="white",font = ("Lemon Juice",14))
        label_nombre.place(x=50,y=50, width=100, height=30)
        combo.place(x=160,y=50, width=200, height=30)
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
        combo["values"]=lista_nombres
        combo.current(0)
        self.separar()

#--------------separo las producciones para meterlos en una tabla
    def separar(self):
        aux=0
        indice=0
        
        nueva_lista=[]
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

#---------------mostrar la informacion de las gramáticas
    def mostrar_info(self):
        aux=0
        indice=0
        while aux < len(lis_todo):
            elemento=lis_todo[aux]
            if indice==0:
                nombre=elemento
                indice+=1
            elif indice==1:
                nterminal=elemento
                indice+=1
            elif indice==2:
                terminal=elemento
                indice+=1
            elif indice==3:
                inicial=elemento
                indice+=1
            elif indice>3 and elemento !="%":
                indice +=1
            elif elemento== "%":
                break
       
            aux+=1
        mostrar=Toplevel()
        mostrar.title("Informacion")
        mostrar.geometry("600x500")
        mostrar.config(bg='#064663')

        boton_salir=Button(mostrar, text='Atras',bg="#ECB365", fg="white", font = ("Lemon Juice",11),command=mostrar.destroy)

        label_nombre=Label(mostrar,text="Nombre",bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_noTerminal=Label(mostrar,text="No Terminales",bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_terminal=Label(mostrar,text="Terminales",bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_inicial=Label(mostrar,text="No Terminal inicial",bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_nombre1=Label(mostrar,text=nombre,bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_noTerminal1=Label(mostrar,text=nterminal,bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_terminal1=Label(mostrar,text=terminal,bg="#064663", fg="white",font = ("Lemon Juice",11))
        label_inicial1=Label(mostrar,text=inicial,bg="#064663", fg="white",font = ("Lemon Juice",11))

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
        tabla1=ttk.Treeview(mostrar,columns="col1")
        tabla1.column('#0', width=250)
        tabla1.column('col1', width=250)

        tabla1.heading('#0',text="No terminales",anchor=CENTER)
        tabla1.heading('col1',text="Expresion",anchor=CENTER)
        aux2=0
        indice2=0
        while aux2 < len(lista_aux):
            elemento2=lista_aux[aux2]
            if indice2==0:
                nombre=elemento2
                indice2+=1

            elif indice>3 and elemento !="%":
                indice +=1
            elif elemento== "%":
                break
       
            aux+=1

        tabla1.place(x=50,y=245)

    def buscar_archivo(self):
        try:
            self.file = askopenfilename(title="Cargar un archivo", filetypes=[("Archivos", f'*.glc')])
            self.text = self.file
            self.openfile = open(self.text, encoding="utf-8")
            self.archivo = self.openfile.read().split("\n")
            
            for lineas in self.archivo:  
                lis_todo.append(lineas)
            print(lis_todo)
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
