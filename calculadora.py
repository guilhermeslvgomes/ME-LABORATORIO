"""Calculadora básica em Python
Este programa implementa uma calculadora simples com as operações de: 
- soma
-subtração 
-multiplicação 
-divisão. """

# Lista para armazenar o histórico
historico = []

def somar(a, b):
    """Soma dois números e registra a operação no histórico.

    Args:
        a: Primeiro número.
        b: Segundo número.

    Returns:
        A soma de `a` e `b`.
    """
    resultado = a + b
    historico.append(f"{a} + {b} = {resultado}")
    return resultado

def subtrair(a, b):
    """Subtrai dois números e registra a operação no histórico.

    Args:
        a: Primeiro número.
        b: Segundo número.

    Returns:
        A diferença entre `a` e `b`.
    """
    resultado = a - b
    historico.append(f"{a} - {b} = {resultado}")
    return resultado

def multiplicar(a, b):
    """Multiplica dois números e registra a operação no histórico.

    Args:
        a: Primeiro número.
        b: Segundo número.

    Returns:
        O produto de `a` e `b`.
    """
    resultado = a * b
    historico.append(f"{a} * {b} = {resultado}")
    return resultado

def dividir(a, b):
    """Divide dois números e registra a operação no histórico.

    Args:
        a: Dividendo.
        b: Divisor.

    Returns:
        O quociente de `a` por `b`.
        Se `b` for 0, retorna a mensagem de erro "Erro: divisão por zero!".
    """
    if b == 0:
        return "Erro: divisão por zero!"
    resultado = a / b
    historico.append(f"{a} / {b} = {resultado}")
    return resultado


while True:
    print("\n=== Calculadora Simples ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Ver histórico")
    print("0 - Sair")

    escolha = input("Digite a opção: ")

    if escolha == "0":
        print("Encerrando calculadora...")
        break

    if escolha == "5":
        print("\n--- Histórico ---")
        if len(historico) == 0:
            print("Nenhuma operação realizada.")
        else:
            for op in historico:
                print(op)
        continue

    if escolha not in ["1", "2", "3", "4"]:
        print("Opção inválida!")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if escolha == "1":
        resultado = somar(num1, num2)
    elif escolha == "2":
        resultado = subtrair(num1, num2)
    elif escolha == "3":
        resultado = multiplicar(num1, num2)
    elif escolha == "4":
        resultado = dividir(num1, num2)


    try:
        if resultado == int(resultado):
            resultado = int(resultado)
    except:
        pass

    print(f"Resultado: {resultado}")