# 1 -  IMPORTAR LIBRERIAS ----------------------------------------------------------

# Libreria "Beautriful Suop", para realizar el scrapping:
from bs4 import BeautifulSoup
# Libreria "Requests", muestra el contenido de la respuesta de la pagina.
import requests
# parser: sirve para extraer la informacion del archivo html. Trabaja con Beautiful Soup
import lxml

# 2 Proceso ----------------------------------------------------------
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
print(soup.prettify())