from bs4 import BeautifulSoup
import requests
print(1)

r=requests.get("http://en.wkipedia.org/wiki/Eagle")
print(r.content)