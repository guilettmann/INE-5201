posicao = int(input("Digite a posição do número na sequência de Fibonacci: "))

ultimo = 1
penultimo = 1

if posicao == 1 or posicao == 2:
    print('O número é 1')
else:
    for i in range (2, posicao):
        numero = ultimo + penultimo
        penultimo = ultimo
        ultimo = numero
print('O número é', numero)