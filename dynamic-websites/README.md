# Scraping Dynamic Websites Using Web Browsers

Muchos sitios web dependen, en gran medida, de Javascript utilizando frameworks como React y Vue para generar datos interactivos. En consecuencia, la Web cada vez es más compleja y dinámica. Provocando que el web scraping tradicional no se ejecute en un navegador completo y no sea capaz de interpretar código Javascript complejo para representar páginas dinámicas.

Hay algunas formas de lidiar con el contenido dinámico generado por JavaScript al hacer Web Scraping:

Por un lado, se podría aplicar ingeniería inversa al comportamiento del sitio web y replicarlo en el programa de web scraping que desarrollemos. Sin embargo, este enfoque ha perdido validéz a medida que crece la complejidad de la web, siendo muy lento, difícil y puede llevar mucho tiempo cuando se extraen múltiples fuentes.

Alternativamente, podemos automatizar un navegador real para extraer páginas web dinámicas e integrándolo a un programa de extracción de datos web. 

## ¿Cuáles son las herramientas disponibles existentes y cómo usarlas?

### Selenium

Selenium es una de las principales herramientas creada para automatizar las pruebas de sitios web. Admite ambos protocolos de control del navegador: webdriver y CDP (a partir de Selenium v4+).

Por ser una de las herramientas más antigua, tiene una gran comunidad y muchas funciones, además de ser compatible con casi todos los lenguajes de programación y ejecutable en casi todos los navegadores web:

Lenguajes: Java, Python, C#, Ruby, JavaScript, Perl, PHP, R, Objective-C y Haskell
Navegadores: Chrome, Firefox, Safari, Edge, Internet Explorer (y sus derivados)
Pros: gran comunidad que ha existido por un tiempo, lo que significa muchos recursos gratuitos. API síncrona fácil de entender para tareas de automatización comunes.

### Puppeteer

Puppeteer es una biblioteca de automatización de navegador web asíncrono para Javascript de Google (así como Python a través del paquete no oficial Pyppeteer).

Lenguajes: Javascript, Python (no oficial)
Navegadores: Chrome, Firefox (Experimental)
Pros: primera implementación sólida de CDP, mantenida por Google, con la intención de ser una herramienta general de automatización para navegadores.

En comparación con Selenium, el Puppeteer admite menos lenguajes, pero implementa completamente el protocolo CDP y cuenta con un sólido equipo de Google detrás. Además, al ser un cliente de automatización de navegador de uso general, los problemas de web scraping reciben soporte oficial.

### Playwright

Playwright es otra biblioteca de automatización para navegadores web síncrona y asíncrona disponible en varios idiomas por Microsoft.
El objetivo principal de Playwright es la prueba confiable de aplicaciones web modernas de extremo a extremo. Además, implementa todas las funciones de automatización de navegador de uso general (como Puppeteer y Selenium) y tiene una comunidad de web scraping en crecimiento.

Lenguajes: Javascript, .Net, Java y Python
Navegadores: Chrome, Firefox, Safari, Edge, Opera
Pros: posee muchas funciones, multilenguaje, multinavegador y proporciona implementaciones de cliente tanto asíncronas como síncronas. Mantenido por Microsoft.

### ScrapFly's API

Si bien es cierto que la automatización del navegador web puede ser un proceso difícil y lento. La API de ScrapFly implementa funciones básicas de automatización del navegador web como procesamiento de páginas, administración de sesiones/proxy, evaluación personalizada de javascript y reglas de carga de páginas. Todo lo anterior permite web scraping altamente escalables y fáciles de administrar.

En este ejemplo de web-scraping se recopilaron datos de experiencia en línea de https://www.airbnb.com/experiences.