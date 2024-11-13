def maior_numero():
    # Lê a linha de entrada e converte em uma lista de inteiros
    numeros = list(map(int, input().split()))

    # Remove o último elemento (0) da lista
    numeros.pop()

    # Imprime o maior número da lista
    print(max(numeros))

if __name__ == "__main__":
    maior_numero()
