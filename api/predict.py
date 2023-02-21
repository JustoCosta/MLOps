import joblib

# Cargar el modelo anteriormente entrenado en la carpeta 'machine_learning'
loaded_svd = joblib.load('machine_learning/svd_model.pkl')

# Crear la clase Predict cargando directamente el archivo .pkl
class Predict():
    def __init__(self, user, movie):
        self.user = user
        self.movie = movie

    def predict(self):
        prediction = loaded_svd.predict(self.user, self.movie)
        if prediction.est > 3.5:
            return 'La pelicula es recomendada para este usuario'
        else:
            return 'La pelicula no es recomendada para este usuario'

# Prueba de la funcion
p = Predict(42, 'as567')
est_rating = p.predict()
print(est_rating)