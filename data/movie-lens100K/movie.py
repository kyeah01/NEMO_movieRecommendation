def genre_make():
    with open('u.genre', 'r', encoding="utf-8") as p:
        res = {}
        for line in p.readlines():
            value, key = line.split('|')
            res[key if key=='18' else key[:-1]] = value
    print(res)

def movie_make():
    with open('u.item', 'rb') as p:
        res = []
        for line in p.readlines():
            
        

if __name__ == '__main__':
    genre_make()