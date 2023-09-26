altura = float(input("insira sua altura"))
sexo = input("insira seu sexo(HOMEM, MULHER)")
if sexo == "HOMEM":
    resutado = (72.7 * altura) - 58
else:
        resutado = (62.1 * altura) - 44.7
print (resutado)
