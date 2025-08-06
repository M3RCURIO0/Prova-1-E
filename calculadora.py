print("Mateus Guastala Montanha")
print("Prova de Introdção à Programação")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))  
operacao = input("Digite a operação (+, -, *, /): ")    
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2 
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero"
print("O resultado é:", resultado)