import webbrowser


class Movie():
        """This class provides a way to store movie related information"""
        VALID_RATINGS = ["G", "PG", "PG-13", "R"]

        def __init__(
                self, movie_title, movie_storyline, poster_image, trailer_youtube
                ):
                """
                Initialize a Movie object
                Parameters
                ----------
                arg1 : str
                        movie_title = a string of the movie's title
                arg2 : srt
                        movie_storyline = a string containing the \
                        story line of the movie
                arg3 : str
                        poster_image = a string containing a URL \
                        to a poster image
                arg4 : str
                        trailer_youtube = a string containing a \
                        youtube URL of the movie's trailer
                """
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
                """ Opens trailer in a web browser"""
                webbrowser.open(self.trailer_youtube_url)
