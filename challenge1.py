import json

places= []
while True:
    place = input("Enter the name of a place(or type 'stop' to finish): ").strip()

    if place.lower()== 'stop':
        break

    places.append(place)

    places_json = json.dumps(places, indent=4)

    print("\nPlaces you entered:")
    print(places_json)