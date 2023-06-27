nombre = Sharon
nombre2 = Zabeth
apellido = Sierra

print(nombre + " " nombre2 + " " apellido)

#Los numeros enteros en Python no tienen limite
#Una solución simple para restringir los flotantes a dos puntos decimales 
#es usar la función integrada round(x[, n]) . devuelve numero x redondeado 
#a n precisión de dígitos después del punto decimal.

print("Ingrese el numero inicial:")
i = int(input())
print("Ingrese el numero final:")
f = int(input())
suma=0
print("**Los numeros pares del rango**")
while i <= f:
    if i % 2 ==0:
        print (i)
        suma = suma+i
    i+=1    
print("La suma de los numeros es: ",suma)