import requests
import json

respond = requests.get("https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=30&before=233450431")
#jsonData = json.loads(respond.text)
jsonData = respond.json
count = 1
for data in jsonData:
    Data = {"Title":data['title'],
            "Topic":data['topics'],
            "Gender":data['gender'],
            "School":data['school']}
    with open("dcard_pet_40info.json","a", encoding="utf-8") as file:
        json.dump(Data, file,ensure_ascii=False)