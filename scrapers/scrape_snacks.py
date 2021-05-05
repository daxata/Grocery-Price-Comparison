from bs4 import BeautifulSoup
import requests
import mysql.connector


HOST = "localhost"
USERNAME = "root"
PASSWORD = "Ashthalin_7"
DATABASE = "product_details"

url_sastodeal = 'https://www.sastodeal.com/sd-fast/food-essentials/salty-snacks-namkeens.html'
url_thulo = 'https://thulo.com/snacks/'
plain_html_text_sastodeal = requests.get(url_sastodeal)
plain_html_text_thulo = requests.get(url_thulo)
soup_sastodeal = BeautifulSoup(plain_html_text_sastodeal.text, "html.parser")
soup_thulo = BeautifulSoup(plain_html_text_thulo.text, "html.parser")

data_list = []
# print(soup.prettify())
for main_block in soup_sastodeal.find_all(name="div", attrs={"class": "product-item-info"}):
    for product_block in main_block.find_all(name="span", attrs={"class": "product-image-wrapper"}):
        for images in product_block.find_all(name="img", attrs={"class": "product-image-photo"}):
            image = images.get('src')
            # print(image)

    for product_block in main_block.find_all(name="div", attrs={"class": "product-item-details"}):

        for title_block in product_block.find_all(name="strong", attrs={"class": "product-item-name"}):
            if title_block.text:
                name = title_block.text
                # print(name)

        for link in product_block.find_all(name="a", href=True, attrs={"class": "product-item-link"}):
            if link.get('href'):
                url = link.get('href')
                # print(url)

        for price_block in product_block.find_all(name="div", attrs={"class": "price-box price-final_price"}):
            offer_price = price_block.find(
                name="span", attrs={"class": "special-price pricenew"})
            normal_price = price_block.find(
                name="span", attrs={"class": "price"})

            price = None

            if offer_price is not None:
                price = offer_price.text
            else:
                price = normal_price.text

    data_list.append((name, price, url, image))


for main_block in soup_thulo.find_all(name="div", attrs={"class": "et-column4 et-grid-item-wrapper"}):
    for product_block in main_block.find_all(name="div", attrs={"class": "ty-grid-list__item ty-quick-view-button__wrapper et-grid-item"}):
        for image_block in product_block.find_all(name="div", attrs={"class": "ty-grid-list__image"}):
            for images in product_block.find_all(name="img", attrs={"class": "ty-pict      cm-image"}):
                image = images.get('src')
                # print(image)
            for image_wrapper in product_block.find_all(name="div", attrs={"class": "ty-center-block"}):
                for image_carousel in image_wrapper.find_all(name="div", attrs={"class": "ty-thumbs-wrapper cm-image-gallery"}):
                    for image_gallery in image_carousel.find_all(name="div", attrs={"class": "cm-gallery-item cm-item-gallery"}):
                        for images in image_gallery.find_all(name="img", attrs={"class": "ty-pict cm-image"}):
                            image = images.get('src')
                            # print(image)

    for product_block in main_block.find_all(name="div", attrs={"class": "et-grid-info-wrapper"}):

        for title_block in product_block.find_all(name="div", attrs={"class": "et-grid-product-name"}):
            for title in title_block.find_all(name="a", attrs={"class": "product-title"}):
                if title.text:
                    name = title.text
                    # print(name)

            for link in product_block.find_all(name="a", href=True, attrs={"class": "product-title"}):
                if link.get('href'):
                    url = link.get('href')
                    # print(url)

        for price_block in product_block.find_all(name="div", attrs={"class": "et-price"}):
            for price in price_block.find_all(name="span", attrs={"class": "ty-price"}):
                price = price.text
                # print(price)

    data_list.append((name, price, url, image))

# print(data_list)
db = mysql.connector.connect(
    host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE, auth_plugin='mysql_native_password')
cursor = db.cursor()
# cursor.execute("DROP TABLE IF EXISTS product")
# sql = '''create table product(id int not null primary key auto_increment, name varchar(100), price varchar(100), url varchar(300), image blob)'''
# cursor.execute(sql)

# sql = ("INSERT INTO snacks(name, price, url, image) VALUES (%s, %s, %s, %s)")
sql = ("INSERT INTO search(name, price, url, image) VALUES (%s, %s, %s, %s)")

cursor.executemany(sql, data_list)
db.commit()

db.close()
