movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1. Check if a movie has an IMDB score above 5.5
def is_highly_rated(movie):
    return movie["imdb"] > 5.5

print(is_highly_rated(movies[0]))
print("                                                            ")
# 2. Get a list of movies with an IMDB score above 5.5
def highly_rated_movies(movies):
    return [movie["name"] for movie in movies if movie["imdb"] > 5.5]

print(highly_rated_movies(movies))
print("                                                            ")
# 3. Get movies by category
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

print(movies_by_category(movies, "Romance"))
print("                                                            ")
# 4. Compute the average IMDB score of a list of movies
def average_imdb_score(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

print(average_imdb_score(movies))
print("                                                            ")
# 5. Compute the average IMDB score of movies in a category
def average_category_imdb_score(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)

print(average_category_imdb_score(movies, "Romance"))
