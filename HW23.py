import json

with open("data.json", "r") as f:
    list_odd = json.load(f)
list_odd_d3 = [i for i in list_odd if i % 3 == 0]
average = sum(list_odd_d3) / len(list_odd_d3)
print(average)
