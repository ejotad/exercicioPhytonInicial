#Faça um Programa que peça dois números e imprima a soma.
def e3Soma(a, b):
    c = int(a) + int(b)
    print(f"A soma de {a}+{b} é = {c}")


a = input("Digite o número 1.")
while not a:
    print("O input 1 não pode estar vazio")
    a = input("Digite o número 1.")
if a:
    if a.isdigit():
        b = input("Digite o número 2.")
        while not b:
            if not b:
                print("O input 2 não pode estar vazio.")
                b = input("Digite o número 2.")
        if b.isdigit():
            e3Soma(a, b)
        else:
            print("Digite somente números.")
    else:
        print("Digite somente números.")