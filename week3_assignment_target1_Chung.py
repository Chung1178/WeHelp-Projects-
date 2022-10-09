import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) #取得網站原始碼
#print(data)
#取得所需資訊 列表出來
NeededList=data["result"]["results"]
with open("data.csv", mode="w", encoding="utf-8") as file:
    for info in NeededList:
        year=int(info["xpostDate"][0:4])
        jpg=info["file"].split("https")
        firstjpg="https"+jpg[1]
        if year >=2015:
            file.write(
                info["stitle"]+","
                +info["address"][5:8]+","
                +info["longitude"]+","
                +info["latitude"]+","
                +firstjpg
                +"\n"
                )