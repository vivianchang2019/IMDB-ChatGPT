import requests
from bs4 import BeautifulSoup
import numpy as np


class MovieData:
    def __init__(self, rank, name, rating, director, stars, url, likes):
        """
        Initialize a new MovieData object with the given rank, name, rating, director, stars, URL, and likes.

        Args:
            rank (int): The movie's ranking on the list.
            name (str): The movie's name.
            rating (float): The movie's rating.
            director (str): The movie's director.
            stars (str): The movie's stars.
            url (str): The URL of the movie's IMDb page.
            likes (int): The number of likes the movie has.
        """
        self.rank = rank
        self.name = name.strip()
        self.rating = rating.strip()
        self.director = director.strip()
        self.stars = stars.strip()
        self.url = url.strip()
        self.likes = likes

    def __str__(self):
        return f'{self.rank}. {self.name} ({self.rating}) {self.director}  {self.stars} | {self.url} | Likes: {self.likes}'

    def write_to_file(self, filename):
        """
        Write the movie data to a file.

        Args:
            filename (str): The name of the file to write to.
        """
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                # Write the movie data to the file in a specific format.
                file.write(f'This is the Top {self.rank} movie in the IMDB top 250 ranking.\
                The Chinese movie name is {self.name}.\
                The rating of movie in IMDB is {self.rating}.\
                The director of the movie is {self.director}.\
                The actors and movie stars of the movie are {self.stars}.\
                The information web page of this movie in IMDB website is {self.url}.\
                The number of likes of this movie is {self.likes}.\n')
        except Exception as e:
            print(f'Error writing to file: {e}')

    def get_init_info(self):
        """
        Get information about each item in the initializer.

        Returns:
            dict: A dictionary containing the name and value of each item in the initializer.
        """
        return {"rank": self.rank, "name": self.name, "rating": self.rating, "director": self.director, \
                "stars": self.stars, "url": self.url, "likes": self.likes}


def generate_like():
    """
    Generate a random number of likes for the movie.

    Returns:
        int: A random integer between 0 and 1000, generated from a normal distribution.
    """
    mean = 500
    std_dev = 150
    likes = int(np.random.normal(mean, std_dev))
    likes = min(max(likes, 0), 1000)  # ensure likes is between 0 and 1000
    return likes


def scrape_imdb_top_movies(url):
    """
    Scrapes the IMDb Top 250 movies list from the given URL and returns a list of MovieData objects,
    each containing information about a single movie.

    Args:
        url (str): The URL of the IMDb Top 250 movies list.

    Returns:
        list: A list of MovieData objects, each containing information about a single movie.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'chart full-width'})
    rows = table.find_all('tr')
    movies = []

    for i, row in enumerate(rows):
        title_column = row.find('td', {'class': 'titleColumn'})
        if title_column is not None:
            movie_link = title_column.find('a')

            # get movie name
            movie_name = movie_link.text

            # get movie title
            movie_title = movie_link["title"].split('(dir.),')
            movie_director = movie_title[0]
            movie_stars = movie_title[1]

            # get movie rating
            rating_column = row.find('td', {'class': 'ratingColumn'})
            movie_rating = rating_column.find('strong').text

            # get movie detail URL
            movie_url = f'https://www.imdb.com{movie_link["href"]}'

            # get movie likes
            movie_likes = generate_like()

            # create a class to store all movie information
            movies.append(MovieData(i, movie_name, movie_rating, movie_director, movie_stars, movie_url, movie_likes))

    return movies


def show_movie(file_path):
    # Open the file in write mode to empty its contents
    with open(file_path, 'w', encoding='utf-8'):
        pass

    # Scrape the top movies and write their info to the file
    imdb_movie_url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    movies = scrape_imdb_top_movies(imdb_movie_url)
    for movie in movies:
        movie.write_to_file(file_path)
        print(movie)



if __name__ == '__main__':
    filename = "data/imdb_movie.txt"
    show_movie(filename)