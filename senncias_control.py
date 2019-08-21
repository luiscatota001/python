tupla = ()
lista = []
diccionario = {}

'''conjunto = set ('12345689')
print(conjunto)'''
lista_pares = []

print("lista con numeros pares")
dim = (int) (input("cuantos numeros pares vas a generar: "))
for i in range (0,dim):
    if (i % 2 == 0):
        lista_pares.append(i)
print("Multiplos del 2")
print(lista_pares)

def clasificar_numeros (lista):
    lista_generada = []
    mul = int (input("ingres multiplo: "))
    for elemento in lista:
        if (elemento%mul == 0):
            lista_generada.append(elemento)
    print(lista_generada)

clasificar_numeros(lista_pares)
