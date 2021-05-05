from bs4 import BeautifulSoup
import requests

url_to_scrape = 'https://www.himalmart.com/category/rice-and-rice-products'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
data_list = []
# print(soup.prettify())

for main_block in soup.find_all(name="div", attrs={"class": "col-6 col-sm-6 col-md-6 col-lg-3 pro-wrap"}):

    for product_block in main_block.find_all(name="div", attrs={"class": "product-box"}):
        for images in product_block.find_all(name="img"):
            image = images.get('src')
            # print(image)

    for product_block in main_block.find_all(name="div", attrs={"class": "product-inner"}):
        for title in product_block.find_all(name="div", attrs={"class": "product_name"}):
            if title.text:
                name = title.text
                # print(name)

        # for link in product_block.find_all(name="a", href=True, attrs={"class": "product_name"}):[0].find("span").text
        #     if link.get('href'):
        #         url = link.get('href')
        #         print(url)

        for price_block in product_block.find_all(name="p", attrs={"class": "p-price-tag"}):
            for price in price_block.find_all(name="span", attrs={"class": "og-price"}):
                price = price.text
                print(price)
