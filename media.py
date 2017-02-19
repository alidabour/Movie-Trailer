import webbrowser


class Movie():
    """Movie provide the basic information about movie
    through title , poster image , youtube trailer"""

    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = (
            'https://images-na.ssl-images-amazon.com/images/' +
            poster_image)
        self.trailer_youtube_url = (
            'https://www.youtube.com/watch?v=' +
            trailer_youtube)
