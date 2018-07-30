#!/usr/bin/python
# -*- coding: utf-8 -*-
#importamos la libreria de limpiar pantalla

import os
import sys

lista=[]
retiro=[]
usuario=[]
password=[]
nombre=[]
rut=[]
apellidos=[];
celular=[]
contador=0;
total=(1000000);
dinero_maximo=(250000)
girar=[];
depositar=[];
mostrar=[];
calcular=();
def IngresosUsuarios():
	lista=[]
	usuario="admin"
	password="root"
	usuario=(input("Ingrese Usuario   : "))
	password=(input("Ingrese Password : "))
	lista.append(usuario)
	lista.append(password)
	if(usuario=="admin" and password=="root"):
		print("Credenciales Validas ....!!!!")
		Menu()
	elif(usuario!="admin" or  password!="root"):
		print("Credenciales Invalidas ....!!!!")
		os.system("cls")
		IngresosUsuarios()
		print("Bienvenidos Al Sistema!!!!!")
def Menu():
	opcion=" "
	while(opcion!="0"):
		os.system("cls")
		print("Bienvenidos Administrador ",lista)
		print("**********Banco Santander *************")
		print("[1] Depositar ")
		print("[2] Ingreso Datos ")
		print("[3] Retirar ")
		print("[0] Salir ")
		print("**********Banco S.A *******************")
		print("\n")
		opcion =(input(" Opcion : "))
			
		if opcion=="1":
			Depositar()
		elif opcion=="2":
			InsertarDatosCliente()
		elif opcion=="3":
			retiro()		
		elif opcion=="0":
				print ("BYE BYE ....HASTA LA PROXIMA....")
				IngresosUsuarios()			
		else:
			print ("OPCION NO VALIDA")
		input()

def Depositar():
	depositar=[]
	girar=[]
	total=(1000000)
	d=int(input("Ingrese Dinero Depositar : "))
	depositar.append(d)
	calcular = total + d
	depositar.append(calcular)
	print("\n")
	print("Saldo Dinero Anterior : --> ",str(total))
	print("\n")
	print("Dinero Depositado : ---> ",str(depositar))
	print("Monto Total Dinero:  ---> ",str(calcular))
	mostrar.append(calcular)
	print("*****************************************")
	
def retiro():
	g=0
	ListaP=[]
	m=(mostrar[0])
	dinero_maximo=(250000)
	girar=[m,g]#concateno Variable
	os.system("cls")
	print("\n")
	print("Dinero Maximo Retirar Al Dia es  : ",str(dinero_maximo))
	print("\n")
	Cliente=(input("Ingrese Cliente Buscar : "))
	print("\n")
	print("Usted Escogio --> ",str(Cliente))
	print("\n")
	g=int(input("Ingrese Dinero A Retirar : "))
	girar.append(g)
	calculo= (m-g)
	print("Su Saldo es : ",str(calculo))
	while(g >= dinero_maximo):
			print("Ha Excedido Monto Permitido")
			retiro()
			if (g <= dinero_maximo):
				print("Usted Ha Retirado : ",str (g))
				print("\n")
			print("Gracias Por Preferirnos!!!!!")
			break
	Cliente=["juan","norma ","oscar","miguel","Karito"]
	Saldo=[Cliente[0],500000,Cliente[1],600000,Cliente[2],800000,Cliente[3],650000,Cliente[4],750000]


def InsertarDatosCliente():
	lista=[]
	rut=int(raw_input("Ingrese Rut Cliente : "))
	nombre=raw_input("Ingrese Nombre Cliente : ")
	apellidos=raw_input("Ingrese Apellido : ")
	celular=int(raw_input("Ingrese Numero Celular : "))
	if rut==[]:
		print("Rut Agregado Correctamente")
	if nombre==[]:
		print("Nombre Agregado Correctamente")
	if apellidos==[]:
		print("Apellidos Agregado Correctamente")
	if celular==[]:
		print("Celular Agregado Correctamente")
	#seccion de las lista---Arreglos---> son siempre se declara asi lista=[]
	lista.append(rut)
	lista.append(nombre)
	lista.append(apellidos)
	lista.append(celular)
	#fin de agregar
	print ("\n")
	print (" ",str (lista))#imprimo la lista de los arreglos agregados anteriormente-->:)

def main():
	IngresosUsuarios()
	
if __name__ == '__main__':
	main () 
