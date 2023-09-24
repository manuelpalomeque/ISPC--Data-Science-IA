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
website = 'https://subslikescript.com/movie/Titanic-120338'

# enviar una solicitud a la pagina y almacenarla en una variable
result = requests.get(website)
