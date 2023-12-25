
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce.settings')


import django
django.setup()


import requests
from bs4 import BeautifulSoup



productList = []
currentPage = 1
maxPage = 5

while currentPage <= maxPage:
    url = f"https://www.jumia.com.ng/mlp-official-stores/?page={currentPage}#catalog-listing"
    res = requests.get(url)

    if res.status_code == 200:
        HTML_content = res.text
        pot = BeautifulSoup(HTML_content, "lxml")
        articles = pot.css.select(".prd")

        for article in articles:
            productList.append({'id': len(productList) + 1,
                                'name': article.css.select(".prd > a")[0]['data-name'],
                                'image': article.css.select(".img")[0]['data-src'],
                                'brand': article.css.select(".prd > a")[0]['data-brand'],
                                'category': article.css.select(".prd > a")[0]['data-category'],
                                'price': article.css.select(".prd > a")[0]['data-price'],
                                'rating': {'rate': article.css.select(".prd > a")[0]['data-dimension27'],
                                           'count': article.css.select(".prd > a")[0]['data-dimension26']}
                                })

        currentPage += 1
    else:
        print(f"Failed to get requests {currentPage}!!!")


from Product.models import Product

def populate():
    # product = Product()

    for prod in productList:
        prd = Product.objects.get_or_create(
            productNo=prod['id'], name=prod['name'], image=prod['image'],
            brand=prod['brand'], price=prod['price'])[0]
        prd.save()


if __name__ == '__main__':
    print('populating')
    populate()
    print("completed")
else:
    print("failed to run script")
