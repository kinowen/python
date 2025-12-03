from bs4 import BeautifulSoup

page = open("Chap08_Selector.html", "rt", encoding="utf-8").read()

soup = BeautifulSoup(page, 'html.parser')

#print(soup.prettify())

#print(soup.find('p'))

#print(soup.find_all('p', class_='inner-text'))

for item in soup.find_all('p'):
    print(item.text.strip())