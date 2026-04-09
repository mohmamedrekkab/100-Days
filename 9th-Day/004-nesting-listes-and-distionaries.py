# Nesting
capitals ={
    "France":"Paris",
    "Germany":"Berline"
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany":["Berline", "Hamburg", "Stutgart"]
}

travel_log2= {
    "France": {"Cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany":{"Cities_visited":["Berline","Hamburg","Stutgart"], "total_visits":5}
}

print(travel_log2)

# Nesting a dictionary in a list

travel_log3= [
    {
    "Country":"France", 
     "Cities_visited":["Paris", "Lille", "Dijon"], 
     "total_visits": 12
     },
    {
    "Country":"Germany",
    "Cities_visited":["Berline","Hamburg","Stutgart"], 
    "total_visits":5
    }
]
print(travel_log3)