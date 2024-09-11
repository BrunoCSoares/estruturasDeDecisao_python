# - Escreva um algoritmo que pergunte o valor de uma mercadoria e qual o valor que o usuário tem em mãos e diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria;

valorMercadoria = float(input("Informe o valor da marcadoria: "))
valorAtual = float(input("Informe o valor atual em mão: "))

if(valorMercadoria >= valorAtual):
    print(f"O dinheiro não é suficiente. Falta R${valorMercadoria - valorAtual}")
else:
    print(f"O dinheiro é suficiene. Sobra R${valorAtual - valorMercadoria}")