def eh_perfeito(numero):
    soma = 0
    for div in range(1, numero//2 + 1):
        if numero % div == 0:
            soma = soma + div
    return soma == numero
   