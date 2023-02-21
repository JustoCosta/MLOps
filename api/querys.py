import pandas as pd

#Extraemos los csv limpios y los cargamos en formato dataframe

Dfamazon = pd.read_csv('datasets/amazon_clean.csv')
Dfnetflix = pd.read_csv('datasets/netflix_clean.csv')
Dfdisney = pd.read_csv('datasets/disney_clean.csv')
Dfhulu = pd.read_csv('datasets/hulu_clean.csv')

class Querys: 
    def __init__(self, platform, keyword, score , year, durationtype, rating):
        self.platform = platform
        self.keyword = keyword
        self.score = score
        self.year = year
        self.durationtype = durationtype
        self.rating = rating
    
    #Consulta 1

    def get_max_duration(year, platform, durationtype):
        if (platform == 'netflix'):
            Df = Dfnetflix.query("release_year == @year and duration_type == @durationtype")
            Df1 = Df.sort_values( by = 'duration_int' , ascending = False)
            title = str(Df1['title'].iloc[0])
            duration = str(Df1['duration_int'].iloc[0])
            if durationtype == 'min':
                return 'La pelicula con mayor duración de ' + platform +' en el año ' + str(year) + ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
            if durationtype == 'season':
                return 'La serie con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
        if (platform == 'amazon'):
            Df = Dfamazon.query("release_year == @year and duration_type == @durationtype")
            Df1 = Df.sort_values( by = 'duration_int' , ascending = False)
            title = str(Df1['title'].iloc[0])
            duration = str(Df1['duration_int'].iloc[0])
            if durationtype == 'min':
                return 'La pelicula con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
            if durationtype == 'season':
                return 'La serie con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
        if (platform == 'disney'):
            Df = Dfdisney.query("release_year == @year and duration_type == @durationtype")
            Df1 = Df.sort_values( by = 'duration_int' , ascending = False)
            title = str(Df1['title'].iloc[0])
            duration = str(Df1['duration_int'].iloc[0])
            if durationtype == 'min':
                return 'La pelicula con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
            if durationtype == 'season':
                return 'La serie con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
        if (platform == 'hulu'):
            Df = Dfhulu.query("release_year == @year and duration_type == @durationtype")
            Df1 = Df.sort_values( by = 'duration_int' , ascending = False)
            title = str(Df1['title'].iloc[0])
            duration = str(Df1['duration_int'].iloc[0])
            if durationtype == 'min':
                return 'La pelicula con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
            if durationtype == 'season':
                return 'La serie con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'       
        else:    
            return 'No existe esa Plataforma'

    #Consulta 2

    def get_score_count(platform , score , year):
        if (platform == 'netflix'):
            return 'La cantidad de peliculas con un puntaje mayor a ' + str(score) + ' en el año '+ str(year)+ ' es de ' + str(len(Dfnetflix.query("type == 'movie' and score > @score and release_year == @year")))
        if (platform == 'amazon'):
            return 'La cantidad de peliculas con un puntaje mayor a ' + str(score) + ' en el año '+ str(year)+ ' es de ' + str(len(Dfamazon.query("type == 'movie' and score > @score and release_year == @year")))
        if (platform == 'disney'):
            return 'La cantidad de peliculas con un puntaje mayor a ' + str(score) + ' en el año '+ str(year)+ ' es de ' + str(len(Dfdisney.query("type == 'movie' and score > @score and release_year == @year")))
        if (platform == 'hulu'):
            return 'La cantidad de peliculas con un puntaje mayor a ' + str(score) + ' en el año '+ str(year)+ ' es de ' + str(len(Dfhulu.query("type == 'movie' and score > @score and release_year == @year")))
        else:    
            return 'No existe esa Plataforma'
    
    #Consulta 3

    def get_count_platform(platform):
        if (platform == 'amazon'):
            return 'La cantidad de Peliculas en ' + str(platform) + ' es de ' + str(len(Dfamazon.query("type == 'movie'")))
        if (platform == 'netflix'):
            return 'La cantidad de Peliculas en ' + str(platform) + ' es de ' + str(len(Dfnetflix.query("type == 'movie'")))
        if (platform == 'disney'):
            return 'La cantidad de Peliculas en ' + str(platform) + ' es de ' + str(len(Dfdisney.query("type == 'movie'")))
        if (platform == 'hulu'):
            return 'La cantidad de Peliculas en ' + str(platform) + ' es de ' + str(len(Dfhulu.query("type == 'movie'")))
        else:    
            return print('No existe esa Plataforma (Intente todo en minúsculas)')

    #Consulta 4

    def get_actor(platform, year):
        if (platform == 'amazon'):
            platform_year_movies = Dfamazon.query("release_year == @year")
            actors = platform_year_movies['cast'].str.split(',').explode()
            actor_counts = actors.value_counts()
            most_common_actor = actor_counts.index[0]
            return 'El Actor que más aparece en la plataforma ' + str(platform) + ' en el año ' + str(year) + ' es: ' + str(most_common_actor)
            
        if (platform == 'netflix'):
            platform_year_movies = Dfnetflix.query("release_year == @year")
            actors = platform_year_movies['cast'].str.split(',').explode()
            actor_counts = actors.value_counts()
            most_common_actor = actor_counts.index[0]
            return 'El Actor que más aparece en la plataforma ' + str(platform) + ' en el año ' + str(year) + ' es: ' + str(most_common_actor)
        
        if (platform == 'disney'):
            platform_year_movies = Dfdisney.query("release_year == @year")
            actors = platform_year_movies['cast'].str.split(',').explode()
            actor_counts = actors.value_counts()
            most_common_actor = actor_counts.index[0]
            return 'El Actor que más aparece en la plataforma ' + str(platform) + ' en el año ' + str(year) + ' es: ' + str(most_common_actor)
        
        if (platform == 'hulu'):
           
            return 'La plataforma hulu no provee la información de los actores en sus peliculas!'
        
        else:    
            return print('No existe esa Plataforma (Intente todo en minúsculas)')

    #Consultas Extras (Cohorte anterior)

    def get_word_count(platform , keyword):
        if (platform == 'amazon'):
            return Dfamazon['title'].str.contains(keyword).sum()
        if (platform == 'netflix'):
            return Dfnetflix['title'].str.contains(keyword).sum()
        if (platform == 'disney'):
            return Dfdisney['title'].str.contains(keyword).sum()
        if (platform == 'hulu'):
            return Dfhulu['title'].str.contains(keyword).sum()
        else:    
            return print('No existe esa Plataforma')

    def get_second_score(platform):
        if (platform == 'netflix'):
            Df = Dfnetflix.query("type == 'movie'")
            n = Df['score'].max()
            c = Df.apply(lambda x: x['score'] == n, axis=1).sum()
            maximos = Df.nlargest(c, ['score'])
            ordenados = maximos['title'].sort_values()
            ordenados.iloc[1]
            return 'La segunda pelicula de '+ platform +' con mayor puntaje en orden alfabético es '+ ordenados.iloc[1] + ' con un puntaje de '+ str(n)
        if (platform == 'amazon'):
            Df = Dfamazon.query("type == 'movie'")
            n = Df['score'].max()
            c = Df.apply(lambda x: x['score'] == n, axis=1).sum()
            maximos = Df.nlargest(c, ['score'])
            ordenados = maximos['title'].sort_values()
            ordenados.iloc[1]
            return 'La segunda pelicula de '+ platform +' con mayor puntaje en orden alfabético es '+ ordenados.iloc[1] + ' con un puntaje de '+ str(n)
        if (platform == 'disney'):
            Df = Dfdisney.query("type == 'movie'")
            n = Df['score'].max()
            c = Df.apply(lambda x: x['score'] == n, axis=1).sum()
            maximos = Df.nlargest(c, ['score'])
            ordenados = maximos['title'].sort_values()
            ordenados.iloc[1]
            return 'La segunda pelicula de '+ platform +' con mayor puntaje en orden alfabético es '+ ordenados.iloc[1] + ' con un puntaje de '+ str(n)
        if (platform == 'hulu'):
            Df = Dfhulu.query("type == 'movie'")
            n = Df['score'].max()
            c = Df.apply(lambda x: x['score'] == n, axis=1).sum()
            maximos = Df.nlargest(c, ['score'])
            ordenados = maximos['title'].sort_values()
            ordenados.iloc[1]
            return 'La segunda pelicula de '+ platform +' con mayor puntaje en orden alfabético es '+ ordenados.iloc[1] + ' con un puntaje de '+ str(n)
        else:    
            return 'No existe esa Plataforma'
    
    def get_rating_count(rating):
        n = Dfnetflix.apply(lambda x: x['rating'] == str(rating), axis = 1).sum()
        d = Dfdisney.apply(lambda x: x['rating'] == str(rating), axis = 1).sum() 
        a = Dfamazon.apply(lambda x: x['rating'] == str(rating), axis = 1).sum()
        h = Dfhulu.apply(lambda x: x['rating'] == str(rating), axis = 1).sum()
        return 'La cantidad de series y peliculas por rating = ' + rating + ' es de ' +str(n + d + a + h) + ' en las cuatro plataformas'

# Prueba de las funciones

#Consulta 1

print(Querys.get_max_duration(2014, 'netflix', 'min'))

#Consulta 2

print(Querys.get_score_count('netflix', 3.5 , '2014'))

#Consulta 3

print(Querys.get_count_platform('netflix'))

#Consulta 4

print(Querys.get_actor('hulu', 2014))