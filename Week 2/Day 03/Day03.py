import csv
import json

# Working with CSV
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 23])
    writer.writerow(['Bob', 30])

# Working with JSON
data = {'name': 'Alice', 'age': 23}
with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
