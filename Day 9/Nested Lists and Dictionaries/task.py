from tracemalloc import Frame

my_dictionary = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])


nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"])

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(dict["b"])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])

starting_dictionary = {
    "a": 10,
    "b": 8,
}
final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
starting_dictionary = ["c"]
starting_dictionary = final_dictionary
print(starting_dictionary)


input(int(7))
print(int(7))
