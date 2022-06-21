#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def e4SomaMedia(a, b, c, d, qtdNotas):
    c = (float(a) + float(b) + float(c) + float(d)) / qtdNotas
    print(f"Nota 1: {a} | Nota 2: {b} | Nota 3: {c} | Nota 4: {d}")
    print(f"A média das notas é: {c}")


a = input("Primeira nota")
while not a:
    print("A nota 1 não pode estar vazio.")
    a = input("Primeira nota")
if not a.isdigit():
    print("Digite somente números.")
    quit()

b = input("Segunda nota")
while not b:
    print("A nota 1 não pode estar vazio.")
    b = input("Segunda nota")
if not b.isdigit():
    print("Digite somente números.")
    quit()

c = input("Terceira nota")
while not c:
    print("A nota 1 não pode estar vazio.")
    c = input("Segunda nota")
if not c.isdigit():
    print("Digite somente números.")
    quit()

d = input("Quarta nota")
while not d:
    print("A nota 1 não pode estar vazio.")
    d = input("Segunda nota")
if not d.isdigit():
    print("Digite somente números.")
    quit()

e4SomaMedia(a, b, c, d, int(4))