nome = input("digite o nome do aluno:")
numero = int(input("digite o numero do aluno:"))
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segundo nota:"))
nota3 = float(input("digite a terceira nota:"))
ME = float(input("digite a media dos exercicios:"))
MA = (nota1 + (nota2 * 2) + (nota3 * 3) + ME) / 7
if MA >= 90:
    resutado = "A"
elif MA >= 75 and MA < 90:
    resutado ="B"
elif MA >=60 and MA < 75:
    resutado ="C"
elif MA >= 40 and MA < 60:
    resutado = "D"
else:
    resutadodo = "E"
print (nome)
print (numero)
if resutado == "A" or "B" or "C" :
    print (resutado)
    print ("Aprovado")
else:
    print (resutado)
    print ("Reprovado")