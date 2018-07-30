#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
Listar2=["M1234","DIFARE","Ecuador","Avenida Francisco Orellana","2-2144556","Difare1984@gmail.com"]
Continente=["America","Asia","Europa"]
lista=[]
def desarrollo():
	dicc={}
	usuario()
	mostrar(dicc)
	mostrar_todo(dicc)
	mostrar_1(dicc)
	
def usuario():
	usuario="admin"
	password="root"
	ingresousuario=raw_input("INGRESE USUARIO:")
	ingresopassword=raw_input("INGRESE PASSWORD:")
	if ingresousuario==usuario and ingresopassword==password:
		print("BIENVENIDO AL MENU PRINCIPAL")
		menu()
	
def menu():
	op=""
	while(op!="9"):
		os.system("cls")
		print("**********Gestion Articulos *************")
		
		print ("\nMENU PRNCIPAL\n")
		print ("[1] Proveedor")
		print ("[2] Producto")
		print ("[9] SALIR")
		
		print("**********Bodega---S.A *******************")
		print("\n")
		op =raw_input("Ingrese opcion : ")
		if op=="1":
			 Proveedor()
		elif op=="2":
			Producto()	
		elif op=="9":
			print ("BYE BYE ....HASTA LA PROXIMA....")
			exit			
		else:
			print ("OPCION NO VALIDA")
			input()
########################################################################
'''
SECCION DE REGISTRO DE PROVEEDORES
'''
########################################################################
def Proveedor():
	r=[]
	DICC={ }	
	op="0"
	while op!="9":
		os.system("cls")
		print ("[1] Registra Proveedor")
		print ("[2] Mostrar Proveedor")
		print ("[3] Listar Proveedor")
		print ("[9] salir")
		op = raw_input("Digite Opcion : ")		
		if(op=="1"):
			ProveedorRegistrado()
			agregar(DICC)	
			print("\n")		
			print (" Proveedor Registrado Exitosamente !!!!")
		elif(op=="2"):
			mostrar_todo(DICC)
		elif (op=="3"):
			mostrar_Proveedor(DICC,r)
		elif(op=="9"):
			print ("ADIOS,.....")
			menu()
		else:
			print("\n")
			print ("OPCION NO VALIDA")
		raw_input()
def ProveedorRegistrado():
	print("\n")
	print("Codigo: ",Listar2[0])
	print("Nombre: ",Listar2[1])
	print("Pais : ",Listar2[2])
	print("Dirreccion: ",Listar2[3])
	print("Telefono: ",Listar2[4])
	print("Correo Electronico: ",Listar2[5])	
	
def agregar(dicc):
	llave = ingreso_codigo()
	info =[]
	ingreso_info(info)
	dicc[llave] = info
	

def mostrar_Proveedor(dicc,r):
	print("\n")
	CodigoProveedor = raw_input("Ingrese Codigo Del Proveedor a imprimir : ")
	print("\n")
	if CodigoProveedor == CodigoProveedor:
		print("Codigo Correcto Proveedor !!!!")
		print("\n")
		print (dicc[CodigoProveedor])
	elif CodigoProveedor!= CodigoProveedor:
		print("Codigo No Existe Base Datos !!!!!")
		print("\n")
		
def mostrar_todo(dicc):
	for r, inf in dicc.items():
		print("***********************************************")
		print ("Codigo       : ",str(r))
		print ("Nombre       : ",str(inf[0]))
		print ("Pais         : ",str(inf[1]))
		print ("Dirreccion   : ",str(inf[2]))
		print ("Telefono     : ",str(inf[3]))
		print ("Correo       : ",str(inf[4]))
		print("***********************************************")
		
def ingreso_info(lista):
	lista.append(ingreso_nombre())
	lista.append(ingresoPais())
	lista.append(IngresoDireccion())
	lista.append(Telefono())
	lista.append(Correo())
def ingreso_nombre():
	nombre=[]
	nombre=raw_input("Ingrese Nombre Proveedor :  ")
	return nombre
	lista.append(nombre)

def ingresoPais():
	pais=raw_input("Ingrese Pais Proveedor : ")
	return pais
	lista.append(pais)

def IngresoDireccion():
	dirreccion=[]
	dirreccion=raw_input("Ingrese Direccion : ")
	return dirreccion	
	lista.append(dirreccion)
	
def Telefono():
	telefono=[]
	telefono=raw_input("Ingrese Telefono Contacto : ")
	return telefono	
	lista.append(telefono)
	
def Correo():
	correo=[]
	correo=raw_input("Ingrese Correo Electronico :")
	return correo	
	lista.append(correo)

def ingreso_codigo():
	codigo=[]
	print("\n")
	codigo=raw_input("Ingreso Codigo Proveedor : ")
	return codigo
	lista.append(codigo)


def VerificarProveedor():
	Listar2=["M1234","DIFARE","Ecuador","Avenida Francisco Orellana","2-2144556","Difare1984@gmail.com"]
	if(Listar2[0]!=codigo[0] and Listar2[1]!=nombre[1] and Listar2[2]!=pais[2] and Listar2[3]!=correo[3] and Listar2[4]!=dirreccion[4] and Listar2[5]!=telefono[5]):
		print("Proveedor Registrado Exitosamente !!!!")	
	elif(Listar2[0]==codigo[0] or Listar2[1]==nombre[1] or Listar2[2]==pais[2]or Listar2[3]==correo[3] or Listar2[4]==dirreccion[4] or Listar2[5]==telefono[5]):
		print("Proveedor Ya Existe En Nuestra Base De Datos !!!!!!")
	else:
		print("Error 404 not Found")

