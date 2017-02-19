import webbrowser


class Movie():
    """Movie provide the basic information about movie
    through title , poster image , youtube trailer"""
    baseImgUrl = "https://images-na.ssl-images-amazon.com/images/"
    baseYouUrl = "https://www.youtube.com/watch?v="

    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = self.baseImgUrl + poster_image
        self.trailer_youtube_url = self.baseYouUrl + trailer_youtube
        print self.poster_image_url
