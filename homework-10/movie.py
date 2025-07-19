import requests
from random import randint

API_KEY = "c6257f8a00f9e55e51d75ed4789b38db"  # Add your API key here
LIST_URL = "https://api.themoviedb.org/3/genre/movie/list?"


def ask_for_genre():
    """Get user input for genre and return a random movie from that genre."""
    user_input = input("Enter a movie genre: ")
    url = f"{LIST_URL}api_key={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching genres: {e}")
        return

    genre_id = get_id_genre(user_input, data)
    if genre_id is None:
        return

    search_url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    random_movie = return_random_movie(search_url)

    if random_movie:
        print(random_movie)


def get_id_genre(user_input, data):
    """Find the genre ID for the given genre name."""
    user_input_lower = user_input.lower()

    for genre in data['genres']:
        if user_input_lower == genre['name'].lower():
            return genre['id']

    print("Such genre does not exist!")
    return None


def return_random_movie(url):
    """Get a random movie from the API results."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching movies: {e}")
        return None

    if not data['results']:
        print("No movies found for this genre.")
        return None

    random_index = randint(0, len(data['results']) - 1)
    movie = data['results'][random_index]

    # Handle missing release date
    release_date = movie.get('release_date', 'Unknown')
    return f"{movie['original_title']} ({release_date})"


if __name__ == "__main__":
    ask_for_genre()