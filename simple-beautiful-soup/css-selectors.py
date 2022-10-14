from bs4 import BeautifulSoup

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

print(soup.select_one('title').text)
"Hello World"

# we can also perform searching by attribute values such as class names
print(soup.select_one('.page-title').text)
"Hello World"

# We can also find _all_ amtching values:
for paragraph in soup.select('#content p'):
    print(paragraph.text)
"first paragraph"
"second paragraph"
"first paragraph of subtitile"

# We can also combine CSS selectors with find functions:
import re
# select node with id=content and then find all paragraphs with text "first" that are under it:
print(soup.select_one('#content').find_all('p', text=re.compile('first')))
["<p>first paragraph</p>", "<p>first paragraph of subtitle</p>"]