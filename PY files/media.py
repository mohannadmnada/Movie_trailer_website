# opens a web browser
import webbrowser

# This class provides a way to store movie information


class Movie():
    VALID_RATINGS = ["G", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # starts Movie class instance variables'
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Plays the movie trailer in the web browser
        webbrowser.open(self.trailer_youtube_url)
