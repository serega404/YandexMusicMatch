import requests 

base_url = "https://music.yandex.ru/handlers/playlist.jsx?kinds=3&owner="

print("Введите имя пользователя 1: ")
name1 = input()

print("Введите имя пользователя 2: ")
name2 = input()

data = requests.get(base_url + name1).json()
user1tracks = data["playlist"]["tracks"]

data = requests.get(base_url + name2).json()
user2tracks = data["playlist"]["tracks"]

similarTracks = []

for track1 in user1tracks:
    for track2 in user2tracks:
        if track1["id"] == track2["id"]:
            similarTracks.append(track1)

print("Общие треки: ")
for track in similarTracks:
    print(track["title"] + " - " + track["artists"][0]["name"])
