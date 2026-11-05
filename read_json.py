import json

with open("responses.json") as f:
    data = json.load(f)

print(data)
print(type(data))


try:
    print(data["response"])
except KeyError:
    print("Missing key: Response")

try:
    print(data["tags"][0])
except IndexError:
    print("No tag at position 5")

print("Script kept going!")