def main():
    # Problema 1
    numeros = [3, 7, 1, 15, 9]
    print(f"1. Maior número na lista: {max(numeros)}")

    # Problema 2
    nomes = ["Ana", "João", "Maria", "Pedro"]
    print(f"2. Número total de nomes na lista: {len(nomes)}")

    # Problema 3
    numeros = [2, 5, 8, 10]
    print(f"3. Soma de todos os números na lista: {sum(numeros)}")

    # Problema 4
    numeros = [3, 6, 9, 12]
    media = sum(numeros) / len(numeros)
    print(f"4. Média dos números na lista: {media}")

    # Problema 5
    palavras = ["Abacaxi", "Amor", "Bola", "Anjo"]
    quantidade_a = sum(1 for palavra in palavras if palavra.startswith('A'))
    print(f"5. Quantidade de palavras que começam com 'A': {quantidade_a}")

    # Problema 6
    palavras = ["gato", "cachorro", "elefante", "hipopótamo"]
    mais_longa = max(palavras, key=len)
    print(f"6. A palavra mais longa na lista é: {mais_longa}")

    # Problema 7
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = [num for num in numeros if num % 2 == 0]
    print(f"7. Números pares na lista: {pares}")

    # Problema 8
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    impares = [num for num in numeros if num % 2 != 0]
    print(f"8. Números ímpares na lista: {impares}")

    # Problema 9
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]
    comuns = [num for num in lista1 if num in lista2]
    print(f"9. Números presentes em ambas as listas: {comuns}")

    # Problema 10
    numeros = [1, 2, 3, 2, 4, 5, 3, 6]
    numeros_sem_repeticao = list(set(numeros))
    print(f"10. Lista sem números repetidos: {numeros_sem_repeticao}")


if __name__ == "__main__":
    main()
