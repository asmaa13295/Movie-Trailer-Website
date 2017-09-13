import webbrowser
# defining a general class to define multiple intances of films


class Movie():
    """this is the documentation of class Movie"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor of class
    def __init__(self, movie_title,  movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # defininf a function to open the wenbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
