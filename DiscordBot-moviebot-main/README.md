# $description
## Description:
	Returns the description for either a movie or TV show or a collection
## parameter_1 - identifier for movie or tv show or collection:
	Any of ['m', 'mov', 'movie', 'movies'] for a movie.
	Any of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.
	Any of ['c', 'collections', 'collection'] for a collection.
## parameter_2 - the title:
	The title of the movie or TV show or collection, the closer the better.
 

 
# $poster
## Description:	
	Returns the poster for either a movie or TV show or a collection or a person
## parameter_1 - identifier for movie or tv show or collection or person:
	Any of ['m', 'mov', 'movie', 'movies'] for a movie.
	Any of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.
	Any of ['c', 'collections', 'collection'] for a collection.
	Any of ['person', 'actor', 'p', 'actress', 'director', 'actors'] for a person.
## parameter_2 - the title or name:
	The title of the movie or TV show or collection or the name of the person, the closer the better.
## parameter_3 - (optional) season number:
	In case of TV show, we can provide an optional season number as {s<num>}. If season number is absent or invalid, the poster for the whole series is returned.
 

 
# $genres
## Description:	
	Returns the list of genres for either a movie or TV show or a collection
## parameter_1 - identifier for movie or tv show:
	Any of ['m', 'mov', 'movie', 'movies'] for a movie.
	Any of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.
## parameter_2 - the title:
	The title of the movie or TV show, the closer the better.
 

 
# $rating
## Description:
	Returns the rating and popularity for either a movie or TV show or a collection
## parameter_1 - identifier for movie or tv show
	Any of ['m', 'mov', 'movie', 'movies'] for a movie.
	Any of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.
## parameter_2 - the title
	The title of the movie or TV show, the closer the better.
 

 
# $production_companies
## Description:
	Returns the list of production for either a movie or TV show or a collection
## parameter_1 - identifier for movie or tv show
	Any of ['m', 'mov', 'movie', 'movies'] for a movie.
	Any of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.
## parameter_2 - the title
	The title of the movie or TV show, the closer the better. 
 

 
# $tagline
## Description:
	Returns the tagline for either a movie or TV show or a collection
## parameter_1 - identifier for movie or tv show:
	Any of ['m', 'mov', 'movie', 'movies'] for a movie.
	Any of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.
## parameter_2 - the title:
	The title of the movie or TV show, the closer the better.
 

 
# $summary
## Description:	
	Returns the summary for either a TV show or a collection or a person
## parameter_1 - identifier for TV show or a collection or a person:
	Any of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.
	Any of ['c', 'collections', 'collection'] for a collection.
	Any of ['person', 'actor', 'p', 'actress', 'director', 'actors'] for a person.
## parameter_2 - the title or name:
s	The title of the TV show or collection or the name of the person, the closer the better.