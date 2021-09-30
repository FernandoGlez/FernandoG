print ("Este programa transforma un número decimal a binario.\nSolo funciona con números enteros entre 0 y 1024")
decimal = input("Introduzca su número aquí:")
decimal = int(decimal)
numero = decimal
p1 = numero % 2
numero = numero/2
numero = int(numero)
p2 = numero % 2
numero = numero/2
numero = int(numero)
p3 = numero % 2
numero = numero/2
numero = int(numero)
p4 = numero % 2
numero = numero/2
numero = int(numero)
p5 = numero % 2
numero = numero/2
numero = int(numero)
p6 = numero % 2
numero = numero/2
numero = int(numero)
p7 = numero % 2
numero = numero/2
numero = int(numero)
p8 = numero % 2
numero = numero/2
numero = int(numero)
p9 = numero % 2
numero = numero/2
numero = int(numero)
p10 = numero % 2
numero = numero/2
numero = int(numero)
p11 = numero % 2

print(f"Su número en decimal es: {decimal}")
print(f"Su número en binario es: {p11}{p10}{p9}{p8}{p7}{p6}{p5}{p4}{p3}{p2}{p1}")
