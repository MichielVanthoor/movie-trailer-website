# Importing required modules
import webbrowser


# Creating Movie data structure
class Movie():
    # Constructor method to constuct a new sinstance
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
