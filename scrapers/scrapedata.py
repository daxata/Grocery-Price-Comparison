from bs4 import BeautifulSoup
import requests
import mysql.connector


HOST = "localhost"
USERNAME = "root"
PASSWORD = "Ashthalin_7"
DATABASE = "product_details"

url_to_scrape = 'https://www.daraz.com.np/rice/?spm=a2a0e.11779170.cate_6_4.3.71f82d2bXunmbX'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
data_list = []
# print(soup.prettify())
for main_block in soup.find_all(name="div", attrs={"class": "product-card product-card--onsale"}):
    for product_block in main_block.find_all(name="div", attrs={"class": "product-card__image-holder"}):
        for images in product_block.find_all(name="img", attrs={"itemprop": "contentUrl"}):
            image = images.get('src')
            print(image)

    # for title_block in product_block.find_all(name="div", attrs={"class": "c3KeDq"}):
    #     for title_block in product_block.find_all(name="div", attrs={"class": "c16H9d"}):
    #         if title_block.get('title'):
    #             name = title_block.get('title')
    #             #print(name)

# for link in product_block.find_all(name="a", href=True, attrs={"class": "product-item-link"}):
#     if link.get('href'):
#         url = link.get('href')
#         # print(url)

# for price_block in product_block.find_all(name="div", attrs={"class": "price-box price-final_price"}):
#     offer_price = price_block.find(
#         name="span", attrs={"class": "special-price pricenew"})
#     normal_price = price_block.find(
#         name="span", attrs={"class": "price"})

#     price = None

#     if offer_price is not None:
#         price = offer_price.text
#     else:
#         price = normal_price.text

    # data_list.append((name, price, url, image))

# # print(data_list)
# db = mysql.connector.connect(
#     host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE, auth_plugin='mysql_native_password')
# cursor = db.cursor()
# # cursor.execute("DROP TABLE IF EXISTS product")
# # sql = '''create table product(id int not null primary key auto_increment, name varchar(100), price varchar(100), url varchar(300), image blob)'''
# # cursor.execute(sql)

# sql = ("INSERT INTO product(name, price, url, image) VALUES (%s, %s, %s, %s)")

# cursor.executemany(sql, data_list)
# db.commit()

# db.close()
