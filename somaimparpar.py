somap = 0
somai = 0 

for count in range (1, 101):
    if count % 2 == 0:
        somap += count
        mediap = somap / count
    elif count % 2 != 0:
        somai += count
        mediai = somai / count
print(f'Soma dos pares é {somap:.2f} e a soma dos ímpares é {somai:.2f}')
print(f'Média dos pares é {mediap:.2f} e a média dos ímpares é {mediai:.2f}')
     
