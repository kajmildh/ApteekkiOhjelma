from bs4 import BeautifulSoup
import requests as requests


def tuurinapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='page-title').find('span').get_text()
            product_price = soup.find('span', class_='price-container price-final_price tax').find('meta', itemprop='price')
            product_currency = soup.find('span', class_='price-container price-final_price tax').find('meta', itemprop='priceCurrency')
            medication.append([product_name, product_price['content'], product_currency['content'], url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def yliopistonapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='page-title').get_text(strip=True)
            product_price = soup.find('div', class_='product-info-price').find('div', class_='price-box price-final_price').find('span', class_='price').get_text(strip=True)
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def vitusapotek(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='name').get_text()
            product_price = soup.find('div', class_='price-value-new').get_text()
            product_currency = 'NOK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def bootsapotek(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('span', {'data-ui-id': 'page-title-wrapper'}).get_text()
            product_price = soup.find('span', class_='price').get_text()
            product_currency = 'NOK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def lyfogheilsa(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('p', class_='parag parag--big').get_text()
            product_price = soup.find('p', class_='price-tag').get_text()
            product_currency = 'ISK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def apoteketsvalen(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('header', class_='col-md-10 page-header').get_text(strip=True)
            product_price = soup.find('p', class_='price').get_text(strip=True)
            product_currency = 'DKK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def apotekhjem(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', itemprop='name').get_text(strip=True)
            product_price = soup.find('span', itemprop='price').get_text(strip=True)
            product_currency = 'NOK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def apoteraapotek(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('span', itemprop='name').get_text()
            product_price = soup.find('span', {'data-price-type': 'finalPrice'}).get_text()
            product_currency = 'NOK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def balderapotek(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='product_title entry-title').get_text()
            product_price = soup.find('p', class_='price').get_text()
            product_currency = 'NOK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def dameapoteket(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='product_title entry-title elementor-heading-title elementor-size-default').get_text()
            product_price = soup.find('p', class_='price').find('bdi').get_text()
            product_currency = 'NOK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def farmasiet(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1',class_='Product__Heading').get_text(strip=True)
            product_price = soup.find('span', class_='Product__PriceDefault').get_text()
            product_currency = 'NOK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication



def dittapotekopera(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='product__title').get_text()
            product_price = soup.find('span', class_='product-price--original').get_text()
            product_currency = 'NOK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def farmakeutAB(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h2', class_='elementor-heading-title').get_text()
            product_price = soup.find('span', class_='woocommerce-Price-amount amount').get_text()
            product_currency = 'SEK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def medsapotekAB(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('div', class_='product-actions').find('h1', class_='h2').get_text(strip=True)
            product_price = soup.find('div', class_='price').get_text(strip=True)
            product_currency = 'SEK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def oloapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='page-title').get_text(strip=True)
            product_price = soup.find('div', class_='price-box price-final_price').find('span', class_='price').get_text(strip=True)
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def pakilanapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', itemprop='name').get_text(strip=True)
            product_price = soup.find('span', itemprop='price').get_text(strip=True)
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def ympyrätalonapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='h2 product-single__title').get_text(strip=True)
            product_price = soup.find('span', class_='product__price').get_text(strip=True)
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def ivalonapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='h2 product-name').get_text()
            product_price = soup.find('div', class_='price').find('span', class_='taxful').get_text()
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def seitsemänveljeksenapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('div', class_='product__title').get_text(strip=True)
            product_price = soup.find('span', class_='price-item price-item--regular').get_text(strip=True)
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def myllynapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='product_title entry-title').get_text()
            product_price = soup.find('div', class_='single-product-price').find('span', class_='woocommerce-Price-amount amount').get_text()
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def wiklundinapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='product-title cell small-order-2 large-order-1').get_text(strip=True)
            product_price = soup.find('div', class_='h4 price').get_text(strip=True)
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def koivukylänapteekki(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('span', itemprop='name').get_text()
            product_price = soup.find('span', class_='price').get_text()
            product_currency = 'EUR'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def apopro(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', itemprop='name').get_text()
            product_name_sub = soup.find('div', class_='mb5').get_text()
            product_price = soup.find('span', itemprop='price').get_text()
            product_currency = 'DKK'
            medication.append([product_name + ", " + product_name_sub, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


def gazelle(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='product-content-title').get_text(strip=True)
            product_price = soup.find('span', class_='price').get_text(strip=True)
            product_currency = 'DKK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication



def ugleapotek(urls):
    medication = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            product_name = soup.find('h1', class_='product_title entry-title elementor-heading-title elementor-size-default').get_text()
            product_price = soup.find('p', class_='price').get_text()
            product_currency = 'DKK'
            medication.append([product_name, product_price, product_currency, url])
        except Exception as e:
            print(f"An error occurred for URL {url}: {e}")

    return medication


