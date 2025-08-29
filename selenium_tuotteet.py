from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from selenium_stealth import stealth

# Variables
SLEEP_AFTER_URL = 15  # amount of sleep/waiting (s) after loading url and before scraping name and price
SLEEP_AFTER_DECLINEBUTTON = 7  # amount of sleep/waiting (s) after clicking all declinebuttons and before refreshing the page


def yliopistonapteekki_selenium(urls, data_value, product_number):
    medication = []
    # Initialize the Firefox WebDriver with options
    options = Options()
    options.add_argument('--headless')  # Run Firefox in headless mode (without GUI)
    driver = webdriver.Firefox(options=options)  # Ensure geckodriver is in your PATH

    try:
        try:
            # Wait until the "Decline" button is clickable
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline")))

            # Click the "Decline" button
            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                medication.append(['', '', '', url])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication

        # Open the website
        for i in range(len(urls)):
            try:
                driver.get(urls[i])
                time.sleep(SLEEP_AFTER_URL)

                # Wait until the dropdown menu is present in the DOM and scroll it into view
                dropdown_div = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".dropdown.configurable__combined-attribute-dropdown")))
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", dropdown_div)

                # Wait until the dropdown menu is clickable
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".dropdown.configurable__combined-attribute-dropdown")))

                dropdown_div.click()

                # Wait until the dropdown options are visible
                option_to_select = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f"option[value='{data_value[i]}']")))

                # Click the desired option
                option_to_select.click()

                # Wait for the price to update
                time.sleep(2)

                # Get the updated page source after interacting with the dropdown
                updated_page_source = driver.page_source

                soup = BeautifulSoup(updated_page_source, 'html.parser')

                product_name = soup.find('h1', class_='page-title').get_text(strip=True)
                product_price = soup.find('span', id=f'product-price-{product_number[i]}').find('span', class_='price').get_text(strip=True)
                product_currency = 'EUR'
                medication.append([product_name, product_price, product_currency, urls[i]])
            except Exception as e:
                medication.append(['', '', '', urls[i]])
                print(f"An error occurred for URL {urls[i]}: {e}")

    finally:
        # Close the WebDriver
        driver.quit()

    return medication


def hjartat_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for i in range(len(urls)):
            try:
                driver.get(urls[i])

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//main[@id='maincontent']/section/div/div/h1").text
                product_price = driver.find_element(By.XPATH, "//main[@id='maincontent']//span[contains(text(), 'Butikspris:')]").text
                product_currency = 'SEK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, urls[i]])
                else:
                    medication.append([product_name, product_price, product_currency, urls[i], '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', urls[i]])
                else:
                    medication.append(['', '', '', urls[i], '', ''])
                print(f"An error occurred for URL {urls[i]}: {e}")

    finally:
        driver.quit()

    return medication


def herreapotek_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//div[@class='payment-methods__wrapper']/parent::div/preceding-sibling::div/preceding-sibling::div/h1").text
                product_price = driver.find_element(By.XPATH, "//div[@class='payment-methods__wrapper']/parent::div/preceding-sibling::div/div/div/span").text
                product_currency = 'NOK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication



def apoteket_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication

        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                name_element = driver.find_element(By.CSS_SELECTOR, '[data-cy="product-name"]')
                product_name = name_element.text if name_element else 'Name not found'

                price_element = driver.find_element(By.XPATH, '//*[contains(@class, "inStorePrice")]')
                product_price = price_element.text if price_element else 'Price not found'
                product_currency = 'SEK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def kronansapotek_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                name_element = driver.find_element(By.XPATH, "//h1[@class='headline-xl mb-2']")
                name_element_sub = driver.find_element(By.XPATH, "//h1[@class='headline-xl mb-2']/following-sibling::h2")
                product_name = name_element.text if name_element else 'Name not found'
                product_name_sub = name_element_sub.text if name_element_sub else 'Description of name not found'

                price_element = driver.find_element(By.XPATH, "//span[@data-testid='in-store-price']/span")
                product_price = price_element.text if price_element else 'Price not found'
                product_currency = 'SEK'
                if USE_CASE == 1:
                    medication.append([product_name + ', ' + product_name_sub, product_price, product_currency, url])
                else:
                    medication.append([product_name + ', ' + product_name_sub, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def apotek1_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('h1', class_='product__name').get_text()
                product_price = soup.find('p', class_='product-price__current').get_text()
                product_currency = 'NOK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication

def lyfjaval_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)
                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('h1', class_='mb-4').get_text()

                price_element = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "items-start")]//div[@class="display-price"]')))
                product_price = price_element.text if price_element else 'Price not found'
                product_currency = 'ISK'
                medication.append([product_name, product_price, product_currency, url])
            except Exception as e:
                medication.append(['', '', '', url])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def lyfjaver_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('h1', class_='text-5xl').get_text()
                product_desc_element = soup.find('div', class_='flex flex-row gap-4 text-normal pb-4')
                product_desc = product_desc_element.get_text() if product_desc_element else ""
                product_price = driver.find_element(By.CSS_SELECTOR, ".kc-product-price.\\!items-start .display-price").get_attribute('textContent')
                product_currency = 'ISK'
                medication.append([product_name + ' ' + product_desc, product_price, product_currency, url])
            except Exception as e:
                medication.append(['', '', '', url])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication

