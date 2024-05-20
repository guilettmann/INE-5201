num = int(input("Digite um numero inteiro que nao seja negativo: "))

fatorial = 1

if num < 0:
    print('E negativo')
elif num == 0:
    print('O fatorial e 1')
else:
    ant = 1
    for count in range (1, num+1):
        fatorial *= count
    print('O fatorial e', fatorial)
