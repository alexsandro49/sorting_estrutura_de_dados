from db import fetch_data
from Sorting import merge_sort

lista = fetch_data(15)
merge_sort(lista)

for i in lista:
    print(f"{i[0]} : {i[1]['ascii_name']} : {i[1]['cou_name_en']}")
