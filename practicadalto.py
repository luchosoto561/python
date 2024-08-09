#metodos para una lista en python
lista=[1,2,3,4]
print(len(lista))
#--------------------------------------------
#diccionarios
diccionario={
    "nombre": "luciano",
    "edad" : 19,
    "ciudad" : "ranelagh"    
}# cuando queres acceder por claves

diccionario["apellido"]="soto"
print(diccionario)
del diccionario["edad"]
print(diccionario)
#--------------------------------------------
edadamigo=input("ingresa edad de tu amigo: ")#siempre se ingresa un dato del tipo String
edadamigo2=int (edadamigo) * 2
print(f'el doble de la edad de mi amigo es {edadamigo2}')
#--------------------------------------------
tupla1=(1,2,3)
valor1,valor2,valor3=tupla1
tupla2=(4,)#requiere una coma para que sea distinguida de un valor entre parentesis
print(valor1, valor2, valor3)
tupla3=tuple(["lucho","soto"])
# las tuplas son inmutables
#--------------------------------------------
conjunto1=set(["dato1","dato2"])
conjunto2={"dato3","dato4"}
conjunto3=set()#conjunto vacio ya que si pones ={} te crea un diccionario vacio
# se utilizan mas para analisis de datos y operaciones matematicas de conjuntos
# un uso facil es que si le mandas al constructor una lista te elimina los repetidos
#--------------------------------------------
for num  in range(5,10):
    print(num)#imprime 5 6 7 8 9 
