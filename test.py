from bs4 import BeautifulSoup as BS
import requests 

file = open("index.html", "r", encoding="utf-8")

html = file.read()

soup = BS(html, "html.parser")

# main = soup.find("div", class_= "footer-box")
# print (main.text.strip())

