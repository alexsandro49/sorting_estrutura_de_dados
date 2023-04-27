import json

def fetch_data(rows=0):
    with open("geonames-all-cities-with-a-population-1000@public.json", encoding='utf-8') as file:
        database = json.load(file)

    dados = []
    c = 0
    
    for i in database:
        if rows > 0 and c == rows:
            break
         
        dados.append((i["geoname_id"], {
            "country_code": i["country_code"], 
            "ascii_name": i["ascii_name"],
            "cou_name_en": i["cou_name_en"],
            "population": i["population"],
            "coordinates": i["coordinates"],
            "modification_date": i["modification_date"]
        }))
        c += 1
    return dados
