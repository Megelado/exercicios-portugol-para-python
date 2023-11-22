import random

vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 20):
    vetor[i] = random.randint(0, 99)
print(vetor)
vetor2 = None
for i in range(0, 19):
    for j in range(i + 1, 20):
        vetor1 = vetor[i]
        if vetor[i] > vetor[j]:
            aux = vetor[j]
            vetor[j] = vetor[i]
            vetor[i] = aux
print(vetor)
