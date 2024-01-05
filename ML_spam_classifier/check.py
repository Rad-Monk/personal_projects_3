import requests

url = "https://api.themoviedb.org/3/movie/65?api_key=2e6ffacd0054f31b37192432b3018716&language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTZmZmFjZDAwNTRmMzFiMzcxOTI0MzJiMzAxODcxNiIsInN1YiI6IjY1NTk5YjliNTM4NjZlMDEzOWUzZmJkNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CCgJ8NilYDXV7MpHI-SacpF4lxyxGWYQScMDqCAojOY"
}

response = requests.get(url, headers=headers)

print(response.text)