def suma_lista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista[0] + suma_lista(lista[1:])

numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = suma_lista(numeros)
print('La suma de los valores de 1 a 10 es igual a %i' % resultado)

print()
