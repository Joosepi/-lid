# küsime IMDB-lt Top filmide nimekirja
url = 'https://www.imdb.com/chart/top'
response = requests.get(url)

# salvestame vastuse sisu muutujasse html_content
html_content = response.content

# kasutame BeautifulSoup-i, et lihtsustada HTML-i lugemist
soup = BeautifulSoup(html_content, 'html.parser')

# loome listi filmidest, mis on nimekirjas
movies = []
for td in soup.find_all('td', class_='titleColumn'):
    # leiame ja salvestame filmi pealkirja
    title = td.find('a').get_text()
    # leiame ja salvestame filmi ilmumisaasta
    year = td.find('span').get_text()[1:5]
    # leiame ja salvestame filmi hinnet
    rating = td.find('strong').get_text()
    # lisame filmi andmed movies listi
    movies.append({'title': title, 'year': year, 'rating': rating})

# muudame filmide hinded float tüüpi muutujateks
for movie in movies:
    movie['rating'] = float(movie['rating'])

# kasutame CountVectorizer-it filmide pealkirjade kirjeldamiseks sõnena
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform([movie['title'] for movie in movies])

# arvutame filmide vahelise sarnasuse
similarity = cosine_similarity(X)

# defineerime funktsiooni, mis soovitab sarnaseid filme
def recommend(title, n=10):
    # leiame antud filmi asukoha movies listis
    index = next((i for i, movie in enumerate(movies) if movie['title'] == title), None)
    # kui film on nimekirjas
    if index is not None:
        # leiame selle filmiga sarnased filmid
        similarities = list(enumerate(similarity[index]))
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
        similarities = similarities[1:(n+1)]
        recommended_movies = [movies[i]['title'] for i, sim in similarities]
        # tagastame soovitatud filmide nimed
        return recommended_movies
    else:
        # kui filmi ei leitud, tagastame None
        return None

# prindime välja soovitatud filmid pealkirja "The Shawshank Redemption" järgi
print(recommend("The Shawshank Redemption"))
