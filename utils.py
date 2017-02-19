import media
movies = []
# return list of movies


def getMovies():
    return movies
# movie detial
title = "Gone Girl"
poster_image_url = (
    'M/MV5BMTk0MDQ3MzAzOV5BMl5BanBnXkFtZTgwNzU1NzE3MjE'
    '@._V1_SY1000_CR0,0,678,1000_AL_.jpg')
youtube_key = "Ym3LB0lOJ0o"
# add movie from media to movies list
movies.extend([media.Movie(title, poster_image_url, youtube_key)])

# same steps again 5 times
title = "Shawshank Redemption"
poster_image_url = (
    'M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE'
    '@._V1_UY1200_CR88,0,630,1200_AL_.jpg')
youtube_key = "6hB3S9bIaco"
movies.extend([media.Movie(title, poster_image_url, youtube_key)])

title = "Arrival"
poster_image_url = (
    'M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy'
    '._V1_SY1000_CR0,0,640,1000_AL_.jpg')
youtube_key = "tFMo3UJ4B4g"
movies.extend([media.Movie(title, poster_image_url, youtube_key)])

title = "Zootopia"
poster_image_url = (
    'M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE'
    '@._V1_SY1000_SX675_AL_.jpgv')
youtube_key = "jWM0ct-OLsM"
movies.extend([media.Movie(title, poster_image_url, youtube_key)])

title = "Steve Jobs"
poster_image_url = (
    'M/MV5BMjE0NTA2MTEwOV5BMl5BanBnXkFtZTgwNzg4NzU2NjE'
    '@._V1_SY1000_CR0,0,631,1000_AL_.jpg')
youtube_key = "ZK6lrmDu7UM"
movies.extend([media.Movie(title, poster_image_url, youtube_key)])

title = "12 Angry Men"
poster_image_url = (
    'M/MV5BODQwOTc5MDM2N15BMl5BanBnXkFtZTcwODQxNTEzNA'
    '@@._V1_SY1000_CR0,0,666,1000_AL_.jpg')
youtube_key = "fSG38tk6TpI"
movies.extend([media.Movie(title, poster_image_url, youtube_key)])
