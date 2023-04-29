from time import sleep
from db import fetch_data


def inicio():
    print(f"{'GEONAMES - ALL CITIES WITH A POPULATION > 1000':^50}")
    sleep(0.5)
    print("\nSELECIONE O MÉTODO DE ORDENAÇÃO:")
    sleep(0.3)
    print("1 - MERGE")
    sleep(0.3)
    print("2 - HEAP")
    sleep(0.3)
    print("3 - QUICK")
    sleep(0.3)
    while True:
        sleep(0.3)
        opc_inicio = input(": ")
        if opc_inicio == "1":
            metodo = 1
            break
        elif opc_inicio == "2":
            metodo = 1
            break
        elif opc_inicio == "3":
            metodo = 1
            break
        else:
            print("\nOPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE!")
    
    print()
    current_search = pesquisa(metodo)
    menu(current_search, metodo)

def menu(current_search, metodo):
    while True:
        sleep(0.5)
        print("O QUE FAZER?")
        sleep(0.2)
        print("1 - DETALHAR DADOS DE UMA CIDADE")
        sleep(0.2)
        print("2 - NOVA PESQUISA")
        sleep(0.2)
        print("0 - FECHAR")
        sleep(0.2)
        while True:
            opc = input(": ")
            sleep(0.5)
            print()
            if opc == "1":
                print("CIDADES EXIBIDAS OU PESQUISA GERAL?")
                sleep(0.5)
                print("PESQUISA GERAL POSSUI UM TEMPO DE ESPERA SUPERIOR")
                sleep(0.5)
                print("1 - CIDADES JÁ MOSTRADAS")
                sleep(0.5)
                print("2 - PESQUISA GERAL")
                sleep(0.5)
                while True:
                    opc_dados = input(": ")
                    if opc_dados == "1":
                        print("\nDIGITE O NOME DA CIDADE:")
                        cid = input(": ")
                        print()
                        cidade_selecionada(cid, current_search)
                        break
                    elif opc_dados == "2":
                        current_search = pesquisa(metodo, False)
                        print("\nDIGITE O NOME DA CIDADE:")
                        cid = input(": ")
                        cidade_selecionada(cid, current_search)
                        break
                    else:
                        print("OPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE!\n")
                        sleep(0.5)
                break

            elif opc == "2":
                current_search = pesquisa(metodo)
                break
            elif opc == "0":
                print("Programa finalizado!")
                sleep(1)
                exit()
            else:
                print("OPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE!\n")
                sleep(0.5)

def pesquisa(metodo, show=True):
    print("INFORME A QUANTIDADE DE CIDADES:")
    sleep(0.3)
    print("0 RETORNA TODO O BANCO")
    while True:
        try:
            opc_pesquisa = int(input(": "))
            current_search = resultados(metodo, show, opc_pesquisa)
            break
        except ValueError:
            print("OPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE!\n")   
    return current_search

def resultados(sorting_type, show, rows=0):
    lista = fetch_data(sorting_type, rows)

    if show:
        print(f"\n{'GEO ID':<11} {'NAME':<19} {'COUNTRY':<8} {'POPULATION'}")
        sleep(0.3)
        for i in lista:
            print(f"{i[0]:<9} : {i[1]['ascii_name']:<17} : {i[1]['country_code']:<6} : {i[1]['population']}")
            sleep(0.2)
        print("=========\n")

    sleep(0.5)
    return lista

def cidade_selecionada(cid, current_search):
    lista = current_search
    found = False
    for i in lista:
        if cid.lower() in i[1]['ascii_name'].lower():
            sleep(0.5)
            print(f"GEO ID: {i[0]}")
            sleep(0.3)
            print(f"NAME: {i[1]['ascii_name']}")
            sleep(0.3)
            print(f"COUNTRY CODE: {i[1]['country_code']}")
            sleep(0.3)
            print(f"POPULATION: {i[1]['population']}")
            sleep(0.3)
            print(f"CORDIRNATES: LAT: {i[1]['coordinates']['lat']}")
            sleep(0.3)
            print(f"{'LONG':>17}: {i[1]['coordinates']['lon']}")
            sleep(0.3)
            print(f"MODIFICATION DATE: {i[1]['modification_date']}")
            sleep(0.3)
            print()
            found = True
    if not found:
        sleep(0.5)
        print("NENHUM CIDADE ENCONTRADA!")
        print()

 
inicio()
