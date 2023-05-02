from time import sleep
from db import fetch_data


def start():
    print("="*60)
    print(f"{'GEONAMES - ALL CITIES WITH A POPULATION > 1000':^60}")
    print("="*60)
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
        opt_start = input(": ")
        if opt_start == "1":
            sorting_method = 1
            break
        elif opt_start == "2":
            sorting_method = 2
            break
        elif opt_start == "3":
            sorting_method = 3
            break
        else:
            print("\nOPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE!")
    
    print()
    current_search = search(sorting_method)
    menu(current_search, sorting_method)

def menu(current_search, sorting_method):
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
            opt_menu = input(": ")
            sleep(0.5)
            print()
            if opt_menu == "1":
                print("CIDADES EXIBIDAS OU PESQUISA GERAL?")
                sleep(0.5)
                print("PESQUISA GERAL POSSUI UM TEMPO DE ESPERA SUPERIOR")
                sleep(0.5)
                print("1 - CIDADES JÁ MOSTRADAS")
                sleep(0.5)
                print("2 - PESQUISA GERAL")
                sleep(0.5)
                while True:
                    opt_data = input(": ")
                    if opt_data == "1":
                        print("\nDIGITE O NOME DA CIDADE:")
                        cid = input(": ")
                        print()
                        find_city(cid, current_search)
                        break
                    elif opt_data == "2":
                        current_search = search(sorting_method, False)
                        print("\nDIGITE O NOME DA CIDADE:")
                        cid = input(": ")
                        find_city(cid, current_search)
                        break
                    else:
                        print("OPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE!\n")
                        sleep(0.5)
                break

            elif opt_menu == "2":
                current_search = search(sorting_method)
                break
            elif opt_menu == "0":
                print("Programa finalizado!")
                sleep(1)
                exit()
            else:
                print("OPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE!\n")
                sleep(0.5)

def search(sorting_method, show=True):
    print("INFORME A QUANTIDADE DE CIDADES:")
    sleep(0.3)
    print("0 RETORNA TODO O BANCO (>140k)")
    while True:
        try:
            opt_search = int(input(": "))
            current_search = results(sorting_method, show, opt_search)
            break
        except ValueError:
            print("OPÇÃO INVÁLIDA. POR FAVOR, TENTE NOVAMENTE!\n")   
    return current_search

def results(sorting_type, show, rows=0):
    x = fetch_data(sorting_type, rows)
    sorted_data = x[0]
    sorting_time = x[1]

    if show:
        print(f"\n{'GEO ID':<11} {'NAME':<19} {'COUNTRY':<8} {'POPULATION'}")
        sleep(0.3)
        for i in sorted_data:
            print(f"{i[0]:<9} : {i[1]['ascii_name']:<17} : {i[1]['country_code']:<6} : {i[1]['population']}")
            sleep(0.2)
        print("="*15)
        sleep(0.2)
        print(f"TEMPO GASTO PARA ORDERNAR: {sorting_time:.2f}s")
        sleep(0.2)
        print("="*9)
        print()
        sleep(0.2)

    sleep(0.5)
    return x

def find_city(city, current_search):
    found = False
    for i in current_search[0]:
        if city.lower() in i[1]['ascii_name'].lower():
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
        print("NENHUMA CIDADE ENCONTRADA!")
        print()

 
start()
