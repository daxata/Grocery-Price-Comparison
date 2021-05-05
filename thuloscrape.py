from bs4 import BeautifulSoup
import requests

url_to_scrape = 'https://thulo.com/rice-and-rice-products/'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
data_list = []
# print(soup.prettify())

for main_block in soup.find_all(name="div", attrs={"class": "et-column4 et-grid-item-wrapper"}):

    for product_block in main_block.find_all(name="div", attrs={"class": "ty-grid-list__image"}):
        for images in product_block.find_all(name="img", attrs={"class": "cm-image"}):
            image = images.get('src')
            print(image)
        for image_wrapper in product_block.find_all(name="div", attrs={"class": "ty-center-block"}):
            for image_carousel in image_wrapper.find_all(name="div", attrs={"class": "ty-thumbs-wrapper owl-carousel cm-image-gallery"}):
                for image_gallery in image_carousel.find_all(name="div", attrs={"class": "1 cm-gallery-item cm-item-gallery"}):
                    for images in image_gallery.find_all(name="img", attrs={"class": "cm-image"}):
                        image = images.get('src')
                        print(image)

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
