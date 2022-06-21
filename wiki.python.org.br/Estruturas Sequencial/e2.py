#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
x = input("Digite um número.")
while not x:
    if not x:
        print("O input não pode ser vazio.")
        x = input("Digite um número.")

if x.isdigit():
    print(f"O número digitado é: {x}")
else:
    print("Digite somente números.")