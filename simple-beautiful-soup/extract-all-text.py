from bs4 import BeautifulSoup

html = """
<div>
  <a>The Avangers: </a>
  <a>End Game</a>
  <p>is one of the most popular Marvel movies</p>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
# join all text values with space, and strip leading/trailing whitespace:
print(soup.div.get_text(' ', strip=True))  
'The Avangers: End Game is one of the most popular Marvel movies'