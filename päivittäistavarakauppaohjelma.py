from lääkepilottiohjelma import save_data_with_fallback
import pandas as pd
import datetime
import apteekit_funktiot as af
from cleaning_price import clean_price


def main():

    af.keraa_tiedot_paivittaistavara()

    data = pd.DataFrame(af.medication_2, columns=['Tuote', 'Hinta', 'Valuutta', 'Valmisteen osoite', 'ICA', 'Kaupunki', 'Verkko-osoite'])
    date_now = datetime.datetime.now().date()
    data['Päivämäärä'] = date_now
    data = data.reindex(columns=['Päivämäärä', 'Tuote', 'Hinta', 'Valuutta', 'Valmisteen osoite', 'Verkko-osoite', 'ICA', 'Kaupunki'])
    print(data.to_string())

    uncleaned_filename = f'ptkauppalääkehinnat_{date_now}.xlsx'
    cleaned_filename = f'ptkauppalääkehinnat_clean_{date_now}.xlsx'

    # Save uncleaned data (only original price column)
    success_uncleaned = save_data_with_fallback(data, uncleaned_filename)

    data['Hinta'] = data['Hinta'].apply(clean_price)
    data['Hinta'] = pd.to_numeric(data['Hinta'], errors='coerce')

    success_cleaned = save_data_with_fallback(data, cleaned_filename)

    # Report outcome
    if not (success_uncleaned and success_cleaned):
        print("Could not save one or both files. Please check directory permissions or close any open Excel files.")
    elif not success_uncleaned:
        print("Failed to save uncleaned data file.")
    elif not success_cleaned:
        print("Failed to save cleaned data file.")

if __name__ == "__main__":
    main()