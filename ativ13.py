nome = input("digite seu nome")
emprego = input("digite seu trabalho")
salario = float(input("digite seu salario"))
if salario <= 2112.00:
    print (salario)
elif salario >2112.01 and salario < 2826.65:
    salarioL = salario - 158.40
    print(salarioL)
elif salario >2826.65 and salario < 3751.05:
    salarioL = salario - 370.40
    print(salarioL)
elif salario >3751.05 and salario < 4664.68:
    salarioL = salario - 651.73
else:
    salarioL = salario - 884.96
    print(salarioL) 
print (salario )
     