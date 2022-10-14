from bs4 import BeautifulSoup
import re

html = """
<head>
  <title class="page-title">Hello World!</title>
</head>
<body>
  <div id="content">
    <h1>Title</h1>
    <p>first paragraph</p>
    <p>second paragraph</p>
    <h2>Subtitle</h2>
    <p>first paragraph of subtitle</p>
  </div>
</body>
"""
soup = BeautifulSoup(html, 'lxml')

print(soup.find('title').text)
"Hello World"

# we can also perform searching by attribute values
print(soup.find(class_='page-title').text)
"Hello World"

# We can even combine these two approaches:
print(soup.find('div', id='content').h2.text)
"Subtitle"

# Finally, we can perform partial attribute matches using regular expressions
# let's select paragraphs that contain the word "first" in it's text:
print(soup.find_all('p', text=re.compile('first')))
["<p>first paragraph</p>", "<p>first paragraph of subtitle</p>"]