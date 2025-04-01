import os
os.system ("cls | clear")
opcao_prato = ""
comanda = 0

while True:
    print ("""

    1 | STROGONOFF      | R$ 10,00
    2 | LASANHA         | R$ 20,00
    3 | FEIJOADA        | R$ 30,00
    4 | MACARRONADA     | R$ 40,00 
    5 | RISOTTO         | R$ 50,00
    6 | MOQUECA         | R$ 60,00
    7 | BOBÓ DE CAMARÃO | R$ 70,00

    """)
    opcao = int (input("Escolha a opção de prato desejada: "))

    match opcao:
        case 1:
            print ("STROGONOFF R$ 10,00")
            prato = 10
            prato2 = "STROGONOFF"
            
        case 2:
            print ("LASANHA R$ 20,00")
            prato = 20
            prato2 = 'LASANHA'
           
        case 3:
            print ("FEIJOADA R$ 30,00")
            prato = 30
            prato2 = 'FEIJOADA'
        
        case 4:
            print ("MACARRONADA R$ 40,00")
            prato = 40
            prato2 = 'MARCARRONADA'
           
        case 5:
            print ("RISOTTO R$ 50,00")
            prato = 50
            prato2 = 'RISOTTO'
            
        case 6:
            print ("MOQUECA R$ 60,00")
            prato = 60
            prato2 = 'MOQUECA'
            
        case 7:
            print ("BOBÓ DE CAMARÃO R$ 70,00")
            prato = 70
            prato2 = 'BOBÓ DE CAMARÃO'
           
        case _:
            print ("OPÇÃO INVÁLIDA")
            print ("PEÇA NOVAMENTE")
        
    comanda += prato
    opcao_prato += prato2 + " "
  
    decisao = int (input("""

SIM - 1
NÃO - 0
                         

DESEJA PEDIR MAIS ALGO? """))
    if decisao == 0:
        break

print ("""
1 - À VISTA
2 - CRÉDITO     
""")
forma_de_pagamento = int (input("ESCOLHA A FORMA DE PAGAMENTO: "))

if forma_de_pagamento == 1:
    desconto = comanda * 0.10
    valor_pagar = comanda - desconto
    print (f"PRATO ESCOLHIDO: {opcao_prato}")
    print (f"SUBTOTAL: {comanda}")
    print (f"VALOR DO DESCONTO: {desconto}")
    print (f"FORMA DE PAGAMENTO ESCOLHIDA: À VISTA")
    print (f"VALOR FINAL: {valor_pagar}")

if forma_de_pagamento == 2 :
    acrescimo = comanda * 0.10
    valor_pagar = comanda + acrescimo
    print (f"PRATO ESCOLHIDO: {opcao_prato}")
    print (f"SUBTOTAL: {comanda}")
    print (f"VALOR DO ACRESCIMO: {acrescimo}")
    print (f"FORMA DE PAGAMENTO ESCOLHIDA: CRÉDITO")
    print (f"VALOR FINAL: {valor_pagar}")
