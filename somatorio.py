soma = 0

for count in range (10):
    num = int(input("Digite um numero inteiro: "))
    soma += num
    media = soma / 10

print('Somatório é: ', soma)
print(f'Media é: {media:.2f}')