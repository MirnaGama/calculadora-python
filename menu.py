from calculadora import Calculadora

calc = Calculadora()

print("Bem-vindo a Calculadora! Escolha uma das operações abaixo:");

escolha = 0

while (escolha != 5):
    print("\n1) Soma")
    print("2) Subtração")
    print("3) Multiplicação")
    print("4) Divisão")
    print("5) Sair")
    escolha = int(input());

    if (escolha == 1):
        num1 = int(input("\n1º Valor: "));
        num2 = int(input("2º Valor: "));
        print("Resultado da Soma: {}".format(calc.sum(num1,num2)))
        print("\nDeseja fazer outra operação?")
    elif (escolha == 2):
        num1 = int(input("\n1º Valor: "));
        num2 = int(input("2º Valor: "));
        print("Resultado da Subtração: {}".format(calc.sub(num1,num2)))
        print("\nDeseja fazer outra operação?")
    elif (escolha == 3):
        num1 = int(input("\n1º Valor: "));
        num2 = int(input("2º Valor: "));
        print("Resultado da Multiplicação: {}".format(calc.mul(num1,num2)))
        print("\nDeseja fazer outra operação?")
    elif (escolha == 4):
        num1 = int(input("\n1º Valor: "));
        num2 = int(input("2º Valor: "));
        print("Resultado da Divisão: {}".format(calc.div(num1,num2)))
        print("\nDeseja fazer outra operação?")
    elif (escolha == 5):
        print("Você saiu do sistema de calculadora!")
    else:
        print("Digite uma opção válida!")


