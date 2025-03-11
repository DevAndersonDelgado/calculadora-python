def calcular():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Digite a operação (+, -, *, /) ou 'sair' para encerrar: ")
            if operador.lower() == 'sair':
                print("Encerrando a calculadora.")
                break
            num2 = float(input("Digite o segundo número: "))

            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2
            else:
                print("Operador inválido! Tente novamente.")
                continue
            
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Erro: Entrada inválida! Digite números válidos.")

if __name__ == "__main__":
    calcular()
