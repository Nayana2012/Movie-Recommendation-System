from os import name
from time import time
import pandas as pd
from sklearn. feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
 
init(autoreset=True)

def load_data(file_path="imdb_top_250.csv"):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(Fore.RED + f"Error loading data: {e}")
        return None
    exit()
    movie_df= load_data()
Tfidf=TfidfVectorizer(stop_words='english')
tfidf_matrix=Tfidf.fit_transform(movie_df['combined_features'])
cosine_sim=cosine_similarity(tfidf_matrix,tfidf_matrix)
def recmmend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_movies = movie_df 
    if genre:
        filtered_movies = filtered_movies[filtered_movies['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtered_movies = filtered_movies[filtered_movies['Rating'] >= rating]
    filtered_movies = filtered_movies.sample(frac=1).reset_index(drop=True)
    recommendations = []
    for index, row in filtered_movies.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity > 0 and polarity > 0) or (TextBlob(mood).sentiment.polarity < 0 and polarity < 0))):
            recommendations.append((row['Title'], row['Genre'], row['Rating']))
            if len(recommendations) >= top_n:
                break
    return recommendations if recommendations else "No movies found matching the criteria."
def display_recommendations(recs, name):

    print(Fore.YELLOW + f"\n AI-Analyzed Movie Recommendations for {name}:")

for idx, (title, genre, rating) in enumerate(recs, 1):

    polarity = TextBlob(title).sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

print(f"{Fore.CYAN}{idx}. {title} (Polarity: {polarity:.2f}, {sentiment})")

# Small processing animation

def processing_animation():

    for _ in range(3):

        print(Fore.YELLOW + ",", end="", flush=True)

# Handle AI recommendation flow

def handle_ai(name):

    print(Fore.BLUE + "\n Let's find the perfect movie for you!\n")

# Show genres in a single line

print(Fore.GREEN + "Available Genres: ", end="")

for idx, genre in enumerate(genres, 1):

    print(f"{Fore.CYAN}{idx}. {genre}")

print() # To move to the next line after all genres are listed

while True:

    genre_input = input(Fore.YELLOW + "Enter genre number or name: ").strip()

if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):

    genre = genres[int(genre_input)-1]

if genre_input.title() in genres:

    genre = genre_input.title()

print(Fore.RED + "Invalid input. Try again.\n")

mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()

# Processing animation while analyzing mood

print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)

processing_animation() # Small processing animation during mood analysis

polarity = TextBlob(mood).sentiment.polarity

mood_desc = "positive" # if polarity > 0 else "negative" # if polarity < 0 else "neutral"

print(f"\n{Fore.GREEN}Your mood is {mood_desc} (Polarity: {polarity:.2f}).\n")

print("What is your age ? (Enter a number): ", end="")
age = int(input())
if age >= 1 and age <= 18:
    print("You are a child. Here are some family-friendly movie recommendations:")
    recs = recmmend_movies(mood=mood, top_n=5)
    display_recommendations(recs, name)
else:
    print("You are an adult. Here are some movie recommendations based on your preferences:")
     
# Get recommendations based on genre, mood, and rating
recs = recmmend_movies(genre=genre, mood=mood, rating=7 if age >= 18 else None, top_n=5)
display_recommendations(recs, name)