from time import sleep


def cardapio():
    print(""""========= ESPECIFICAÇÃO===============|==CODIGO==| |===PREÇO===|
           CACHORRO QUENTE                  100        1.20 R$
           BAURU SIMPLES                    101        1.30 R$
           BAURU COM OVO                    102        1.50 R$
           HAMBURGER                        103        1.20 R$
           CHEESBURGER                      104        1.70 R$
           SUCO                             105        2.20 R$""")

totalapagar = 0
listap = []
comidas = [100, 101, 102, 103, 104, 105]

while True:
    cardapio()
    print("\033[1;31mPara finalizar os pedidos, digite 99\033[0;0m")
    try:
        pedido = int(input("Digite o codigo do seu lanche:\n>>> "))
        listap.append(pedido)
    except ValueError as err:
        print("ALGO DEU ERRADO :0\nTENTE NOVAMENTE\n\n\n")
    else:
        if pedido == 100:
            listap.remove(100)
            listap.append("CACHORRO QUENTE")
            totalapagar += 1.20
        elif pedido == 101:
            listap.remove(101)
            listap.append("BAURU SIMPLES")
            totalapagar += 1.30
        elif pedido == 102:
            listap.remove(102)
            listap.append("BAURU COM OVO")
            totalapagar += 1.50
        elif pedido == 103:
            listap.remove(103)
            listap.append("HAMBURGER")
            totalapagar += 1.20
        elif pedido == 104:
            listap.remove(104)
            listap.append("CHEESBURGER")
            totalapagar += 1.70
        elif pedido == 105:
            listap.remove(105)
            listap.append("SUCO")
            totalapagar += 2.20
        elif pedido == 99:
            print("Obrigado pela preferência")
            sleep(1)
            print(f"PAGUE NO CAIXA O VALOR R$ {totalapagar:.2f}")
            exit()
    i = 0
    print("\n\033[1;94mSEUS PEDIDOS:\033[0;0m\n")
    if i < listap.__len__():
        print(listap)
        i += 1
    print(f"\033[1;92mTOTAL A PAGAR R$ {totalapagar:.2f}\n\033[0;0m")
