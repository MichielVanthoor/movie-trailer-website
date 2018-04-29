# Importing required modules
import media
import fresh_tomatoes


# Creating multiple instances representing my favorite movies
toy_story = media.Movie("Toy Story",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=eNt1jF4fhnE")

avatar = media.Movie("Avatar",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=aVdO-cx-McA")

star_wars = media.Movie("Star Wars",
                        "https://pbs.twimg.com/media/DLvAUShUIAASVox.jpg",  # NOQA
                        "https://youtu.be/Q0CbN8sfihY")

# Group all instances together in a list
movies = [toy_story, avatar, star_wars]

# Generate website
fresh_tomatoes.open_movies_page(movies)
