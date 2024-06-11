def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida"

def main():
    while True:
        # Exibir o menu de opções
        print("\nCalculadora:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        # Solicitar ao usuário que escolha uma operação
        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo do programa. Até logo!")
            break
        elif escolha in ['1', '2', '3', '4']:
            try:
                # Solicitar os números ao usuário
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                # Executar a operação escolhida
                if escolha == '1':
                    print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
                elif escolha == '2':
                    print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
                elif escolha == '3':
                    print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    if resultado == "Erro: Divisão por zero não é permitida":
                        print(resultado)
                    else:
                        print(f"Resultado: {num1} / {num2} = {resultado}")
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()