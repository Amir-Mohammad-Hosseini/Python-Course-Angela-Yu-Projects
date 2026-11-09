travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]

    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country (country , visits , cities) :
    new_travel_datas = {
        "country" :country ,
        "visits":visits ,
         "cities" : cities
    }
    travel_log.append(new_travel_datas)
    print(travel_log)

add_new_country("Iran" , 2 , ["Tehran" , "Shiraz"])