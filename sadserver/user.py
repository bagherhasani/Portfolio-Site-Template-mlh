import json

with open("user.json") as file:
    data=json.load(file)

    for item in data:
        name=item["name"]
        team=item["team"]
        score=item["score"]

        print(name,team,score)