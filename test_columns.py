import pandas as pd

movies = pd.read_csv("Files/tmdb_5000_movies.csv")
credits = pd.read_csv("Files/tmdb_5000_credits.csv")

print("Movies columns:", movies.columns)
print("Credits columns:", credits.columns)
