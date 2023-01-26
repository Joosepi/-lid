import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
movies = []
for td in soup.find_all('td', class_='titleColumn'):
    title = td.find('a').get_text()
    year = td.find('span').get_text()[1:5]
    rating = td.find('strong').get_text()
    movies.append({'title': title, 'year': year, 'rating': rating})

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# convert the rating strings to floats
for movie in movies:
    movie['rating'] = float(movie['rating'])

# create a count vectorizer and fit it to the title data
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform([movie['title'] for movie in movies])

# calculate cosine similarity
similarity = cosine_similarity(X)

# define a function to recommend similar movies
def recommend(title, n=10):
    index = next((i for i, movie in enumerate(movies) if movie['title'] == title), None)
    if index is not None:
        similarities = list(enumerate(similarity[index]))
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
        similarities = similarities[1:(n+1)]
        recommended_movies = [movies[i]['title'] for i, sim in similarities]
        return recommended_movies
    else:
        return None

# test the function
print(recommend("The Shawshank Redemption"))
