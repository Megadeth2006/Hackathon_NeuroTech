from os import listdir, walk
from db import DB

db = DB()
def main():
    f = {}
    listing = listdir("static")
    for i in range(len(listing)):
        albom = listing[i].split('-')[0]
        author = listing[i].split('-')[1]
        for j in listdir('static/'+listing[i]):
            print(j, albom, author)
            print(db.musics_yep(j, albom, author))

    print('Урааааа')