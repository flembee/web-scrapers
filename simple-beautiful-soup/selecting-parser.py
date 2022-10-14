from bs4 import BeautifulSoup, SoupStrainer

html = """
<head><title>hello world</title></head>
<body>
  <div>
      <a>Link 1</a>
      <a>Link 2</a>
      <div>
        <a>Link 3</a>
      /div>
  </div>
</body>
"""
link_strainer = SoupStrainer('a')
soup = BeautifulSoup(html, features="lxml", parse_only=link_strainer)
print(soup)
#<a>Link 1</a><a>Link 2</a><a>Link 3</a>