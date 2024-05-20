n = int(input("Digite o número natural n: "))

def soma_algarismos(n):
    soma = 0
    while n > 0:
        # Adiciona o último dígito ao total
        soma = soma + n % 10
        # Remove o último dígito de n
        n = n//10
    return soma

# Teste da função
print("A soma dos algarismos de", n, "é igual a", soma_algarismos(n))