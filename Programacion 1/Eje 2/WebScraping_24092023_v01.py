# 1 -  IMPORTAR LIBRERIAS ----------------------------------------------------------

# Libreria "Beautriful Suop", para realizar el scrapping:
from bs4 import BeautifulSoup
# Libreria "Requests", muestra el contenido de la respuesta de la pagina.
import requests
# parser: sirve para extraer la informacion del archivo html. Trabaja con Beautiful Soup
import lxml

# 2 Extraer el codigo HTML de una pagina ----------------------------------------------------------
# Extraere el titulo y el contenido

# Definir en la variable "website", la web en la que voy a trabajar
paginaWeb = 'https://subslikescript.com/movie/Titanic-120338'

# enviar una solicitud a la pagina y almacenarla en una variable
resultado = requests.get(paginaWeb)

# Obtendre el textro del resultado y lo guardo en una variable. El ".text" es como se obtiene
contenido = resultado.text

# Variable "soup", que permitira encontrar elementos en una pagina web. El parser obtiene el codigo html de la
# respuesta que obtuvimos
soup = BeautifulSoup(contenido,'lxml')

# Nos muestra el codigo html pero dificil de leer:
# print(soup)
# se recomienda usar .prettify para mejorar la visualizacion:
# print(soup.prettify())

# 3 Obtener los datos que queremos --------------------------------------------------

# extraer el titulo
box= soup.find('article', class_='main-article')
nombrePelicula = box.find('h1').get_text()
print('El nombre de la pelicula es: {}'.format(nombrePelicula))

# extraer el guion:
nombreGuion = box.find('div', class_='full-script').get_text()
#print('El guion es: {}'.format(nombreGuion))

# devuelve el guion perno no esta bien visualmente, por lo cual agrego funciones:
# strip: borra espacios vacios al inicio y al final
#separator:  reemplaza saltos de linea con un espacio en blanco
nombreGuion1 = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
print('El guion es: {}'.format(nombreGuion1))

#4  Exportar lo extraido en un archivo de texto ---------------------------------------

