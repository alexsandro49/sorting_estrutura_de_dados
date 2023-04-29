import json
from Sorting import *


def fetch_data(sorting_type, rows=0):
    with open("geonames-all-cities-with-a-population-1000@public.json", encoding='utf-8') as file:
        database = json.load(file)

    all_data = []
    data = []
    
    for i in database:
        if i["population"] == 0:
            population = "sem dados"
        else:
            population = i["population"]

        all_data.append((int(i["geoname_id"]), {
            "country_code": i["country_code"], 
            "ascii_name": i["ascii_name"],              
            "cou_name_en": i["cou_name_en"],
            "population": population,
            "coordinates": i["coordinates"],
            "modification_date": i["modification_date"]
        }))
        
    if sorting_type == 1:
        merge_sort(all_data)
    """ elif sorting_type == 2:
        heap_sort(all_data)
    else:
        quick_sort(all_data) """

    if rows == 0:
        return all_data
    else:
        for i in range(rows):
            data.append(all_data[i])

    return data