def apoteketonline_selenium(urls, location):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 25)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "declineButton")))
            decline_button.click()

            time.sleep(5)

            location_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "locationInput")))
            location_input.clear()

            location_input.send_keys(location)
            time.sleep(7)
            location_input.send_keys(Keys.RETURN)

            time.sleep(3)
            choose_loc_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="resultlist"]/div[1]/button[@id="choosePharmacy"]')))
            choose_loc_button.click()

            time.sleep(5)
            driver.get(urls[0])

            time.sleep(SLEEP_AFTER_URL)
        except Exception as e:
            for url in urls:
                medication.append(['', '', '', url])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.CLASS_NAME, "item-name").text
                product_desc = driver.find_element(By.CLASS_NAME, 'strength').text
                product_price_before_decimal = driver.find_element(By.XPATH, '//*[@id="price-block-outer"]/div[1]/p[1]/span[1]').text
                product_price_after_decimal = driver.find_element(By.XPATH, '//*[@id="price-block-outer"]/div[1]/p[1]/span[2]').text
                product_currency = 'DKK'
                medication.append([product_name + ' ' + product_desc, product_price_before_decimal + ',' + product_price_after_decimal, product_currency, url])
            except Exception as e:
                medication.append(['', '', '', url])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication

def dinapoteker_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('h1', itemprop='name').get_text(strip=True)
                product_price = soup.find('span', itemprop='price').get_text(strip=True)
                product_currency = 'DKK'
                medication.append([product_name, product_price, product_currency, url])
            except Exception as e:
                medication.append(['', '', '', url])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def apomed_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "declineButton")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('h1', class_='productFullDetail-productName-6ZL').get_text()
                product_price = soup.find('span', class_='price-root-vWW').get_text()
                product_currency = 'NOK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication

def apotekdirekte_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('h1', class_='product-title-v1').get_text(strip=True)
                product_price = soup.find('span', class_='product-price products_price').get_text(strip=True)
                product_currency = 'NOK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def apotekhjem_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "declineButton")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                medication.append(['', '', '', url])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('h1', itemprop='name').get_text()
                product_price = soup.find('span', itemprop='price').get_text()
                product_currency = 'NOK'
                medication.append([product_name, product_price, product_currency, url])
            except Exception as e:
                medication.append(['', '', '', url])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication

def appoteket_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('span', {'data-ui-id': 'page-title-wrapper'}).get_text()
                price_element = driver.find_element(By.XPATH, """//div[@class='final-price inline-block']//*[contains(@id, "product-price-")]""")
                product_price = price_element.text if price_element else 'Price not found'
                product_currency = 'NOK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication

def foodora_selenium(urls, ids):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for i in range(len(urls)):
            try:
                driver.get(urls[i])

                time.sleep(30)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('div', {'data-id': f'product-{ids[i]}'}).find('p', class_='product-card-name').get_text()
                product_price = soup.find('div', {'data-id': f'product-{ids[i]}'}).find('span', {'data-testid': 'product-card-price'}).get_text()
                product_currency = 'NOK'
                medication.append([product_name, product_price, product_currency, urls[i]])
            except Exception as e:
                medication.append(['', '', '', urls[i]])
                print(f"An error occurred for URL {urls[i]}: {e}")

    finally:
        driver.quit()

    return medication


def med24apotek_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "declineButton")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('section', class_='productInfo').find('h1', class_='hidden-xs-down').get_text()
                product_price = soup.find('div', class_='currentPrice').find('span', class_='price').get_text()
                product_currency = 'NOK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication

