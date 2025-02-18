import pandas as pd
import datetime
import apteekit_funktiot as af
from cleaning_price import clean_price


def main():

    af.keraa_tiedot()

    data = pd.DataFrame(af.medication, columns=['Tuote', 'Hinta', 'Valuutta', 'Valmisteen osoite', 'Verkko-osoite'])
    date_now = datetime.datetime.now().date()
    data['Päivämäärä'] = date_now
    data = data.reindex(columns=['Päivämäärä', 'Tuote', 'Hinta', 'Valuutta', 'Valmisteen osoite', 'Verkko-osoite'])
    print(data.to_string())

    data.to_excel(f'lääkehinnat_{date_now}.xlsx', index=False)

    data['Hinta'] = data['Hinta'].apply(clean_price)
    data.to_excel(f'lääkehinnat_clean_{date_now}.xlsx', index=False)

if __name__ == "__main__":
    main()