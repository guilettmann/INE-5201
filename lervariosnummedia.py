quant = int(input("Quantos números serão digitados? "))

soma = 0

for count in range(quant):
    num = int(input("Digite o número: "))
    soma += num
    media = soma / quant
print(f'Média é: {media:.2f}')