def wolt_selenium(urls, currency, special_link):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-localization-key='gdpr-consents.banner.accept-button']")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                medication.append(['', '', '', url])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for i in range(len(urls)):
            try:
                driver.get(urls[i])

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                if special_link[i] == 1: #(lohja, koivuhaka); otrivin
                    product_name = driver.find_element(By.XPATH, "//*[@id=':R196piq:']/div/aside/div[2]/div/div/div/div[1]/div/h2").text
                elif special_link[i] == 2: #ässäapteekki:
                    product_name = driver.find_element(By.XPATH, "//*[@id='«R54r7aq»']/div/aside/div[2]/div/div[2]/div/div[1]/div/h2").text
                else:
                    product_name = driver.find_element(By.XPATH, "//*[@id=':R196piq:']/div/aside/div[2]/div/div[2]/div/div[1]/div/h2").text
                product_price = soup.find('span', {'data-test-id': 'product-modal.total-price'}).get_text()
                product_currency = currency
                medication.append([product_name, product_price, product_currency, urls[i]])
            except Exception as e:
                medication.append(['', '', '', urls[i]])
                print(f"An error occurred for URL {urls[i]}: {e}")

    finally:
        driver.quit()

    return medication


def apohem_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//button[@data-test-id='toggle-wishlist-item-button']/parent::div/following-sibling::h1").text
                product_price = driver.find_element(By.XPATH, "//button[@data-test-id='toggle-wishlist-item-button']/parent::div/parent::div/following-sibling::div/div/div/span").text
                product_currency = 'SEK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication

def apotea_selenium(urls):
    medication = []
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                medication.append(['', '', '', url])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                soup = BeautifulSoup(driver.page_source, 'html.parser')

                product_name = soup.find('h1', id='product-name').get_text()
                product_price = soup.find('span', class_='price').get_text()
                product_currency = 'SEK'
                medication.append([product_name, product_price, product_currency, url])
            except Exception as e:
                medication.append(['', '', '', url])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def admenta_selenium(USE_CASE, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//div[@id='gallery']/following-sibling::div/div/h1").text
                product_price = driver.find_element(By.XPATH, '//span[contains(@x-text, "formatPrice")]').text
                product_currency = 'SEK'
                if USE_CASE == 1:
                    medication.append([product_name, product_price, product_currency, url])
                else:
                    medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                if USE_CASE == 1:
                    medication.append(['', '', '', url])
                else:
                    medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def treet_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div[2]/div[1]/div[1]/h1[1]").text
                product_price = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div[2]/div[1]/div[2]/h2/span").text
                product_currency = 'EUR'
                medication.append([product_name, product_price, product_currency, url])
            except Exception as e:
                medication.append(['', '', '', url])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def isyliopistonapteekki_selenium(urls, data_value):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "declineButton")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                medication.append(['', '', '', url])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication

        for i in range(len(urls)):
            try:
                driver.get(urls[i])
                time.sleep(SLEEP_AFTER_URL)

                dropdown_div = wait.until(
                    EC.presence_of_element_located((By.ID, "SelectedVariation0")))
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", dropdown_div)

                wait.until(EC.element_to_be_clickable((By.ID, "SelectedVariation0")))

                dropdown_div.click()

                option_to_select = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f"option[value='{data_value[i]}']")))

                option_to_select.click()

                time.sleep(2)

                updated_page_source = driver.page_source

                soup = BeautifulSoup(updated_page_source, 'html.parser')

                product_name = soup.find('h1', itemprop='name').get_text()
                product_price = soup.find('span', itemprop='price').get_text()
                product_currency = 'EUR'
                medication.append([product_name, product_price, product_currency, urls[i]])
            except Exception as e:
                medication.append(['', '', '', urls[i]])
                print(f"An error occurred for URL {urls[i]}: {e}")

    finally:
        driver.quit()

    return medication


def lansikeskuksenapteekki_selenium(urls, data_value):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".ep-uiInput.ep-uiInput-button.gbase-refuse-all")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                medication.append(['', '', '', url])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication

        for i in range(len(urls)):
            try:
                driver.get(urls[i])
                time.sleep(SLEEP_AFTER_URL)

                dropdown_div = wait.until(
                    EC.presence_of_element_located((By.ID, "SelectedVariation0")))
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", dropdown_div)

                wait.until(EC.element_to_be_clickable((By.ID, "SelectedVariation0")))

                dropdown_div.click()

                option_to_select = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f"option[value='{data_value[i]}']")))

                option_to_select.click()

                time.sleep(2)

                updated_page_source = driver.page_source

                soup = BeautifulSoup(updated_page_source, 'html.parser')

                product_name = soup.find('h1', itemprop='name').get_text()
                product_price = soup.find('span', itemprop='price').get_text()
                product_currency = 'EUR'
                medication.append([product_name, product_price, product_currency, urls[i]])
            except Exception as e:
                medication.append(['', '', '', urls[i]])
                print(f"An error occurred for URL {urls[i]}: {e}")

    finally:
        driver.quit()

    return medication


