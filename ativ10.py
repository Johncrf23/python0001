peso = float(input("coloque seu peso"))
altura = float(input("coloque sua altura"))
IMC = peso / altura**2 
print (IMC)
if IMC < 18.5:
    print("abaixo do peso")
elif IMC >= 18.5 and IMC <= 25:
    print("peso normal")
elif IMC >= 25 and IMC <= 30:
    print("acima do peso")
else:
    print("obeso")
