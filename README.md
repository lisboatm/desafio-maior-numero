# Desafio do Maior Número

## Descrição
Leonardo é um garoto muito criativo e adora desafiar seus colegas da escola. Ele criou um desafio no qual uma sequência de números é dita em voz alta. Quando o número **0** é pronunciado, o desafio termina, e seus colegas devem dizer imediatamente qual foi o **maior número** mencionado. Leonardo tem dificuldade em verificar se a resposta está correta, especialmente quando a sequência é longa, então ele pediu a sua ajuda!

## Problema
Escreva um programa que, dada uma sequência de números inteiros positivos terminada por 0 (zero), determine e imprima o maior número da sequência.

## Entrada
- A entrada é composta por uma única linha contendo uma sequência de números inteiros positivos.
- A sequência é terminada pelo número **0**, que não deve ser considerado na busca pelo maior número.
- **Restrições**:
  - A sequência contém no máximo 100 números.
  - Cada número está no intervalo de **1 a 1000**.

## Saída
- O programa deve imprimir o maior número da sequência fornecida.

## Exemplo

### Exemplo de Entrada 1
```
10 30 20 5 0
```

### Exemplo de Saída 1
```
30
```

### Exemplo de Entrada 2
```
99 1000 55 1 2 9 0
```

### Exemplo de Saída 2
```
1000
```

## Explicação
O programa deve ler a sequência de números até encontrar o **0**, ignorá-lo, e então determinar o maior número presente na sequência.

## Solução em Python
```python
def maior_numero():
    # Lê a linha de entrada e converte em uma lista de inteiros
    numeros = list(map(int, input().split()))

    # Remove o último elemento (0) da lista
    numeros.pop()

    # Imprime o maior número da lista
    print(max(numeros))

if __name__ == "__main__":
    maior_numero()
```

## Como Executar
Para rodar o programa, basta utilizar um terminal e executar o seguinte comando:
```
python3 maior_numero.py
```

Insira a sequência de números e pressione **Enter**. O programa imprimirá o maior número da sequência antes do **0**.

## Complexidade
- A solução possui uma complexidade de **O(n)**, onde **n** é o número de elementos na sequência. Ela é eficiente para o limite máximo de **100 números**.

---

**Tags**: Python, Algoritmos, Números Inteiros, Desafios de Programação, OBI (Olimpíada Brasileira de Informática)
