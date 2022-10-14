from bs4 import BeautifulSoup

# this is our HTML page:
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

# 1. build soup object from html text
soup = BeautifulSoup(html, 'lxml')

# then we can navigate the html tree via python API:
# for example title is under `head` node:
print(soup.head.title)
'<title class="page-title">Hello World!</title>'

# this gives us a whole HTML node but we can also just select the text:
print(soup.head.title.text)
"Hello World!"

# or it's other attributes:
print(soup.head.title["class"])
"page-title"