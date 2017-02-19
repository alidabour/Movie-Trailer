import webbrowser


class Movie():
    """Movie provide the basic information about movie
    through title , poster image , youtube trailer"""
    baseImgUrl = "https://images-na.ssl-images-amazon.com/images/"
    baseYouUrl = "https://www.youtube.com/watch?v="

    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = baseImgUrl + poster_image
        self.trailer_youtube_url = baseYouUrl + trailer_youtube
