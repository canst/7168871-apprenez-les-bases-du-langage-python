# Écrivez votre code ici !
from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

title = soup.title.string
print("Titre de la page:", title)

h1_text = soup.find("h1").string
print("Texte de la balise h1:", h1_text)

all_products = dict()

products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string
    price_list = price_str.split(" ")
    all_products[name] = {"prix": price_list[1]}
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description

print("Produits:", all_products)

for name in all_products.keys():
    price_str = all_products[name]["prix"]
    price = price_str.strip("€")
    price = float(price)
    dollar_price = price * 1.2
    all_products[name]["prix_dollar"] = f"{dollar_price}$"

print("Tous les produits:", all_products)
