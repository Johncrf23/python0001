valor1 = int(input("insira o primeiro valor"))
valor2 = int(input("insira o segundo valor"))
valor3 = int(input("insira o terceiro valor"))
if valor1 > valor2 and valor1 > valor3 and valor2 > valor3:
    print(valor1, valor2, valor3)
elif valor1 < valor2 and valor1 < valor3 and valor2 < valor3:
    print(valor3, valor2, valor1)
elif valor2 > valor1 and valor2 > valor3 and valor3 > valor1:
    print(valor2, valor3, valor1)
elif valor2 > valor1 and valor2 > valor3 and valor3 < valor1:
    print(valor2, valor1, valor3)
elif valor3 > valor1 and valor3 > valor2 and valor1 > valor2:
    print(valor3, valor1, valor2)
elif valor1 > valor2 and valor1 > valor3 and valor3 > valor2:
    print(valor3, valor1, valor2)