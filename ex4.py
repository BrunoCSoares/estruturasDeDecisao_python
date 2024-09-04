# - Um estacionamento cobra R$ 5,00 por hora porém possui um teto de cobrança máxima de R$ 35,00, independente do número de horas. Escreva um algoritmo que pergunte ao usuário qual foi o período de permanência em horas e escreva na tela o total a pagar.

horas = int(input("Informe a quantidade de horas no estabelecimento: "))

if(horas < 7):
    print(f"A sua conta é de R${float(horas*5):.2f}")
else:
    print(f"A sua conta é de R$35.00")