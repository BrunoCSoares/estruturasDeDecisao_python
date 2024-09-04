# - Um condomínio possui 20 blocos e para uma correta administração possui dois síndicos: o sr José que administra os blocos de 1 a 10 e o sr Hamilton que administra os blocos de 11 a 20. Escreva um algoritmo que pergunte ao usuário em qual bloco ele mora e escreva na tela qual o síndico responsável;

bloco = int(input("Informe o número do seu bloco (1-20): "))

if(bloco<11):
    print("O seu síndico é o Sr. José")
else:
    print("O seu síndico é o Sr. Hamilton")