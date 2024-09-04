# - Um condomínio possui 4 blocos que são abastecidos por duas caixas d’água diferentes. A caixa A abastece os blocos pares e a caixa B abastece os blocos ímpares. Escreva um algoritmo que pergunte ao usuário em qual bloco ele mora (1-4) e escreva na tela qual a caixa que abastece seu bloco: a caixa a ou a caixa B;

bloco = int(input("Informe o número do seu bloco (1-4): "))

if(bloco%2==0):
    print("A caixa de água A abastece o seu bloco")
else:
    print("A caixa de água B abastece o seu bloco")