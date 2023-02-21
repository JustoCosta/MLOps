import pandas as pd 
from extract import Extract

# Definimos variable 'path' 

pathnetflix = 'datasets/netflix_titles.csv'
pathamazon = 'datasets/amazon_prime_titles.csv'
pathhulu = 'datasets/hulu_titles.csv'
pathdisney = 'datasets/disney_plus_titles.csv'

path1 = ('ratings/1.csv')
path2 = ('ratings/2.csv')
path3 = ('ratings/3.csv')
path4 = ('ratings/4.csv')
path5 = ('ratings/5.csv')
path6 = ('ratings/6.csv')
path7 = ('ratings/7.csv')
path8 = ('ratings/8.csv')

#Extracción de las tablas ratings #

df1 = Extract.extract(path1)
df2 = Extract.extract(path2)
df3 = Extract.extract(path3)
df4 = Extract.extract(path4)
df5 = Extract.extract(path5)
df6 = Extract.extract(path6)
df7 = Extract.extract(path7)
df8 = Extract.extract(path8)

#Concatenación de las tablas ratings #

ratings = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis = 0)
ratings.rename(columns = {'rating' : 'score'}, inplace = True) #Cambiar el nombre de la columna rating a score

#Crear la columna score e integrarla a los datasets de las plataformas #
#Para crear la columna score por pelicula, hallaremos antes la media del puntaje de todos los usuarios #

score = ratings[['movieId', 'score']].groupby('movieId').mean()


# PLATAFORMA DISNEY #

Dfdisney = Extract.extract(pathdisney) #Leer el archivo csv
Dfdisney.insert(0, 'id', 'd' + Dfdisney['show_id'], allow_duplicates=False) #Insertar Columna 'id'
Dfdisney['rating'] = Dfdisney['rating'].fillna('G') #Reemplazar NaN por 'G' en columna 'rating'
Dfdisney['date_added'] = pd.to_datetime(Dfdisney['date_added']) #Cambiar formato de fecha
Dfdisney['type'] = Dfdisney['type'].str.lower() #Cambiar a minúsculas las columnas con formato string
Dfdisney['title'] = Dfdisney['title'].str.lower()
Dfdisney['director'] = Dfdisney['director'].str.lower()
Dfdisney['cast'] = Dfdisney['cast'].str.lower()
Dfdisney['country'] = Dfdisney['country'].str.lower()
Dfdisney['rating'] = Dfdisney['rating'].str.lower()
Dfdisney['listed_in'] = Dfdisney['type'].str.lower()
Dfdisney['description'] = Dfdisney['description'].str.lower()
Dfdisney[['duration_int', 'duration_type']] = Dfdisney['duration'].str.split(expand = True) #Separar la columna duration en dos
Dfdisney['duration_type'] = Dfdisney['duration_type'].str.lower().replace('seasons','season') #Cambiar a minusculas la nueva columna str y poner en singular
Dfdisney['duration_int'] = Dfdisney['duration_int'].fillna(0) #Cambiar valores NaN por '0'(sino no se puede convertir a entero)
Dfdisney['duration_int'] = Dfdisney['duration_int'].astype(int) #Cambiar la otra nueva columna a entero

Dfdisney = Dfdisney.merge(score, left_on = 'id', right_on='movieId', how='left') #Insertamos la nueva columna score según el índice de la película
Dfdisney['score'].fillna(0) #Cambiamos los valores nulos que no se pudieron integrar a 0


# PLATAFORMA NETFLIX #

Dfnetflix = Extract.extract(pathnetflix) #Leer el archivo csv
Dfnetflix.insert(0, 'id', 'n' + Dfnetflix['show_id'], allow_duplicates=False) #Insertar Columna 'id'
Dfnetflix['rating'] = Dfnetflix['rating'].fillna('G') #Reemplazar NaN por 'G' en columna 'rating'
Dfnetflix['date_added'] = pd.to_datetime(Dfnetflix['date_added']) #Cambiar formato de fecha
Dfnetflix['type'] = Dfnetflix['type'].str.lower() #Cambiar a minúsculas las columnas con formato string
Dfnetflix['title'] = Dfnetflix['title'].str.lower()
Dfnetflix['director'] = Dfnetflix['director'].str.lower()
Dfnetflix['cast'] = Dfnetflix['cast'].str.lower()
Dfnetflix['country'] = Dfnetflix['country'].str.lower()
Dfnetflix['rating'] = Dfnetflix['rating'].str.lower()
Dfnetflix['listed_in'] = Dfnetflix['type'].str.lower()
Dfnetflix['description'] = Dfnetflix['description'].str.lower()
Dfnetflix[['duration_int', 'duration_type']] = Dfnetflix['duration'].str.split(expand = True) #Separar la columna duration en dos
Dfnetflix['duration_type'] = Dfnetflix['duration_type'].str.lower().replace('seasons','season') #Cambiar a minusculas la nueva columna str y poner en singular
Dfnetflix['duration_int'] = Dfnetflix['duration_int'].fillna(0) #Cambiar valores NaN por '0'(sino no se puede convertir a entero)
Dfnetflix['duration_int'] = Dfnetflix['duration_int'].astype(int) #Cambiar la otra nueva columna a entero

