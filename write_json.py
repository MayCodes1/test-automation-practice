import json

result = {
    "id": 1,
    "check": "no em dashes",
    "passed": True,
    "issues": None
}

with open("results.json", "w") as f:
    json.dump(result, f, indent=2)

print("Saved!")