import tkinter
import customtkinter 
import datetime
import random
from datetime import datetime
from datetime import timedelta
from customtkinter import *
#Apariencia de la ventana
customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")
#Creacion de la ventana
ventana = customtkinter.CTk()
ventana.geometry("500x500")
#Tab
texto_actividades = customtkinter.CTkLabel(master=ventana, text = "Actividades", font= ("NORMAL",18))
texto_actividades.pack(pady = 5)
pestaña = customtkinter.CTkTabview(master=ventana)
pestaña.pack(padx=20,pady = 10)
lunes = pestaña.add("Lunes")
martes = pestaña.add("Martes")
miercoles = pestaña.add("Miercoles")
jueves = pestaña.add("Jueves")
viernes = pestaña.add("Viernes")
sabado = pestaña.add("Sabado")
domingo = pestaña.add("Domingo")
#Entradas
cantidad = customtkinter.CTkEntry(master=ventana)
cantidad.pack(padx=10,side = LEFT)
cantidad_actividades = cantidad.get()
#Label
texto_cantidad = customtkinter.CTkLabel(master=ventana, text="Ingresa la cantidad de actividades",font=("NORMAL",16))
texto_cantidad.pack(side =LEFT)

#Clase dia (funcion especial: trabajo de objetos y orden de actividades)
class dias:

    def __init__(self):
        " "
    def listaAlumnos(self):
        self.lista_dias = [Lunes,Martes,Miercoles,Jueves,Viernes,Sabado,Domingo]
        # return lista_dias
#Armar pestañas, y guardar texto
    def armar(self, estructura):
        #Entry 1 (Primer row)
        self.entry1 = customtkinter.CTkEntry(master=estructura, width= 120, height= 50, font=("Roboto Cn", 18))
        self.entry1.grid(row = 0, column = 0, pady = 5, padx = 5)
        #Entry 2 (Primer row)
        self.entry2 = customtkinter.CTkEntry(master=estructura, width= 120, height= 50, font=("Roboto Cn", 18))
        self.entry2.grid(row = 0, column = 1, pady = 5, padx = 5)
        #Entry 3 (Primer row)
        self.entry3 = customtkinter.CTkEntry(master=estructura, width= 120, height= 50, font=("Roboto Cn", 18))
        self.entry3.grid(row = 0, column = 2, pady = 5, padx = 5)
        #Entry 1 (Segundo row)
        self.entry4 = customtkinter.CTkEntry(master=estructura, width= 120, height= 50, font=("Roboto Cn", 18))
        self.entry4.grid(row = 1, column = 0 , pady = 5 , padx = 5)
        #Entry 2 (Segundo row)
        self.entry5 = customtkinter.CTkEntry(master=estructura, width= 120, height= 50, font=("Roboto Cn", 18))
        self.entry5.grid(row = 1, column = 1 , pady = 5, padx = 5)
        #Entry 3 (Segundo row)
        self.entry6 = customtkinter.CTkEntry(master=estructura, width= 120, height= 50, font=("Roboto Cn", 18))
        self.entry6.grid(row = 1, column = 2 , pady = 5, padx = 5)
        #Entry 1 (Tercer row, columna 1)
        self.entry7 = customtkinter.CTkEntry(master=estructura, width= 120, height= 50, font=("Roboto Cn", 18))
        self.entry7.grid(row = 2, column = 1 , pady = 5, padx = 5)
    def conseguir_texto(self):
        lista = [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get(), self.entry7.get()]
        return (lista)
#Lo que permite dar un dato aleatorio en tanto a las horas, y a las actividades diarias
    def randomact(self, lista):
        for act in lista:
            if act == "":
                lista.remove(act)
        resultado = random.sample(lista, k = int(texto_cantidad))
        print(resultado)
        return resultado
#Saber cual dia de la semana es
    def diaActual(self):
        listadias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        dia = datetime.now()
        horadia = dia.strftime("%d-%m-%Y %H:%M:%S")
        estructura = "%d-%m-%Y %H:%M:%S"
        d = datetime.strptime(horadia, estructura)
        return listadias[d.weekday()]
#Buscar dia
    def BuscarPorNombre(self, nombre):
        for dia_semana in self.lista_dias:
            if dia_semana == nombre:
                return dia_semana
#Mandar gmail
    def Gmail():
        "hola"
#Guardar texto
    def guardar_texto(self,diaActual):
        for dia in self.lista_dias:
            dia.conseguir_texto()
            if dia == diaActual:
                dia.randomact(dia.conseguir_texto())
#Objetos (Dias) / Crear una lista de los dias
Lunes = dias()
Martes = dias()
Miercoles = dias()
Jueves = dias()
Viernes = dias()
Sabado = dias()
Domingo = dias() 
instancia = dias()
#Crear las ventanas
Lunes.armar(lunes)
Martes.armar(martes)
Miercoles.armar(miercoles)
Jueves.armar(jueves) 
Viernes.armar(viernes)
Sabado.armar(sabado)
Domingo.armar(domingo)
#Instancias
instancia.listaAlumnos()
Diaactual = instancia.diaActual()
dia_act = instancia.BuscarPorNombre(Diaactual)
# while Diaactual != Diaactual:
#     Diaactual = instancia.diaActual
#Botones
boton_guardar = customtkinter.CTkButton(master=ventana, command = lambda: instancia.guardar_texto(Diaactual), width= 20, height=20, text="Guardar")
boton_guardar.pack(side=TOP)
# boton_guardar = customtkinter.CTkButton(master=ventana, command = lambda: instancia.print_dia, width= 20, height=20, text="Print")
# boton_guardar.pack(side=TOP)
ventana.mainloop()