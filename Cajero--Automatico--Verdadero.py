#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

lista=[]
usuario=[]
password=[]
nombre=[]
rut=[]
apellidos=[];
celular=[]
contador=0;
total=(1000000);
mostrar=[];
calcular=();

def IngresosUsuarios():
	lista=[]
	usuario="admin"
	password="root"
	print"*************Bienvenidos Administrador**********"
	usuario=raw_input("Ingrese Usuario   : ")
	password=raw_input("Ingrese Password : ")
	print"************* S.A ******************************"
	lista.append(usuario)
	lista.append(password)
	if(usuario=="admin" and password=="root"):
		print"\n"
		print"Credenciales Validas ....!!!!"
		Menu()
	elif(usuario<>"admin" or  password<>"root"):
		print"\n"
		print"Credenciales Invalidas ....!!!!"
		os.system("cls")
		IngresosUsuarios()
		print"Bienvenidos Al Sistema!!!!!"
def Menu():
	DEPOSITOS = []
	GIROS = []
	SALDO=0
	op=""
	while(op<>"9"):
		os.system("cls")
		print "[1] DEPOSITAR"
		print "[2] GIRAR"
		print "[3] MOSTRAR DEPOSITOS"
		print "[4] MOSTRAR GIROS"
		print "[5] MOSTRAR SALDO"
		print "[6] Ingreso Cliente"
		print "[9] SALIR"
		op = raw_input("Ingrese opcion : ")
		if op=="1":
			#llamar a la funcion que insertara
			D= deposito()
			SALDO= calculo_saldo(SALDO,D,0)
			insertar_lista(DEPOSITOS,D)
		elif op=="2":
			#llamar a la funcion que hara giro
			G = giro()
			
			if SALDO>G:
				SALDO= calculo_saldo(SALDO,0,G)
				insertar_lista(GIROS,G)			
		elif op=="3":
			#llamar a la funcion que sumara
			mostrar_dep(DEPOSITOS)
		elif op=="4":
			mostrar_gir(GIROS)	
		elif op=="5":
			mostrar_saldo(SALDO)
		elif op=="6":
			InsertarDatosCliente()	
		elif op=="9":
			print "ADIOS..... BYE... BYE"
		else:
			print "OPCION NO VALIDA"
		raw_input()

def calculo_saldo(saldo,dep, giro):
	if giro>saldo:
		giro=0
		print "Saldo Insuficiente"
	s= saldo+dep-giro	
	return s
	
	
def deposito():
	num = int(raw_input("Ingrese Monto Depositar : "))
	return num

def giro():
	num = int(raw_input("Ingrese Monto a Girar : "))
	return num
	
def insertar_lista(lista,num):
	lista.append(num)
	
def mostrar_dep(lista):
	for e in lista:
		print "Deposito : ",e
		
def mostrar_gir(lista):
	for e in lista:
		print "Giro : ",e

def mostrar_saldo(s):
	print "Saldo De La Cuenta : ",s

def InsertarDatosCliente():
	lista=[]
	rut=int(raw_input("Ingrese Rut Cliente : "))
	nombre=raw_input("Ingrese Nombre Cliente : ")
	apellidos=raw_input("Ingrese Apellido : ")
	celular=int(raw_input("Ingrese Numero Celular : "))
	if rut==[]:
		print"Rut Agregado Correctamente"
	if nombre==[]:
		print"Nombre Agregado Correctamente"
	if apellidos==[]:
		print"Apellidos Agregado Correctamente"
	if celular==[]:
		print"Celular Agregado Correctamente"
	#seccion de las lista---Arreglos---> son siempre se declara asi lista=[]
	lista.append(rut)
	lista.append(nombre)
	lista.append(apellidos)
	lista.append(celular)
	#fin de agregar
	print "\n"
	print lista#imprimo la lista de los arreglos agregados anteriormente-->:)

def main():
	IngresosUsuarios()
	raw_input()
	
if __name__ == '__main__':
	main ()


