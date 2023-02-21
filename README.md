# MLOps
Alumno: Costa, Justo Gastón.
Mail: justocosta99@gmail.com

Bienvenidos al primer proyecto individual de la parte de labs del bootcamp de Henry

- Empezamos con la Carpeta 'datasets':
  - En ella se encuentra un archivo formato texto 'url.text' contiene un link al drive donde están los archivos .csv. 
    Se deben descargar y ubicar en esta misma carpeta los archivos que contienen la información de las plataformas. 
    Los archivos de la carpeta del drive llamada rating (Ej: 1.csv, etc), estas se deben descargar y ubicar en una carpeta nueva llamada 'ratings' en la raiz de la Biblioteca.
    
- Carpeta 'etl':
  En esta Carpeta se hace el proceso etl de los datos.
  - 'extract.py' Archivo en el cual instancie una función destinada a leer csv de manera importable.
  - 'transform.py' Archivo dedicado a la transformación de las tablas y columnas según la consigna del proyecto.

- Carpeta 'machine_learning':
  En esta carpeta se guarda todo lo referido a la funcionalidad del sistema de recomendación
  - 'modelsvd.py' Archivo dedicado al entrenamiento del algoritmo de recomendación, instacia de parámetros.
  - svd_model.pkl Archivo formato pkl, en el cuál se encuentra el modelo de machine learning listo para exportar y utilizar en una función.

- Carpet 'api':
  En esta carpeta se encuentran todos los archivos necesarios para el funcionamiento de la Api.
  - 'querys.py' Archivo en el cual se plantean mediante funciones todas las consultas requeridas a las tablas anteriormente cargadas.
  - 'predict.py' Archivo en el cual se plantea mediante una función la predicción del sistema de recomendación usando las tablas ratings.
  - 'main.py' En este archivo se crea la api, se crean y enlazan los endpoints del sitio web y sus retornos. 
  - Carpeta 'templates':
    En esta carpeta se guardan archivos en formato .html lo cual le da la interfaz gráfica a las respuestas http. 

- El sitio web cuenta con una página principal llamada home, en donde se encuentran todas las preguntas para hacerle a la base de datos, al elegir una
se deben llenar los datos necesarios para realizar la consulta y ella misma te retorna la respuesta. 
También dentro se encuentra la recomendación de peliculas para un usuario. 

