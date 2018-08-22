# imports HTML & CSS formating for the wenpage
import fresh_tomatoes
import media

# movie details
city_of_angels = media.Movie("City of Angels",
                             "A romance Movie",
                             "https://bit.ly/2JuK2sY",
                             "https://www.youtube.com/watch?v=mwWL8cB2Ix8")

print (city_of_angels.storyline)


UP = media.Movie("UP",
                 "A family movie",
                 "https://bit.ly/2r3afHw",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

print (UP.storyline)


Fearless = media.Movie("Fearless",
                       "A Kung Fu Movie",
                       "https://bit.ly/2JvfAik",
                       "https://www.youtube.com/watch?v=23LxENZE8zo")

print (Fearless.storyline)

# idintifying the names of movies will be presented as a list
movies = [city_of_angels, UP, Fearless]

# Open the movie website in the user's browser, featuring the movies above
fresh_tomatoes.open_movies_page(movies)

print (media.Movie.VALID_RATINGS)
