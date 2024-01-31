import requests

print(requests.get('http://localhost:8080/get_random_musics', data={"id":"1", "relax":"2.4","consentration":"4.6"}))


# print(requests.get('http://192.168.1.175:8080/get_random_musics').json())
