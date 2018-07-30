#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
mostrar=[]

Listar1=["Codigo","Nombre","Pais","Direccion","Telefono","Correo Electronico"]
Listar2=["M1234","DIFARE","Ecuador","Avenida Francisco Orellana","2-2144556","Difare1984@gmail.com"]
LISTA=[]
def Menu():
	opcion=" "
	LISTA=[]
	while(opcion!="0"):
		os.system("cls")
		print("\n")
		print("**********Gestion Articulos *************")
		print("[1] Registrar Proveedor ")
		print("[2] Registrar Producto Electronico ")
		print("[3] Listar Proveedores ")
		print("[4] Listar Producto Electronico ")
		print("[5] Eliminar Proveedor ")
		print("[6] Eliminar Producto ")
		print("[0] Salir ")
		print("**********Bodega---S.A *******************")
		print("\n")
		opcion =int(input(" Opcion : "))
			
		if opcion=="1":
			VerificarProveedor()
		elif opcion=="2":
			RegistrarProducto()
		elif opcion=="3":
			mostrar(LISTA)
		elif opcion=="4":
			cuarto()
		elif opcion=="5":
			eliminar_elem(lista)
		elif opcion=="6":
			eliminar_elem(lista)		
		elif opcion=="0":
			print ("BYE BYE ....HASTA LA PROXIMA....")
			exit	
		else:
			print ("OPCION NO VALIDA")
			raw_input()
def VerificarProveedor():
	print("***************Nombre Proveedor Registrado********************",
	"\n",Listar1[0],":",Listar2[0],"\n",Listar1[1],":",Listar2[1],
	"\n",Listar1[2],":",Listar2[2],"\n",Listar1[3],":",Listar2[3],
	"\n",Listar1[4],":",Listar2[4],"\n",Listar1[5],":",Listar2[5],
	"\n","************************************************************")
	ReingresoProveedores()
#########################################################################
def ReingresoProveedores():
	opcion=" "
	while(opcion!="2"):
		os.system("cls")
		print("\n")
		print("Quieres Ingresar Otro Proveedor ")
		print("\n")
		print("[1] SI ")
		print("[2] NO ")
		print("\n")
		opcion =(input(" Opcion : "))	
		if opcion=="1":
			RegistroProveedores()
		elif opcion=="2":
			Menu()
		else:
			print ("OPCION NO VALIDA")	
				
def RegistroProveedores(LISTA):
	LISTA=[]
	codigo=input("Ingrese Codigo del Proveedor : ")
	nombre=input("Ingrese Nombre del Proveedor : ")
	pais=input("Ingrese Pais : ")
	dirreccion=input("Ingrese Direccion : ")
	correo=input("Ingrese Correo Electronico : ")
	telefono=int(input("Ingrese Numero Telefono : "))
	
	LISTA.append(codigo())
	LISTA.append(nombre())
	LISTA.append(pais())
	LISTA.append(dirreccion())
	LISTA.append(correo())
	LISTA.append(telefono())
	
def mostrar(LISTA):
	m=int(input("Ingrese Codigo Proveedor : "))
	print (LISTA[m])
		
def RegistrarProducto():
	print("\n")
	codigoProveedor=(input("Ingrese Codigo del Producto : "))
	opcion=" "
	while(opcion!="3"):
		os.system("cls")
		print("Categoria  ")
		print("\n")
		print("[1] Computador ")
		print("[2] Camara Fotografica ")
		print("[3] Drone ")
		print("\n")
		opcion =(input("Ingresa Opcion : "))
			
		if opcion=="1" or opcion=="2" or opcion=="3":
			IngresoMarca()
			IngresoModelo()
			continente()	
		else:
			print("\n")
			print ("OPCION NO VALIDA")

def continente():
	op=" "
	while(op!="3"):
		os.system("cls")
		print("Elige Continente  ")
		print("\n")
		print("[1] America ")
		print("[2] Asia ")
		print("[3] Europa ")
		print("\n")
		op =(input("Ingresa Opcion : "))
			
		if op=="1":
			precio()
			cantidad()
			Menu()
		elif op=="2":
			precio()
			cantidad()
			Menu()
		elif op=="3":
			precio()
			cantidad()
			Menu()
		else: 
			print ("OPCION NO VALIDA")
			
def IngresoMarca():
	marca=(input("Ingrese Marca Producto : "))
	return marca
def IngresoModelo():
	modelo=(input("Ingrese Modelo Producto : "))
	return modelo
def precio():
	precio=int(input("Ingrese Precio del Producto : "))
	return precio
def cantidad():
	cantidad=int(input("Ingrese Cantidad Llevar : "))
	return cantidad	
def Codigo():
	codigo=input("Ingrese Codigo del Proveedor Eliminar : ")
	return codigo	

def main():
	Menu()
	 	
if __name__ == '__main__':
	main () 




















