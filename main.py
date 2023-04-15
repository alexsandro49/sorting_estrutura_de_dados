import os
import pandas as pd
from time import sleep

def selecionar_loja(opc, opc1, opc2):
    if opc == "1":
        colunas = ["Quantidade Vendida", "Preco Unitario"]
    else:
        colunas = ["Quantidade Devolvida", "Preço Unitário"]

    if opc1 == "1":
        chave = "Belo Horizonte"
    elif opc1 == "2":
        chave = "Curitiba"
    elif opc1 == "3":
        chave = "Fortaleza"
    elif opc1 == "4":
        chave = "Goiás"
    elif opc1 == "5":
        chave = "Porto Alegre"
    elif opc1 == "6":
        chave = "Recife"
    elif opc1 == "7":
        chave = "Rio de Janeiro"
    elif opc1 == "8":
        chave = "Salvador"
    else:
        chave = "São Paulo"
    
    if (opc2 == "1"):
        coluna = colunas[0]
    else:
        coluna = colunas[1]

    if (opc == "1"):
        print(df_vendas[chave][coluna].values)
    else:
        print(df_devolucoes[chave][coluna].values)


endereco = f"{os.getcwd()}/Vendas/"

df_vendas = {}
df_devolucoes = {}

for i in os.listdir(endereco):
    if ("Vendas" in i):
        df_vendas[i[i.index("-")+2:i.index(".")]] = pd.read_csv(endereco+i)
    else:
        df_devolucoes[i[i.index("-")+2:i.index(".")]] = pd.read_csv(endereco+i)

lojas = ['1 - BELO HORIZONTE', '2 - CURITIBA', '3 - FORTALEZA', '4 - GOIÁS', '5 - PORTO ALEGRE', '6 - RECIFE', '7 - RIO DE JANEIRO', '8 - SALVADOR', '9 - SÃO PAULO', '-------', '0 - CANCELAR']

while (True):
    print("==========================")
    sleep(0.3)
    print("1 - VENDAS")
    sleep(0.3)
    print("2 - DEVOLUÇÕES")
    sleep(0.3)
    print("0 - FECHAR")
    sleep(0.3)
    opc = input(": ")
    if (opc == "1" or opc == "2"):
        while (True):
            sleep(0.3)
            print("\nESCOLHA A LOJA:")
            for i in lojas:
                sleep(0.2)
                print(i)
            opc1 = input(": ")
            
            print()
            sleep(0.3)
            if (opc1 in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
                while (True):
                    print("SELECIONE O DADO:")
                    sleep(0.3)
                    print("1 - QUANTIDADE VENDIDA")
                    sleep(0.3)
                    print("2 - PREÇO UNITÁRIO")
                    sleep(0.3)
                    print("0 - CANCELAR")
                    opc2 = input(": ")
                    if (opc2 == "1" or opc2 == "2"):
                        print("\n===========")
                        selecionar_loja(opc, opc1, opc2)
                        break
                    elif (opc2 == "0"):
                        break
                    else:
                        print("OPÇÃO INVÁLIDA! POR FAVOR, TENTE NOVAMENTE.")
                        sleep(0.5)
                break

            elif (opc1 == "0"):
                break
            else:
                print("OPÇÃO INVÁLIDA! POR FAVOR, TENTE NOVAMENTE.")
                sleep(0.5)
    elif (opc == "0"):
        exit()
    else:
        print("OPÇÃO INVÁLIDA! POR FAVOR, TENTE NOVAMENTE.")
