import csv

# Define the movie data
movies = [
    {"title": "Movie 1", "image": "https://via.placeholder.com/150", "genre": "Action", "year": 2021, "avg_rating": 4.5},
    {"title": "Movie 2", "image": "https://via.placeholder.com/150", "genre": "Comedy", "year": 2020, "avg_rating": 4.0},
    {"title": "Movie 3", "image": "https://via.placeholder.com/150", "genre": "Drama", "year": 2019, "avg_rating": 3.5},
    {"title": "Movie 4", "image": "https://via.placeholder.com/150", "genre": "Action", "year": 2021, "avg_rating": 4.2},
    {"title": "Movie 5", "image": "https://via.placeholder.com/150", "genre": "Action", "year": 2021, "avg_rating": 4.1},
    {"title": "Movie 6", "image": "https://via.placeholder.com/150", "genre": "Comedy", "year": 2020, "avg_rating": 3.8},
    {"title": "Movie 7", "image": "https://via.placeholder.com/150", "genre": "Drama", "year": 2019, "avg_rating": 4.3},
    {"title": "Movie 8", "image": "https://via.placeholder.com/150", "genre": "Drama", "year": 2019, "avg_rating": 4.0},
    {"title": "Movie 9", "image": "https://via.placeholder.com/150", "genre": "Horror", "year": 2018, "avg_rating": 3.9},
    {"title": "Movie 10", "image": "https://via.placeholder.com/150", "genre": "Horror", "year": 2018, "avg_rating": 4.1},
    {"title": "Movie 11", "image": "https://via.placeholder.com/150", "genre": "Horror", "year": 2018, "avg_rating": 3.7},
    {"title": "Movie 12", "image": "https://via.placeholder.com/150", "genre": "Horror", "year": 2018, "avg_rating": 4.0},
    {"title": "Movie 13", "image": "https://via.placeholder.com/150", "genre": "Action", "year": 2021, "avg_rating": 4.4},
    {"title": "Movie 14", "image": "https://via.placeholder.com/150", "genre": "Comedy", "year": 2020, "avg_rating": 3.9},
    {"title": "Movie 15", "image": "https://via.placeholder.com/150", "genre": "Drama", "year": 2019, "avg_rating": 4.2},
]

# Define the CSV file path
csv_file_path = 'movies.csv'

# Write the movie data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "image", "genre", "year", "avg_rating"])
    writer.writeheader()
    for movie in movies:
        writer.writerow(movie)

print(f"CSV file '{csv_file_path}' has been created successfully.")