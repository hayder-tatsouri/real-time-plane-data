import requests, json

url = "https://opensky-network.org/api/states/all?lamin=36.6&lomin=9.8&lamax=37.1&lomax=10.5"

print("Calling OpenSky...")
r = requests.get(url, timeout=10)
print(f"Status code : {r.status_code}")
print(f"Response size: {len(r.text)} bytes")
print(f"First 300 chars: {r.text[:300]}")
print()

data = r.json()
states = data.get("states")
print(f"'states' key value: {states}")
print(f"Type: {type(states)}")

if states:
    print(f"\nFound {len(states)} planes. First one:")
    print(states[0])
else:
    print("\n→ states is None or empty list — OpenSky returned no aircraft in that bbox right now.")
    print("  Try widening the bbox or waiting a few minutes and retrying.")