def apopro_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                try:
                    product_name = driver.find_element(By.XPATH, "/html/body/main/article/section/div[2]/div[2]/div[2]/div[2]/h1").text
                    product_desc = driver.find_element(By.XPATH,"/html/body/main/article/section/div[2]/div[2]/div[2]/div[2]/h1/span").text
                except NoSuchElementException:
                    product_name = driver.find_element(By.XPATH,"/html/body/main/article/section/div[2]/div[2]/div[2]/div[1]/h1").text
                    product_desc = driver.find_element(By.XPATH,"/html/body/main/article/section/div[2]/div[2]/div[2]/div[1]/ul/li[1]").text

                product_price = driver.find_element(By.XPATH, "//div[@data-testid='pdp-price']").text
                product_currency = 'DKK'
                medication.append([product_name + ' ' + product_desc, product_price, product_currency, url])
            except Exception as e:
                medication.append(['', '', '', url])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def joker_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.CLASS_NAME, "ws-product-details__title").text
                product_name_sub = driver.find_element(By.CLASS_NAME, "ws-product-details__subtitle").text
                product_price = driver.find_element(By.CLASS_NAME, "ws-price").find_element(By.XPATH, "//strong/span").get_attribute("aria-label")
                product_currency = 'NOK'
                medication.append([product_name + ' ' + product_name_sub, product_price, product_currency, url, '', ''])
            except Exception as e:
                medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def meny_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        try:
            driver.get(urls[0])
            wait = WebDriverWait(driver, 50)
            decline_button = wait.until(
                EC.element_to_be_clickable((By.ID, "declineButton")))

            decline_button.click()

            time.sleep(SLEEP_AFTER_DECLINEBUTTON)
        except Exception as e:
            for url in urls:
                medication.append(['', '', '', url, '', ''])
            print(f"An error occurred while accessing the first URL or clicking the decline button: {e}")
            return medication

        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.CLASS_NAME, "ws-product-details__title").text
                product_name_sub = driver.find_element(By.CLASS_NAME, "ws-product-details__subtitle").text
                product_price = driver.find_element(By.CLASS_NAME, "ws-price").find_element(By.XPATH, "//strong/span").get_attribute("aria-label")
                product_currency = 'NOK'
                medication.append([product_name + ' ' + product_name_sub, product_price, product_currency, url, '', ''])
            except Exception as e:
                medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def coop_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//*[@id='pageContent']/div/div[2]/div[1]/article/div/div[2]/div/div[1]/h1").text
                product_price = driver.find_element(By.XPATH, "//*[@id='pageContent']/div/div[2]/div[1]/article/div/div[2]/div/div[2]/div[1]/div/div").text
                product_currency = 'SEK'
                medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def citygross_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//div[@class='content-right']/div/h1").text
                product_name_sub = driver.find_element(By.XPATH, "//div[@class='content-right']/div/p").text
                product_price = driver.find_element(By.XPATH, "//div[@class='price-tag-container']/meta[3]").get_attribute("content")
                product_currency = 'SEK'
                medication.append([product_name + ' ' + product_name_sub, product_price, product_currency, url, '', ''])
            except Exception as e:
                medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def hemkop_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[1]/div/div[2]/h1").text
                product_price = driver.find_element(By.XPATH, "//span[@data-testid='price-container']").text
                product_currency = 'SEK'
                medication.append([product_name, product_price, product_currency, url, '', ''])
            except Exception as e:
                medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


def ica_selenium(stores_and_locations, urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for i in range(len(urls)):
            store_index = i // 5
            store_type = stores_and_locations[store_index][0]
            location = stores_and_locations[store_index][1]
            try:
                driver.get(urls[i])

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div[1]/h1").text
                product_price = driver.find_element(By.XPATH, "//div[@data-test='price-container']").text
                product_currency = 'SEK'
                medication.append([product_name, product_price, product_currency, urls[i], store_type, location])
            except Exception as e:
                medication.append(['', '', '', urls[i], stores_and_locations[store_index][0], stores_and_locations[store_index][1]])
                print(f"An error occurred for URL {urls[i]}: {e}")

    finally:
        driver.quit()

    return medication


def willys_selenium(urls):
    medication = []
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    try:
        for url in urls:
            try:
                driver.get(url)

                time.sleep(SLEEP_AFTER_URL)

                product_name = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[4]/main/section/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/h2/span").text
                product_price = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[4]/main/section/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/span[1]").text
                product_price_cents = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[4]/main/section/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div/span[1]").text
                product_currency = 'SEK'
                medication.append([product_name, product_price + '.' + product_price_cents, product_currency, url, '', ''])
            except Exception as e:
                medication.append(['', '', '', url, '', ''])
                print(f"An error occurred for URL {url}: {e}")

    finally:
        driver.quit()

    return medication


