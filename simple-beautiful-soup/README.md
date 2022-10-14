# Web Scraping with Python and BeautifulSoup

Una de las bibliotecas más populares utilizadas en web scraping es BeautifulSoup, la cual se utiliza para analizar documentos HTML y extraer datos, a través de secuencias de comandos de Python o con el uso de selectores de CSS.

## ¿Qué es Web Scraping?

Web scraping es el proceso de recopilación de datos de la web, mediante un programa que recupera datos de sitios web (generalmente páginas HTML) y luego los analiza en busca de datos específicos. Luego estos datos se pueden utilizar para estudios de mercado, análisis inmobiliario, inteligencia empresarial, etc.

## Beautifulsoup 

Utilizando Beautifulsoup podemos navegar datos HTML para extraer/eliminar/reemplazar elementos HTML particulares. También viene con funciones de utilidad como formato visual y limpieza del árbol de análisis.

## Elegir un back-end

Bs4 proporciona algoritmos de análisis de HTML:

- html.parser: es un parser escrito en python. Es lento.
- lxml: biblioteca basada en C para el análisis de HTML: muy rápida, pero puede ser un poco más difícil de instalar.
- html5lib: otro analizador escrito en python que está diseñado para ser totalmente compatible con html5.

Nota: lxml es mucho más rápido, sin embargo, html.parser sigue siendo una buena opción para proyectos más pequeños. En cuanto a html5lib, es principalmente mejor para casos extremos donde es necesario el cumplimiento de la especificación html5.

## Extras de Beautifulsoup

Además de ser un excelente analizador de HTML, Beautifulsoup también incluye una gran cantidad de funciones de ayuda y utilidades relacionadas con HTML. 

### Extraer todo el texto

A menudo, las estructuras de texto complejas se representan a través de múltiples nodos HTML que pueden ser difíciles de extraer. Para esto, bs4 implementa un método llamado get_text().

### Formato "bonito" HTML

Frecuentemente, cuando hacemos web scraping, queremos almacenar o mostrar contenido HTML en algún lugar para integrarlo con otras herramientas o depurarlo. El método .prettify() reestructura la salida HTML para que sea más legible para los humanos.

### Análisis selectivo

Algunos web scrapers no necesitan el documento HTML completo para extraer datos valiosos. Por ejemplo, cuando se rastrea la web, solo queremos analizar los nodos <a> para los enlaces. Por esta razón, BeautifulSoup ofrece el objeto SoupStrainer que permite restringir nuestro análisis solo a elementos HTML específicos.

### Modificar HTML

Dado que bs4 carga todo el árbol HTML como un objeto de Python, podemos modificar, eliminar o reemplazar fácilmente cada nodo adjunto:

Nota: Beautifulsoup no es solo una biblioteca de análisis HTML, sino una suite HTML completa.

## Alternativas de BeautifulSoup

Una alternativa es parsel (basado en lxml) que usa scrapy, otra es html5lib, que puede ser utilizada por beautifulsoup4 como backend. Otros lenguajes tienen bibliotecas similares como nokogiri en Ruby, DomCrawler en PHP, rvest en R, etc.


## ¿Es BeautifulSoup una biblioteca de web scraping?

No exactamente, Beautifulsoup es una biblioteca de análisis de HTML. Si bien se usa para el web scraping, no es un suite/framework completo de web scraping como scrapy. El analizador HTML de Beautifulsoup debe combinarse con la biblioteca de cliente HTTP "requests" (u otras alternativas como httpx, selenio) para recuperar páginas HTML.