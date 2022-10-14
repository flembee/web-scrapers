from bs4 import BeautifulSoup

html = """
<div><h1>The Avangers: </h1><a>End Game</a><p>is one of the most popular Marvel movies</p></div>
"""
soup = BeautifulSoup(html, features="lxml")
print(soup.prettify())
"""
<html>
 <body>
  <div>
   <h1>
    The Avangers:
   </h1>
   <a>
    End Game
   </a>
   <p>
    is one of the most popular Marvel movies
   </p>
  </div>
 </body>
</html>
"""