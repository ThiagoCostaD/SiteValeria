def imprimir_padrao(n):
    for i in range(n):
        espacos = n - i - 1
        asteriscos = 2 * i + 1
        linha = " " * espacos + "*" * asteriscos
        print(linha)

    for i in range(n - 2, -1, -1):
        espacos = n - i - 1
        asteriscos = 2 * i + 1
        linha = " " * espacos + "*" * asteriscos
        print(linha)


def main():
    altura = 4  # Defina a altura desejada do padrão
    imprimir_padrao(altura)


if __name__ == '__main__':
    main()
