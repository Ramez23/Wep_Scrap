import requests
from bs4 import BeautifulSoup

product_name = []
product_price = []
links = []

result = requests.get("https://www.lcwaikiki.eg/en-US/EG/product-group/men")

src = result.content

soup = BeautifulSoup (src,"html.parser")

link = soup.find_all("a",{'class':"lazy-load-button"},"href")

for i in range(1,10):
        result = requests.get(f"https://www.lcwaikiki.eg/en-US/EG/product-group/men?PageIndex={i}")
        src = result.content
        soup = BeautifulSoup(src, "html.parser")
        product_names = soup.find_all("h3")
        for i in range(len(product_names)):
                product_name.append(product_names[i].text)
        product_prices = soup.find_all("div", {'class': "raw-price"})
        for i in range(len(product_prices)):
                product_price.append(product_prices[i].text)


for i1 in range(len(product_name)):
        print(f'''Product Num:{i1+1}
                  Product_Name:{product_name[i1]}
                  Product_Price:{product_price[i1]}
''')