###################################################################################
'''
SECCION DE Productos Electronicos
'''
###################################################################################
def Producto():
	dicc={ }	
	op="0"
	while op!="9":
		os.system("cls")
		print ("[1] Registra Producto")
		print ("[2] Mostrar Producto")
		print ("[3] Listar Producto")
		print ("[9] salir")
		op = raw_input("Digite Opcion : ")		
		if(op=="1"):
			agregarProducto(dicc)
			print("\n")		
			print ("Producto Registrado Exitosamente !!!!")
		elif(op=="2"):
			mostrar_Producto(dicc)
		elif (op=="3"):
			mostrar_ProDucto(dicc)
		elif(op=="9"):
			print ("ADIOS,.....")
			menu()
		else:
			print("\n")
			print ("OPCION NO VALIDA")
			input()
	
def agregarProducto(dicc):
	LLAVE= Ingreso_CodigoProducto()
	producto =[]
	ingreso_info_Producto(producto)
	dicc[LLAVE] = producto
	
def ingreso_info_Producto(Lista):
	Lista.append(ingreso_nombre_producto())
	Lista.append(Ingresa_Categoria())
	Lista.append(IngresoMarca())
	Lista.append(IngresoModelo())
	Lista.append(Ingresa_Continente())
	Lista.append(Ingreso_precio())
	Lista.append(Ingreso_cantidad())	
def Ingresa_Categoria():
	Lista=[]
	global inp
	global iva
	global precio
	cate=" "
	###################################
	cate=[0,"Computador",2,"Camara",4,"Drone"]
	print (cate)
	###############################
	print("\n")
	cate=raw_input("Ingrese categoria : ")
		
	if cate=="1":
		print("\n")
		print("Eligiste Computador!!!")
		'''
		inp= precio * 0.03
		iva = precio * 0.19
		return inp 
		return iva	
		'''	
	elif cate=="3":
		print("\n")
		print("Camara Fotografica")
		'''
		inp= precio* 0.05
		iva = precio * 0.19
		return inp 
		return iva	
		'''	
	elif cate=="5":
		print("\n")
		print("Drone")
		'''
		inp= precio * 0.04
		iva = precio * 0.19
		return inp 
		return iva	
		'''	
	else:
		print("\n")
		print("El Producto Buscas No Existe")
		print("\n")
		Ingresa_Categoria()
def Ingresa_Continente():
	Lista=[]
	Pfinal=[]
	america=[]
	asia=[]
	europa=[]
	cate=" "
	global precio 
	global iva
	global inp
	C=[0,"America",2,"Asia",4,"Europa"]
	print (C)
	print("\n")
	cate=(raw_input("Ingrese Continente : "))
	print("\n")
	if cate=="1":
		print("Eligiste America !!!! ")
		'''
		continente=precio*0,1
		pfinal=precio+continente+iva+inp
		Lista.append(pfinal)
		dicc=[pfinal]
		iva=0
		inp=0
		precio=0
		return iva
		return inp
		return precio
		'''
	elif cate=="3":
		print("Eligiste Asia !!!!! ")
		'''
		continente=precio*0,07
		Pfinal=precio+continente+iva+inp
		Lista.append(Pfinal)
		dicc=[Pfinal]
		iva=0
		inp=0
		precio=0
		return iva
		return inp
		return precio
		'''
	elif cate=="5":
		print("Eligiste Europa !!!!! ")
		'''
		continente=precio*0,14
		pfinal=precio+continente+iva+inp
		Lista.append(pfinal)
		dicc=[pfinal]
		iva=0
		inp=0
		precio=0
		return iva
		return inp
		return precio
		'''
	else:
		print("\n")
		print("El Continente Que Buscas No Existe")
		Ingresa_Continente()
		
def IngresoMarca():
	marca=raw_input("Ingrese Marca Producto : ")
	return marca
	
def IngresoModelo():
	modelo=raw_input("Ingrese Modelo Producto : ")
	return modelo
	
def Ingreso_precio():
	precio=float(raw_input("Ingrese Precio del Producto : "))
	return precio
	
def Ingreso_cantidad():
	cantidad=int(raw_input("Ingrese Cantidad Llevar : "))
	return cantidad			
	
def ingreso_nombre_producto():
	nombreproducto=raw_input("Ingrese Nombre del Producto : ")
	return nombreproducto
	
def Ingreso_CodigoProducto():
	codigoproducto=raw_input("Ingrese Codigo del Producto : ")
	return codigoproducto
	
def mostrar_Producto(dicc):
	for r, inf in dicc.items():
		print("***********************************************")
		print ("Codigo           : ",str(r))
		print ("Nombre           : ",str(inf[0]))
		print ("Categoria        : ",str(inf[1]))
		print ("Marca            : ",str(inf[2]))
		print ("Modelo           : ",str(inf[3]))
		print ("Continente       : ",str(inf[4]))
		print ("precio           : ",str(inf[5]))
		print ("Cantidad         : ",str(inf[6]))
		print("***********************************************")

def mostrar_ProDucto(dicc):
	print("\n")
	codigoProDucto=raw_input("Ingrese Codigo del Producto A Imprimir : ")
	print("\n")
	if codigoProDucto == codigoProDucto :
		print("Codigo Correcto Producto !!!!")
		print("\n")		
	print dicc[codigoProDucto]

def main():
	menu()	
if __name__=='__main__':
	main ()
