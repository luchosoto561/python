# lo que tengo que hacer es un proyecto en el cual creo una lista de libros y le pido al usuario que ingrese
# nombre de autor que le gusta y cantidad de paginas que tolera leer; a partir de ahi le recomiendo uno de los 
# libros que tengo segun su gusto; ademas puede la persona traer para donar un libro por lo que tengo que 
# hacer en ese caso es agregarlo a mi biblioteca; puedo crear una interfaz grafica con la biblioteca tkinder
import tkinter as tk

class Libro: #self es un parametro que hace referencia a la instancia del objeto
    def constructor(self,cantpag,nombre):
        self.cantpag=cantpag
        self.nombre=nombre

lista=[Libro(120,"el principito"),Libro(356,"Los secretos de la mente Millonaria"),Libro(4355,"stalins"),Libro(324,'la bella y la bestia'),Libro(785,"Joyeria Encantada")]
proposito=input("escriba retirar si vino para retirar un libro, si vino para donar escriba donar")

if(proposito=="retirar"):
    autor=input("ingrese el nombre del autor que le gustaria leer")
    pagoptimo=input("ingrese la cantidad de paginas que desea leer aproximadamente del autor antes mencionado")
    #tengo que recomendar uno de los libros segun los gustos del logi este
    indice=0
    encontro=False
    while( indice < len(lista) ):
        if(lista[indice].cantpag==pagoptimo or lista[indice].nombre==autor ):
            print("se encontro el libro que buscas")
            encontro=True
            break
        else:
            indice+=1
    if(encontro==False):
        print("no tenemos ese libro que asi que pedilo corta la bocha")    
else:
    autor=input("ingrese el autor del libro")
    cantpag=input("ingrese la cantidad de paginas del libro")
    libro=Libro(cantpag,autor)#libro que se quiere donar
    lista.append(libro)
