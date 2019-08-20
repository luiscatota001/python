'''
x = 6
y = 9
print(x+y)
n = "santiago"
a = 'solis'
e = 35
print("hola "+n+" tu aplelido es "+a+" y tienes "+str (e)+"años")
print ("hola {} tu apellido es {} y tienes {} años".format(n,a,e))
print(n.upper())


f = (float) (input("ingrese un numero: "))
g = (float) (input("ingrese otro numero: "))
print("la suma de {} + {} = {}".format(f,g,(f+g)))
print("la resta de {} - {} = {}".format(f,g,(f-g)))
print("la multiplicacion  de {} * {} = {}".format(f,g,(f*g)))
print("la division de {} / {} = {}".format(f,g,(f/g)))
b =  True
print(type(b))

mi_tupla = ('cadena de texto', 15, 12, 'otro valor', True)
x = (6,97,7)
mi_tupla.__add__(x)
print("los datos de mi tupla son " + str(mi_tupla))


mi_lista = ["cadena de las lista",57,True,98.2]
print(mi_lista)
mi_lista.append("nuevo dato")
print(mi_lista)

usuario = ('ssolis','sys.solis@gmail.com',15,'Ambato')
print(usuario)
print(usuario[2])
if (usuario[2]>=18):
    print("mayor de edad")
    print("ya debistes terminar el colegio")
for elementos in usuario:
    print(elementos)

lista_enteros = [8,4,5,7,1,9,2]
print(lista_enteros)
lista_enteros.sort()
print(lista_enteros)
lista_enteros[3]=25
lista_enteros[5]='hola'
print(lista_enteros)
lista_enteros.append("hola 2")
print(lista_enteros)
lista_enteros.pop()
print(lista_enteros)
lista_b=[100,200,300]
lista_enteros.extend(lista_b)
print(lista_enteros)
del lista_enteros [5]
print(lista_enteros)
lista_enteros.remove(25)
print(lista_enteros)
'''

lista_pares=[]
for i in range (0,100):
    if (i % 2 ==0):
        lista_pares.append(i)
print(lista_pares)

for elmento in lista_pares:
    if (elmento % 3 == 0):
        lista_pares.remove(elmento)
print(lista_pares)

