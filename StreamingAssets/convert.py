import sqlite3
import json

# Open a connection to the SQLite database
conn = sqlite3.connect('farmburgh_data.db')
cursor = conn.cursor()

# Open the JSON file and parse the data
with open('useablebuilding_data.json') as json_file:
    json_data = json.load(json_file)

# Insert the data into the table
for json_data2 in json_data:
    cursor.execute('INSERT INTO useablebuilding_data (key, name, cost, type, slots, size_x, size_y, crafting_types, animal_types, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (json_data2, json_data[json_data2]['name'], json_data[json_data2]['cost'], json_data[json_data2]['type'], json_data[json_data2]['slots'], json_data[json_data2]['size_x'], json_data[json_data2]['size_y'], json_data[json_data2]['crafting_types'], json_data[json_data2]['animal_types'], json_data[json_data2]['description']))
# Commit the transaction
    conn.commit()

# Close the connection
conn.close()