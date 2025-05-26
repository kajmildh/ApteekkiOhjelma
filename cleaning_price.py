import pandas as pd
import re

# Load the CSV file into a DataFrame
# df = pd.read_csv('lääkehinnat.csv')


# Function to clean the price
def clean_price(price):
    price_str = str(price).strip()

    # Handle prices with "kr" suffix by removing it
    price_str = price_str.replace('kr.', '').replace('kr', '').replace('Kr', '').replace('Butikspris:','').strip().replace('€', '').replace('ISK', '')

    # Check for spaces used as thousands separators and remove them
    if ' ' in price_str:
        price_str = price_str.replace(' ', '')

    pattern = r"^\d\.\d{3}$"  # Format: Single digit, dot, three digits
    if re.match(pattern, price_str):
        price_str = price_str.replace(".", "")  # Remove the dot

    price_str = re.sub(r'(?<=\d):(?=\d)', '.', price_str)

    # Check if the comma is used as a decimal separator
    if ',' in price_str and '.' not in price_str:
        price_str = price_str.replace(',', '.')

    # Remove any remaining non-numeric characters except for the decimal point
    price_str = ''.join(char for char in price_str if char.isdigit() or char == '.')

    # Convert the cleaned price to float
    try:
        return float(price_str)
    except ValueError:
        return ""

