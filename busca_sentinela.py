# busca com sentinela

def busca_sentinela(v, x):
    i = 0
    v.append(x)  # essa é a sentinels
    while v[i] != x:
        i += 1

    if i == len(v) -1:
            return -1
    return i

#programa principal

vetor = list(range(0,100000))
print(vetor)
numero_procurado =  97864
posicao = busca_sentinela(vetor, numero_procurado)
if posicao >= 0:
    print("O número procurado é:", numero_procurado)
    print("O número está na posição:", posicao)
else:
    print("O número não está na lista")


