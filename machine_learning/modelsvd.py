import os
import pandas as pd
import joblib
from surprise import Dataset
from surprise import Reader
from surprise import SVD

# Cargar los datos desde un archivo CSV y concatenarlos verticalmente
dataset = pd.concat([pd.read_csv('ratings/1.csv'), pd.read_csv('ratings/2.csv')]) # pd.read_csv('ratings/3.csv'), pd.read_csv('ratings/4.csv'), pd.read_csv('ratings/5.csv'), pd.read_csv('ratings/6.csv'), pd.read_csv('ratings/7.csv'), pd.read_csv('ratings/8.csv')])

# Crear un Reader para definir el rango de puntuaciones
reader = Reader(rating_scale=(1, 5))

# Instanciar el conjunto de datos y especificar las columnas correspondientes
ratings = Dataset.load_from_df(dataset[['userId', 'movieId', 'rating']], reader)

# Verificar si se ha entrenado y guardado un modelo previamente
if os.path.exists('machine_learning/svd_model.pkl'):
    loaded_svd = joblib.load('machine_learning/svd_model.pkl')
    print('Se cargó el modelo previamente entrenado.')
else:
    # Definir los conjuntos de entrenamiento y prueba
    trainset = ratings.build_full_trainset()
    
    # Configurar el modelo SVD
    svd = SVD(n_factors=100, n_epochs=20, biased=True, lr_all=0.005, reg_all=0.02)
    
    # Entrenar el modelo
    svd.fit(trainset)
    
    # Guardar el modelo entrenado
    joblib.dump(svd, 'machine_learning/svd_model.pkl')
    loaded_svd = svd

# Hacer una prueba de predición aleatoria para un usuario y una película 
userId = 42
movieId = 'as567'
pred = loaded_svd.predict(userId, movieId, verbose=True)
print(pred)


