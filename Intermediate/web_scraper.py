import requests
from bs4 import BeautifulSoup

url = "https://shadowfox.in"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Website Title:")
print(soup.title.text)

print("\nParagraphs:")

paragraphs = soup.find_all("p")

for p in paragraphs:
    print(p.text)