Dfnetflix = Dfnetflix.merge(score, left_on = 'id', right_on='movieId', how='left') #Insertamos la nueva columna score según el índice de la película
Dfnetflix['score'].fillna(0) #Cambiamos los valores nulos que no se pudieron integrar a 0


# PLATAFORMA AMAZON #

Dfamazon = Extract.extract(pathamazon) #Leer el archivo csv
Dfamazon.insert(0, 'id', 'a' + Dfamazon['show_id'], allow_duplicates=False) #Insertar Columna 'id'
Dfamazon['rating'] = Dfamazon['rating'].fillna('G') #Reemplazar NaN por 'G' en columna 'rating'
Dfamazon['date_added'] = pd.to_datetime(Dfamazon['date_added']) #Cambiar formato de fecha
Dfamazon['type'] = Dfamazon['type'].str.lower() #Cambiar a minúsculas las columnas con formato string
Dfamazon['title'] = Dfamazon['title'].str.lower()
Dfamazon['director'] = Dfamazon['director'].str.lower()
Dfamazon['cast'] = Dfamazon['cast'].str.lower()
Dfamazon['country'] = Dfamazon['country'].str.lower()
Dfamazon['rating'] = Dfamazon['rating'].str.lower()
Dfamazon['listed_in'] = Dfamazon['type'].str.lower()
Dfamazon['description'] = Dfamazon['description'].str.lower()
Dfamazon[['duration_int', 'duration_type']] = Dfamazon['duration'].str.split(expand = True) #Separar la columna duration en dos
Dfamazon['duration_type'] = Dfamazon['duration_type'].str.lower().replace('seasons','season') #Cambiar a minusculas la nueva columna str y poner en singular
Dfamazon['duration_int'] = Dfamazon['duration_int'].fillna(0) #Cambiar valores NaN por '0'(sino no se puede convertir a entero)
Dfamazon['duration_int'] = Dfamazon['duration_int'].astype(int) #Cambiar la otra nueva columna a entero

Dfamazon = Dfamazon.merge(score, left_on = 'id', right_on='movieId', how='left') #Insertamos la nueva columna score según el índice de la película
Dfamazon['score'].fillna(0) #Cambiamos los valores nulos que no se pudieron integrar a 0

# PLATAFORMA HULU #

Dfhulu = Extract.extract(pathhulu) #Leer el archivo csv
Dfhulu.insert(0, 'id', 'h' + Dfhulu['show_id'], allow_duplicates=False) #Insertar Columna 'id'
Dfhulu['rating'] = Dfhulu['rating'].fillna('G') #Reemplazar NaN por 'G' en columna 'rating'
Dfhulu['date_added'] = pd.to_datetime(Dfhulu['date_added']) #Cambiar formato de fecha
Dfhulu['type'] = Dfhulu['type'].str.lower() #Cambiar a minúsculas las columnas con formato string
Dfhulu['title'] = Dfhulu['title'].str.lower()
Dfhulu['director'] = Dfhulu['director'].str.lower()
Dfhulu['country'] = Dfhulu['country'].str.lower()
Dfhulu['rating'] = Dfhulu['rating'].str.lower()
Dfhulu['listed_in'] = Dfhulu['type'].str.lower()
Dfhulu['description'] = Dfhulu['description'].str.lower()
Dfhulu[['duration_int', 'duration_type']] = Dfhulu['duration'].str.split(expand = True) #Separar la columna duration en dos
Dfhulu['duration_type'] = Dfhulu['duration_type'].str.lower().replace('seasons','season') #Cambiar a minusculas la nueva columna str y poner en singular
Dfhulu['duration_int'] = Dfhulu['duration_int'].fillna(0) #Cambiar valores NaN por '0'(sino no se puede convertir a entero)
Dfhulu['duration_int'] = Dfhulu['duration_int'].astype(int) #Cambiar la otra nueva columna a entero

Dfhulu = Dfhulu.merge(score, left_on = 'id', right_on='movieId', how='left') #Insertamos la nueva columna score según el índice de la película
Dfhulu['score'].fillna(0) #Cambiamos los valores nulos que no se pudieron integrar a 0



# Carga de los dataframes transformados como csv en la carpeta /datasets # 

Dfdisney.to_csv('datasets/disney_clean.csv', index=False)
Dfnetflix.to_csv('datasets/netflix_clean.csv', index=False)
Dfamazon.to_csv('datasets/amazon_clean.csv', index=False)
Dfhulu.to_csv('datasets/hulu_clean.csv', index=False)

print('Se corrió transform.py')