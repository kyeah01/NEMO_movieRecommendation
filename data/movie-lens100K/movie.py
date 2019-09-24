import csv

def genre_make():
    with open('u.genre', 'r', encoding="UTF-8") as p:
        res = []
        for line in p.readlines():
            value, key = line.split('|')
            res += [value]
    return res

def poster_url():
    with open('movie_poster.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, quotechar=',')
        res = {}
        for row in reader:
            res[row[0]] = row[1]
    return res

def movie_make(genre_name, poster):
    with open('u.item', 'r', encoding = "ISO-8859-1") as p:
        res = []
        for line in p.readlines():
            # ['1682', 'Scream of Stone (Schrei aus Stein) (1991)', '08-Mar-1996', '', 'http://us.imdb.com/M/title-exact?Schrei%20aus%20Stein%20(1991)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0\n']
            movie = line.split('|')[:-1]
            movie = {
                'id' : movie[0],
                'title' : movie[1],
                'date' : movie[2],
                'genres' : [genre_name[i] for i in range(len(movie[5:])) if int(movie[5+i])],
                'poster_url' : poster.get(movie[0])
            }
            print(movie)
        

if __name__ == '__main__':
    genres = genre_make()
    poster = poster_url()
    movie_make(genres, poster)