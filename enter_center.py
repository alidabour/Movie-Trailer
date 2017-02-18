import fresh_tomatoes
import utils
#get list of movies from utils
movies = utils.getMovies()
#genrate html page 
fresh_tomatoes.open_movies_page(movies)
