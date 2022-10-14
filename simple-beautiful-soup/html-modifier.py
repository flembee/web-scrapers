from bs4 import BeautifulSoup
html = """
<div>
  <button class="flat-button red">Subscribe</button>
</div>
"""
soup = BeautifulSoup(html)
soup.div.button['class'] = "shiny-button blue"
soup.div.button.string = "Unsubscribe"
print(soup.prettify())
# <html>
#  <body>
#   <div>
#    <button class="shiny-button blue">
#     Unsubscribe
#    </button>
#   </div>
#  </body>
# </html>