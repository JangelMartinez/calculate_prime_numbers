import time

numString = int(input('Introduce un número para sacar los números primos:'))

inicio = time.time()

primos = [ 2, 3]

myNum = primos[len(primos) - 1] + 2

while myNum <=  numString and myNum <= numString:

    nodivisble = True

    for i in primos:
        if i > myNum:
            break
        
        if myNum % i == 0 and i < myNum/2:
            nodivisble=False
            break

    if nodivisble:
        primos.append(myNum)
        
    myNum = myNum + 2

fin = time.time()


print(primos)

if numString in primos:
    print(numString, ' es un número primo')
else:
    print(numString, ' no es un número primo')

print('encontrados ', len(primos), ' numeros primos')
print ('ejecutado en: ', fin - inicio)