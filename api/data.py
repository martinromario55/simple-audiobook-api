import json

# Open JSON file
def parse_json_data(filename):
    with open(filename, "r") as f:
        # Parse data file
        data = json.load(f)
    return data
    
# Access data
# print(data["audiobooks"][0]["title"])
# print(data["audiobooks"][0]["author"])
# print(data["audiobooks"][0])

