import selenium_tuotteet as seltuot
import normi_tuotteet as nt

medication = []


def keraa_tiedot():

    # Tuurin apteekki

    pharmacy_url_1 = "tuurinapteekki.fi"
    URLs_1_normi = ['https://www.tuurinapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                    'https://www.tuurinapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                    'https://www.tuurinapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                    'https://www.tuurinapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                    'https://www.tuurinapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                    'https://www.tuurinapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                    'https://www.tuurinapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_1 = nt.tuurinapteekki(URLs_1_normi)

    for i in fetched_data_1:
        i.append(pharmacy_url_1)
    medication.extend(fetched_data_1)

    # Yliopiston apteekki

    pharmacy_url_2 = "yliopistonapteekki.fi"
    URLs_2_selenium = ['https://www.yliopistonapteekki.fi/burana-tabletti-400mg',
                       'https://www.yliopistonapteekki.fi/voltaren-forte-geeli-23-2mg-g',
                       'https://www.yliopistonapteekki.fi/panadol-tabletti-500mg',
                       'https://www.yliopistonapteekki.fi/somac-control-enterotabletti-20mg',
                       'https://www.yliopistonapteekki.fi/zyrtec-tabletti-10mg']

    URLs_2_normi = ['https://www.yliopistonapteekki.fi/hydrocortison-emulsiovoide-1',
                    'https://www.yliopistonapteekki.fi/otrivin-menthol-sailytysaineeton-1-mg-ml-nenasumute-10-ml-98344']

    data_values_2_selenium = ["21545", "14423", "66485", "6392", "22610"]
    product_numbers_2_selenium = ["56883", "57648", "66962", "56535", "59346"]

    fetched_data_2_first = seltuot.yliopistonapteekki_selenium(URLs_2_selenium, data_values_2_selenium, product_numbers_2_selenium)
    fetched_data_2_second = nt.yliopistonapteekki(URLs_2_normi)

    for i in fetched_data_2_first + fetched_data_2_second:
        i.append(pharmacy_url_2)

    medication.extend(fetched_data_2_first + fetched_data_2_second)

    # Hjärtat
    pharmacy_url_4 = "apotekhjartat.se"
    URLs_4_normi = ['https://www.apotekhjartat.se/produkt/ipren-filmdragerad-tablett-400-mg-30-st/',
                    'https://www.apotekhjartat.se/produkt/panodil-500-mg-filmdragerad-tablett-20-st/',
                    'https://www.apotekhjartat.se/produkt/voltaren-gel-232-mgag-100-g/',
                    'https://www.apotekhjartat.se/produkt/clarityn-tablett-10-mg-30-tabletter-10/',
                    'https://www.apotekhjartat.se/produkt/otrivin-menthol-nasspray-utan-konserveringsmedel-1mgoml/',
                    'https://www.apotekhjartat.se/produkt/hydrokortison-evolan-10-mgag-kram-20-g/']

    fetched_data_4 = seltuot.hjartat_selenium(URLs_4_normi)

    for i in fetched_data_4:
        i.append(pharmacy_url_4)
    medication.extend(fetched_data_4)

    #Apoteket
    pharmacy_url_5 = "apoteket.se"
    URLs_5_selenium = ['https://www.apoteket.se/produkt/ipren-filmdragerad-tablett-400-mg-30-st-blister-114936/',
                      'https://www.apoteket.se/produkt/losec-enterotablett-20-mg-14-st-blister-218102/',
                       'https://www.apoteket.se/produkt/voltaren-gel-232-mg-per-g-100-g-tub-250186/',
                       'https://www.apoteket.se/produkt/clarityn-tablett-10-mg-30-st-blister-1330996/',
                       'https://www.apoteket.se/produkt/otrivin-menthol-utan-konserveringsmedel-nasspray-losning-1-mg-per-ml-10-ml-flaska-1570771/',
                       'https://www.apoteket.se/produkt/hydrokortison-evolan-kram-10-mg-per-g-20-g-tub-57582/']

    fetched_data_5 = seltuot.apoteket_selenium(URLs_5_selenium)

    for i in fetched_data_5:
        i.append(pharmacy_url_5)
    medication.extend(fetched_data_5)

    # Kronans Apotek
    pharmacy_url_6 = "kronansapotek.se"
    URLs_6_selenium = ['https://www.kronansapotek.se/Ipren-400-mg/p/088534/',
                       'https://www.kronansapotek.se/panodil-filmdragerad-tablett/p/196456/',
                       'https://www.kronansapotek.se/Losec/p/492546/',
                       'https://www.kronansapotek.se/Voltaren-/p/533022/',
                       'https://www.kronansapotek.se/clarityn-10-mg/p/154158/',
                       'https://www.kronansapotek.se/otrivin-nasspray-menthol-1mg-ml-10ml/p/389805/',
                       'https://www.kronansapotek.se/evolan-hydrokortison-kram/p/046776/']

    fetched_data_6 = seltuot.kronansapotek_selenium(URLs_6_selenium)

    for i in fetched_data_6:
        i.append(pharmacy_url_6)
    medication.extend(fetched_data_6)
    
    # Apotek 1
    pharmacy_url_7 = "apotek1.no"
    URLs_7_selenium = ['https://www.apotek1.no/produkter/hydrokortison-1-krem-20g-112847p',
                       'https://www.apotek1.no/produkter/ibux-400mg-tabletter-20stk-21630p',
                       'https://www.apotek1.no/produkter/otrivin-1mg-ml-nesespray-med-mentol-10ml-166451p',
                       'https://www.apotek1.no/produkter/panodil-500mg-tabletter-20stk-83621p',
                       'https://www.apotek1.no/produkter/somac-control-20mg-enterotabletter-14stk-50387p',
                       'https://www.apotek1.no/produkter/voltarol-forte-232mg-g-gel-100g-392871p',
                       'https://www.apotek1.no/produkter/zyrtec-10mg-tabletter-30stk-24101p']

    fetched_data_7 = seltuot.apotek1_selenium(URLs_7_selenium)

    for i in fetched_data_7:
        i.append(pharmacy_url_7)
    medication.extend(fetched_data_7)

    # Vitusapotek
    pharmacy_url_8 = "vitusapotek.no"
    URLs_8_normi = ['https://www.vitusapotek.no/sol%2c-fritid-og-reise/reiseapotek/smertestillende/ibux-tabletter-400-mg-20-stk/p/021630',
                    'https://www.vitusapotek.no/smerte%2c-feber-og-forkjolelse/smertestillende/smertestillende-tabletter/panodil-500-mg-tabletter-20-stk/p/083621?s=qsearch&text=panodil',
                    'https://www.vitusapotek.no/mage-og-tarm/halsbrann/somac-control-enterotabletter-20-mg-1-x-14-stk/p/050387?s=qsearch&text=somac%20control',
                    'https://www.vitusapotek.no/sol%2c-fritid-og-reise/reiseapotek/smertestillende/voltarol-forte-gel-23%2c2mg-g-smertestillende-gel--100-g/p/392871?s=qsearch&text=voltarol%20forte',
                    'https://www.vitusapotek.no/allergimedisin/allergitabletter/zyrtec-tabletter-10-mg-30-stk/p/024101?s=qsearch&text=yrtec',
                    'https://www.vitusapotek.no/smerte%2c-feber-og-forkjolelse/nesespray/otrivin-mentol-nesespray-forkjolelse-1-mg-ml-10-ml/p/166451?s=qsearch&text=otrivin',
                    'https://www.vitusapotek.no/kroppspleie/after-sun/kjop-hydrokortison-krem-20g-%7c-vitusapotek/p/112847?s=qsearch&text=hydrokortison']

    fetched_data_8 = nt.vitusapotek(URLs_8_normi)

    for i in fetched_data_8:
        i.append(pharmacy_url_8)
    medication.extend(fetched_data_8)

    # Boots Apotek
    pharmacy_url_9 = "boots.no"
    URLs_9_normi = ['https://www.boots.no/ibux-tabletter-400-mg-20-stk-021630',
                    'https://www.boots.no/panodil-tabletter-500-mg-20-stk-083621',
                    'https://www.boots.no/somac-control-enterotabletter-20-mg-14-stk-050387',
                    'https://www.boots.no/voltarol-forte-gel-23-2-mg-g-100g-392871',
                    'https://www.boots.no/zyrtec-tabletter-10-mg-30-stk-024101',
                    'https://www.boots.no/otrivin-nesespray-mentol-1-mg-ml-10-ml-166451',
                    'https://www.boots.no/evolan-hydrokortison-krem-1-20g-112847']

    fetched_data_9 = nt.bootsapotek(URLs_9_normi)

    for i in fetched_data_9:
        i.append(pharmacy_url_9)
    medication.extend(fetched_data_9)

    # Lyfjaval
    pharmacy_url_10 = "lyfjaval.is"
    URLs_10_selenium = ['https://www.lyfjaval.is/verslun/lausasolulyf/ibufen-30stk-400mg-filmhtfl?q=ibufen',
                        'https://www.lyfjaval.is/verslun/lausasolulyf/panodil-30stk-500mg-filmhtfl?q=panodil',
                        'https://www.lyfjaval.is/verslun/lausasolulyf/omeprazol-actavis-14stk-20mg-sh-hylki',
                        'https://www.lyfjaval.is/verslun/lausasolulyf/voltaren-forte-23-2mg-g-100g?q=voltaren',
                        'https://www.lyfjaval.is/verslun/lausasolulyf/histasin-30stk-10mg-toflur?q=histasin',
                        'https://www.lyfjaval.is/verslun/lausasolulyf/otrivin-menthol-ukonserveret-10ml-1mg-ml?q=otrivin',
                        'https://www.lyfjaval.is/verslun/lausasolulyf/mildison-lipid-15g-10mg-g-krem?q=mildison']

    fetched_data_10 = seltuot.lyfjaval_selenium(URLs_10_selenium)

    for i in fetched_data_10:
        i.append(pharmacy_url_10)
    medication.extend(fetched_data_10)

    # Lyf Og Heilsa
    pharmacy_url_11 = "lyfogheilsa.is"
    URLs_11_normi = ['https://www.lyfogheilsa.is/lausasolulyf/2531',
                     'https://www.lyfogheilsa.is/lausasolulyf/2542',
                     'https://www.lyfogheilsa.is/lausasolulyf/2552',
                     'https://www.lyfogheilsa.is/lausasolulyf/3067',
                     'https://www.lyfogheilsa.is/lausasolulyf/3096',
                     'https://www.lyfogheilsa.is/lausasolulyf/3114',
                     'https://www.lyfogheilsa.is/lausasolulyf/5844']

    fetched_data_11 = nt.lyfogheilsa(URLs_11_normi)

    for i in fetched_data_11:
        i.append(pharmacy_url_11)
    medication.extend(fetched_data_11)
    
    # Lyfjaver
    pharmacy_url_12 = "lyfjaver.is"
    URLs_12_selenium = ['https://www.lyfjaver.is/verslun/ofnaemis-og-ondunarfaeralyf/histasin-toflur-10-mg-30-stk',
                        'https://www.lyfjaver.is/verslun/verkjalyf/ibufen-toflur-400-mg-30-stk',
                        'https://www.lyfjaver.is/verslun/hudlyf/mildison-lipid-krem-10-mg-g-15-g-feitt',
                        'https://www.lyfjaver.is/verslun/magi-meltingarfaeri-og-munnur/omeprazol-actavis-sh-hylki-20-mg-14-stk',
                        'https://www.lyfjaver.is/verslun/ofnaemis-og-ondunarfaeralyf/otrivin-menthol-ukonserveret-nefudi-1-mg-ml-10-ml-2',
                        'https://www.lyfjaver.is/verslun/verkjalyf/panodil-filmhtfl-500-mg-30-stk',
                        'https://www.lyfjaver.is/verslun/verkjalyf/voltaren-forte-hlaup-2320-mg-g-100-g']

    fetched_data_12 = seltuot.lyfjaver_selenium(URLs_12_selenium)

    for i in fetched_data_12:
        i.append(pharmacy_url_12)
    medication.extend(fetched_data_12)
    
    # Holte Apotek
    pharmacy_url_13 = "apoteket-online.dk/apotek/holte-apotek"
    URLs_13_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                        'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                        'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                        'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                        'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                        'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                        'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_13 = seltuot.apoteketonline_selenium(URLs_13_selenium, "Holte Apotek")

    for i in fetched_data_13:
        i.append(pharmacy_url_13)
    medication.extend(fetched_data_13)

    # Hvidovre Apotek
    pharmacy_url_14 = "hvidovre.dinapoteker.dk"
    URLs_14_selenium = ['https://hvidovre.dinapoteker.dk/ipren-200-mg-p6366',
                        'https://hvidovre.dinapoteker.dk/panodil-500-mg-blister-p12445',
                        'https://hvidovre.dinapoteker.dk/pantoprazol-20-mg-krka-1-p4178',
                        'https://hvidovre.dinapoteker.dk/voltaren-forte-23-2-mg-g-1-p51188',
                        'https://hvidovre.dinapoteker.dk/alnok-10-mg-1-p6037',
                        'https://hvidovre.dinapoteker.dk/otrivin-menthol-ukonserveret-1-p12770',
                        'https://hvidovre.dinapoteker.dk/mildison-lipid-10-mg-g-0-p43108']

    fetched_data_14 = seltuot.dinapoteker_selenium(URLs_14_selenium)

    for i in fetched_data_14:
        i.append(pharmacy_url_14)
    medication.extend(fetched_data_14)

    # Lyngby svane apotek
    pharmacy_url_15 = "apotekeren.dk"
    URLs_15_normi = ['https://www.apotekeren.dk/produkter/ipren-tabl-200-mg/p-26144',
                     'https://www.apotekeren.dk/produkter/panodil-tabl-500-mg/p-25660',
                     'https://www.apotekeren.dk/produkter/pantoprazol-enttabl-20-mg-(krk/p-25688',
                     'https://www.apotekeren.dk/produkter/voltaren-forte-gel-232-mgg/p-25798',
                     'https://www.apotekeren.dk/produkter/alnok-tabl-10-mg/p-26041',
                     'https://www.apotekeren.dk/produkter/otrivin-menthol-uk-naesesp-1mg/p-26225',
                     'https://www.apotekeren.dk/produkter/mildison-lipid-creme-10-mgg/p-25760']

    fetched_data_15 = nt.apoteketsvalen(URLs_15_normi)

    for i in fetched_data_15:
        i.append(pharmacy_url_15)
    medication.extend(fetched_data_15)

    # Akureyrarapotek
    pharmacy_url_16 = "akureyrarapotek.is"
    URLs_16_selenium = ['https://www.akureyrarapotek.is/verslun/lausasolulyf/histasin-10mg-30stk?q=histasin',
                        'https://www.akureyrarapotek.is/verslun/lausasolulyf/ibufen-400mg-30stk?q=ibufen',
                        'https://www.akureyrarapotek.is/verslun/lausasolulyf/mildison-lipid-10mg-g-15g',
                        'https://www.akureyrarapotek.is/verslun/lausasolulyf/omeprazol-actavis-20mg-14stk?q=omeprazol',
                        'https://www.akureyrarapotek.is/verslun/lausasolulyf/otrivin-menthol-ukonserveret-1mg-ml-10ml?q=otrivin',
                        'https://www.akureyrarapotek.is/verslun/lausasolulyf/panodil-500mg-30stk?q=panodil',
                        'https://www.akureyrarapotek.is/verslun/lausasolulyf/voltaren-forte-23-2mg-g-100g?q=voltaren']

    fetched_data_16 = seltuot.lyfjaval_selenium(URLs_16_selenium)

    for i in fetched_data_16:
        i.append(pharmacy_url_16)
    medication.extend(fetched_data_16)


    # Efstaleitis
    pharmacy_url_17 = "lyfjaapotekid.is"
    URLs_17_selenium = ['https://www.lyfjaapotekid.is/verslun/lausasolulyf/ibufen-30stk-400mg-filmhtfl',
                        'https://www.lyfjaapotekid.is/verslun/lausasolulyf/mildison-lipid-15g-10mg-g-krem-2?q=mildison',
                        'https://www.lyfjaapotekid.is/verslun/lausasolulyf/otrivin-menthol-ukonserveret-10ml-1mg-ml',
                        'https://www.lyfjaapotekid.is/verslun/lausasolulyf/panodil-30stk-500mg-filmhtfl']

    fetched_data_17 = seltuot.lyfjaval_selenium(URLs_17_selenium)

    for i in fetched_data_17:
        i.append(pharmacy_url_17)
    medication.extend(fetched_data_17)

    # Rima apotek
    pharmacy_url_18 = "rimaapotek.is"
    URLs_18_selenium = ['https://www.rimaapotek.is/verslun/lausasolulyf/histasin-10mg-30stk?q=histasin',
                        'https://www.rimaapotek.is/verslun/lausasolulyf/ibufen-toflur-400mg-30stk?q=ibufen',
                        'https://www.rimaapotek.is/verslun/lausasolulyf/mildison-lipid-10mg-g-15g?q=mildison',
                        'https://www.rimaapotek.is/verslun/lausasolulyf/omeprazol-actavis-20mg-14stk',
                        'https://www.rimaapotek.is/verslun/lausasolulyf/otrivin-menthol-ukonserveret-10ml-1mg-ml',
                        'https://www.rimaapotek.is/verslun/lausasolulyf/panodil-500mg-30stk?q=panodil',
                        'https://www.rimaapotek.is/verslun/lausasolulyf/voltaren-forte-23-2mg-g-100g?q=voltaren']

    fetched_data_18 = seltuot.lyfjaval_selenium(URLs_18_selenium)

    for i in fetched_data_18:
        i.append(pharmacy_url_18)
    medication.extend(fetched_data_18)

    # Urdarapotek
    pharmacy_url_19 = "urdarapotek.is"
    URLs_19_selenium = ['https://urdarapotek.is/verslun/lausasolulyf/histasin-10mg-30stk',
                        'https://urdarapotek.is/verslun/lausasolulyf/ibufen-400mg-30stk?q=ibufen',
                        'https://urdarapotek.is/verslun/lausasolulyf/mildison-lipid-10mg-g-15g?q=mildison',
                        'https://urdarapotek.is/verslun/lausasolulyf/omeprazol-actavis-20mg-14stk?q=omepra',
                        'https://urdarapotek.is/verslun/lausasolulyf/otrivin-ukonserveret-1mg-ml-10ml',
                        'https://urdarapotek.is/verslun/lausasolulyf/panodil-500mg-30stk',
                        'https://urdarapotek.is/verslun/lausasolulyf/voltaren-forte-23-2mg-g-100g?q=voltaren']

    fetched_data_19 = seltuot.lyfjaval_selenium(URLs_19_selenium)

    for i in fetched_data_19:
        i.append(pharmacy_url_19)
    medication.extend(fetched_data_19)

    # Apomed
    pharmacy_url_20 = "apomed.no"
    URLs_20_selenium = ['https://www.apomed.no/ibux-tab-400mg-021630',
                        'https://www.apomed.no/panodil-tab-500mg-083621',
                        'https://www.apomed.no/voltarol-forte-gel-23-2mg-g-392871',
                        'https://www.apomed.no/zyrtec-tab-10mg-024101']

    fetched_data_20 = seltuot.apomed_selenium(URLs_20_selenium)

    for i in fetched_data_20:
        i.append(pharmacy_url_20)
    medication.extend(fetched_data_20)

    # ApotekDirekte
    pharmacy_url_21 = "apotekdirekte.no"
    URLs_21_selenium = ['https://www.apotekdirekte.no/products/hydrokortison-ccs-krem-1-20g2',
                        'https://www.apotekdirekte.no/products/ibux-tabletter-400mg-20-stk',
                        'https://www.apotekdirekte.no/products/otrivin-nesespray-1mgml-mentol-10ml',
                        'https://www.apotekdirekte.no/products/panodil-tab500mg',
                        'https://www.apotekdirekte.no/products/somac-control-20mg-14-entrotabletter',
                        'https://www.apotekdirekte.no/products/voltarol-forte-gel-232mgg-100g',
                        'https://www.apotekdirekte.no/products/zyrtec-10mg-30-tabletter']

    fetched_data_21 = seltuot.apotekdirekte_selenium(URLs_21_selenium)

    for i in fetched_data_21:
        i.append(pharmacy_url_21)
    medication.extend(fetched_data_21)

    # Apotek for deg
    pharmacy_url_22 = "apotekfordeg.no"
    URLs_22_selenium = ['https://www.apotekfordeg.no/products/hydrokortison-evolan-10-mgg-krem-20-g',
                        'https://www.apotekfordeg.no/products/ibux-tabletter-400-mg-20-stk',
                        'https://www.apotekfordeg.no/products/otrivin-mentol-1-mgml-nesespray-10-ml',
                        'https://www.apotekfordeg.no/products/panodil-tabletter-500-mg-20-stk',
                        'https://www.apotekfordeg.no/products/somac-control-20-mg-enterotabletter-14-stk',
                        'https://www.apotekfordeg.no/products/voltarol-forte-gel-232-mgg-100-g',
                        'https://www.apotekfordeg.no/products/zyrtec-10-mg-tabletter-30-stk']

    fetched_data_22 = seltuot.apotekdirekte_selenium(URLs_22_selenium)

    for i in fetched_data_22:
        i.append(pharmacy_url_22)
    medication.extend(fetched_data_22)

    # Apotekhjem
    pharmacy_url_23 = "apotekhjem.no"
    URLs_23_normi = ['https://www.apotekhjem.no/apotek-apotekhjem-voltarol-forte-gel-232mgg',
                     'https://www.apotekhjem.no/apotek-nettapotek-zyrtec-tab-10mg-30stk',
                     'https://www.apotekhjem.no/hydrokortison-trimb-krem-10mg',
                     'https://www.apotekhjem.no/ibux-tab-400mg-2',
                     'https://www.apotekhjem.no/panodil-tab-500mg',
                     'https://www.apotekhjem.no/somac-control-enterotab-20mg']

    fetched_data_23 = nt.apotekhjem(URLs_23_normi)

    for i in fetched_data_23:
        i.append(pharmacy_url_23)
    medication.extend(fetched_data_23)

    # Apotera apotek
    pharmacy_url_24 = "apotera.no"
    URLs_24_normi = ['https://www.apotera.no/ibux-400-mg-tabletter-20-stk',
                     'https://www.apotera.no/panodil-500-mg-tabletter-20-stk',
                     'https://www.apotera.no/somac-control-20-mg-enterotabletter-14-stk',
                     'https://www.apotera.no/voltarol-forte-23-2-mg-g-gel-100-g',
                     'https://www.apotera.no/zyrtec-10-mg-tabletter-30-stk',
                     'https://www.apotera.no/otrivin-1-mg-ml-nesespray-med-mentol-voksne-10-ml',
                     'https://www.apotera.no/hydrokortison-evolan-10-mg-g-krem-20-g']

    fetched_data_24 = nt.apoteraapotek(URLs_24_normi)

    for i in fetched_data_24:
        i.append(pharmacy_url_24)
    medication.extend(fetched_data_24)

    # Appoteket
    pharmacy_url_25 = "appoteket.no"
    URLs_25_selenium = ['https://appoteket.no/ibux-400mg-tabletter-20stk',
                        'https://appoteket.no/panodil-tabletter-20-stk-500mg',
                        'https://appoteket.no/somac-control-20mg-enterotabletter-14stk',
                        'https://appoteket.no/voltarol-forte-gel-23-2mg-g-100g',
                        'https://appoteket.no/zyrtec-10mg-tabletter-30stk',
                        'https://appoteket.no/otrivin-nesespray-mentol-1-mg-ml',
                        'https://appoteket.no/hydrokortison-1-evolan-10-mg-g-krem']

    fetched_data_25 = seltuot.appoteket_selenium(URLs_25_selenium)

    for i in fetched_data_25:
        i.append(pharmacy_url_25)
    medication.extend(fetched_data_25)

    # Balder apotek
    pharmacy_url_26 = "balderapotek.no"
    URLs_26_normi = ['https://balderapotek.no/produkt/ibux-tabletter-400-mg-20-stk/',
                     'https://balderapotek.no/produkt/panodil-tabletter-500-mg-20-stk/',
                     'https://balderapotek.no/produkt/somac-control-enterotab-20mg/',
                     'https://balderapotek.no/produkt/voltarol-forte-gel-232mg-g/',
                     'https://balderapotek.no/produkt/zyrtec-tabletter-10-mg-30-stk/',
                     'https://balderapotek.no/produkt/otrivin-nesespray-1mg-ml-mentol/',
                     'https://balderapotek.no/produkt/hydrokortison-trimb-krem-10mg/']

    fetched_data_26 = nt.balderapotek(URLs_26_normi)

    for i in fetched_data_26:
        i.append(pharmacy_url_26)
    medication.extend(fetched_data_26)

    # Dameapoteket
    pharmacy_url_27 = "dameapoteket.no"
    URLs_27_normi = ['https://dameapoteket.no/butikk/ibux-tab-400mg-20-enpac/',
                     'https://dameapoteket.no/butikk/panodil-tab-500mg-20-enpac/',
                     'https://dameapoteket.no/butikk/voltarol-forte-gel-23-2mg-g-100-g/',
                     'https://dameapoteket.no/butikk/zyrtec-tab-10mg-30-enpac/',
                     'https://dameapoteket.no/butikk/otrivin-nesespray-1mg-ml-mentol-10-ml/',
                     'https://dameapoteket.no/butikk/hydrokortison-evol-krem-10mg-20-g/']

    fetched_data_27 = nt.dameapoteket(URLs_27_normi)

    for i in fetched_data_27:
        i.append(pharmacy_url_27)
    medication.extend(fetched_data_27)

    # Farmasiet
    pharmacy_url_28 = "farmasiet.no"
    URLs_28_normi = ['https://www.farmasiet.no/catalog/feber-og-forkjolelse/smertestillende-og-febernedsettende/ibux-tab-400mg-20,5000086',
                     'https://www.farmasiet.no/catalog/feber-og-forkjolelse/smertestillende-og-febernedsettende/panodil-tab--500mg-20,5000203',
                     'https://www.farmasiet.no/catalog/mage-og-tarm/halsbrann-og-syreplager/somac-control-enterotab-20mg-14,5000246',
                     'https://www.farmasiet.no/catalog/smerte/forstuelse/voltarol-forte-gel-232mgg-100,5001535',
                     'https://www.farmasiet.no/catalog/allergi-og-astma/pollenallergi/zyrtec-tab-10mg-30,5000298',
                     'https://www.farmasiet.no/catalog/feber-og-forkjolelse/nesespray-og-nesedraper/otrivin-nesespr-1mgml-mentol-10,5000195',
                     'https://www.farmasiet.no/catalog/allergi-og-astma/eksem/hydrokortison-evol-krem-10mg-20,5000074']

    fetched_data_28 = nt.farmasiet(URLs_28_normi)

    for i in fetched_data_28:
        i.append(pharmacy_url_28)
    medication.extend(fetched_data_28)

    # Herreapoteket
    pharmacy_url_29 = "herreapoteket.no"
    URLs_29_normi = ['https://herreapoteket.no/no/shop/apotekvarer/ibux-tab-400mg-20-enpac',
                     'https://herreapoteket.no/no/shop/apotekvarer/panodil-tab-500mg-20-enpac',
                     'https://herreapoteket.no/no/shop/apotekvarer/somac-control-enterotab-20mg-14-enpac',
                     'https://herreapoteket.no/no/shop/apotekvarer/voltarol-forte-gel-232mgg-100-g',
                     'https://herreapoteket.no/no/shop/apotekvarer/allergi/zyrtec-10-mg-tabletter-30-stk',
                     'https://herreapoteket.no/no/shop/apotekvarer/otrivin-1-mgml-nesespray-med-mentol-voksne-10-ml',
                     'https://herreapoteket.no/no/shop/apotekvarer/hydrokortison-evolan-10-mgg-krem-20-g']

    fetched_data_29 = seltuot.herreapotek_selenium(URLs_29_normi)

    for i in fetched_data_29:
        i.append(pharmacy_url_29)
    medication.extend(fetched_data_29)

    # Med24apotek
    pharmacy_url_30 = "med24.no"
    URLs_30_selenium = ['https://www.med24.no/helse-og-livsstil/smerte-og-plager/smertestillende/ibux-tabletter-400mg-20-tabletter',
                        'https://www.med24.no/helse-og-livsstil/smerte-og-plager/smertestillende/panodil-tabletter-500mg-20-stk',
                        'https://www.med24.no/helse-og-livsstil/smerte-og-plager/halsbrann-og-sure-oppstoet/somac-control-20-mg-enterotabletter-14-stk',
                        'https://www.med24.no/helse-og-livsstil/smerte-og-plager/smertestillende/voltarol-forte-gel-23-2-mg-g-100-g',
                        'https://www.med24.no/helse-og-livsstil/smerte-og-plager/allergi/zyrtec-tabletter-10-mg-30-tabletter',
                        'https://www.med24.no/helse-og-livsstil/smerte-og-plager/forkjoelelse-og-influensa/otrivin-nesespray-mentol-1-mg-10-ml',
                        'https://www.med24.no/helse-og-livsstil/saar-og-skader/saarheling/hydrokortison-evolan-krem-1-prosent-20-gram']

    fetched_data_30 = seltuot.med24apotek_selenium(URLs_30_selenium)

    for i in fetched_data_30:
        i.append(pharmacy_url_30)
    medication.extend(fetched_data_30)

    # Ditt apotek opera
    pharmacy_url_31 = "osloapotek.no"
    URLs_31_normi = ['https://osloapotek.no/products/ibux-tabletter-400-mg-20-stykk-tablett?_pos=2&_psq=ibux&_ss=e&_v=1.0',
                     'https://osloapotek.no/products/paracetamol-paracet-pinex-panodil?_pos=1&_psq=panodil&_ss=e&_v=1.0&variant=48144804184376',
                     'https://osloapotek.no/products/somac-control-enterotabletter-20-mg-14-stk-050387?_pos=1&_psq=somac&_ss=e&_v=1.0',
                     'https://osloapotek.no/products/voltarol-forskjellge-typer?variant=48144868999480',
                     'https://osloapotek.no/products/cetirizin-zyrtec-tabletter?variant=48137766502712',
                     'https://osloapotek.no/products/otrivin-mentol-nesespray-forkjolelse-1-mg-ml?_pos=3&_psq=otrivin&_ss=e&_v=1.0',
                     'https://osloapotek.no/products/hydrokortison-evolan-krem-10-mg-g-20-gram-112848?_pos=1&_psq=hydrok&_ss=e&_v=1.0']

    fetched_data_31 = nt.dittapotekopera(URLs_31_normi)

    for i in fetched_data_31:
        i.append(pharmacy_url_31)
    medication.extend(fetched_data_31)

    # Apohem
    pharmacy_url_33 = "apohem.se"
    URLs_33_selenium = ['https://www.apohem.se/vark-feber/huvudvark/ipren-400mg-ibuprofen-30-tabletter',
                        'https://www.apohem.se/vark-feber/huvudvark/panodil-500mg-paracetamol-20-tabletter',
                        'https://www.apohem.se/vark-feber/ledvark-artros/voltaren-232-mgg-gel-100g',
                        'https://www.apohem.se/allergi/pollenallergi/antihistamin-vid-pollenallergi/clarityn-tabletter-10-mg-30-st',
                        'https://www.apohem.se/forkylning/bihaleinflammation/nasspray-och-tabletter/otrivin-nasspray-1mgml-10-ml',
                        'https://www.apohem.se/sar-bett-stick/bett-stick/efter-bett/hydrokortison-evolan-10-mgg-kram-20-g']

    fetched_data_33 = seltuot.apohem_selenium(URLs_33_selenium)

    for i in fetched_data_33:
        i.append(pharmacy_url_33)
    medication.extend(fetched_data_33)

    # Farmakeut AB
    pharmacy_url_34 = "aposve.se"
    URLs_34_normi = ['https://www.aposve.se/product/ipren-400-mg-30-filmdragerade-tabletter/',
                     'https://www.aposve.se/product/panodil-500-mg-20-filmdragerade-tabletter/',
                     'https://www.aposve.se/product/losec-20-mg-14-enterotabletter-5/',
                     'https://www.aposve.se/product/voltaren-232-mg-g-gel-100g/',
                     'https://www.aposve.se/product/clarityn-10-mg-30-tabletter/',
                     'https://www.aposve.se/product/otrivin-menthol-1mg-ml-nasspray-10-ml/',
                     'https://www.aposve.se/product/hydrokortison-evolan-10-mg-g-kram-20-g/']

    fetched_data_34 = nt.farmakeutAB(URLs_34_normi)

    for i in fetched_data_34:
        i.append(pharmacy_url_34)
    medication.extend(fetched_data_34)

    # Apotea AB NOT WORKING / CLOUDFLARE DETECTION
    #
    #pharmacy_url_35 = "apotea.se"
    #URLs_35_selenium = ['https://www.apotea.se/ipren-filmdragerad-tablett-400-mg-30-st',
    #                     'https://www.apotea.se/panodil-tablett-500-mg-20-st',
    #                     'https://www.apotea.se/losec-enterotablett-20-mg-14-tabletter',
    #                     'https://www.apotea.se/voltaren-gel-100-g',
    #                     'https://www.apotea.se/clarityn-tablett-10-mg-30-st',
    #                     'https://www.apotea.se/otrivin-menthol-nasspray-1-mg-per-ml-10-ml',
    #                     'https://www.apotea.se/hydrokortison-evolan-kram-10-mgg-20-g']
    #
    #fetched_data_35 = seltuot.apotea_selenium(URLs_35_selenium)
    #
    #for i in fetched_data_35:
    #    i.append(pharmacy_url_35)
    #medication.extend(fetched_data_35)

    # Admenta Sweden AB
    pharmacy_url_36 = "dozapotek.se"
    URLs_36_selenium = ['https://dozapotek.se/ipren-filmdragerad-tablett-400-mg-30-tablett-er-088534.html',
                        'https://dozapotek.se/panodil-filmdragerad-tablett-500-mg-20-styck-196456.html',
                        'https://dozapotek.se/losec-enterotablett-20-mg-cheplapharm-arzneimittel-gmbh-14-styck-492546.html',
                        'https://dozapotek.se/voltaren-gel-23-2-mg-g-haleon-denmark-aps-100-gram-533022.html',
                        'https://dozapotek.se/clarityn-tablett-10-mg-bayer-ab-30-tablett-er-154158.html',
                        'https://dozapotek.se/otrivin-menthol-utan-konserveringsmedel-nasspray-losning-1-mg-ml-10-milliliter-389805.html',
                        'https://dozapotek.se/hydrokortison-evolan-kram-10-mg-g-20-gram-046776.html']

    fetched_data_36 = seltuot.admenta_selenium(URLs_36_selenium)

    for i in fetched_data_36:
        i.append(pharmacy_url_36)
    medication.extend(fetched_data_36)

    # Meds Apotek AB
    pharmacy_url_37 = "meds.se"
    URLs_37_normi = ['https://www.meds.se/ipren-filmdragerad-tablett-400-mg-30-st',
                     'https://www.meds.se/panodil-filmdragerad-tablett-500-mg-20-st',
                     'https://www.meds.se/losec-enterotablett-20-mg-14-st',
                     'https://www.meds.se/voltaren-gel-23-2-mg-g-100-g',
                     'https://www.meds.se/allergi/allergitabletter/clarityn-10-mg-30-tablett-tablett',
                     'https://www.meds.se/otrivin-menthol-nasspray-losning-1-mg-ml-10-ml',
                     'https://www.meds.se/hydrokortison-evolan-kram-10-mg-g-20-g']

    fetched_data_37 = nt.medsapotekAB(URLs_37_normi)

    for i in fetched_data_37:
        i.append(pharmacy_url_37)
    medication.extend(fetched_data_37)

    # Ditt Apotek Rådhuset NOT WORKING DUE TO BOT CAPTCHA AFTER FIRST LINK REFRESH
    #
    # URLs_38_selenium = ['https://www.foodora.no/en/shop/molh/ditt-apotek-radhuset/search?q=ibux%20tabletter%20400%20mg%2020stk',
    #                     'https://www.foodora.no/en/shop/molh/ditt-apotek-radhuset/search?q=panodil%20500mg%2020stk',
    #                     'https://www.foodora.no/en/shop/molh/ditt-apotek-radhuset/search?q=somac%20control%2014stk',
    #                     'https://www.foodora.no/en/shop/molh/ditt-apotek-radhuset/search?q=zyrtec%2030stk',
    #                     'https://www.foodora.no/en/shop/molh/ditt-apotek-radhuset/search?q=otrivin%20mentol',
    #                     'https://www.foodora.no/en/shop/molh/ditt-apotek-radhuset/search?q=hydrokortison%20evolan']
    #
    # product_ids_38_selenium = ['19132643', '19184416', '19310892', '19184727', '19120848', '19192714']
    #
    # medication.extend(seltuot.foodora_selenium(URLs_38_selenium, product_ids_38_selenium))

    # Vitalis Apotek NOT WORKING DUE TO BOT CAPTCHA AFTER FIRST LINK REFRESH
    #
    # URLs_39_selenium = ['https://www.foodora.no/en/shop/tspc/vitalis-apotek/search?q=ibux%20tabletter%20400%20mg%2020stk',
    #                     'https://www.foodora.no/en/shop/tspc/vitalis-apotek/search?q=panodil',
    #                     'https://www.foodora.no/en/shop/tspc/vitalis-apotek/search?q=somac%20control%2014stk',
    #                     'https://www.foodora.no/en/shop/tspc/vitalis-apotek/search?q=zyrtec%2030stk',
    #                     'https://www.foodora.no/en/shop/tspc/vitalis-apotek/search?q=otrivin%20mentol',
    #                     'https://www.foodora.no/en/shop/tspc/vitalis-apotek/search?q=hydrokortison%2020g']
    #
    # product_ids_39_selenium = ['19178823', '19189034', '19311996', '19178816', '19120867', '19178769']
    #
    # medication.extend(seltuot.foodora_selenium(URLs_39_selenium, product_ids_39_selenium))

    # Sandviken apotek NOT WORKING DUE TO BOT CAPTCHA AFTER FIRST LINK REFRESH
    #
    # URLs_40_selenium = ['https://www.foodora.no/en/shop/d1be/sandviken-apotek/search?q=ibux%20tabletter%20400%20mg%2020stk',
    #                     'https://www.foodora.no/en/shop/d1be/sandviken-apotek/search?q=panodil',
    #                     'https://www.foodora.no/en/shop/d1be/sandviken-apotek/search?q=somac%20control%2014stk',
    #                     'https://www.foodora.no/en/shop/d1be/sandviken-apotek/search?q=voltarol%20forte%20gel%20100g',
    #                     'https://www.foodora.no/en/shop/d1be/sandviken-apotek/search?q=zyrtec%2030stk',
    #                     'https://www.foodora.no/en/shop/d1be/sandviken-apotek/search?q=otrivin%20mentol']
    #
    # product_ids_40_selenium = ['19583893', '18650296', '19583793', '19929112', '19602215', '19568996']
    #
    # medication.extend(seltuot.foodora_selenium(URLs_40_selenium, product_ids_40_selenium))

    # Konnerud apotek (NOT WORKING DUE TO BOT CAPTCHA AFTER FIRST LINK REFRESH) N/A since only one link for now
    #
    # URLs_41_selenium = ['https://www.foodora.no/en/shop/rkdv/ditt-apotek-konnerud/search?q=hydrokortison']
    #
    # product_ids_41_selenium = ['19483143']
    #
    # medication.extend(seltuot.foodora_selenium(URLs_41_selenium, product_ids_41_selenium))

    # Tapiolan apteekki
    pharmacy_url_42 = "tapiolanapteekki.fi"
    URLs_42_normi = ['https://www.tapiolanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.tapiolanapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.tapiolanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.tapiolanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.tapiolanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.tapiolanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.tapiolanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_42 = nt.yliopistonapteekki(URLs_42_normi)

    for i in fetched_data_42:
        i.append(pharmacy_url_42)
    medication.extend(fetched_data_42)

    # Sellon apteekki
    pharmacy_url_43 = "verkkokauppa.sellonapteekki.fi"
    URLs_43_normi = ['https://verkkokauppa.sellonapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://verkkokauppa.sellonapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://verkkokauppa.sellonapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://verkkokauppa.sellonapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://verkkokauppa.sellonapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://verkkokauppa.sellonapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_43 = nt.yliopistonapteekki(URLs_43_normi)

    for i in fetched_data_43:
        i.append(pharmacy_url_43)
    medication.extend(fetched_data_43)

    # Hangon apteekki
    pharmacy_url_44 = "hangonapteekki.fi"
    URLs_44_normi = ['https://hangonapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://hangonapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://hangonapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://hangonapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://hangonapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://hangonapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://hangonapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_44 = nt.yliopistonapteekki(URLs_44_normi)

    for i in fetched_data_44:
        i.append(pharmacy_url_44)
    medication.extend(fetched_data_44)

    # Harjavallan apteekki
    pharmacy_url_45 = "harjavallanapteekki.fi"
    URLs_45_normi = ['https://harjavallanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://harjavallanapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://harjavallanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://harjavallanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://harjavallanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://harjavallanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://harjavallanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_45 = nt.yliopistonapteekki(URLs_45_normi)

    for i in fetched_data_45:
        i.append(pharmacy_url_45)
    medication.extend(fetched_data_45)

    # Hartolan apteekki
    pharmacy_url_46 = "suomalainenverkkoapteekki.fi"
    URLs_46_normi = ['https://suomalainenverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://suomalainenverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://suomalainenverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://suomalainenverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://suomalainenverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://suomalainenverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://suomalainenverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_46 = nt.yliopistonapteekki(URLs_46_normi)

    for i in fetched_data_46:
        i.append(pharmacy_url_46)
    medication.extend(fetched_data_46)

    # Heinolan vanha apteekki
    pharmacy_url_47 = "heinolanvanhaapteekki.fi"
    URLs_47_normi = ['https://www.heinolanvanhaapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.heinolanvanhaapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.heinolanvanhaapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.heinolanvanhaapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.heinolanvanhaapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.heinolanvanhaapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.heinolanvanhaapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_47 = nt.yliopistonapteekki(URLs_47_normi)

    for i in fetched_data_47:
        i.append(pharmacy_url_47)
    medication.extend(fetched_data_47)
    
    # Helsingin kaivopuiston apteekki
    pharmacy_url_48 = "oloapteekki.fi"
    URLs_48_normi = ['https://www.oloapteekki.fi/burana-400-mg-30-fol-tabl-kalvopaall?queryID=0b40b2558c42fa9d2a993a0b5db7c395&objectID=16935&indexName=olo_prod_fi_products',
                     'https://www.oloapteekki.fi/hydrocortison-1-20-g-emuls-voide',
                     'https://www.oloapteekki.fi/otrivin-menthol-sailytysaineeton-1-mg-ml-10-ml-nenasumute-liuos-khone-pumppu',
                     'https://www.oloapteekki.fi/panadol-500-mg-30-fol-tabl-kalvopaall',
                     'https://www.oloapteekki.fi/somac-control-20-mg-14-fol-enterotabl',
                     'https://www.oloapteekki.fi/voltaren-forte-23-2-mg-g-100-g-geeli-3',
                     'https://www.oloapteekki.fi/zyrtec-10-mg-30-fol-tabl-kalvopaall']

    fetched_data_48 = nt.oloapteekki(URLs_48_normi)

    for i in fetched_data_48:
        i.append(pharmacy_url_48)
    medication.extend(fetched_data_48)

    # Ruoholahden ässäapteekki
    pharmacy_url_49 = "wolt.com/fi/fin/helsinki/venue/ruoholahden-ssapteekki"
    URLs_49_selenium = ['https://wolt.com/fi/fin/helsinki/venue/ruoholahden-ssapteekki/burana-400-mg-itemid-6625e6355e428b195c35dd94?search=burana',
                        'https://wolt.com/fi/fin/helsinki/venue/ruoholahden-ssapteekki/hydrocortison-1-itemid-6625e6355e428b195c35dc34?search=hydrocorti',
                        'https://wolt.com/fi/fin/helsinki/venue/ruoholahden-ssapteekki/panadol-500-mg-itemid-6625e6355e428b195c35dd2f?search=panadol',
                        'https://wolt.com/fi/fin/helsinki/venue/ruoholahden-ssapteekki/somac-control-20-mg-itemid-6625e6355e428b195c35dc09?search=somac',
                        'https://wolt.com/fi/fin/helsinki/venue/ruoholahden-ssapteekki/voltaren-forte-23-2-mg-g-itemid-6625e6355e428b195c35dcea?search=voltaren',
                        'https://wolt.com/fi/fin/helsinki/venue/ruoholahden-ssapteekki/zyrtec-10-mg-itemid-6625e6355e428b195c35daf2?search=zyrtec']

    special_link = [0,0,0,0,0,0,0] # 1,2,3... if link needs to be treated separately due to different html structure, 0 otherwise
    fetched_data_49 = seltuot.wolt_selenium(URLs_49_selenium, 'EUR', special_link)

    for i in fetched_data_49:
        i.append(pharmacy_url_49)
    medication.extend(fetched_data_49)

    # Käpylän apteekki
    pharmacy_url_50 = "kapylanapteekki.fi"
    URLs_50_normi = ['https://www.kapylanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kapylanapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.kapylanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.kapylanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kapylanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.kapylanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.kapylanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_50 = nt.yliopistonapteekki(URLs_50_normi)

    for i in fetched_data_50:
        i.append(pharmacy_url_50)
    medication.extend(fetched_data_50)

    # Lauttasaaren keskusapteekki
    pharmacy_url_51 = "e-apteekkari.fi"
    URLs_51_normi = ['https://www.e-apteekkari.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.e-apteekkari.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.e-apteekkari.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.e-apteekkari.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.e-apteekkari.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.e-apteekkari.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.e-apteekkari.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_51 = nt.yliopistonapteekki(URLs_51_normi)

    for i in fetched_data_51:
        i.append(pharmacy_url_51)
    medication.extend(fetched_data_51)

    # Munkkiniemen apteekki
    pharmacy_url_52 = "munkkiniemenapteekki.fi"
    URLs_52_normi = ['https://www.munkkiniemenapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.munkkiniemenapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.munkkiniemenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.munkkiniemenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.munkkiniemenapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.munkkiniemenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.munkkiniemenapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_52 = nt.yliopistonapteekki(URLs_52_normi)

    for i in fetched_data_52:
        i.append(pharmacy_url_52)
    medication.extend(fetched_data_52)

    # Herttoniemen apteekki
    pharmacy_url_53 = "herttoniemenapteekki.fi"
    URLs_53_normi = ['https://www.herttoniemenapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.herttoniemenapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.herttoniemenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.herttoniemenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.herttoniemenapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.herttoniemenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.herttoniemenapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_53 = nt.yliopistonapteekki(URLs_53_normi)

    for i in fetched_data_53:
        i.append(pharmacy_url_53)
    medication.extend(fetched_data_53)
    
    # Erottajan apteekki
    pharmacy_url_54 = "wolt.com/fi/fin/helsinki/venue/erottajan-apteekki"
    URLs_54_selenium = ['https://wolt.com/fi/fin/helsinki/venue/erottajan-apteekki/burana-400-mg-itemid-6625fe054240d60cdca26fe7?search=burana',
                        'https://wolt.com/fi/fin/helsinki/venue/erottajan-apteekki/hydrocortison-1-itemid-6625fe054240d60cdca26e87?search=hydrocortison',
                        'https://wolt.com/fi/fin/helsinki/venue/erottajan-apteekki/panadol-500-mg-itemid-6625fe054240d60cdca26f82?search=panadol',
                        'https://wolt.com/fi/fin/helsinki/venue/erottajan-apteekki/somac-control-20-mg-itemid-6625fe054240d60cdca26e5c?search=somac',
                        'https://wolt.com/fi/fin/helsinki/venue/erottajan-apteekki/voltaren-forte-23-2-mg-g-itemid-6625fe054240d60cdca26f3d?search=voltaren',
                        'https://wolt.com/fi/fin/helsinki/venue/erottajan-apteekki/zyrtec-10-mg-itemid-6625fe054240d60cdca26d45?search=zyrtec']

    special_link = [0,0,0,0,0,0,0] # 1,2,3... if link needs to be treated separately due to different html structure, 0 otherwise
    fetched_data_54 = seltuot.wolt_selenium(URLs_54_selenium, 'EUR', special_link)

    for i in fetched_data_54:
        i.append(pharmacy_url_54)
    medication.extend(fetched_data_54)

    # Kaaren apteekki
    pharmacy_url_55 = "wolt.com/fi/fin/helsinki/venue/kaaren-apteekki"
    URLs_55_selenium = ['https://wolt.com/fi/fin/helsinki/venue/kaaren-apteekki/burana-400-mg-itemid-6625f152763afb5a93bba0f9?search=burana',
                        'https://wolt.com/fi/fin/helsinki/venue/kaaren-apteekki/hydrocortison-1-itemid-6625f152763afb5a93bb9f99?search=hydrocortison',
                        'https://wolt.com/fi/fin/helsinki/venue/kaaren-apteekki/panadol-500-mg-itemid-6625f152763afb5a93bba094?search=panadol']

    special_link = [0,0,0,0,0,0,0] # 1,2,3... if link needs to be treated separately due to different html structure, 0 otherwise
    fetched_data_55 = seltuot.wolt_selenium(URLs_55_selenium, 'EUR', special_link)

    for i in fetched_data_55:
        i.append(pharmacy_url_55)
    medication.extend(fetched_data_55)
    
    # Hertsin apteekki
    pharmacy_url_56 = "hertsinapteekki.fi"
    URLs_56_normi = ['https://hertsinapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://hertsinapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://hertsinapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://hertsinapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://hertsinapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://hertsinapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://hertsinapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_56 = nt.yliopistonapteekki(URLs_56_normi)

    for i in fetched_data_56:
        i.append(pharmacy_url_56)
    medication.extend(fetched_data_56)

    # Vuosaaren apteekki
    pharmacy_url_57 = "vuosaarenapteekki.fi"
    URLs_57_normi = ['https://vuosaarenapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://vuosaarenapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://vuosaarenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://vuosaarenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://vuosaarenapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://vuosaarenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://vuosaarenapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_57 = nt.yliopistonapteekki(URLs_57_normi)

    for i in fetched_data_57:
        i.append(pharmacy_url_57)
    medication.extend(fetched_data_57)

    # Jakomäen apteeekki
    pharmacy_url_58 = "jakomaenapteekki.fi"
    URLs_58_normi = ['https://jakomaenapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://jakomaenapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://jakomaenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://jakomaenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://jakomaenapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://jakomaenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://jakomaenapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_58 = nt.yliopistonapteekki(URLs_58_normi)

    for i in fetched_data_58:
        i.append(pharmacy_url_58)
    medication.extend(fetched_data_58)

    # Laajasalon apteekki
    pharmacy_url_59 = "laajasalonapteekki.fi"
    URLs_59_normi = ['https://laajasalonapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://laajasalonapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://laajasalonapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://laajasalonapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://laajasalonapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://laajasalonapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://laajasalonapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_59 = nt.yliopistonapteekki(URLs_59_normi)

    for i in fetched_data_59:
        i.append(pharmacy_url_59)
    medication.extend(fetched_data_59)

    # Pasilan apteekki
    pharmacy_url_60 = "pasilanapteekinverkkokauppa.fi"
    URLs_60_normi = ['https://www.pasilanapteekinverkkokauppa.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.pasilanapteekinverkkokauppa.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.pasilanapteekinverkkokauppa.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.pasilanapteekinverkkokauppa.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.pasilanapteekinverkkokauppa.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.pasilanapteekinverkkokauppa.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.pasilanapteekinverkkokauppa.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_60 = nt.yliopistonapteekki(URLs_60_normi)

    for i in fetched_data_60:
        i.append(pharmacy_url_60)
    medication.extend(fetched_data_60)
    
    # Kaartin apteekki
    pharmacy_url_61 = "wolt.com/fi/fin/helsinki/venue/kaartin-apteekki"
    URLs_61_selenium = ['https://wolt.com/fi/fin/helsinki/venue/kaartin-apteekki/burana-400-mg-itemid-662766bda6c9a3a2e16b37d1?search=burana',
                        'https://wolt.com/fi/fin/helsinki/venue/kaartin-apteekki/hydrocortison-1-itemid-662766bda6c9a3a2e16b3660?search=hydrocortison',
                        'https://wolt.com/fi/fin/helsinki/venue/kaartin-apteekki/panadol-500-mg-itemid-662766bda6c9a3a2e16b3733?search=panadol',
                        'https://wolt.com/fi/fin/helsinki/venue/kaartin-apteekki/somac-control-20-mg-itemid-662766bda6c9a3a2e16b365f?search=somac',
                        'https://wolt.com/fi/fin/helsinki/venue/kaartin-apteekki/voltaren-forte-23-2-mg-g-itemid-662766bda6c9a3a2e16b3761?search=voltaren',
                        'https://wolt.com/fi/fin/helsinki/venue/kaartin-apteekki/zyrtec-10-mg-itemid-662766bda6c9a3a2e16b3524?search=zyrtec']

    special_link = [0,0,0,0,0,0,0] # 1,2,3... if link needs to be treated separately due to different html structure, 0 otherwise
    fetched_data_61 = seltuot.wolt_selenium(URLs_61_selenium, 'EUR', special_link)

    for i in fetched_data_61:
        i.append(pharmacy_url_61)
    medication.extend(fetched_data_61)
    
    # Hollolan apteekki
    pharmacy_url_62 = "hollolanapteekki.fi"
    URLs_62_normi = ['https://hollolanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://hollolanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://hollolanapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://hollolanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://hollolanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://hollolanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://hollolanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_62 = nt.yliopistonapteekki(URLs_62_normi)

    for i in fetched_data_62:
        i.append(pharmacy_url_62)
    medication.extend(fetched_data_62)

    # Vehkojan apteekki
    pharmacy_url_63 = "vehkojanverkkoapteekki.fi"
    URLs_63_normi = ['https://www.vehkojanverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.vehkojanverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.vehkojanverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.vehkojanverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.vehkojanverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.vehkojanverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.vehkojanverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_63 = nt.yliopistonapteekki(URLs_63_normi)

    for i in fetched_data_63:
        i.append(pharmacy_url_63)
    medication.extend(fetched_data_63)

    # Tiiriön apteekki
    pharmacy_url_64 = "tiirionapteekki.fi"
    URLs_64_normi = ['https://www.tiirionapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.tiirionapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.tiirionapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.tiirionapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.tiirionapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.tiirionapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.tiirionapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_64 = nt.yliopistonapteekki(URLs_64_normi)

    for i in fetched_data_64:
        i.append(pharmacy_url_64)
    medication.extend(fetched_data_64)

    # Iisalmen ykkösapteekki
    pharmacy_url_65 = "iisalmenapteekki.fi"
    URLs_65_normi = ['https://www.iisalmenapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.iisalmenapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.iisalmenapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.iisalmenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.iisalmenapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.iisalmenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_65 = nt.yliopistonapteekki(URLs_65_normi)

    for i in fetched_data_65:
        i.append(pharmacy_url_65)
    medication.extend(fetched_data_65)

    # Ilmajoen apteekki
    pharmacy_url_66 = "ilmajoenverkkoapteekki.fi"
    URLs_66_normi = ['https://www.ilmajoenverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.ilmajoenverkkoapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.ilmajoenverkkoapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.ilmajoenverkkoapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.ilmajoenverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.ilmajoenverkkoapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.ilmajoenverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_66 = nt.yliopistonapteekki(URLs_66_normi)

    for i in fetched_data_66:
        i.append(pharmacy_url_66)
    medication.extend(fetched_data_66)

    # Apteekki Imatra
    pharmacy_url_67 = "saimaanverkkoapteekki.fi"
    URLs_67_normi = ['https://saimaanverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://saimaanverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://saimaanverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://saimaanverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://saimaanverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://saimaanverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://saimaanverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_67 = nt.yliopistonapteekki(URLs_67_normi)

    for i in fetched_data_67:
        i.append(pharmacy_url_67)
    medication.extend(fetched_data_67)

    # Joensuun uusi apteekki
    pharmacy_url_68 = "uusiverkkoapteekki.fi"
    URLs_68_normi = ['https://uusiverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://uusiverkkoapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://uusiverkkoapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://uusiverkkoapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://uusiverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://uusiverkkoapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://uusiverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_68 = nt.yliopistonapteekki(URLs_68_normi)

    for i in fetched_data_68:
        i.append(pharmacy_url_68)
    medication.extend(fetched_data_68)

    # Juuan apteekki
    pharmacy_url_69 = "juuanapteekki.fi"
    URLs_69_normi = ['https://juuanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://juuanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://juuanapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://juuanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://juuanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://juuanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://juuanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_69 = nt.yliopistonapteekki(URLs_69_normi)

    for i in fetched_data_69:
        i.append(pharmacy_url_69)
    medication.extend(fetched_data_69)

    # Tikkakosken apteekki
    pharmacy_url_70 = "tikkakoskenapteekki.fi"
    URLs_70_normi = ['https://www.tikkakoskenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.tikkakoskenapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.tikkakoskenapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.tikkakoskenapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.tikkakoskenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.tikkakoskenapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.tikkakoskenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_70 = nt.yliopistonapteekki(URLs_70_normi)

    for i in fetched_data_70:
        i.append(pharmacy_url_70)
    medication.extend(fetched_data_70)

    # Korpilahden apteekki
    pharmacy_url_71 = "korpilahdenverkkoapteekki.fi"
    URLs_71_normi = ['https://www.korpilahdenverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.korpilahdenverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.korpilahdenverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.korpilahdenverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.korpilahdenverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.korpilahdenverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.korpilahdenverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_71 = nt.yliopistonapteekki(URLs_71_normi)

    for i in fetched_data_71:
        i.append(pharmacy_url_71)
    medication.extend(fetched_data_71)

    # Jyväskylän uusi apteekki
    pharmacy_url_72 = "uusiapteekkiverkossa.fi"
    URLs_72_normi = ['https://www.uusiapteekkiverkossa.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.uusiapteekkiverkossa.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.uusiapteekkiverkossa.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.uusiapteekkiverkossa.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.uusiapteekkiverkossa.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.uusiapteekkiverkossa.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.uusiapteekkiverkossa.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_72 = nt.yliopistonapteekki(URLs_72_normi)

    for i in fetched_data_72:
        i.append(pharmacy_url_72)
    medication.extend(fetched_data_72)

    # Sonaatti apteekki
    pharmacy_url_73 = "netti-apteekki.fi"
    URLs_73_normi = ['https://www.netti-apteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.netti-apteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.netti-apteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.netti-apteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.netti-apteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.netti-apteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.netti-apteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_73 = nt.yliopistonapteekki(URLs_73_normi)

    for i in fetched_data_73:
        i.append(pharmacy_url_73)
    medication.extend(fetched_data_73)

    # Veturi apteekki
    pharmacy_url_74 = "veturiapteekki.fi"
    URLs_74_normi = ['https://www.veturiapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.veturiapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.veturiapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.veturiapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.veturiapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.veturiapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.veturiapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_74 = nt.yliopistonapteekki(URLs_74_normi)

    for i in fetched_data_74:
        i.append(pharmacy_url_74)
    medication.extend(fetched_data_74)

    # Suoraman apteekki
    pharmacy_url_75 = "suoramanapteekki.fi"
    URLs_75_normi = ['https://www.suoramanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.suoramanapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.suoramanapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.suoramanapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.suoramanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.suoramanapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.suoramanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_75 = nt.yliopistonapteekki(URLs_75_normi)

    for i in fetched_data_75:
        i.append(pharmacy_url_75)
    medication.extend(fetched_data_75)

    # Keskusapteekki
    pharmacy_url_76 = "kankaanpaankeskusapteekki.fi"
    URLs_76_normi = ['https://www.kankaanpaankeskusapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kankaanpaankeskusapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kankaanpaankeskusapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.kankaanpaankeskusapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.kankaanpaankeskusapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.kankaanpaankeskusapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kankaanpaankeskusapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_76 = nt.yliopistonapteekki(URLs_76_normi)

    for i in fetched_data_76:
        i.append(pharmacy_url_76)
    medication.extend(fetched_data_76)

    # Kauniaisten apteekki
    pharmacy_url_77 = "kauniaistenapteekki.fi"
    URLs_77_normi = ['https://kauniaistenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://kauniaistenapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://kauniaistenapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                     'https://kauniaistenapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://kauniaistenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://kauniaistenapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://kauniaistenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_77 = nt.yliopistonapteekki(URLs_77_normi)

    for i in fetched_data_77:
        i.append(pharmacy_url_77)
    medication.extend(fetched_data_77)

    # Kaustisen apteekki
    pharmacy_url_78 = "kaustisenapteekki.fi"
    URLs_78_normi = ['https://www.kaustisenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kaustisenapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kaustisenapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://www.kaustisenapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.kaustisenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.kaustisenapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kaustisenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_78 = nt.yliopistonapteekki(URLs_78_normi)

    for i in fetched_data_78:
        i.append(pharmacy_url_78)
    medication.extend(fetched_data_78)

    # Kimito apotek
    pharmacy_url_79 = "kimitoapotek.fi"
    URLs_79_normi = ['https://kimitoapotek.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://kimitoapotek.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://kimitoapotek.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                     'https://kimitoapotek.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://kimitoapotek.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://kimitoapotek.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://kimitoapotek.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_79 = nt.yliopistonapteekki(URLs_79_normi)

    for i in fetched_data_79:
        i.append(pharmacy_url_79)
    medication.extend(fetched_data_79)

    # Zeppelinin apteekki
    pharmacy_url_80 = "zeppelininapteekki.fi"
    URLs_80_normi = ['https://www.zeppelininapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.zeppelininapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.zeppelininapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.zeppelininapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.zeppelininapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.zeppelininapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.zeppelininapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_80 = nt.yliopistonapteekki(URLs_80_normi)

    for i in fetched_data_80:
        i.append(pharmacy_url_80)
    medication.extend(fetched_data_80)

    # Kiteen 1. apteekki
    pharmacy_url_81 = "kiteenverkkoapteekki.fi"
    URLs_81_normi = ['https://www.kiteenverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.kiteenverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kiteenverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kiteenverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.kiteenverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kiteenverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.kiteenverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_81 = nt.yliopistonapteekki(URLs_81_normi)

    for i in fetched_data_81:
        i.append(pharmacy_url_81)
    medication.extend(fetched_data_81)

    # Kokemäen apteekki
    pharmacy_url_82 = "kokemaenapteekki.fi"
    URLs_82_normi = ['https://kokemaenapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://kokemaenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://kokemaenapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://kokemaenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://kokemaenapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://kokemaenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://kokemaenapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_82 = nt.yliopistonapteekki(URLs_82_normi)

    for i in fetched_data_82:
        i.append(pharmacy_url_82)
    medication.extend(fetched_data_82)

    # Tervahovin apteekki
    pharmacy_url_83 = "kauppa.tervahovinapteekki.fi"
    URLs_83_normi = ['https://kauppa.tervahovinapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://kauppa.tervahovinapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://kauppa.tervahovinapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://kauppa.tervahovinapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://kauppa.tervahovinapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://kauppa.tervahovinapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://kauppa.tervahovinapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_83 = nt.yliopistonapteekki(URLs_83_normi)

    for i in fetched_data_83:
        i.append(pharmacy_url_83)
    medication.extend(fetched_data_83)

    # Kälviän apteekki
    pharmacy_url_84 = "kalvianverkkoapteekki.fi"
    URLs_84_normi = ['https://www.kalvianverkkoapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.kalvianverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kalvianverkkoapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kalvianverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.kalvianverkkoapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kalvianverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.kalvianverkkoapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_84 = nt.yliopistonapteekki(URLs_84_normi)

    for i in fetched_data_84:
        i.append(pharmacy_url_84)
    medication.extend(fetched_data_84)

    # Valtarin apteekki
    pharmacy_url_85 = "kouvolanverkkoapteekki.fi"
    URLs_85_normi = ['https://kouvolanverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://kouvolanverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://kouvolanverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://kouvolanverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://kouvolanverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://kouvolanverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://kouvolanverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_85 = nt.yliopistonapteekki(URLs_85_normi)

    for i in fetched_data_85:
        i.append(pharmacy_url_85)
    medication.extend(fetched_data_85)

    # Tornionmäen apteekki
    pharmacy_url_86 = "tornionmaenverkkoapteekki.fi"
    URLs_86_normi = ['https://tornionmaenverkkoapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://tornionmaenverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://tornionmaenverkkoapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://tornionmaenverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://tornionmaenverkkoapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://tornionmaenverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://tornionmaenverkkoapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_86 = nt.yliopistonapteekki(URLs_86_normi)

    for i in fetched_data_86:
        i.append(pharmacy_url_86)
    medication.extend(fetched_data_86)

    # Kauppakeskus Veturin apteekki
    pharmacy_url_87 = "apteekkikulma.fi"
    URLs_87_normi = ['https://www.apteekkikulma.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.apteekkikulma.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.apteekkikulma.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.apteekkikulma.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.apteekkikulma.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.apteekkikulma.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.apteekkikulma.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_87 = nt.yliopistonapteekki(URLs_87_normi)

    for i in fetched_data_87:
        i.append(pharmacy_url_87)
    medication.extend(fetched_data_87)

    # Juankosken apteekki
    pharmacy_url_88 = "juankoskenapteekki.fi"
    URLs_88_normi = ['https://juankoskenapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://juankoskenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://juankoskenapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://juankoskenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://juankoskenapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://juankoskenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://juankoskenapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_88 = nt.yliopistonapteekki(URLs_88_normi)

    for i in fetched_data_88:
        i.append(pharmacy_url_88)
    medication.extend(fetched_data_88)

    # Kupion uusi apteekki
    pharmacy_url_89 = "kuopionuusiverkkoapteekki.fi"
    URLs_89_normi = ['https://www.kuopionuusiverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.kuopionuusiverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kuopionuusiverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kuopionuusiverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.kuopionuusiverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.kuopionuusiverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.kuopionuusiverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_89 = nt.yliopistonapteekki(URLs_89_normi)

    for i in fetched_data_89:
        i.append(pharmacy_url_89)
    medication.extend(fetched_data_89)

    # Petosen apteekki
    pharmacy_url_90 = "apteekkinettikauppa.fi"
    URLs_90_normi = ['https://www.apteekkinettikauppa.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.apteekkinettikauppa.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.apteekkinettikauppa.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.apteekkinettikauppa.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.apteekkinettikauppa.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.apteekkinettikauppa.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.apteekkinettikauppa.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_90 = nt.yliopistonapteekki(URLs_90_normi)

    for i in fetched_data_90:
        i.append(pharmacy_url_90)
    medication.extend(fetched_data_90)

    # Kuusamon 1. apteekki
    pharmacy_url_91 = "kuusamon1apteekki.fi"
    URLs_91_normi = ['https://kuusamon1apteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://kuusamon1apteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://kuusamon1apteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://kuusamon1apteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://kuusamon1apteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://kuusamon1apteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_91 = nt.yliopistonapteekki(URLs_91_normi)

    for i in fetched_data_91:
        i.append(pharmacy_url_91)
    medication.extend(fetched_data_91)

    # Apteekki trio
    pharmacy_url_92 = "verkkoapteekkitrio.fi"
    URLs_92_normi = ['https://verkkoapteekkitrio.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://verkkoapteekkitrio.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://verkkoapteekkitrio.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://verkkoapteekkitrio.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://verkkoapteekkitrio.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://verkkoapteekkitrio.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://verkkoapteekkitrio.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_92 = nt.yliopistonapteekki(URLs_92_normi)

    for i in fetched_data_92:
        i.append(pharmacy_url_92)
    medication.extend(fetched_data_92)

    # Ykkösapteekki
    pharmacy_url_93 = "ykkosverkkoapteekki.fi"
    URLs_93_normi = ['https://www.ykkosverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.ykkosverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.ykkosverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.ykkosverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.ykkosverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html']

    fetched_data_93 = nt.yliopistonapteekki(URLs_93_normi)

    for i in fetched_data_93:
        i.append(pharmacy_url_93)
    medication.extend(fetched_data_93)

    # Apteekki saimaa
    pharmacy_url_94 = "nettiapteekkisaimaa.fi"
    URLs_94_normi = ['https://nettiapteekkisaimaa.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://nettiapteekkisaimaa.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://nettiapteekkisaimaa.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://nettiapteekkisaimaa.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://nettiapteekkisaimaa.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://nettiapteekkisaimaa.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://nettiapteekkisaimaa.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_94 = nt.yliopistonapteekki(URLs_94_normi)

    for i in fetched_data_94:
        i.append(pharmacy_url_94)
    medication.extend(fetched_data_94)

    # Lauritsalan apteekki
    pharmacy_url_95 = "apotekasaimaa.fi"
    URLs_95_normi = ['https://apotekasaimaa.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://apotekasaimaa.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://apotekasaimaa.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://apotekasaimaa.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://apotekasaimaa.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://apotekasaimaa.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://apotekasaimaa.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_95 = nt.yliopistonapteekki(URLs_95_normi)

    for i in fetched_data_95:
        i.append(pharmacy_url_95)
    medication.extend(fetched_data_95)

    # Lapuan 2. apteekki (Keskusapteekki)
    pharmacy_url_96 = "lapuanapteekki.fi"
    URLs_96_normi = ['https://verkkokauppa.lapuanapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://verkkokauppa.lapuanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://verkkokauppa.lapuanapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://verkkokauppa.lapuanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://verkkokauppa.lapuanapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://verkkokauppa.lapuanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://verkkokauppa.lapuanapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_96 = nt.yliopistonapteekki(URLs_96_normi)

    for i in fetched_data_96:
        i.append(pharmacy_url_96)
    medication.extend(fetched_data_96)

    # Liedon apteekki
    pharmacy_url_97 = "liedonverkkoapteekki.fi"
    URLs_97_normi = ['https://liedonverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://liedonverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://liedonverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://liedonverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://liedonverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://liedonverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://liedonverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_97 = nt.yliopistonapteekki(URLs_97_normi)

    for i in fetched_data_97:
        i.append(pharmacy_url_97)
    medication.extend(fetched_data_97)

    # Pielis apteekki
    pharmacy_url_98 = "pielisapteekki.fi"
    URLs_98_normi = ['https://www.pielisapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.pielisapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.pielisapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.pielisapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.pielisapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.pielisapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.pielisapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_98 = nt.yliopistonapteekki(URLs_98_normi)

    for i in fetched_data_98:
        i.append(pharmacy_url_98)
    medication.extend(fetched_data_98)

    # Ylämyllyn apteekki
    pharmacy_url_99 = "ylamyllynverkkoapteekki.fi"
    URLs_99_normi = ['https://www.ylamyllynverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                     'https://www.ylamyllynverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                     'https://www.ylamyllynverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.ylamyllynverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                     'https://www.ylamyllynverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                     'https://www.ylamyllynverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_99 = nt.yliopistonapteekki(URLs_99_normi)

    for i in fetched_data_99:
        i.append(pharmacy_url_99)
    medication.extend(fetched_data_99)
    
    # Lohjan onni apteekki
    pharmacy_url_100 = "wolt.com/fi/fin/lohja/venue/lohjan-onni-apteekki"
    URLs_100_selenium = ['https://wolt.com/fi/fin/lohja/venue/lohjan-onni-apteekki/voltaren-forte-23-2-mg-g-itemid-66289c2eb56ba77203d55c44?search=voltaren',
                         'https://wolt.com/fi/fin/lohja/venue/lohjan-onni-apteekki/somac-control-20-mg-itemid-66289c2eb56ba77203d55b42?search=somac',
                         'https://wolt.com/fi/fin/lohja/venue/lohjan-onni-apteekki/panadol-500-mg-itemid-66289c2eb56ba77203d55c16?search=panadol',
                         'https://wolt.com/fi/fin/lohja/venue/lohjan-onni-apteekki/zyrtec-10-mg-itemid-66289c2eb56ba77203d55a07?search=zyrtec',
                         'https://wolt.com/fi/fin/lohja/venue/lohjan-onni-apteekki/otrivin-menthol-sailytysaineeton-1-mg-ml-itemid-67039dcb97cad016388bf520?search=otrivin',
                         'https://wolt.com/fi/fin/lohja/venue/lohjan-onni-apteekki/hydrocortison-1-itemid-66289c2eb56ba77203d55b43?search=hydrocortison',
                         'https://wolt.com/fi/fin/lohja/venue/lohjan-onni-apteekki/burana-400-mg-itemid-66289c2eb56ba77203d55cb4?search=burana']

    special_link = [0,0,0,0,1,0,0] # 1,2,3... if link needs to be treated separately due to different html structure, 0 otherwise
    fetched_data_100 = seltuot.wolt_selenium(URLs_100_selenium, 'EUR', special_link)

    for i in fetched_data_100:
        i.append(pharmacy_url_100)
    medication.extend(fetched_data_100)
    
    # Ensimmäinen apteekki
    pharmacy_url_101 = "apoteket.ax"
    URLs_101_normi = ['https://www.apoteket.ax/se/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.apoteket.ax/se/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.apoteket.ax/se/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apoteket.ax/se/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apoteket.ax/se/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.apoteket.ax/se/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.apoteket.ax/se/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_101 = nt.yliopistonapteekki(URLs_101_normi)

    for i in fetched_data_101:
        i.append(pharmacy_url_101)
    medication.extend(fetched_data_101)
    
    # Maarianhaminan 2. apteekki (keskusapteekki)
    pharmacy_url_102 = "central-apoteket.ax"
    URLs_102_normi = ['https://www.central-apoteket.ax/se/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.central-apoteket.ax/se/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.central-apoteket.ax/se/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.central-apoteket.ax/se/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html            ',
                      'https://www.central-apoteket.ax/se/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.central-apoteket.ax/se/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.central-apoteket.ax/se/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_102 = nt.yliopistonapteekki(URLs_102_normi)

    for i in fetched_data_102:
        i.append(pharmacy_url_102)
    medication.extend(fetched_data_102)

    # Maskun apteekki
    pharmacy_url_103 = "maskunapteekki.fi"
    URLs_103_normi = ['https://www.maskunapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.maskunapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.maskunapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.maskunapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.maskunapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.maskunapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.maskunapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_103 = nt.yliopistonapteekki(URLs_103_normi)

    for i in fetched_data_103:
        i.append(pharmacy_url_103)
    medication.extend(fetched_data_103)

    # Mikkelin 1. apteekki
    pharmacy_url_104 = "mikkelinapteekki.fi"
    URLs_104_normi = ['https://mikkelinapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://mikkelinapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://mikkelinapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://mikkelinapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://mikkelinapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://mikkelinapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_104 = nt.yliopistonapteekki(URLs_104_normi)

    for i in fetched_data_104:
        i.append(pharmacy_url_104)
    medication.extend(fetched_data_104)

    # Muhoksen apteekki
    pharmacy_url_105 = "muhoksenapteekki.fi"
    URLs_105_normi = ['https://muhoksenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://muhoksenapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://muhoksenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://muhoksenapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://muhoksenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://muhoksenapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://muhoksenapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_105 = nt.yliopistonapteekki(URLs_105_normi)

    for i in fetched_data_105:
        i.append(pharmacy_url_105)
    medication.extend(fetched_data_105)

    # Mäntsälän ykkösapteekki
    pharmacy_url_106 = "mantsalanykkosapteekki.fi"
    URLs_106_normi = ['https://www.mantsalanykkosapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.mantsalanykkosapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.mantsalanykkosapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.mantsalanykkosapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.mantsalanykkosapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.mantsalanykkosapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.mantsalanykkosapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_106 = nt.yliopistonapteekki(URLs_106_normi)

    for i in fetched_data_106:
        i.append(pharmacy_url_106)
    medication.extend(fetched_data_106)

    # Apteekkisydän
    pharmacy_url_107 = "apteekkisydan.fi"
    URLs_107_normi = ['https://www.apteekkisydan.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.apteekkisydan.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.apteekkisydan.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkisydan.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkisydan.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.apteekkisydan.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.apteekkisydan.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_107 = nt.yliopistonapteekki(URLs_107_normi)

    for i in fetched_data_107:
        i.append(pharmacy_url_107)
    medication.extend(fetched_data_107)

    # Nokian 1. apteekki
    pharmacy_url_108 = "oma-apteekki.fi"
    URLs_108_normi = ['https://www.oma-apteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.oma-apteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.oma-apteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.oma-apteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.oma-apteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.oma-apteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.oma-apteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_108 = nt.yliopistonapteekki(URLs_108_normi)

    for i in fetched_data_108:
        i.append(pharmacy_url_108)
    medication.extend(fetched_data_108)

    # Koskenmäen apteekki
    pharmacy_url_109 = "koskenmaenapteekki.fi"
    URLs_109_normi = ['https://www.koskenmaenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.koskenmaenapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.koskenmaenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.koskenmaenapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.koskenmaenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.koskenmaenapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.koskenmaenapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_109 = nt.yliopistonapteekki(URLs_109_normi)

    for i in fetched_data_109:
        i.append(pharmacy_url_109)
    medication.extend(fetched_data_109)

    # Klaukkalan uusi apteekki
    pharmacy_url_110 = "klaukkalanuusiapteekki.fi"
    URLs_110_normi = ['https://klaukkalanuusiapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://klaukkalanuusiapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://klaukkalanuusiapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://klaukkalanuusiapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://klaukkalanuusiapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://klaukkalanuusiapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://klaukkalanuusiapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_110 = nt.yliopistonapteekki(URLs_110_normi)

    for i in fetched_data_110:
        i.append(pharmacy_url_110)
    medication.extend(fetched_data_110)

    # Oriveden apteekki
    pharmacy_url_111 = "orimattilanapteekki.fi"
    URLs_111_normi = ['https://www.oriapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.oriapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.oriapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.oriapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.oriapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.oriapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.oriapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_111 = nt.yliopistonapteekki(URLs_111_normi)

    for i in fetched_data_111:
        i.append(pharmacy_url_111)
    medication.extend(fetched_data_111)

    # Kiimingin apteekki
    pharmacy_url_112 = "arkiapteekki.fi"
    URLs_112_normi = ['https://arkiapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://arkiapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://arkiapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://arkiapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://arkiapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://arkiapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://arkiapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_112 = nt.yliopistonapteekki(URLs_112_normi)

    for i in fetched_data_112:
        i.append(pharmacy_url_112)
    medication.extend(fetched_data_112)

    # Oulunsalon apteekki
    pharmacy_url_113 = "oulunsalonverkkoapteekki.fi"
    URLs_113_normi = ['https://www.oulunsalonverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.oulunsalonverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.oulunsalonverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.oulunsalonverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.oulunsalonverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.oulunsalonverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.oulunsalonverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_113 = nt.yliopistonapteekki(URLs_113_normi)

    for i in fetched_data_113:
        i.append(pharmacy_url_113)
    medication.extend(fetched_data_113)

    # Rotuaarin apteekki
    pharmacy_url_114 = "rotuaarinverkkoapteekki.fi"
    URLs_114_normi = ['https://rotuaarinverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://rotuaarinverkkoapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://rotuaarinverkkoapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://rotuaarinverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://rotuaarinverkkoapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://rotuaarinverkkoapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_114 = nt.yliopistonapteekki(URLs_114_normi)

    for i in fetched_data_114:
        i.append(pharmacy_url_114)
    medication.extend(fetched_data_114)

    # Oulun keskus apteekki
    pharmacy_url_115 = "oulunverkkoapteekki.fi"
    URLs_115_normi = ['https://www.oulunverkkoapteekki.fi/voltaren-forte-geeli-23-2-mg-g-100-g.html',
                      'https://www.oulunverkkoapteekki.fi/somac-control-enterotabletti-20-mg-14-fol.html',
                      'https://www.oulunverkkoapteekki.fi/panadol-tabletti-kalvopaallysteinen-500-mg-30-fol.html',
                      'https://www.oulunverkkoapteekki.fi/zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol.html',
                      'https://www.oulunverkkoapteekki.fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.oulunverkkoapteekki.fi/hydrocortison-emulsiovoide-1-20-g.html',
                      'https://www.oulunverkkoapteekki.fi/burana-tabletti-kalvopaallysteinen-400-mg-30-fol.html']

    fetched_data_115 = nt.yliopistonapteekki(URLs_115_normi)

    for i in fetched_data_115:
        i.append(pharmacy_url_115)
    medication.extend(fetched_data_115)

    # Pateniemen apteekki
    pharmacy_url_116 = "pateniemenverkkoapteekki.fi"
    URLs_116_normi = ['https://pateniemenverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://pateniemenverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://pateniemenverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://pateniemenverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://pateniemenverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://pateniemenverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_116 = nt.yliopistonapteekki(URLs_116_normi)

    for i in fetched_data_116:
        i.append(pharmacy_url_116)
    medication.extend(fetched_data_116)

    # Ruskon apteekki
    pharmacy_url_117 = "ruskonapteekki.fi"
    URLs_117_normi = ['https://www.ruskonapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.ruskonapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.ruskonapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.ruskonapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.ruskonapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.ruskonapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.ruskonapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_117 = nt.yliopistonapteekki(URLs_117_normi)

    for i in fetched_data_117:
        i.append(pharmacy_url_117)
    medication.extend(fetched_data_117)

    # Outokummun apteekki
    pharmacy_url_118 = "siunapteekki.fi"
    URLs_118_normi = ['https://www.siunapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.siunapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.siunapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.siunapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.siunapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.siunapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.siunapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_118 = nt.yliopistonapteekki(URLs_118_normi)

    for i in fetched_data_118:
        i.append(pharmacy_url_118)
    medication.extend(fetched_data_118)

    # Pellon apteekki
    pharmacy_url_119 = "meänapteekki.fi"
    URLs_119_normi = ['https://www.meanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.meanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.meanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.meanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.meanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.meanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_119 = nt.yliopistonapteekki(URLs_119_normi)

    for i in fetched_data_119:
        i.append(pharmacy_url_119)
    medication.extend(fetched_data_119)

    # Pielaveden apteekki
    pharmacy_url_120 = "savonverkkoapteekki.fi"
    URLs_120_normi = ['https://savonverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://savonverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://savonverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://savonverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://savonverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://savonverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://savonverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_120 = nt.yliopistonapteekki(URLs_120_normi)

    for i in fetched_data_120:
        i.append(pharmacy_url_120)
    medication.extend(fetched_data_120)

    # Medi-apteekki
    pharmacy_url_121 = "mediapteekki.fi"
    URLs_121_normi = ['https://mediapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://mediapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://mediapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://mediapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://mediapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://mediapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html']

    fetched_data_121 = nt.yliopistonapteekki(URLs_121_normi)

    for i in fetched_data_121:
        i.append(pharmacy_url_121)
    medication.extend(fetched_data_121)

    # Pirkkalan 1. apteekki
    pharmacy_url_122 = "pirkkalanapteekki.fi"
    URLs_122_normi = ['https://www.pirkkalanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.pirkkalanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.pirkkalanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.pirkkalanapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.pirkkalanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.pirkkalanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_122 = nt.yliopistonapteekki(URLs_122_normi)

    for i in fetched_data_122:
        i.append(pharmacy_url_122)
    medication.extend(fetched_data_122)

    # Puuvillan apteekki
    pharmacy_url_123 = "puuvillanapteekki.fi"
    URLs_123_normi = ['https://www.puuvillanapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.puuvillanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.puuvillanapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.puuvillanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.puuvillanapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.puuvillanapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.puuvillanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_123 = nt.yliopistonapteekki(URLs_123_normi)

    for i in fetched_data_123:
        i.append(pharmacy_url_123)
    medication.extend(fetched_data_123)

    # Asema-apteekki
    pharmacy_url_124 = "asema-apteekki.fi"
    URLs_124_normi = ['https://www.asema-apteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.asema-apteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.asema-apteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.asema-apteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.asema-apteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.asema-apteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.asema-apteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_124 = nt.yliopistonapteekki(URLs_124_normi)

    for i in fetched_data_124:
        i.append(pharmacy_url_124)
    medication.extend(fetched_data_124)

    # Porin 8. apteekki
    pharmacy_url_125 = "lansiporinuusiverkkoapteekki.fi"
    URLs_125_normi = ['https://www.lansiporinuusiverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.lansiporinuusiverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.lansiporinuusiverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.lansiporinuusiverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.lansiporinuusiverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.lansiporinuusiverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.lansiporinuusiverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_125 = nt.yliopistonapteekki(URLs_125_normi)

    for i in fetched_data_125:
        i.append(pharmacy_url_125)
    medication.extend(fetched_data_125)

    # Tammisaaren apteekki
    pharmacy_url_126 = "ekenas1apotek.fi"
    URLs_126_normi = ['https://ekenas1apotek.fi/se/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://ekenas1apotek.fi/se/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://ekenas1apotek.fi/se/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://ekenas1apotek.fi/se/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://ekenas1apotek.fi/se/hydrocortison-1-emuls-voide-20-g.html',
                      'https://ekenas1apotek.fi/se/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://ekenas1apotek.fi/se/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_126 = nt.yliopistonapteekki(URLs_126_normi)

    for i in fetched_data_126:
        i.append(pharmacy_url_126)
    medication.extend(fetched_data_126)

    # Karjaan apteekki
    pharmacy_url_127 = "karisapotek.fi"
    URLs_127_normi = ['https://www.karisapotek.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.karisapotek.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.karisapotek.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.karisapotek.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.karisapotek.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.karisapotek.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.karisapotek.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_127 = nt.yliopistonapteekki(URLs_127_normi)

    for i in fetched_data_127:
        i.append(pharmacy_url_127)
    medication.extend(fetched_data_127)

    # Rauman 1. apteekki
    pharmacy_url_128 = "raumanverkkoapteekki.fi"
    URLs_128_normi = ['https://raumanverkkoapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://raumanverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://raumanverkkoapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://raumanverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://raumanverkkoapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://raumanverkkoapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://raumanverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_128 = nt.yliopistonapteekki(URLs_128_normi)

    for i in fetched_data_128:
        i.append(pharmacy_url_128)
    medication.extend(fetched_data_128)

    # Riihimäen aurinkoapteekki
    pharmacy_url_129 = "aurinkonet.fi"
    URLs_129_normi = ['https://aurinkonet.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://aurinkonet.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://aurinkonet.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://aurinkonet.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://aurinkonet.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://aurinkonet.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://aurinkonet.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_129 = nt.yliopistonapteekki(URLs_129_normi)

    for i in fetched_data_129:
        i.append(pharmacy_url_129)
    medication.extend(fetched_data_129)

    # Aarre apteekki
    pharmacy_url_130 = "aarreapteekki.fi"
    URLs_130_normi = ['https://www.aarreapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.aarreapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.aarreapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.aarreapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.aarreapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.aarreapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.aarreapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_130 = nt.yliopistonapteekki(URLs_130_normi)

    for i in fetched_data_130:
        i.append(pharmacy_url_130)
    medication.extend(fetched_data_130)

    # Ounas apteekki
    pharmacy_url_131 = "ounasapteekki.fi"
    URLs_131_normi = ['https://www.ounasapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.ounasapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.ounasapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.ounasapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.ounasapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.ounasapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.ounasapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_131 = nt.yliopistonapteekki(URLs_131_normi)

    for i in fetched_data_131:
        i.append(pharmacy_url_131)
    medication.extend(fetched_data_131)

    # Ruokolahden apteekki
    pharmacy_url_132 = "ruokolahdenverkkoapteekki.fi"
    URLs_132_normi = ['https://ruokolahdenverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://ruokolahdenverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://ruokolahdenverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://ruokolahdenverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://ruokolahdenverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://ruokolahdenverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://ruokolahdenverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_132 = nt.yliopistonapteekki(URLs_132_normi)

    for i in fetched_data_132:
        i.append(pharmacy_url_132)
    medication.extend(fetched_data_132)

    # Halikon apteekki
    pharmacy_url_133 = "salonverkkoapteekki.fi"
    URLs_133_normi = ['https://salonverkkoapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://salonverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://salonverkkoapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://salonverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://salonverkkoapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://salonverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://salonverkkoapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_133 = nt.yliopistonapteekki(URLs_133_normi)

    for i in fetched_data_133:
        i.append(pharmacy_url_133)
    medication.extend(fetched_data_133)

    # Sastamalan 1. apteekki
    pharmacy_url_134 = "hyvinvointiapteekki.fi"
    URLs_134_normi = ['https://hyvinvointiapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://hyvinvointiapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://hyvinvointiapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://hyvinvointiapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://hyvinvointiapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://hyvinvointiapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://hyvinvointiapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_134 = nt.yliopistonapteekki(URLs_134_normi)

    for i in fetched_data_134:
        i.append(pharmacy_url_134)
    medication.extend(fetched_data_134)

    # Sipoon apteekki
    pharmacy_url_135 = "nikkilänapteekki.fi"
    URLs_135_normi = ['https://nikkilanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://nikkilanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://nikkilanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://nikkilanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://nikkilanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://nikkilanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_135 = nt.yliopistonapteekki(URLs_135_normi)

    for i in fetched_data_135:
        i.append(pharmacy_url_135)
    medication.extend(fetched_data_135)

    # Söderkullan apteekki
    pharmacy_url_136 = "sipoonverkkoapteekki.fi"
    URLs_136_normi = ['https://www.sipoonverkkoapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.sipoonverkkoapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.sipoonverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.sipoonverkkoapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.sipoonverkkoapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.sipoonverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_136 = nt.yliopistonapteekki(URLs_136_normi)

    for i in fetched_data_136:
        i.append(pharmacy_url_136)
    medication.extend(fetched_data_136)

    # Sodankylän apteekki
    pharmacy_url_137 = "sodankylanapteekki.fi"
    URLs_137_normi = ['https://www.sodankylanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.sodankylanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.sodankylanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.sodankylanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.sodankylanapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.sodankylanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.sodankylanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_137 = nt.yliopistonapteekki(URLs_137_normi)

    for i in fetched_data_137:
        i.append(pharmacy_url_137)
    medication.extend(fetched_data_137)

    # Sulkavan apteekki
    pharmacy_url_138 = "sulkavaneapteekki.fi"
    URLs_138_normi = ['https://www.sulkavaneapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.sulkavaneapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.sulkavaneapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.sulkavaneapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.sulkavaneapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.sulkavaneapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.sulkavaneapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_138 = nt.yliopistonapteekki(URLs_138_normi)

    for i in fetched_data_138:
        i.append(pharmacy_url_138)
    medication.extend(fetched_data_138)

    # Suomussalmen apteekki
    pharmacy_url_139 = "suomussalmenverkkoapteekki.fi"
    URLs_139_normi = ['https://www.suomussalmenverkkoapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.suomussalmenverkkoapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.suomussalmenverkkoapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.suomussalmenverkkoapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.suomussalmenverkkoapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.suomussalmenverkkoapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.suomussalmenverkkoapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_139 = nt.yliopistonapteekki(URLs_139_normi)

    for i in fetched_data_139:
        i.append(pharmacy_url_139)
    medication.extend(fetched_data_139)

    # Säkylän apteekki
    pharmacy_url_140 = "apteekkikotona.fi"
    URLs_140_normi = ['https://apteekkikotona.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://apteekkikotona.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://apteekkikotona.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://apteekkikotona.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://apteekkikotona.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://apteekkikotona.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://apteekkikotona.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_140 = nt.yliopistonapteekki(URLs_140_normi)

    for i in fetched_data_140:
        i.append(pharmacy_url_140)
    medication.extend(fetched_data_140)

    # Haka apteekki
    pharmacy_url_141 = "hakaeapteekki.fi"
    URLs_141_normi = ['https://hakaeapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://hakaeapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://hakaeapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://hakaeapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://hakaeapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://hakaeapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://hakaeapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_141 = nt.yliopistonapteekki(URLs_141_normi)

    for i in fetched_data_141:
        i.append(pharmacy_url_141)
    medication.extend(fetched_data_141)

    # Moroapteekki
    pharmacy_url_142 = "eapteekkitampere.fi"
    URLs_142_normi = ['https://eapteekkitampere.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://eapteekkitampere.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://eapteekkitampere.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://eapteekkitampere.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://eapteekkitampere.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://eapteekkitampere.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://eapteekkitampere.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_142 = nt.yliopistonapteekki(URLs_142_normi)

    for i in fetched_data_142:
        i.append(pharmacy_url_142)
    medication.extend(fetched_data_142)

    # Linnainmaan apteekki
    pharmacy_url_143 = "apteekkinne.fi"
    URLs_143_normi = ['https://apteekkinne.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://apteekkinne.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://apteekkinne.fi/fi/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://apteekkinne.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://apteekkinne.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://apteekkinne.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://apteekkinne.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_143 = nt.yliopistonapteekki(URLs_143_normi)

    for i in fetched_data_143:
        i.append(pharmacy_url_143)
    medication.extend(fetched_data_143)

    # Apteekki koilliskeskus
    pharmacy_url_144 = "apteekkiostos.fi"
    URLs_144_normi = ['https://www.apteekkiostos.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkiostos.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.apteekkiostos.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.apteekkiostos.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html',
                      'https://www.apteekkiostos.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.apteekkiostos.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkiostos.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html']

    fetched_data_144 = nt.yliopistonapteekki(URLs_144_normi)

    for i in fetched_data_144:
        i.append(pharmacy_url_144)
    medication.extend(fetched_data_144)

    # Tammerkosken apteekki
    pharmacy_url_145 = "tammerkoskenapteekki.fi"
    URLs_145_normi = ['https://tammerkoskenapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://tammerkoskenapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://tammerkoskenapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://tammerkoskenapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://tammerkoskenapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://tammerkoskenapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://tammerkoskenapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_145 = nt.yliopistonapteekki(URLs_145_normi)

    for i in fetched_data_145:
        i.append(pharmacy_url_145)
    medication.extend(fetched_data_145)
    
    # Turtolan apteekki
    pharmacy_url_146 = "wolt.com/fi/fin/tampere/venue/turtolan-apteekki"
    URLs_146_selenium = ['https://wolt.com/fi/fin/tampere/venue/turtolan-apteekki/zyrtec-10-mg-itemid-662785bd9d4f568969a6f25b?search=zyrtec',
                         'https://wolt.com/fi/fin/tampere/venue/turtolan-apteekki/voltaren-forte-23-2-mg-g-itemid-662785bd9d4f568969a6f498?search=voltaren',
                         'https://wolt.com/fi/fin/tampere/venue/turtolan-apteekki/hydrocortison-1-itemid-662785bd9d4f568969a6f397?search=hydrocortison',
                         'https://wolt.com/fi/fin/tampere/venue/turtolan-apteekki/burana-400-mg-itemid-662785bd9d4f568969a6f508?search=burana',
                         'https://wolt.com/fi/fin/tampere/venue/turtolan-apteekki/panadol-500-mg-itemid-662785bd9d4f568969a6f46a?search=panadol',
                         'https://wolt.com/fi/fin/tampere/venue/turtolan-apteekki/somac-control-20-mg-itemid-662785bd9d4f568969a6f396?search=somac']

    special_link = [0, 0, 0, 0, 0, 0, 0]  # 1,2,3... if link needs to be treated separately due to different html structure, 0 otherwise
    fetched_data_146 = seltuot.wolt_selenium(URLs_146_selenium, 'EUR', special_link)

    for i in fetched_data_146:
        i.append(pharmacy_url_146)
    medication.extend(fetched_data_146)
    
    # Lempi apteekki
    pharmacy_url_147 = "lempiapteekki.fi"
    URLs_147_normi = ['https://lempiapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://lempiapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://lempiapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://lempiapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://lempiapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://lempiapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://lempiapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_147 = nt.yliopistonapteekki(URLs_147_normi)

    for i in fetched_data_147:
        i.append(pharmacy_url_147)
    medication.extend(fetched_data_147)

    # Kupittaan apteekki
    pharmacy_url_148 = "apteekkiextra.fi"
    URLs_148_normi = ['https://apteekkiextra.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://apteekkiextra.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://apteekkiextra.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://apteekkiextra.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://apteekkiextra.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://apteekkiextra.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://apteekkiextra.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_148 = nt.yliopistonapteekki(URLs_148_normi)

    for i in fetched_data_148:
        i.append(pharmacy_url_148)
    medication.extend(fetched_data_148)

    # Nova apteekki
    pharmacy_url_149 = "novaapteekki.fi"
    URLs_149_normi  = ['https://novaapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                       'https://novaapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                       'https://novaapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                       'https://novaapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                       'https://novaapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                       'https://novaapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                       'https://novaapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_149 = nt.yliopistonapteekki(URLs_149_normi)

    for i in fetched_data_149:
        i.append(pharmacy_url_149)
    medication.extend(fetched_data_149)

    # Skanssin apteekki
    pharmacy_url_150 = "verkkoapteekit.fi"
    URLs_150_normi = ['https://verkkoapteekit.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://verkkoapteekit.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://verkkoapteekit.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://verkkoapteekit.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://verkkoapteekit.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://verkkoapteekit.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://verkkoapteekit.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_150 = nt.yliopistonapteekki(URLs_150_normi)

    for i in fetched_data_150:
        i.append(pharmacy_url_150)
    medication.extend(fetched_data_150)

    # Uudenkaarlepyyn apteekki
    pharmacy_url_151 = "nykarlebyapotek.fi"
    URLs_151_normi = ['https://nykarlebyapotek.fi/se/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://nykarlebyapotek.fi/se/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://nykarlebyapotek.fi/se/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://nykarlebyapotek.fi/se/hydrocortison-1-emuls-voide-20-g.html',
                      'https://nykarlebyapotek.fi/se/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://nykarlebyapotek.fi/se/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://nykarlebyapotek.fi/se/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_151 = nt.yliopistonapteekki(URLs_151_normi)

    for i in fetched_data_151:
        i.append(pharmacy_url_151)
    medication.extend(fetched_data_151)

    # Uudenkaupungin 1. apteekki
    pharmacy_url_152 = "apteekkipalvelu.fi"
    URLs_152_normi = ['https://www.apteekkipalvelu.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.apteekkipalvelu.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkipalvelu.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.apteekkipalvelu.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.apteekkipalvelu.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkipalvelu.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkipalvelu.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_152 = nt.yliopistonapteekki(URLs_152_normi)

    for i in fetched_data_152:
        i.append(pharmacy_url_152)
    medication.extend(fetched_data_152)

    # Vaasan keskusapteekki
    pharmacy_url_153 = "apocentral.fi"
    URLs_153_normi = ['https://apocentral.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://apocentral.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://apocentral.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://apocentral.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://apocentral.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://apocentral.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://apocentral.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_153 = nt.yliopistonapteekki(URLs_153_normi)

    for i in fetched_data_153:
        i.append(pharmacy_url_153)
    medication.extend(fetched_data_153)

    # Kuninkaanapteekki
    pharmacy_url_154 = "vaasankuninkaanapteekki.fi"
    URLs_154_normi = ['https://www.vaasankuninkaanapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.vaasankuninkaanapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.vaasankuninkaanapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.vaasankuninkaanapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.vaasankuninkaanapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.vaasankuninkaanapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.vaasankuninkaanapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_154 = nt.yliopistonapteekki(URLs_154_normi)

    for i in fetched_data_154:
        i.append(pharmacy_url_154)
    medication.extend(fetched_data_154)

    # Apteekki kivihaka
    pharmacy_url_155 = "apteekkikivihaka.fi"
    URLs_155_normi = ['https://www.apteekkikivihaka.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.apteekkikivihaka.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkikivihaka.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.apteekkikivihaka.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.apteekkikivihaka.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkikivihaka.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkikivihaka.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_155 = nt.yliopistonapteekki(URLs_155_normi)

    for i in fetched_data_155:
        i.append(pharmacy_url_155)
    medication.extend(fetched_data_155)

    # Tikkurilan ykkösapteekki
    pharmacy_url_156 = "tikkurilanlaatuapteekki.fi"
    URLs_156_normi = ['https://tikkurilanlaatuapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://tikkurilanlaatuapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://tikkurilanlaatuapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://tikkurilanlaatuapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://tikkurilanlaatuapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://tikkurilanlaatuapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://tikkurilanlaatuapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_156 = nt.yliopistonapteekki(URLs_156_normi)

    for i in fetched_data_156:
        i.append(pharmacy_url_156)
    medication.extend(fetched_data_156)
    
    # Apteekki koivuhaka
    pharmacy_url_157 = "wolt.com/fi/fin/vantaa/venue/apteekki-koivuhaka"
    URLs_157_selenium = ['https://wolt.com/fi/fin/vantaa/venue/apteekki-koivuhaka/otrivin-menthol-sailytysaineeton-1-mg-ml-itemid-66f4f43758a663648449afc0?search=otrivin',
                         'https://wolt.com/fi/fin/vantaa/venue/apteekki-koivuhaka/zyrtec-10-mg-itemid-66e90c8f279b4ca34c8a9b36?search=zyrtec',
                         'https://wolt.com/fi/fin/vantaa/venue/apteekki-koivuhaka/burana-400-mg-itemid-66e90c8f279b4ca34c8a9de3?search=burana',
                         'https://wolt.com/fi/fin/vantaa/venue/apteekki-koivuhaka/panadol-500-mg-itemid-66e90c8f279b4ca34c8a9d45?search=panadol',
                         'https://wolt.com/fi/fin/vantaa/venue/apteekki-koivuhaka/somac-control-20-mg-itemid-66e90c8f279b4ca34c8a9c71?search=somac']

    special_link = [1, 0, 0, 0, 0, 0, 0]  # 1,2,3... if link needs to be treated separately due to different html structure, 0 otherwise
    fetched_data_157 = seltuot.wolt_selenium(URLs_157_selenium, 'EUR', special_link)

    for i in fetched_data_157:
        i.append(pharmacy_url_157)
    medication.extend(fetched_data_157)
    
    # Tammiston apteekki
    pharmacy_url_158 = "apteekkishoppi.fi"
    URLs_158_normi = ['https://www.apteekkishoppi.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.apteekkishoppi.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkishoppi.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.apteekkishoppi.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.apteekkishoppi.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkishoppi.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.apteekkishoppi.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_158 = nt.yliopistonapteekki(URLs_158_normi)

    for i in fetched_data_158:
        i.append(pharmacy_url_158)
    medication.extend(fetched_data_158)

    # Korson apteekki
    pharmacy_url_159 = "korsonapteekki.fi"
    URLs_159_normi = ['https://www.korsonapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.korsonapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.korsonapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.korsonapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.korsonapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.korsonapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.korsonapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_159 = nt.yliopistonapteekki(URLs_159_normi)

    for i in fetched_data_159:
        i.append(pharmacy_url_159)
    medication.extend(fetched_data_159)

    # Vihdin apteekki
    pharmacy_url_160 = "vihdinapteekki.fi"
    URLs_160_normi = ['https://www.vihdinapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.vihdinapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.vihdinapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.vihdinapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.vihdinapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.vihdinapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.vihdinapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_160 = nt.yliopistonapteekki(URLs_160_normi)

    for i in fetched_data_160:
        i.append(pharmacy_url_160)
    medication.extend(fetched_data_160)

    # Nummelan apteekki
    pharmacy_url_161 = "verkkoapteekkisi.fi"
    URLs_161_normi = ['https://www.verkkoapteekkisi.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.verkkoapteekkisi.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.verkkoapteekkisi.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.verkkoapteekkisi.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.verkkoapteekkisi.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.verkkoapteekkisi.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_161 = nt.yliopistonapteekki(URLs_161_normi)

    for i in fetched_data_161:
        i.append(pharmacy_url_161)
    medication.extend(fetched_data_161)

    # Nummelan uusi apteekki
    pharmacy_url_162 = "airapteekki.fi"
    URLs_162_normi = ['https://www.airapteekki.fi/fi/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.airapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.airapteekki.fi/fi/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.airapteekki.fi/fi/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.airapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.airapteekki.fi/fi/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_162 = nt.yliopistonapteekki(URLs_162_normi)

    for i in fetched_data_162:
        i.append(pharmacy_url_162)
    medication.extend(fetched_data_162)

    # Ylivieskan 1. apteekki
    pharmacy_url_163 = "ylivieskanykkosapteekki.fi"
    URLs_163_normi = ['https://www.ylivieskanykkosapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.ylivieskanykkosapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.ylivieskanykkosapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.ylivieskanykkosapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.ylivieskanykkosapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.ylivieskanykkosapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.ylivieskanykkosapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_163 = nt.yliopistonapteekki(URLs_163_normi)

    for i in fetched_data_163:
        i.append(pharmacy_url_163)
    medication.extend(fetched_data_163)

    # Savarin apteekki
    pharmacy_url_164 = "savarinapteekki.fi"
    URLs_164_normi = ['https://www.savarinapteekki.fi/fi/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml.html',
                      'https://www.savarinapteekki.fi/fi/tuotteet/allergia/zyrtec-10-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.savarinapteekki.fi/fi/voltaren-forte-23-2-mg-g-geeli-100-g.html',
                      'https://www.savarinapteekki.fi/fi/tuotteet/matkalle-ja-mokille/hydrocortison-1-emuls-voide-20-g.html',
                      'https://www.savarinapteekki.fi/fi/tuotteet/kipu-ja-flunssa/kipu-ja-kuume/burana-400-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.savarinapteekki.fi/fi/panadol-500-mg-tabl-kalvopaall-30-fol.html',
                      'https://www.savarinapteekki.fi/fi/tuotteet/vatsa/narastys/somac-control-20-mg-enterotabl-14-fol.html']

    fetched_data_164 = nt.yliopistonapteekki(URLs_164_normi)

    for i in fetched_data_164:
        i.append(pharmacy_url_164)
    medication.extend(fetched_data_164)

    # Espoonlahden apteekki
    pharmacy_url_165 = "app.treet.fi/pharmacy/espoonlahden-apteekki"
    URLs_165_selenium = ['https://app.treet.fi/pharmacy/espoonlahden-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/espoonlahden-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/espoonlahden-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/espoonlahden-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/espoonlahden-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/espoonlahden-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/espoonlahden-apteekki/product/131583']

    fetched_data_165 = seltuot.treet_selenium(URLs_165_selenium)

    for i in fetched_data_165:
        i.append(pharmacy_url_165)
    medication.extend(fetched_data_165)

    # Ruoholahden uusi apteekki
    pharmacy_url_166 = "app.treet.fi/pharmacy/ruoholahden-uusi-apteekki"
    URLs_166_selenium = ['https://app.treet.fi/pharmacy/ruoholahden-uusi-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/ruoholahden-uusi-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/ruoholahden-uusi-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/ruoholahden-uusi-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/ruoholahden-uusi-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/ruoholahden-uusi-apteekki/product/131583']

    fetched_data_166 = seltuot.treet_selenium(URLs_166_selenium)

    for i in fetched_data_166:
        i.append(pharmacy_url_166)
    medication.extend(fetched_data_166)

    # Steissin apteekki
    pharmacy_url_167 = "app.treet.fi/pharmacy/steissin-apteekki"
    URLs_167_selenium = ['https://app.treet.fi/pharmacy/steissin-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/steissin-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/steissin-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/steissin-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/steissin-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/steissin-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/steissin-apteekki/product/131583']

    fetched_data_167 = seltuot.treet_selenium(URLs_167_selenium)

    for i in fetched_data_167:
        i.append(pharmacy_url_167)
    medication.extend(fetched_data_167)

    # Apteekki primavera
    pharmacy_url_168 = "app.treet.fi/pharmacy/apteekki-primavera"
    URLs_168_selenium = ['https://app.treet.fi/pharmacy/apteekki-primavera/product/117648',
                         'https://app.treet.fi/pharmacy/apteekki-primavera/product/048769',
                         'https://app.treet.fi/pharmacy/apteekki-primavera/product/057965',
                         'https://app.treet.fi/pharmacy/apteekki-primavera/product/056698',
                         'https://app.treet.fi/pharmacy/apteekki-primavera/product/519994',
                         'https://app.treet.fi/pharmacy/apteekki-primavera/product/131583']

    fetched_data_168 = seltuot.treet_selenium(URLs_168_selenium)

    for i in fetched_data_168:
        i.append(pharmacy_url_168)
    medication.extend(fetched_data_168)

    # Munkkiniemen puisto apteekki
    pharmacy_url_169 = "app.treet.fi/pharmacy/munkkiniemen-puisto-apteekki"
    URLs_169_selenium = ['https://app.treet.fi/pharmacy/munkkiniemen-puisto-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/munkkiniemen-puisto-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/munkkiniemen-puisto-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/munkkiniemen-puisto-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/munkkiniemen-puisto-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/munkkiniemen-puisto-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/munkkiniemen-puisto-apteekki/product/131583']

    fetched_data_169 = seltuot.treet_selenium(URLs_169_selenium)

    for i in fetched_data_169:
        i.append(pharmacy_url_169)
    medication.extend(fetched_data_169)

    # Apteekki medena
    pharmacy_url_170 = "app.treet.fi/pharmacy/apteekki-medena"
    URLs_170_selenium = ['https://app.treet.fi/pharmacy/apteekki-medena/product/117648',
                         'https://app.treet.fi/pharmacy/apteekki-medena/product/048769',
                         'https://app.treet.fi/pharmacy/apteekki-medena/product/134589',
                         'https://app.treet.fi/pharmacy/apteekki-medena/product/057965',
                         'https://app.treet.fi/pharmacy/apteekki-medena/product/056698',
                         'https://app.treet.fi/pharmacy/apteekki-medena/product/519994',
                         'https://app.treet.fi/pharmacy/apteekki-medena/product/131583']

    fetched_data_170 = seltuot.treet_selenium(URLs_170_selenium)

    for i in fetched_data_170:
        i.append(pharmacy_url_170)
    medication.extend(fetched_data_170)

    # Lauttasaaren kirrko apteekki
    pharmacy_url_171 = "app.treet.fi/pharmacy/lauttasaaren-kirkkoapteekki"
    URLs_171_selenium = ['https://app.treet.fi/pharmacy/lauttasaaren-kirkkoapteekki/product/117648',
                         'https://app.treet.fi/pharmacy/lauttasaaren-kirkkoapteekki/product/048769',
                         'https://app.treet.fi/pharmacy/lauttasaaren-kirkkoapteekki/product/057965',
                         'https://app.treet.fi/pharmacy/lauttasaaren-kirkkoapteekki/product/056698',
                         'https://app.treet.fi/pharmacy/lauttasaaren-kirkkoapteekki/product/519994',
                         'https://app.treet.fi/pharmacy/lauttasaaren-kirkkoapteekki/product/131583']

    fetched_data_171 = seltuot.treet_selenium(URLs_171_selenium)

    for i in fetched_data_171:
        i.append(pharmacy_url_171)
    medication.extend(fetched_data_171)

    # Kipparlahden apteekki
    pharmacy_url_172 = "app.treet.fi/pharmacy/kipparlahden-apteekki"
    URLs_172_selenium = ['https://app.treet.fi/pharmacy/kipparlahden-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kipparlahden-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/kipparlahden-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/kipparlahden-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/kipparlahden-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kipparlahden-apteekki/product/131583']

    fetched_data_172 = seltuot.treet_selenium(URLs_172_selenium)

    for i in fetched_data_172:
        i.append(pharmacy_url_172)
    medication.extend(fetched_data_172)

    # Kruununhaan apteekki
    pharmacy_url_173 = "app.treet.fi/pharmacy/kruununhaan-apteekki "
    URLs_173_selenium = ['https://app.treet.fi/pharmacy/kruununhaan-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kruununhaan-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/kruununhaan-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/kruununhaan-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/kruununhaan-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kruununhaan-apteekki/product/131583']

    fetched_data_173 = seltuot.treet_selenium(URLs_173_selenium)

    for i in fetched_data_173:
        i.append(pharmacy_url_173)
    medication.extend(fetched_data_173)

    # Apteekki51
    pharmacy_url_174 = "app.treet.fi/pharmacy/apteekki-51"
    URLs_174_selenium = ['https://app.treet.fi/pharmacy/apteekki-51/product/117648',
                         'https://app.treet.fi/pharmacy/apteekki-51/product/048769',
                         'https://app.treet.fi/pharmacy/apteekki-51/product/134589',
                         'https://app.treet.fi/pharmacy/apteekki-51/product/057965',
                         'https://app.treet.fi/pharmacy/apteekki-51/product/056698',
                         'https://app.treet.fi/pharmacy/apteekki-51/product/519994',
                         'https://app.treet.fi/pharmacy/apteekki-51/product/131583']

    fetched_data_174 = seltuot.treet_selenium(URLs_174_selenium)

    for i in fetched_data_174:
        i.append(pharmacy_url_174)
    medication.extend(fetched_data_174)

    # Töölön apteekki
    pharmacy_url_175 = "app.treet.fi/pharmacy/toolon-apteekki"
    URLs_175_selenium = ['https://app.treet.fi/pharmacy/toolon-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/toolon-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/toolon-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/toolon-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/toolon-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/toolon-apteekki/product/134589']

    fetched_data_175 = seltuot.treet_selenium(URLs_175_selenium)

    for i in fetched_data_175:
        i.append(pharmacy_url_175)
    medication.extend(fetched_data_175)

    # Hyvinkään 1. apteekki
    pharmacy_url_176 = "app.treet.fi/pharmacy/hyvinkaan-ykkosapteekki"
    URLs_176_selenium = ['https://app.treet.fi/pharmacy/hyvinkaan-ykkosapteekki/product/117648',
                         'https://app.treet.fi/pharmacy/hyvinkaan-ykkosapteekki/product/048769',
                         'https://app.treet.fi/pharmacy/hyvinkaan-ykkosapteekki/product/134589',
                         'https://app.treet.fi/pharmacy/hyvinkaan-ykkosapteekki/product/056698',
                         'https://app.treet.fi/pharmacy/hyvinkaan-ykkosapteekki/product/519994',
                         'https://app.treet.fi/pharmacy/hyvinkaan-ykkosapteekki/product/131583']

    fetched_data_176 = seltuot.treet_selenium(URLs_176_selenium)

    for i in fetched_data_176:
        i.append(pharmacy_url_176)
    medication.extend(fetched_data_176)

    # Hämeenlinnnan 1. apteekki
    pharmacy_url_177 = "app.treet.fi/pharmacy/hameenlinnan-tori-apteekki"
    URLs_177_selenium = ['https://app.treet.fi/pharmacy/hameenlinnan-tori-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/hameenlinnan-tori-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/hameenlinnan-tori-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/hameenlinnan-tori-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/hameenlinnan-tori-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/hameenlinnan-tori-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/hameenlinnan-tori-apteekki/product/134589']

    fetched_data_177 = seltuot.treet_selenium(URLs_177_selenium)

    for i in fetched_data_177:
        i.append(pharmacy_url_177)
    medication.extend(fetched_data_177)

    # Priima apteekki
    pharmacy_url_178 = "app.treet.fi/pharmacy/priima-apteekki"
    URLs_178_selenium = ['https://app.treet.fi/pharmacy/priima-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/priima-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/priima-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/priima-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/priima-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/priima-apteekki/product/131583']

    fetched_data_178 = seltuot.treet_selenium(URLs_178_selenium)

    for i in fetched_data_178:
        i.append(pharmacy_url_178)
    medication.extend(fetched_data_178)

    # Ilomantsin apteekki
    pharmacy_url_179 = "app.treet.fi/pharmacy/ilomantsin-apteekki"
    URLs_179_selenium = ['https://app.treet.fi/pharmacy/ilomantsin-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/ilomantsin-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/ilomantsin-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/ilomantsin-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/ilomantsin-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/ilomantsin-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/ilomantsin-apteekki/product/134589']

    fetched_data_179 = seltuot.treet_selenium(URLs_179_selenium)

    for i in fetched_data_179:
        i.append(pharmacy_url_179)
    medication.extend(fetched_data_179)

    # Joutsan apteekki
    pharmacy_url_180 = "app.treet.fi/pharmacy/joutsan-apteekki"
    URLs_180_selenium = ['https://app.treet.fi/pharmacy/joutsan-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/joutsan-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/joutsan-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/joutsan-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/joutsan-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/joutsan-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/joutsan-apteekki/product/134589']

    fetched_data_180 = seltuot.treet_selenium(URLs_180_selenium)

    for i in fetched_data_180:
        i.append(pharmacy_url_180)
    medication.extend(fetched_data_180)

    # Jämsänkosken apteekki
    pharmacy_url_181 = "app.treet.fi/pharmacy/jamsankosken-apteekki"
    URLs_181_selenium = ['https://app.treet.fi/pharmacy/jamsankosken-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/jamsankosken-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/jamsankosken-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/jamsankosken-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/jamsankosken-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/jamsankosken-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/jamsankosken-apteekki/product/134589']

    fetched_data_181 = seltuot.treet_selenium(URLs_181_selenium)

    for i in fetched_data_181:
        i.append(pharmacy_url_181)
    medication.extend(fetched_data_181)

    # Kangasniemen apteekki
    pharmacy_url_183 = "app.treet.fi/pharmacy/kangasniemen-apteekki"
    URLs_183_selenium = ['https://app.treet.fi/pharmacy/kangasniemen-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/kangasniemen-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kangasniemen-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/kangasniemen-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/kangasniemen-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kangasniemen-apteekki/product/131583']

    fetched_data_183 = seltuot.treet_selenium(URLs_183_selenium)

    for i in fetched_data_183:
        i.append(pharmacy_url_183)
    medication.extend(fetched_data_183)

    # Kankaanpään vuokko apteekki
    pharmacy_url_184 = "app.treet.fi/pharmacy/vuokko-apteekki"
    URLs_184_selenium = ['https://app.treet.fi/pharmacy/vuokko-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/vuokko-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/vuokko-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/vuokko-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/vuokko-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/vuokko-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/vuokko-apteekki/product/134589']

    fetched_data_184 = seltuot.treet_selenium(URLs_184_selenium)

    for i in fetched_data_184:
        i.append(pharmacy_url_184)
    medication.extend(fetched_data_184)

    # Keminmaan apteekki
    pharmacy_url_185 = "app.treet.fi/pharmacy/keminmaan-apteekki"
    URLs_185_selenium = ['https://app.treet.fi/pharmacy/keminmaan-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/keminmaan-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/keminmaan-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/keminmaan-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/keminmaan-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/keminmaan-apteekki/product/131583']

    fetched_data_185 = seltuot.treet_selenium(URLs_185_selenium)

    for i in fetched_data_185:
        i.append(pharmacy_url_185)
    medication.extend(fetched_data_185)

    # Kempeleen 1. apteekki
    pharmacy_url_186 = "app.treet.fi/pharmacy/kempeleen-1-apteekki"
    URLs_186_selenium = ['https://app.treet.fi/pharmacy/kempeleen-1-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/kempeleen-1-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/kempeleen-1-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kempeleen-1-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kempeleen-1-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/kempeleen-1-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/kempeleen-1-apteekki/product/048769']

    fetched_data_186 = seltuot.treet_selenium(URLs_186_selenium)

    for i in fetched_data_186:
        i.append(pharmacy_url_186)
    medication.extend(fetched_data_186)

    # Kirkkonummen uusi apteekki
    pharmacy_url_187 = "app.treet.fi/pharmacy/kirkkonummen-uusi-apteekki"
    URLs_187_selenium = ['https://app.treet.fi/pharmacy/kirkkonummen-uusi-apteekki/product/152429',
                         'https://app.treet.fi/pharmacy/kirkkonummen-uusi-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/kirkkonummen-uusi-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kirkkonummen-uusi-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kirkkonummen-uusi-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/kirkkonummen-uusi-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/kirkkonummen-uusi-apteekki/product/048769']

    fetched_data_187 = seltuot.treet_selenium(URLs_187_selenium)

    for i in fetched_data_187:
        i.append(pharmacy_url_187)
    medication.extend(fetched_data_187)

    # Kittilän apteekki
    pharmacy_url_188 = "app.treet.fi/pharmacy/kittilan-apteekki"
    URLs_188_selenium = ['https://app.treet.fi/pharmacy/kittilan-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/kittilan-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/kittilan-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kittilan-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kittilan-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/kittilan-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/kittilan-apteekki/product/048769']

    fetched_data_188 = seltuot.treet_selenium(URLs_188_selenium)

    for i in fetched_data_188:
        i.append(pharmacy_url_188)
    medication.extend(fetched_data_188)

    # Kuopion eka apteekki
    pharmacy_url_189 = "app.treet.fi/pharmacy/eka-apteekki"
    URLs_189_selenium = ['https://app.treet.fi/pharmacy/eka-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/eka-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/eka-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/eka-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/eka-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/eka-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/eka-apteekki/product/048769']

    fetched_data_189 = seltuot.treet_selenium(URLs_189_selenium)

    for i in fetched_data_189:
        i.append(pharmacy_url_189)
    medication.extend(fetched_data_189)

    # Kuopion toriapteekki
    pharmacy_url_190 = "app.treet.fi/pharmacy/kuopion-toriapteekki"
    URLs_190_selenium = ['https://app.treet.fi/pharmacy/kuopion-toriapteekki/product/056698',
                         'https://app.treet.fi/pharmacy/kuopion-toriapteekki/product/057965',
                         'https://app.treet.fi/pharmacy/kuopion-toriapteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kuopion-toriapteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kuopion-toriapteekki/product/131583',
                         'https://app.treet.fi/pharmacy/kuopion-toriapteekki/product/048769']

    fetched_data_190 = seltuot.treet_selenium(URLs_190_selenium)

    for i in fetched_data_190:
        i.append(pharmacy_url_190)
    medication.extend(fetched_data_190)

    # Niiralan apteekki
    pharmacy_url_191 = "app.treet.fi/pharmacy/niiralan-apteekki"
    URLs_191_selenium = ['https://app.treet.fi/pharmacy/niiralan-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/niiralan-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/niiralan-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/niiralan-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/niiralan-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/niiralan-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/niiralan-apteekki/product/048769']

    fetched_data_191 = seltuot.treet_selenium(URLs_191_selenium)

    for i in fetched_data_191:
        i.append(pharmacy_url_191)
    medication.extend(fetched_data_191)

    # Puijonlaakson apteekki
    pharmacy_url_192 = "app.treet.fi/pharmacy/puijonlaakson-apteekki"
    URLs_192_selenium = ['https://app.treet.fi/pharmacy/puijonlaakson-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/puijonlaakson-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/puijonlaakson-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/puijonlaakson-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/puijonlaakson-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/puijonlaakson-apteekki/product/048769']

    fetched_data_192 = seltuot.treet_selenium(URLs_192_selenium)

    for i in fetched_data_192:
        i.append(pharmacy_url_192)
    medication.extend(fetched_data_192)

    # Lahden helmi apteekki
    pharmacy_url_193 = "app.treet.fi/pharmacy/helmi-apteekki"
    URLs_193_selenium = ['https://app.treet.fi/pharmacy/helmi-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/helmi-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/helmi-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/helmi-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/helmi-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/helmi-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/helmi-apteekki/product/048769']

    fetched_data_193 = seltuot.treet_selenium(URLs_193_selenium)

    for i in fetched_data_193:
        i.append(pharmacy_url_193)
    medication.extend(fetched_data_193)

    # Lapinlahden apteekki
    pharmacy_url_194 = "app.treet.fi/pharmacy/lapinlahden-apteekki"
    URLs_194_selenium = ['https://app.treet.fi/pharmacy/lapinlahden-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/lapinlahden-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/lapinlahden-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/lapinlahden-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/lapinlahden-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/lapinlahden-apteekki/product/048769']

    fetched_data_194 = seltuot.treet_selenium(URLs_194_selenium)

    for i in fetched_data_194:
        i.append(pharmacy_url_194)
    medication.extend(fetched_data_194)

    # Loimaan ykkös apteekki
    pharmacy_url_196 = "app.treet.fi/pharmacy/loimaan-ykkosapteekki"
    URLs_196_selenium = ['https://app.treet.fi/pharmacy/loimaan-ykkosapteekki/product/519994',
                         'https://app.treet.fi/pharmacy/loimaan-ykkosapteekki/product/056698',
                         'https://app.treet.fi/pharmacy/loimaan-ykkosapteekki/product/057965',
                         'https://app.treet.fi/pharmacy/loimaan-ykkosapteekki/product/131583',
                         'https://app.treet.fi/pharmacy/loimaan-ykkosapteekki/product/048769',
                         'https://app.treet.fi/pharmacy/loimaan-ykkosapteekki/product/117648']

    fetched_data_196 = seltuot.treet_selenium(URLs_196_selenium)

    for i in fetched_data_196:
        i.append(pharmacy_url_196)
    medication.extend(fetched_data_196)

    # Muuramen apteekki
    pharmacy_url_197 = "app.treet.fi/pharmacy/muuramen-apteekki"
    URLs_197_selenium = ['https://app.treet.fi/pharmacy/muuramen-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/muuramen-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/muuramen-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/muuramen-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/muuramen-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/muuramen-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/muuramen-apteekki/product/117648']

    fetched_data_197 = seltuot.treet_selenium(URLs_197_selenium)

    for i in fetched_data_197:
        i.append(pharmacy_url_197)
    medication.extend(fetched_data_197)

    # Mäntän apteekki
    pharmacy_url_198 = "app.treet.fi/pharmacy/mantan-apteekki"
    URLs_198_selenium = ['https://app.treet.fi/pharmacy/mantan-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/mantan-apteekki/product/152429',
                         'https://app.treet.fi/pharmacy/mantan-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/mantan-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/mantan-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/mantan-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/mantan-apteekki/product/117648']

    fetched_data_198 = seltuot.treet_selenium(URLs_198_selenium)

    for i in fetched_data_198:
        i.append(pharmacy_url_198)
    medication.extend(fetched_data_198)

    # Naantalin apteekki
    pharmacy_url_199 = "app.treet.fi/pharmacy/naantalin-apteekki"
    URLs_199_selenium = ['https://app.treet.fi/pharmacy/naantalin-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/naantalin-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/naantalin-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/naantalin-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/naantalin-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/naantalin-apteekki/product/117648']

    fetched_data_199 = seltuot.treet_selenium(URLs_199_selenium)

    for i in fetched_data_199:
        i.append(pharmacy_url_199)
    medication.extend(fetched_data_199)

    # Merikosken apteekki
    pharmacy_url_200 = "app.treet.fi/pharmacy/oulun-merikosken-apteekki"
    URLs_200_selenium = ['https://app.treet.fi/pharmacy/oulun-merikosken-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/oulun-merikosken-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/oulun-merikosken-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/oulun-merikosken-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/oulun-merikosken-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/oulun-merikosken-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/oulun-merikosken-apteekki/product/117648']

    fetched_data_200 = seltuot.treet_selenium(URLs_200_selenium)

    for i in fetched_data_200:
        i.append(pharmacy_url_200)
    medication.extend(fetched_data_200)

    # Kaakkurin apteekki
    pharmacy_url_201 = "app.treet.fi/pharmacy/oulun-kaakkurin-apteekki"
    URLs_201_selenium = ['https://app.treet.fi/pharmacy/oulun-kaakkurin-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/oulun-kaakkurin-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/oulun-kaakkurin-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/oulun-kaakkurin-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/oulun-kaakkurin-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/oulun-kaakkurin-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/oulun-kaakkurin-apteekki/product/117648']

    fetched_data_201 = seltuot.treet_selenium(URLs_201_selenium)

    for i in fetched_data_201:
        i.append(pharmacy_url_201)
    medication.extend(fetched_data_201)

    # Pihtiputaan apteekki
    pharmacy_url_202 = "app.treet.fi/pharmacy/pihtiputaan-apteekki"
    URLs_202_selenium = ['https://app.treet.fi/pharmacy/pihtiputaan-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/pihtiputaan-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/pihtiputaan-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/pihtiputaan-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/pihtiputaan-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/pihtiputaan-apteekki/product/117648']

    fetched_data_202 = seltuot.treet_selenium(URLs_202_selenium)

    for i in fetched_data_202:
        i.append(pharmacy_url_202)
    medication.extend(fetched_data_202)

    # Kauppaporvarin apteekki
    pharmacy_url_203 = "app.treet.fi/pharmacy/kauppaporvarin-apteekki"
    URLs_203_selenium = ['https://app.treet.fi/pharmacy/kauppaporvarin-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/kauppaporvarin-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kauppaporvarin-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/kauppaporvarin-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/kauppaporvarin-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kauppaporvarin-apteekki/product/057965']

    fetched_data_203 = seltuot.treet_selenium(URLs_203_selenium)

    for i in fetched_data_203:
        i.append(pharmacy_url_203)
    medication.extend(fetched_data_203)

    # Tammisaaren uusi apteekki
    pharmacy_url_204 = "app.treet.fi/pharmacy/tammisaaren-uusi-apteekki"
    URLs_204_selenium = ['https://app.treet.fi/pharmacy/tammisaaren-uusi-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/tammisaaren-uusi-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/tammisaaren-uusi-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/tammisaaren-uusi-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/tammisaaren-uusi-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/tammisaaren-uusi-apteekki/product/057965']

    fetched_data_204 = seltuot.treet_selenium(URLs_204_selenium)

    for i in fetched_data_204:
        i.append(pharmacy_url_204)
    medication.extend(fetched_data_204)
    
    # Apteekki sastamala
    pharmacy_url_205 = "app.treet.fi/pharmacy/apteekki-sastamala"
    URLs_205_selenium = ['https://app.treet.fi/pharmacy/apteekki-sastamala/product/131583',
                         'https://app.treet.fi/pharmacy/apteekki-sastamala/product/519994',
                         'https://app.treet.fi/pharmacy/apteekki-sastamala/product/056698',
                         'https://app.treet.fi/pharmacy/apteekki-sastamala/product/048769',
                         'https://app.treet.fi/pharmacy/apteekki-sastamala/product/117648',
                         'https://app.treet.fi/pharmacy/apteekki-sastamala/product/057965']

    fetched_data_205 = seltuot.treet_selenium(URLs_205_selenium)

    for i in fetched_data_205:
        i.append(pharmacy_url_205)
    medication.extend(fetched_data_205)

    # Siilinjärven 1. apteekki
    pharmacy_url_206 = "app.treet.fi/pharmacy/siilinjarven-apteekki"
    URLs_206_selenium = ['https://app.treet.fi/pharmacy/siilinjarven-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/siilinjarven-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/siilinjarven-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/siilinjarven-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/siilinjarven-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/siilinjarven-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/siilinjarven-apteekki/product/057965']

    fetched_data_206 = seltuot.treet_selenium(URLs_206_selenium)

    for i in fetched_data_206:
        i.append(pharmacy_url_206)
    medication.extend(fetched_data_206)

    # Sammon apteekki
    pharmacy_url_207 = "app.treet.fi/pharmacy/sammon-apteekki"
    URLs_207_selenium = ['https://app.treet.fi/pharmacy/sammon-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/sammon-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/sammon-apteekki/product/056698',
                         'https://app.treet.fi/pharmacy/sammon-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/sammon-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/sammon-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/sammon-apteekki/product/057965']

    fetched_data_207 = seltuot.treet_selenium(URLs_207_selenium)

    for i in fetched_data_207:
        i.append(pharmacy_url_207)
    medication.extend(fetched_data_207)

    # Raunistulan apteekki
    pharmacy_url_208 = "app.treet.fi/pharmacy/raunistulan-apteekki"
    URLs_208_selenium = ['https://app.treet.fi/pharmacy/raunistulan-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/raunistulan-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/raunistulan-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/raunistulan-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/raunistulan-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/raunistulan-apteekki/product/056698']

    fetched_data_208 = seltuot.treet_selenium(URLs_208_selenium)

    for i in fetched_data_208:
        i.append(pharmacy_url_208)
    medication.extend(fetched_data_208)

    # Uusi apteekki
    pharmacy_url_209 = "app.treet.fi/pharmacy/uudenkaupungin-uusi-apteekki"
    URLs_209_selenium = ['https://app.treet.fi/pharmacy/uudenkaupungin-uusi-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/uudenkaupungin-uusi-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/uudenkaupungin-uusi-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/uudenkaupungin-uusi-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/uudenkaupungin-uusi-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/uudenkaupungin-uusi-apteekki/product/056698']

    fetched_data_209 = seltuot.treet_selenium(URLs_209_selenium)

    for i in fetched_data_209:
        i.append(pharmacy_url_209)
    medication.extend(fetched_data_209)

    # Koskikaran apteekki
    pharmacy_url_210 = "app.treet.fi/pharmacy/koskikaran-apteekki"
    URLs_210_selenium = ['https://app.treet.fi/pharmacy/koskikaran-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/koskikaran-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/koskikaran-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/koskikaran-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/koskikaran-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/koskikaran-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/koskikaran-apteekki/product/056698']

    fetched_data_210 = seltuot.treet_selenium(URLs_210_selenium)

    for i in fetched_data_210:
        i.append(pharmacy_url_210)
    medication.extend(fetched_data_210)

    # Kivistön apteekki
    pharmacy_url_211 = "app.treet.fi/pharmacy/kiviston-apteekki"
    URLs_211_selenium = ['https://app.treet.fi/pharmacy/kiviston-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/kiviston-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/kiviston-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/kiviston-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/kiviston-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/kiviston-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/kiviston-apteekki/product/056698']

    fetched_data_211 = seltuot.treet_selenium(URLs_211_selenium)

    for i in fetched_data_211:
        i.append(pharmacy_url_211)
    medication.extend(fetched_data_211)

    # Pakilan apteekki
    pharmacy_url_212 = "kehaykkosenapteekki.fi"
    URLs_212_normi = ['https://www.kehaykkosenapteekki.fi/epages/K1A.sf/fi_FI/?ObjectPath=/Shops/K1A/Products/117648',
                      'https://www.kehaykkosenapteekki.fi/epages/K1A.sf/fi_FI/?ObjectPath=/Shops/K1A/Products/048769',
                      'https://www.kehaykkosenapteekki.fi/epages/K1A.sf/fi_FI/?ObjectPath=/Shops/K1A/Products/134589',
                      'https://www.kehaykkosenapteekki.fi/epages/K1A.sf/fi_FI/?ObjectPath=/Shops/K1A/Products/057965',
                      'https://www.kehaykkosenapteekki.fi/epages/K1A.sf/fi_FI/?ObjectPath=/Shops/K1A/Products/056698',
                      'https://www.kehaykkosenapteekki.fi/epages/K1A.sf/fi_FI/?ObjectPath=/Shops/K1A/Products/519994',
                      'https://www.kehaykkosenapteekki.fi/epages/K1A.sf/fi_FI/?ObjectPath=/Shops/K1A/Products/131583']

    fetched_data_212 = nt.pakilanapteekki(URLs_212_normi)

    for i in fetched_data_212:
        i.append(pharmacy_url_212)
    medication.extend(fetched_data_212)

    # Munkkivuoren apteekki
    pharmacy_url_213 = "apteekkipaikka.fi"
    URLs_213_normi = ['https://www.apteekkipaikka.fi/epages/mva.sf/fi_FI/?ObjectID=39263',
                      'https://www.apteekkipaikka.fi/epages/mva.sf/fi_FI/?ObjectID=39301',
                      'https://www.apteekkipaikka.fi/epages/mva.sf/fi_FI/?ObjectID=40335',
                      'https://www.apteekkipaikka.fi/epages/mva.sf/fi_FI/?ObjectID=41263',
                      'https://www.apteekkipaikka.fi/epages/mva.sf/fi_FI/?ObjectID=39438',
                      'https://www.apteekkipaikka.fi/epages/mva.sf/fi_FI/?ObjectID=42648']

    fetched_data_213 = nt.pakilanapteekki(URLs_213_normi)

    for i in fetched_data_213:
        i.append(pharmacy_url_213)
    medication.extend(fetched_data_213)

    # Apteekki 360 ympyrätalo
    pharmacy_url_214 = "apteekki360.fi"
    URLs_214 = ['https://apteekki360.fi/products/burana-400-mg-kalvopaallysteinen-tabletti?_pos=1&_sid=2acd94771&_ss=r&_fid=5fd402d21&variant=42450129715452',
                'https://apteekki360.fi/products/hydrokortisoni-10mg-emulsio-voide?_pos=3&_sid=7d49435e6&_ss=r&_fid=20d740a87&variant=42450215502076',
                'https://apteekki360.fi/products/panadol-500-mg-tabletti-kalvopaallysteinen?variant=42450455199996',
                'https://apteekki360.fi/products/somac-control-20mg-enterotabletti?variant=42450230903036',
                'https://apteekki360.fi/products/voltaren-forte-232-mg-g-geeli?_pos=1&_sid=fae615ad5&_ss=r&_fid=5cc1a4f14&variant=42450090492156',
                'https://apteekki360.fi/products/zyrtec-10mg-tabletti-kalvopaallysteinen?variant=42450559336700']

    fetched_data_214 = nt.ympyrätalonapteekki(URLs_214)

    for i in fetched_data_214:
        i.append(pharmacy_url_214)
    medication.extend(fetched_data_214)

    # Itä-Suomen yliopiston apteekki
    pharmacy_url_215 = "yliopistonverkkoapteekki.fi"
    URLs_215_selenium = ['https://www.yliopistonverkkoapteekki.fi/epages/KYA.sf/fi_FI/?ObjectPath=/Shops/KYA/Products/405069',
                         'https://www.yliopistonverkkoapteekki.fi/epages/KYA.sf/fi_FI/?ObjectPath=/Shops/KYA/Products/436162',
                         'https://www.yliopistonverkkoapteekki.fi/epages/KYA.sf/fi_FI/?ObjectPath=/Shops/KYA/Products/056686/SubProducts/056686',
                         'https://www.yliopistonverkkoapteekki.fi/epages/KYA.sf/fi_FI/?ObjectPath=/Shops/KYA/Products/133965',
                         'https://www.yliopistonverkkoapteekki.fi/epages/KYA.sf/fi_FI/?ObjectPath=/Shops/KYA/Products/461889/SubProducts/461889']

    URLs_215_normi = ['https://www.yliopistonverkkoapteekki.fi/epages/KYA.sf/fi_FI/?ObjectID=26394108',
                      'https://www.yliopistonverkkoapteekki.fi/epages/KYA.sf/fi_FI/?ObjectID=38765905']

    data_values_215 = ['118079', '117660', '120017', '120666', '118079']

    fetched_data_215_first = seltuot.isyliopistonapteekki_selenium(URLs_215_selenium, data_values_215)
    fetched_data_215_second = nt.pakilanapteekki(URLs_215_normi)

    for i in fetched_data_215_first + fetched_data_215_second:
        i.append(pharmacy_url_215)
    medication.extend(fetched_data_215_first + fetched_data_215_second)

    # Ivalon apteekki
    pharmacy_url_216 = "iapteekki.fi"
    URLs_216_normi = ['https://www.iapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/',
                      'https://www.iapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.iapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://www.iapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://www.iapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/']

    fetched_data_216 = nt.ivalonapteekki(URLs_216_normi)

    for i in fetched_data_216:
        i.append(pharmacy_url_216)
    medication.extend(fetched_data_216)

    # Turengin apteekki
    pharmacy_url_217 = "janakkalan-turengin-apteekki.eapteekki.fi"
    URLs_217_normi = ['https://janakkalan-turengin-apteekki.eapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://janakkalan-turengin-apteekki.eapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://janakkalan-turengin-apteekki.eapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://janakkalan-turengin-apteekki.eapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://janakkalan-turengin-apteekki.eapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://janakkalan-turengin-apteekki.eapteekki.fi/tuotteet/398/nenan-tukkoisuus/91351/134589-otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mgml-khon/']

    fetched_data_217 = nt.ivalonapteekki(URLs_217_normi)

    for i in fetched_data_217:
        i.append(pharmacy_url_217)
    medication.extend(fetched_data_217)

    # Järvenpään lähiapteekki
    pharmacy_url_218 = "verkkoapteekki.fi"
    URLs_218_normi = ['https://www.verkkoapteekki.fi/epages/verkkoapteekki.sf/fi_FI/?ObjectID=24919127',
                      'https://www.verkkoapteekki.fi/epages/verkkoapteekki.sf/fi_FI/?ObjectPath=/Shops/verkkoapteekki/Products/117648',
                      'https://www.verkkoapteekki.fi/epages/verkkoapteekki.sf/fi_FI/?ObjectID=24918024',
                      'https://www.verkkoapteekki.fi/epages/verkkoapteekki.sf/fi_FI/?ObjectPath=/Shops/verkkoapteekki/Products/056698',
                      'https://www.verkkoapteekki.fi/epages/verkkoapteekki.sf/fi_FI/?ObjectID=24918174',
                      'https://www.verkkoapteekki.fi/epages/verkkoapteekki.sf/fi_FI/?ObjectID=24921884',
                      'https://www.verkkoapteekki.fi/epages/verkkoapteekki.sf/fi_FI/?ObjectID=26447441']

    fetched_data_218 = nt.pakilanapteekki(URLs_218_normi)

    for i in fetched_data_218:
        i.append(pharmacy_url_218)
    medication.extend(fetched_data_218)

    # Kangasalan 1. apteekki
    pharmacy_url_219 = "laakeverkkokauppa.fi"
    URLs_219_normi = ['https://www.laakeverkkokauppa.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/',
                      'https://www.laakeverkkokauppa.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.laakeverkkokauppa.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://www.laakeverkkokauppa.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://www.laakeverkkokauppa.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://www.laakeverkkokauppa.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/']

    fetched_data_219 = nt.ivalonapteekki(URLs_219_normi)

    for i in fetched_data_219:
        i.append(pharmacy_url_219)
    medication.extend(fetched_data_219)

    # Kauhavan ykköapteekki
    pharmacy_url_220 = "ykkosapteekki.fi"
    URLs_220_normi = ['https://www.ykkosapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/',
                      'https://www.ykkosapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.ykkosapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://www.ykkosapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://www.ykkosapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://www.ykkosapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://www.ykkosapteekki.fi/tuotteet/398/nenan-tukkoisuus/91351/134589-otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mgml-10-ml/']

    fetched_data_220 = nt.ivalonapteekki(URLs_220_normi)

    for i in fetched_data_220:
        i.append(pharmacy_url_220)
    medication.extend(fetched_data_220)

    # Kokkolan 3. apteekki (Keskusapteekki)
    pharmacy_url_221 = "kokkolanverkkoapteekki.fi"
    URLs_221_normi = ['https://www.kokkolanverkkoapteekki.fi/epages/kokkolanverkkoapteekki.sf/fi_FI/?ObjectID=180847',
                      'https://www.kokkolanverkkoapteekki.fi/epages/kokkolanverkkoapteekki.sf/fi_FI/?ObjectID=180714',
                      'https://www.kokkolanverkkoapteekki.fi/epages/kokkolanverkkoapteekki.sf/fi_FI/?ObjectPath=/Shops/kokkolanverkkoapteekki/Products/117648',
                      'https://www.kokkolanverkkoapteekki.fi/epages/kokkolanverkkoapteekki.sf/fi_FI/?ObjectID=180915',
                      'https://www.kokkolanverkkoapteekki.fi/epages/kokkolanverkkoapteekki.sf/fi_FI/?ObjectID=180248',
                      'https://www.kokkolanverkkoapteekki.fi/epages/kokkolanverkkoapteekki.sf/fi_FI/?ObjectPath=/Shops/kokkolanverkkoapteekki/Products/134589',
                      'https://www.kokkolanverkkoapteekki.fi/epages/kokkolanverkkoapteekki.sf/fi_FI/?ObjectID=180492']

    fetched_data_221 = nt.pakilanapteekki(URLs_221_normi)

    for i in fetched_data_221:
        i.append(pharmacy_url_221)
    medication.extend(fetched_data_221)

    # Kotkan ankkuriapteekki
    pharmacy_url_222 = "tarjousapteekki.fi"
    URLs_222_normi = ['https://www.tarjousapteekki.fi/epages/TA.sf/fi_FI/?ObjectPath=/Shops/TA/Products/056698',
                      'https://www.tarjousapteekki.fi/epages/TA.sf/fi_FI/?ObjectPath=/Shops/TA/Products/057965',
                      'https://www.tarjousapteekki.fi/epages/TA.sf/fi_FI/?ObjectPath=/Shops/TA/Products/117648',
                      'https://www.tarjousapteekki.fi/epages/TA.sf/fi_FI/?ObjectPath=/Shops/TA/Products/519994',
                      'https://www.tarjousapteekki.fi/epages/TA.sf/fi_FI/?ObjectID=34988',
                      'https://www.tarjousapteekki.fi/epages/TA.sf/fi_FI/?ObjectPath=/Shops/TA/Products/048769']

    fetched_data_222 = nt.pakilanapteekki(URLs_222_normi)

    for i in fetched_data_222:
        i.append(pharmacy_url_222)
    medication.extend(fetched_data_222)

    # Inkeroisten apteekki
    pharmacy_url_223 = "kouvolan-inkeroisten-apteekki.eapteekki.fi"
    URLs_223_normi = ['https://kouvolan-inkeroisten-apteekki.eapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://kouvolan-inkeroisten-apteekki.eapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/',
                      'https://kouvolan-inkeroisten-apteekki.eapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://kouvolan-inkeroisten-apteekki.eapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://kouvolan-inkeroisten-apteekki.eapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://kouvolan-inkeroisten-apteekki.eapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/']

    fetched_data_223 = nt.ivalonapteekki(URLs_223_normi)

    for i in fetched_data_223:
        i.append(pharmacy_url_223)
    medication.extend(fetched_data_223)

    # Teerijärven apteekki
    pharmacy_url_224 = "apteekkini.fi"
    URLs_224_normi = ['https://www.apteekkini.fi/epages/apteekkini.sf/fi_FI/?ObjectPath=/Shops/09022011-998764/Products/056698',
                      'https://www.apteekkini.fi/epages/apteekkini.sf/fi_FI/?ObjectPath=/Shops/09022011-998764/Products/057965',
                      'https://www.apteekkini.fi/epages/apteekkini.sf/fi_FI/?ObjectPath=/Shops/09022011-998764/Products/117648',
                      'https://www.apteekkini.fi/epages/apteekkini.sf/fi_FI/?ObjectPath=/Shops/09022011-998764/Products/519994',
                      'https://www.apteekkini.fi/epages/apteekkini.sf/fi_FI/?ObjectPath=/Shops/09022011-998764/Products/131583',
                      'https://www.apteekkini.fi/epages/apteekkini.sf/fi_FI/?ObjectPath=/Shops/09022011-998764/Products/134589',
                      'https://www.apteekkini.fi/epages/apteekkini.sf/fi_FI/?ObjectID=24354744']

    fetched_data_224 = nt.pakilanapteekki(URLs_224_normi)

    for i in fetched_data_224:
        i.append(pharmacy_url_224)
    medication.extend(fetched_data_224)

    # Kuhmon apteekki
    pharmacy_url_225 = "suomiapteekki.fi"
    URLs_225_normi = ['https://www.suomiapteekki.fi/epages/Kuhmonapteekki.sf/fi_FI/?ObjectPath=/Shops/Kuhmonapteekki/Products/056698',
                      'https://www.suomiapteekki.fi/epages/Kuhmonapteekki.sf/fi_FI/?ObjectPath=/Shops/Kuhmonapteekki/Products/057965',
                      'https://www.suomiapteekki.fi/epages/Kuhmonapteekki.sf/fi_FI/?ObjectPath=/Shops/Kuhmonapteekki/Products/117648',
                      'https://www.suomiapteekki.fi/epages/Kuhmonapteekki.sf/fi_FI/?ObjectPath=/Shops/Kuhmonapteekki/Products/519994',
                      'https://www.suomiapteekki.fi/epages/Kuhmonapteekki.sf/fi_FI/?ObjectID=26153002',
                      'https://www.suomiapteekki.fi/epages/Kuhmonapteekki.sf/fi_FI/?ObjectID=26153287']

    fetched_data_225 = nt.pakilanapteekki(URLs_225_normi)

    for i in fetched_data_225:
        i.append(pharmacy_url_225)
    medication.extend(fetched_data_225)

    # Lähiapteekki syke
    pharmacy_url_226 = "etuapteekki.fi"
    URLs_226_normi = ['https://www.etuapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://www.etuapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.etuapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://www.etuapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://www.etuapteekki.fi/tuotteet/398/nenan-tukkoisuus/91351/134589-otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mgml-10-ml/',
                      'https://www.etuapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/']

    fetched_data_226 = nt.ivalonapteekki(URLs_226_normi)

    for i in fetched_data_226:
        i.append(pharmacy_url_226)
    medication.extend(fetched_data_226)

    # Apteekki ideapark
    pharmacy_url_227 = "apteekki-ideapark.eapteekki.fi"
    URLs_227_normi = [
        'https://www.apteekkiideapark.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
        'https://www.apteekkiideapark.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/',
        'https://www.apteekkiideapark.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
        'https://www.apteekkiideapark.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
        'https://www.apteekkiideapark.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
        'https://www.apteekkiideapark.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/']

    fetched_data_227 = nt.ivalonapteekki(URLs_227_normi)

    for i in fetched_data_227:
        i.append(pharmacy_url_227)
    medication.extend(fetched_data_227)

    # Virkkalan omena-apteekki
    pharmacy_url_228 = "apo24.fi"
    URLs_228_normi = ['https://www.apo24.fi/epages/apo24.sf/sec6038248e42/?ObjectPath=/Shops/apo24/Products/519994',
                      'https://www.apo24.fi/epages/apo24.sf/sec6038248e42/?ObjectPath=/Shops/apo24/Products/056698',
                      'https://www.apo24.fi/epages/apo24.sf/fi_FI/?ObjectPath=/Shops/apo24/Products/057965',
                      'https://www.apo24.fi/epages/apo24.sf/sec6038248e42/?ObjectPath=/Shops/apo24/Products/131583',
                      'https://www.apo24.fi/epages/apo24.sf/sec6038248e42/?ObjectPath=/Shops/apo24/Products/048769',
                      'https://www.apo24.fi/epages/apo24.sf/fi_FI/?ObjectPath=/Shops/apo24/Products/117648']

    fetched_data_228 = nt.pakilanapteekki(URLs_228_normi)

    for i in fetched_data_228:
        i.append(pharmacy_url_228)
    medication.extend(fetched_data_228)

    # Loimaan uusi apteekki
    pharmacy_url_229 = "loimaan-uusi.eapteekki.fi"
    URLs_229_normi = ['https://loimaan-uusi.eapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://loimaan-uusi.eapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://loimaan-uusi.eapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/',
                      'https://loimaan-uusi.eapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://loimaan-uusi.eapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://loimaan-uusi.eapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/']

    fetched_data_229 = nt.ivalonapteekki(URLs_229_normi)

    for i in fetched_data_229:
        i.append(pharmacy_url_229)
    medication.extend(fetched_data_229)

    # Lopen apteekki
    pharmacy_url_230 = "lopen-apteekki.eapteekki.fi"
    URLs_230_normi = ['https://lopen-apteekki.eapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://lopen-apteekki.eapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://lopen-apteekki.eapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/',
                      'https://lopen-apteekki.eapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://lopen-apteekki.eapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://lopen-apteekki.eapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/']

    fetched_data_230 = nt.ivalonapteekki(URLs_230_normi)

    for i in fetched_data_230:
        i.append(pharmacy_url_230)
    medication.extend(fetched_data_230)

    # Seitsemän veljeksen apteekki
    pharmacy_url_231 = "nettiapteekki.fi"
    URLs_231_normi = ['https://www.nettiapteekki.fi/products/voltaren-forte-232-mg-g-geeli-tamro-1?variant=31963895267375',
                      'https://www.nettiapteekki.fi/products/somac-control-20-mg-enterotabl-tamro?variant=31963894644783',
                      'https://www.nettiapteekki.fi/products/panadol-500-mg-tabl-kalvopaall-tamro-2?variant=40204627836975',
                      'https://www.nettiapteekki.fi/products/zyrtec-10-mg-tabl-kalvopaall-oriola?variant=32463933472815',
                      'https://www.nettiapteekki.fi/products/otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mg-ml-khone-pumppu-10-ml?_pos=6&_psq=otrivin&_ss=e&_v=1.0',
                      'https://www.nettiapteekki.fi/products/hydrocortison-10-mg-g-emuls-voide-oriola?_pos=2&_sid=577e59eed&_ss=r',
                      'https://www.nettiapteekki.fi/products/burana-400-mg-tabl?variant=31962297794607']

    fetched_data_231 = nt.seitsemänveljeksenapteekki(URLs_231_normi)

    for i in fetched_data_231:
        i.append(pharmacy_url_231)
    medication.extend(fetched_data_231)

    # Orimattilan 1. apteekki
    pharmacy_url_232 = "orimattilanapteekki.fi"
    URLs_232_normi = ['https://www.orimattilanapteekki.fi/epages/OrimattilanApteekki.sf/fi_FI/?ObjectPath=/Shops/OrimattilanApteekki/Products/519994',
                      'https://www.orimattilanapteekki.fi/epages/OrimattilanApteekki.sf/fi_FI/?ObjectPath=/Shops/OrimattilanApteekki/Products/056698',
                      'https://www.orimattilanapteekki.fi/epages/OrimattilanApteekki.sf/fi_FI/?ObjectPath=/Shops/OrimattilanApteekki/Products/057965',
                      'https://www.orimattilanapteekki.fi/epages/OrimattilanApteekki.sf/fi_FI/?ObjectPath=/Shops/OrimattilanApteekki/Products/131583',
                      'https://www.orimattilanapteekki.fi/epages/OrimattilanApteekki.sf/fi_FI/?ObjectPath=/Shops/OrimattilanApteekki/Products/134589',
                      'https://www.orimattilanapteekki.fi/epages/OrimattilanApteekki.sf/fi_FI/?ObjectPath=/Shops/OrimattilanApteekki/Products/048769',
                      'https://www.orimattilanapteekki.fi/epages/OrimattilanApteekki.sf/fi_FI/?ObjectPath=/Shops/OrimattilanApteekki/Products/117648']

    fetched_data_232 = nt.pakilanapteekki(URLs_232_normi)

    for i in fetched_data_232:
        i.append(pharmacy_url_232)
    medication.extend(fetched_data_232)

    # Hansa apteekki
    pharmacy_url_233 = "nettiterveysapteekki.fi"
    URLs_233_normi = ['https://www.nettiterveysapteekki.fi/voltaren_forte_232_mgg_geeli_100_g',
                      'https://www.nettiterveysapteekki.fi/zyrtec_10_mg_tabletti_kalvopaallysteinen_30_lapipainopakkaus',
                      'https://www.nettiterveysapteekki.fi/hydrocortison_1__emulsiovoide_20_g',
                      'https://www.nettiterveysapteekki.fi/burana_400_mg_tabletti_kalvopaallysteinen_30_lapipainopakkaus']

    fetched_data_233 = nt.pakilanapteekki(URLs_233_normi)

    for i in fetched_data_233:
        i.append(pharmacy_url_233)
    medication.extend(fetched_data_233)

    # Porin Karhu apteekki
    pharmacy_url_234 = "karhuapteekki.fi"
    URLs_234_normi = ['https://www.karhuapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://www.karhuapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://www.karhuapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://www.karhuapteekki.fi/tuotteet/398/nenan-tukkoisuus/91351/134589-otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mgml-khon/',
                      'https://www.karhuapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://www.karhuapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.karhuapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/']

    fetched_data_234 = nt.ivalonapteekki(URLs_234_normi)

    for i in fetched_data_234:
        i.append(pharmacy_url_234)
    medication.extend(fetched_data_234)

    # Porvoon uusi apteekki
    pharmacy_url_235 = "apteekkipiste.fi"
    URLs_235_normi = ['https://www.apteekkipiste.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://www.apteekkipiste.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://www.apteekkipiste.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://www.apteekkipiste.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://www.apteekkipiste.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.apteekkipiste.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/']

    fetched_data_235 = nt.ivalonapteekki(URLs_235_normi)

    for i in fetched_data_235:
        i.append(pharmacy_url_235)
    medication.extend(fetched_data_235)

    # Myllyn apteekki
    pharmacy_url_236 = "myllynapteekki.fi"
    URLs_236_normi = ['https://app.treet.fi/pharmacy/myllyn-apteekki/product/131583',
                      'https://app.treet.fi/pharmacy/myllyn-apteekki/product/519994',
                      'https://app.treet.fi/pharmacy/myllyn-apteekki/product/056698',
                      'https://app.treet.fi/pharmacy/myllyn-apteekki/product/134589',
                      'https://app.treet.fi/pharmacy/myllyn-apteekki/product/048769',
                      'https://app.treet.fi/pharmacy/myllyn-apteekki/product/117648',
                      'https://app.treet.fi/pharmacy/myllyn-apteekki/product/057965']

    fetched_data_236 = seltuot.treet_selenium(URLs_236_normi)

    for i in fetched_data_236:
        i.append(pharmacy_url_236)
    medication.extend(fetched_data_236)

    # Saarijärven apteekki
    pharmacy_url_237 = "saarijarvenapteekki.fi"
    URLs_237_selenium = ['https://app.treet.fi/pharmacy/saarijarven-apteekki/product/134589',
                         'https://app.treet.fi/pharmacy/saarijarven-apteekki/product/131583',
                         'https://app.treet.fi/pharmacy/saarijarven-apteekki/product/519994',
                         'https://app.treet.fi/pharmacy/saarijarven-apteekki/product/048769',
                         'https://app.treet.fi/pharmacy/saarijarven-apteekki/product/117648',
                         'https://app.treet.fi/pharmacy/saarijarven-apteekki/product/057965',
                         'https://app.treet.fi/pharmacy/saarijarven-apteekki/product/056698']

    fetched_data_237 = seltuot.treet_selenium(URLs_237_selenium)

    for i in fetched_data_237:
        i.append(pharmacy_url_237)
    medication.extend(fetched_data_237)

    # Keskus-apteekki
    pharmacy_url_238 = "aitoapteekki.fi"
    URLs_238_normi = ['https://www.aitoapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://www.aitoapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://www.aitoapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://www.aitoapteekki.fi/tuotteet/398/nenan-tukkoisuus/91351/134589-otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mgml-10-ml/',
                      'https://www.aitoapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://www.aitoapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.aitoapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/']

    fetched_data_238 = nt.ivalonapteekki(URLs_238_normi)

    for i in fetched_data_238:
        i.append(pharmacy_url_238)
    medication.extend(fetched_data_238)

    # Koivu apteekki
    pharmacy_url_239 = "koivuapteekki.fi"
    URLs_239_normi = ['https://www.koivuapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://www.koivuapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://www.koivuapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/',
                      'https://www.koivuapteekki.fi/tuotteet/398/nenan-tukkoisuus/91351/134589-otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mgml-khon/',
                      'https://www.koivuapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://www.koivuapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.koivuapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/']

    fetched_data_239 = nt.ivalonapteekki(URLs_239_normi)

    for i in fetched_data_239:
        i.append(pharmacy_url_239)
    medication.extend(fetched_data_239)

    # Lielahden apteekki
    pharmacy_url_240 = "apteekkishop.fi"
    URLs_240_normi = ['https://www.apteekkishop.fi/epages/ApteekkiShop.sf/fi_FI/?ObjectPath=/Shops/ApteekkiShop/Products/131583',
                      'https://www.apteekkishop.fi/epages/ApteekkiShop.sf/fi_FI/?ObjectID=35855100',
                      'https://www.apteekkishop.fi/epages/ApteekkiShop.sf/fi_FI/?ObjectPath=/Shops/ApteekkiShop/Products/056698',
                      'https://www.apteekkishop.fi/epages/ApteekkiShop.sf/fi_FI/?ObjectID=42264371',
                      'https://www.apteekkishop.fi/epages/ApteekkiShop.sf/fi_FI/?ObjectID=35854579',
                      'https://www.apteekkishop.fi/epages/ApteekkiShop.sf/fi_FI/?ObjectID=35854521',
                      'https://www.apteekkishop.fi/epages/ApteekkiShop.sf/fi_FI/?ObjectPath=/Shops/ApteekkiShop/Products/057965']

    fetched_data_240 = nt.ivalonapteekki(URLs_240_normi)

    for i in fetched_data_240:
        i.append(pharmacy_url_240)
    medication.extend(fetched_data_240)

    # Tammedica apteekki
    pharmacy_url_241 = "247apteekkiin.fi"
    URLs_241_normi = ['https://www.247apteekkiin.fi/epages/TCA.sf/fi_FI/?ObjectID=1057054',
                      'https://www.247apteekkiin.fi/epages/TCA.sf/fi_FI/?ObjectID=48540',
                      'https://www.247apteekkiin.fi/epages/TCA.sf/fi_FI/?ObjectID=39458',
                      'https://www.247apteekkiin.fi/epages/TCA.sf/fi_FI/?ObjectID=40640',
                      'https://www.247apteekkiin.fi/epages/TCA.sf/fi_FI/?ObjectPath=/Shops/TCA/Products/117648',
                      'https://www.247apteekkiin.fi/epages/TCA.sf/fi_FI/?ObjectID=48549',
                      'https://www.247apteekkiin.fi/epages/TCA.sf/fi_FI/?ObjectID=40760']

    fetched_data_241 = nt.pakilanapteekki(URLs_241_normi)

    for i in fetched_data_241:
        i.append(pharmacy_url_241)
    medication.extend(fetched_data_241)

    # Länsikeskuksen apteekki
    pharmacy_url_242 = "apteekkituotteet.fi"
    URLs_242_selenium = ['https://www.apteekkituotteet.fi/epages/Kaupat.sf/fi_FI/?ObjectPath=/Shops/Eura/Products/0461889',
                         'https://www.apteekkituotteet.fi/epages/Kaupat.sf/fi_FI/?ObjectPath=/Shops/Eura/Products/0502546',
                         'https://www.apteekkituotteet.fi/epages/Kaupat.sf/fi_FI/?ObjectPath=/Shops/Eura/Products/0436162',
                         'https://www.apteekkituotteet.fi/epages/Kaupat.sf/fi_FI/?ObjectPath=/Shops/Eura/Products/0370842',
                         'https://www.apteekkituotteet.fi/epages/Kaupat.sf/fi_FI/?ObjectPath=/Shops/Eura/Products/0056686']

    URLs_242_normi = ['https://www.apteekkituotteet.fi/epages/Kaupat.sf/fi_FI/?ObjectID=36156901',
                      'https://www.apteekkituotteet.fi/epages/Kaupat.sf/fi_FI/?ObjectPath=/Shops/Eura/Products/0478800']

    data_values_242 = ['12911301', '12911367', '12911299', '12911301', '12911316']

    fetched_data_242_first = seltuot.lansikeskuksenapteekki_selenium(URLs_242_selenium, data_values_242)
    fetched_data_242_second = nt.pakilanapteekki(URLs_242_normi)

    for i in fetched_data_242_first + fetched_data_242_second:
        i.append(pharmacy_url_242)
    medication.extend(fetched_data_242_first + fetched_data_242_second)

    # Hirvensalon apteekki
    pharmacy_url_243 = "saaristoapteekki.fi"
    URLs_243_normi = ['https://saaristoapteekki.fi/tuotteet/398/nenan-tukkoisuus/91351/134589-otrivin-menthol-sailytysaineeton-nenasumute-liuos-1-mgml-10-ml/',
                      'https://saaristoapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://saaristoapteekki.fi/tuotteet/396/kivun-paikallishoito/44610/519994-voltaren-forte-geeli-232-mgg-100-g/',
                      'https://saaristoapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://saaristoapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://saaristoapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/']

    fetched_data_243 = nt.ivalonapteekki(URLs_243_normi)

    for i in fetched_data_243:
        i.append(pharmacy_url_243)
    medication.extend(fetched_data_243)

    # Wiklundin apteekki
    pharmacy_url_244 = "apteekkiplus.fi"
    URLs_244_normi = ['https://www.apteekkiplus.fi/products/otrivin-menthol-sailytysaineeton-1-mg-ml-10-ml-nenasumute-liuos-khone-pumppu?variant=49062410256721',
                      'https://www.apteekkiplus.fi/products/zyrtec-10-mg?variant=17279512051827',
                      'https://www.apteekkiplus.fi/products/voltaren-forte-23-2-mg-g?variant=47979728404817',
                      'https://www.apteekkiplus.fi/products/hydrocortison-1?variant=17280046235763',
                      'https://www.apteekkiplus.fi/products/burana-400-mg?variant=17280296091763',
                      'https://www.apteekkiplus.fi/products/panadol-500-mg-tabletti?variant=39644707192947',
                      'https://www.apteekkiplus.fi/products/somac-control-20-mg?variant=17276947693683']

    fetched_data_244 = nt.wiklundinapteekki(URLs_244_normi)

    for i in fetched_data_244:
        i.append(pharmacy_url_244)
    medication.extend(fetched_data_244)

    # Pyhän Henrikin apteekki
    pharmacy_url_245 = "apteekkiverkkokauppa.fi"
    URLs_245_normi = ['https://www.apteekkiverkkokauppa.fi/epages/apteekkiverkkokauppa.sf/fi_FI/?ObjectID=25218679',
                      'https://www.apteekkiverkkokauppa.fi/epages/apteekkiverkkokauppa.sf/fi_FI/?ObjectID=24951573',
                      'https://www.apteekkiverkkokauppa.fi/epages/apteekkiverkkokauppa.sf/fi_FI/?ObjectPath=/Shops/PHA/Products/519994',
                      'https://www.apteekkiverkkokauppa.fi/epages/apteekkiverkkokauppa.sf/fi_FI/?ObjectID=24951604',
                      'https://www.apteekkiverkkokauppa.fi/epages/apteekkiverkkokauppa.sf/fi_FI/?ObjectPath=/Shops/PHA/Products/117648',
                      'https://www.apteekkiverkkokauppa.fi/epages/apteekkiverkkokauppa.sf/fi_FI/?ObjectPath=/Shops/PHA/Products/057965',
                      'https://www.apteekkiverkkokauppa.fi/epages/apteekkiverkkokauppa.sf/fi_FI/?ObjectID=24993188']

    fetched_data_245 = nt.pakilanapteekki(URLs_245_normi)

    for i in fetched_data_245:
        i.append(pharmacy_url_245)
    medication.extend(fetched_data_245)

    # Koivukylän apteekki
    pharmacy_url_246 = "apomera.fi"
    URLs_246_normi = ['https://www.apomera.fi/otrivin-menthol-sailytysaineeton-1-mg-10-ml',
                      'https://www.apomera.fi/zyrtec-10-mg-30-tablettia',
                      'https://www.apomera.fi/voltaren-forte-100-g',
                      'https://www.apomera.fi/hydrocortison-1-20-g',
                      'https://www.apomera.fi/burana-400-mg-30-kpl',
                      'https://www.apomera.fi/panadol-500-mg-30-kpl',
                      'https://www.apomera.fi/somac-control-20-mg-14-kpl']

    fetched_data_246 = nt.koivukylänapteekki(URLs_246_normi)

    for i in fetched_data_246:
        i.append(pharmacy_url_246)
    medication.extend(fetched_data_246)

    # Hyvän mielen apteekki
    pharmacy_url_247 = "bonusapteekki.fi"
    URLs_247_normi = ['https://www.bonusapteekki.fi/epages/Bonusapteekki.sf/fi_FI/?ObjectPath=/Shops/Bonusapteekki/Products/134589',
                      'https://www.bonusapteekki.fi/epages/Bonusapteekki.sf/fi_FI/?ObjectPath=/Shops/Bonusapteekki/Products/131583',
                      'https://www.bonusapteekki.fi/epages/Bonusapteekki.sf/fi_FI/?ObjectPath=/Shops/Bonusapteekki/Products/519994',
                      'https://www.bonusapteekki.fi/epages/Bonusapteekki.sf/fi_FI/?ObjectPath=/Shops/Bonusapteekki/Products/048769',
                      'https://www.bonusapteekki.fi/epages/Bonusapteekki.sf/fi_FI/?ObjectPath=/Shops/Bonusapteekki/Products/117648',
                      'https://www.bonusapteekki.fi/epages/Bonusapteekki.sf/fi_FI/?ObjectPath=/Shops/Bonusapteekki/Products/057965',
                      'https://www.bonusapteekki.fi/epages/Bonusapteekki.sf/fi_FI/?ObjectPath=/Shops/Bonusapteekki/Products/056698']

    fetched_data_247 = nt.pakilanapteekki(URLs_247_normi)

    for i in fetched_data_247:
        i.append(pharmacy_url_247)
    medication.extend(fetched_data_247)

    # Suolahden apteekki
    pharmacy_url_248 = "viherapteekki.fi"
    URLs_248_normi = ['https://www.viherapteekki.fi/tuotteet/361/antihistamiinit/32148/131583-zyrtec-tabletti-kalvopaallysteinen-10-mg-30-fol/',
                      'https://www.viherapteekki.fi/tuotteet/384/kortisonivoiteet-ja-geelit/23437/048769-hydrocortison-emulsiovoide-1-20-g/',
                      'https://www.viherapteekki.fi/tuotteet/492/ibuprofeeni/22545/117648-burana-tabletti-kalvopaallysteinen-400-mg-30-fol/',
                      'https://www.viherapteekki.fi/tuotteet/494/parasetamoli/80255/057965-panadol-tabletti-kalvopaallysteinen-500-mg-30-fol/',
                      'https://www.viherapteekki.fi/tuotteet/506/happosalpaajat/33614/056698-somac-control-enterotabletti-20-mg-14-fol/']

    fetched_data_248 = nt.ivalonapteekki(URLs_248_normi)

    for i in fetched_data_248:
        i.append(pharmacy_url_248)
    medication.extend(fetched_data_248)

    # Aabenraa Love Apotek
    pharmacy_url_249 = "apoteket-online.dk/apotek/aabenraa-loeve-apotek"
    URLs_249_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_249 = seltuot.apoteketonline_selenium(URLs_249_selenium, "Aabenraa Loeve")

    for i in fetched_data_249:
        i.append(pharmacy_url_249)
    medication.extend(fetched_data_249)

    # Aalborg Budolfi Apotek
    pharmacy_url_250 = "apoteket-online.dk/apotek/aalborg-budolfi-apotek"
    URLs_250_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_250 = seltuot.apoteketonline_selenium(URLs_250_selenium, "Aalborg Budolfi Apotek")

    for i in fetched_data_250:
        i.append(pharmacy_url_250)
    medication.extend(fetched_data_250)

    # Aalborg Loeve Apotek
    pharmacy_url_251 = "apoteket-online.dk/apotek/aalborg-loeve-apotek"
    URLs_251_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_251 = seltuot.apoteketonline_selenium(URLs_251_selenium, "Aalborg Loeve Apotek")

    for i in fetched_data_251:
        i.append(pharmacy_url_251)
    medication.extend(fetched_data_251)

    # Aalborg Reberbane Apotek
    pharmacy_url_252 = "apoteket-online.dk/apotek/aalborg-reberbane-apotek"
    URLs_252_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_252 = seltuot.apoteketonline_selenium(URLs_252_selenium, "Aalborg Reberbane Apotek")

    for i in fetched_data_252:
        i.append(pharmacy_url_252)
    medication.extend(fetched_data_252)

    # Aalborg Vejgaard Apotek
    pharmacy_url_253 = "apoteket-online.dk/apotek/aalborg-vejgaard-apotek"
    URLs_253_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_253 = seltuot.apoteketonline_selenium(URLs_253_selenium, "Aalborg Vejgaard Apotek")

    for i in fetched_data_253:
        i.append(pharmacy_url_253)
    medication.extend(fetched_data_253)

    # Aalborghus Apotek
    pharmacy_url_254 = "apoteket-online.dk/apotek/aalborghus-apotek"
    URLs_254_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_254 = seltuot.apoteketonline_selenium(URLs_254_selenium, "Aalborghus Apotek")

    for i in fetched_data_254:
        i.append(pharmacy_url_254)
    medication.extend(fetched_data_254)

    # Aarhus Loeve Apotek
    pharmacy_url_255 = "apoteket-online.dk/apotek/aarhus-loeve-apotek"
    URLs_255_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_255 = seltuot.apoteketonline_selenium(URLs_255_selenium, "Aarhus Loeve Apotek")

    for i in fetched_data_255:
        i.append(pharmacy_url_255)
    medication.extend(fetched_data_255)

    # Aarhus Stjerne Apotek
    pharmacy_url_256 = "apoteket-online.dk/apotek/aarhus-stjerne-apotek"
    URLs_256_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_256 = seltuot.apoteketonline_selenium(URLs_256_selenium, "Aarhus Stjerne Apotek")

    for i in fetched_data_256:
        i.append(pharmacy_url_256)
    medication.extend(fetched_data_256)

    # Aarhus Vejlby Apotek
    pharmacy_url_257 = "apoteket-online.dk/apotek/aarhus-vejlby-apotek"
    URLs_257_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_257 = seltuot.apoteketonline_selenium(URLs_257_selenium, "Aarhus Vejlby Apotek")

    for i in fetched_data_257:
        i.append(pharmacy_url_257)
    medication.extend(fetched_data_257)

    # Aarhus Viby Apotek
    pharmacy_url_258 = "apoteket-online.dk/apotek/aarhus-viby-apotek"
    URLs_258_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_258 = seltuot.apoteketonline_selenium(URLs_258_selenium, "Aarhus Viby Apotek")

    for i in fetched_data_258:
        i.append(pharmacy_url_258)
    medication.extend(fetched_data_258)

    # Aarhus Åbyhøj Apotek
    pharmacy_url_259 = "apoteket-online.dk/apotek/aarhus-aabyhoej-apotek"
    URLs_259_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_259 = seltuot.apoteketonline_selenium(URLs_259_selenium, "Aarhus Aabyhoej Apotek")

    for i in fetched_data_259:
        i.append(pharmacy_url_259)
    medication.extend(fetched_data_259)

    # Ringkoebing loeve apotek
    pharmacy_url_260 = "ringkoebing.dinapoteker.dk"
    URLs_260_selenium = ['https://www.dinapoteker.dk/a/ringkoebing/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/ringkoebing/panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/ringkoebing/pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/ringkoebing/voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/ringkoebing/alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/ringkoebing/otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/ringkoebing/mildison-lipid-10-mg-g-0-p43108']

    fetched_data_260 = seltuot.dinapoteker_selenium(URLs_260_selenium)

    for i in fetched_data_260:
        i.append(pharmacy_url_260)
    medication.extend(fetched_data_260)

    # Apoteket Lille Bjoern
    pharmacy_url_261 = "apoteket-online.dk/apotek/apoteket-lille-bjoern"
    URLs_261_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_261 = seltuot.apoteketonline_selenium(URLs_261_selenium, "Apoteket Lille Bjoern")

    for i in fetched_data_261:
        i.append(pharmacy_url_261)
    medication.extend(fetched_data_261)

    # Bjerringbro Apotek
    pharmacy_url_262 = "apoteket-online.dk/apotek/bjerringbro-apotek"
    URLs_262_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_262 = seltuot.apoteketonline_selenium(URLs_262_selenium, "Bjerringbro Apotek")

    for i in fetched_data_262:
        i.append(pharmacy_url_262)
    medication.extend(fetched_data_262)

    # Charlottenlund Apotek
    pharmacy_url_263 = "apoteket-online.dk/apotek/charlottenlund-apotek"
    URLs_263_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_263 = seltuot.apoteketonline_selenium(URLs_263_selenium, "Charlottenlund Apotek")

    for i in fetched_data_263:
        i.append(pharmacy_url_263)
    medication.extend(fetched_data_263)

    # Christianshavns Apotek
    pharmacy_url_264 = "apoteket-online.dk/apotek/koebenhavn-christianshavn-apotek"
    URLs_264_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_264 = seltuot.apoteketonline_selenium(URLs_264_selenium, "Christianshavns Apotek")

    for i in fetched_data_264:
        i.append(pharmacy_url_264)
    medication.extend(fetched_data_264)

    # Dalgas Boulevard Apotek
    pharmacy_url_265 = "apoteket-online.dk/apotek/frederiksberg-dalgas-boulevard-apotek"
    URLs_265_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_265 = seltuot.apoteketonline_selenium(URLs_265_selenium, "Dalgas Boulevard Apotek")

    for i in fetched_data_265:
        i.append(pharmacy_url_265)
    medication.extend(fetched_data_265)

    # Ejby Apotek
    pharmacy_url_266 = "apoteket-online.dk/apotek/ejby-apotek"
    URLs_266_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_266 = seltuot.apoteketonline_selenium(URLs_266_selenium, "Ejby Apotek")

    for i in fetched_data_266:
        i.append(pharmacy_url_266)
    medication.extend(fetched_data_266)

    # Esbjerg Jerne Apotek
    pharmacy_url_267 = "apoteket-online.dk/apotek/esbjerg-jerne-apotek"
    URLs_267_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_267 = seltuot.apoteketonline_selenium(URLs_267_selenium, "Esbjerg Jerne Apotek")

    for i in fetched_data_267:
        i.append(pharmacy_url_267)
    medication.extend(fetched_data_267)

    # Faaborg Loeve Apotek
    pharmacy_url_268 = "apoteket-online.dk/apotek/faaborg-love-apotek"
    URLs_268_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_268 = seltuot.apoteketonline_selenium(URLs_268_selenium, "Faaborg Loeve Apotek")

    for i in fetched_data_268:
        i.append(pharmacy_url_268)
    medication.extend(fetched_data_268)

    # Farum Apotek
    pharmacy_url_269 = "apoteket-online.dk/apotek/farum-apotek"
    URLs_269_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_269 = seltuot.apoteketonline_selenium(URLs_269_selenium, "Farum Apotek")

    for i in fetched_data_269:
        i.append(pharmacy_url_269)
    medication.extend(fetched_data_269)

    # Give Apotek
    pharmacy_url_270 = "apoteket-online.dk/apotek/give-apotek"
    URLs_270_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_270 = seltuot.apoteketonline_selenium(URLs_270_selenium, "Give Apotek")

    for i in fetched_data_270:
        i.append(pharmacy_url_270)
    medication.extend(fetched_data_270)

    # Grenaa Apotek
    pharmacy_url_271 = "apoteket-online.dk/apotek/grenaa-apotek"
    URLs_271_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_271 = seltuot.apoteketonline_selenium(URLs_271_selenium, "Grenaa Apotek")

    for i in fetched_data_271:
        i.append(pharmacy_url_271)
    medication.extend(fetched_data_271)

    # Greve Apotek
    pharmacy_url_272 = "apoteket-online.dk/apotek/greve-apotek"
    URLs_272_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_272 = seltuot.apoteketonline_selenium(URLs_272_selenium, "Greve Apotek")

    for i in fetched_data_272:
        i.append(pharmacy_url_272)
    medication.extend(fetched_data_272)

    # Graasten Apotek
    pharmacy_url_273 = "apoteket-online.dk/apotek/graasten-apotek"
    URLs_273_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_273 = seltuot.apoteketonline_selenium(URLs_273_selenium, "Graasten Apotek")

    for i in fetched_data_273:
        i.append(pharmacy_url_273)
    medication.extend(fetched_data_273)

    # Hammel Frijsenborg Apotek
    pharmacy_url_274 = "apoteket-online.dk/apotek/hammel-frijsenborg-apotek"
    URLs_274_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_274 = seltuot.apoteketonline_selenium(URLs_274_selenium, "Hammel Frijsenborg Apotek")

    for i in fetched_data_274:
        i.append(pharmacy_url_274)
    medication.extend(fetched_data_274)

    # Haslev Apotek
    pharmacy_url_275 = "apoteket-online.dk/apotek/haslev-apotek"
    URLs_275_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_275 = seltuot.apoteketonline_selenium(URLs_275_selenium, "Haslev Apotek")

    for i in fetched_data_275:
        i.append(pharmacy_url_275)
    medication.extend(fetched_data_275)

    # Herning Loeve Apotek
    pharmacy_url_276 = "apoteket-online.dk/apotek/herning-loeve-apotek"
    URLs_276_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_276 = seltuot.apoteketonline_selenium(URLs_276_selenium, "Herning Loeve Apotek")

    for i in fetched_data_276:
        i.append(pharmacy_url_276)
    medication.extend(fetched_data_276)

    # Hirtshals Apotek
    pharmacy_url_277 = "apoteket-online.dk/apotek/hirtshals-apotek"
    URLs_277_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_277 = seltuot.apoteketonline_selenium(URLs_277_selenium, "Hirtshals Apotek")

    for i in fetched_data_277:
        i.append(pharmacy_url_277)
    medication.extend(fetched_data_277)

    # Holstebro Loeveapotek
    pharmacy_url_278 = "apoteket-online.dk/apotek/holstebro-loeveapotek"
    URLs_278_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_278 = seltuot.apoteketonline_selenium(URLs_278_selenium, "Holstebro Loeveapotek")

    for i in fetched_data_278:
        i.append(pharmacy_url_278)
    medication.extend(fetched_data_278)

    # Hurup Apotek
    pharmacy_url_279 = "apoteket-online.dk/apotek/hurup-apotek"
    URLs_279_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_279 = seltuot.apoteketonline_selenium(URLs_279_selenium, "Hurup Apotek")

    for i in fetched_data_279:
        i.append(pharmacy_url_279)
    medication.extend(fetched_data_279)

    # Ikast Apotek
    pharmacy_url_280 = "apoteket-online.dk/apotek/ikast-apotek"
    URLs_280_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_280 = seltuot.apoteketonline_selenium(URLs_280_selenium, "Ikast Apotek")

    for i in fetched_data_280:
        i.append(pharmacy_url_280)
    medication.extend(fetched_data_280)

    # Linde Apoteket
    pharmacy_url_281 = "apoteket-online.dk/apotek/koebenhavn-linde-apotek"
    URLs_281_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_281 = seltuot.apoteketonline_selenium(URLs_281_selenium, "Linde Apoteket")

    for i in fetched_data_281:
        i.append(pharmacy_url_281)
    medication.extend(fetched_data_281)

    # Loeve Apoteket Nykoebing F.
    pharmacy_url_282 = "apoteket-online.dk/apotek/loeve-apotek-nykoebing-f"
    URLs_282_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_282 = seltuot.apoteketonline_selenium(URLs_282_selenium, "Loeve Apoteket Nykoebing F.")

    for i in fetched_data_282:
        i.append(pharmacy_url_282)
    medication.extend(fetched_data_282)

    # Naestved Loeve Apotek
    pharmacy_url_283 = "apoteket-online.dk/apotek/naestved-loeve-apotek"
    URLs_283_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_283 = seltuot.apoteketonline_selenium(URLs_283_selenium, "Naestved Loeve Apotek")

    for i in fetched_data_283:
        i.append(pharmacy_url_283)
    medication.extend(fetched_data_283)

    # Nexoe Apotek
    pharmacy_url_284 = "apoteket-online.dk/apotek/nexoe-apotek"
    URLs_284_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_284 = seltuot.apoteketonline_selenium(URLs_284_selenium, "Nexoe Apotek")

    for i in fetched_data_284:
        i.append(pharmacy_url_284)
    medication.extend(fetched_data_284)

    # Nyborg Apotek
    pharmacy_url_285 = "apoteket-online.dk/apotek/nyborg-apotek"
    URLs_285_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_285 = seltuot.apoteketonline_selenium(URLs_285_selenium, "Nyborg Apotek")

    for i in fetched_data_285:
        i.append(pharmacy_url_285)
    medication.extend(fetched_data_285)

    # Noerre Alslev Apotek
    pharmacy_url_286 = "apoteket-online.dk/apotek/noerre-alslev-apotek"
    URLs_286_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_286 = seltuot.apoteketonline_selenium(URLs_286_selenium, "Noerre Alslev Apotek")

    for i in fetched_data_286:
        i.append(pharmacy_url_286)
    medication.extend(fetched_data_286)

    # Noerresundby Apotek
    pharmacy_url_287 = "apoteket-online.dk/apotek/noerresundby-apotek"
    URLs_287_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_287 = seltuot.apoteketonline_selenium(URLs_287_selenium, "Noerresundby Apotek")

    for i in fetched_data_287:
        i.append(pharmacy_url_287)
    medication.extend(fetched_data_287)

    # Odder Apotek
    pharmacy_url_288 = "apoteket-online.dk/apotek/odder-apotek"
    URLs_288_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_288 = seltuot.apoteketonline_selenium(URLs_288_selenium, "Odder Apotek")

    for i in fetched_data_288:
        i.append(pharmacy_url_288)
    medication.extend(fetched_data_288)

    # Odense Albani Apotek
    pharmacy_url_289 = "apoteket-online.dk/apotek/odense-albani-apotek"
    URLs_289_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_289 = seltuot.apoteketonline_selenium(URLs_289_selenium, "Odense Albani Apotek")

    for i in fetched_data_289:
        i.append(pharmacy_url_289)
    medication.extend(fetched_data_289)

    # Praestoe Apotek
    pharmacy_url_290 = "apoteket-online.dk/apotek/praestoe-apotek"
    URLs_290_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_290 = seltuot.apoteketonline_selenium(URLs_290_selenium, "Praestoe Apotek")

    for i in fetched_data_290:
        i.append(pharmacy_url_290)
    medication.extend(fetched_data_290)

    # Ringe Apotek
    pharmacy_url_291 = "apoteket-online.dk/apotek/ringe-apotek"
    URLs_291_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_291 = seltuot.apoteketonline_selenium(URLs_291_selenium, "Ringe Apotek")

    for i in fetched_data_291:
        i.append(pharmacy_url_291)
    medication.extend(fetched_data_291)

    # Roenne Apotek
    pharmacy_url_292 = "apoteket-online.dk/apotek/roenne-apotek"
    URLs_292_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_292 = seltuot.apoteketonline_selenium(URLs_292_selenium, "Roenne Apotek")

    for i in fetched_data_292:
        i.append(pharmacy_url_292)
    medication.extend(fetched_data_292)

    # Sejlflod Apotek
    pharmacy_url_293 = "apoteket-online.dk/apotek/storvorde-sejlflod-apotek"
    URLs_293_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_293 = seltuot.apoteketonline_selenium(URLs_293_selenium, "Sejlflod Apotek")

    for i in fetched_data_293:
        i.append(pharmacy_url_293)
    medication.extend(fetched_data_293)

    # Skagen Apotek
    pharmacy_url_294 = "apoteket-online.dk/apotek/skagen-apotek"
    URLs_294_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_294 = seltuot.apoteketonline_selenium(URLs_294_selenium, "Skagen Apotek")

    for i in fetched_data_294:
        i.append(pharmacy_url_294)
    medication.extend(fetched_data_294)

    # Skjern Apotek
    pharmacy_url_295 = "apoteket-online.dk/apotek/skjern-apotek"
    URLs_295_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_295 = seltuot.apoteketonline_selenium(URLs_295_selenium, "Skjern Apotek")

    for i in fetched_data_295:
        i.append(pharmacy_url_295)
    medication.extend(fetched_data_295)

    # Stevns Apotek
    pharmacy_url_296 = "apoteket-online.dk/apotek/stevns-apotek"
    URLs_296_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_296 = seltuot.apoteketonline_selenium(URLs_296_selenium, "Stevns Apotek")

    for i in fetched_data_296:
        i.append(pharmacy_url_296)
    medication.extend(fetched_data_296)

    # Svane Apoteket Frederikshavn
    pharmacy_url_297 = "apoteket-online.dk/apotek/frederikshavn-svane-apotek"
    URLs_297_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_297 = seltuot.apoteketonline_selenium(URLs_297_selenium, "Svane Apoteket Frederikshavn")

    for i in fetched_data_297:
        i.append(pharmacy_url_297)
    medication.extend(fetched_data_297)

    # Svendborg Loeve Apotek
    pharmacy_url_298 = "apoteket-online.dk/apotek/svendborg-loeve-apotek"
    URLs_298_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_298 = seltuot.apoteketonline_selenium(URLs_298_selenium, "Svendborg Loeve Apotek")

    for i in fetched_data_298:
        i.append(pharmacy_url_298)
    medication.extend(fetched_data_298)

    # Soenderborg Jernbane Apotek
    pharmacy_url_299 = "apoteket-online.dk/apotek/soenderborg-jernbane-apotek"
    URLs_299_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_299 = seltuot.apoteketonline_selenium(URLs_299_selenium, "Soenderborg Jernbane Apotek")

    for i in fetched_data_299:
        i.append(pharmacy_url_299)
    medication.extend(fetched_data_299)

    # Thisted Svane Apotek
    pharmacy_url_300 = "apoteket-online.dk/apotek/thisted-svane-apotek"
    URLs_300_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_300 = seltuot.apoteketonline_selenium(URLs_300_selenium, "Thisted Svane Apotek")

    for i in fetched_data_300:
        i.append(pharmacy_url_300)
    medication.extend(fetched_data_300)

    # Tinglev Apotek
    pharmacy_url_301 = "apoteket-online.dk/apotek/tinglev-apotek"
    URLs_301_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_301 = seltuot.apoteketonline_selenium(URLs_301_selenium, "Tinglev Apotek")

    for i in fetched_data_301:
        i.append(pharmacy_url_301)
    medication.extend(fetched_data_301)

    # Toftlund Apotek
    pharmacy_url_302 = "apoteket-online.dk/apotek/toftlund-apotek"
    URLs_302_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_302 = seltuot.apoteketonline_selenium(URLs_302_selenium, "Toftlund Apotek")

    for i in fetched_data_302:
        i.append(pharmacy_url_302)
    medication.extend(fetched_data_302)

    # Taastrup Apotek
    pharmacy_url_303 = "apoteket-online.dk/apotek/taastrup-apotek"
    URLs_303_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_303 = seltuot.apoteketonline_selenium(URLs_303_selenium, "Taastrup Apotek")

    for i in fetched_data_303:
        i.append(pharmacy_url_303)
    medication.extend(fetched_data_303)

    # Toender Loeve Apotek
    pharmacy_url_304 = "apoteket-online.dk/apotek/toender-loeve-apotek"
    URLs_304_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_304 = seltuot.apoteketonline_selenium(URLs_304_selenium, "Toender")

    for i in fetched_data_304:
        i.append(pharmacy_url_304)
    medication.extend(fetched_data_304)

    # Ulve Apoteket-Kolding Soenderbro
    pharmacy_url_305 = "apoteket-online.dk/apotek/ulve-apoteket-kolding-soenderbro"
    URLs_305_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_305 = seltuot.apoteketonline_selenium(URLs_305_selenium, "Ulve Apoteket-Kolding Soenderbro")

    for i in fetched_data_305:
        i.append(pharmacy_url_305)
    medication.extend(fetched_data_305)

    # Vanloese Loeve Apotek
    pharmacy_url_306 = "apoteket-online.dk/apotek/vanloese-loeve-apotek"
    URLs_306_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_306 = seltuot.apoteketonline_selenium(URLs_306_selenium, "Vanloese Loeve Apotek")

    for i in fetched_data_306:
        i.append(pharmacy_url_306)
    medication.extend(fetched_data_306)

    # Vejle Gorms Apotek
    pharmacy_url_307 = "apoteket-online.dk/apotek/vejle-gorms-apotek"
    URLs_307_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_307 = seltuot.apoteketonline_selenium(URLs_307_selenium, "Vejle Gorms Apotek")

    for i in fetched_data_307:
        i.append(pharmacy_url_307)
    medication.extend(fetched_data_307)

    # Vejle Loeve Apotek
    pharmacy_url_308 = "apoteket-online.dk/apotek/vejle-loeve-apotek"
    URLs_308_selenium = ['https://apoteket-online.dk/ipren-tabl-200-mg-184963',
                         'https://apoteket-online.dk/panodil-tabletter-500-mg-409193',
                         'https://apoteket-online.dk/pantoprazol-20-mg-krka-102887',
                         'https://apoteket-online.dk/voltaren-forte-gel-23%2c2-mgg-559165',
                         'https://apoteket-online.dk/alnok-tabletter-10-mg-170251',
                         'https://apoteket-online.dk/behandling-af/forkoelelse/stoppet-naese/otrivin-menthol-ukonserveret-n%c3%a6sespray-1-mg-423414',
                         'https://apoteket-online.dk/mildison-lipid-creme-10-mgg-486750']

    fetched_data_308 = seltuot.apoteketonline_selenium(URLs_308_selenium, "Vejle Loeve Apotek")

    for i in fetched_data_308:
        i.append(pharmacy_url_308)
    medication.extend(fetched_data_308)

    # Aarhus marselisborg apotek
    pharmacy_url_309 = "marselisborg.dinapoteker.dk"
    URLs_309_selenium = ['https://www.dinapoteker.dk/a/marselisborg/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/marselisborg/panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/marselisborg/pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/marselisborg/voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/marselisborg/alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/marselisborg/otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/marselisborg/mildison-lipid-10-mg-g-0-p43108']

    fetched_data_309 = seltuot.dinapoteker_selenium(URLs_309_selenium)

    for i in fetched_data_309:
        i.append(pharmacy_url_309)
    medication.extend(fetched_data_309)

    # Aars apotek
    pharmacy_url_310 = "aars.dinapoteker.dk"
    URLs_310_selenium = ['https://www.dinapoteker.dk/a/aars/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/aars/panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/aars/pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/aars/voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/aars/alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/aars/otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/aars/mildison-lipid-10-mg-g-0-p43108']

    fetched_data_310 = seltuot.dinapoteker_selenium(URLs_310_selenium)

    for i in fetched_data_310:
        i.append(pharmacy_url_310)
    medication.extend(fetched_data_310)

    # Amagerbro apotek
    pharmacy_url_311 = "dinapoteker.dk/a/amagerbro"
    URLs_311_selenium = ['https://www.dinapoteker.dk/a/amagerbro/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/amagerbro/panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/amagerbro/pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/amagerbro/voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/amagerbro/alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/amagerbro/otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/amagerbro/mildison-lipid-10-mg-g-0-p43108']

    fetched_data_311 = seltuot.dinapoteker_selenium(URLs_311_selenium)

    for i in fetched_data_311:
        i.append(pharmacy_url_311)
    medication.extend(fetched_data_311)

    # Bagsvaerd apotek
    pharmacy_url_312 = "bagsvaerd.dinapoteker.dk"
    URLs_312_selenium = ['https://www.dinapoteker.dk/a/bagsvaerd/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/bagsvaerd//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/bagsvaerd//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/bagsvaerd//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/bagsvaerd//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/bagsvaerd//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/bagsvaerd//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_312 = seltuot.dinapoteker_selenium(URLs_312_selenium)

    for i in fetched_data_312:
        i.append(pharmacy_url_312)
    medication.extend(fetched_data_312)

    # Broendbystrand apotek
    pharmacy_url_313 = "dinapoteker.dk/a/broendbystrand"
    URLs_313_selenium = ['https://www.dinapoteker.dk/a/broendbystrand/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/broendbystrand//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/broendbystrand//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/broendbystrand//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/broendbystrand//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/broendbystrand//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/broendbystrand//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_313 = seltuot.dinapoteker_selenium(URLs_313_selenium)

    for i in fetched_data_313:
        i.append(pharmacy_url_313)
    medication.extend(fetched_data_313)

    # Dalum apotek odense
    pharmacy_url_314 = "dalum.dinapoteker.dk"
    URLs_314_selenium = ['https://www.dinapoteker.dk/a/dalum/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/dalum//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/dalum//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/dalum//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/dalum//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/dalum//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/dalum//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_314 = seltuot.dinapoteker_selenium(URLs_314_selenium)

    for i in fetched_data_314:
        i.append(pharmacy_url_314)
    medication.extend(fetched_data_314)

    # Egtved apotek
    pharmacy_url_315 = "egtved.dinapoteker.dk"
    URLs_315_selenium = ['https://www.dinapoteker.dk/a/egtved/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/egtved//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/egtved//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/egtved//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/egtved//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/egtved//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/egtved//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_315 = seltuot.dinapoteker_selenium(URLs_315_selenium)

    for i in fetched_data_315:
        i.append(pharmacy_url_315)
    medication.extend(fetched_data_315)

    # Engelsborg apotek
    pharmacy_url_316 = "engelsborg.dinapoteker.dk"
    URLs_316_selenium = ['https://www.dinapoteker.dk/a/engelsborg/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/engelsborg//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/engelsborg//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/engelsborg//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/engelsborg//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/engelsborg//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/engelsborg//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_316 = seltuot.dinapoteker_selenium(URLs_316_selenium)

    for i in fetched_data_316:
        i.append(pharmacy_url_316)
    medication.extend(fetched_data_316)

    # Enghave apotek
    pharmacy_url_317 = "enghave.dinapoteker.dk"
    URLs_317_selenium = ['https://www.dinapoteker.dk/a/enghave/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/enghave//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/enghave//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/enghave//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/enghave//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/enghave//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/enghave//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_317 = seltuot.dinapoteker_selenium(URLs_317_selenium)

    for i in fetched_data_317:
        i.append(pharmacy_url_317)
    medication.extend(fetched_data_317)

    # Frederikssund apotek
    pharmacy_url_318 = "frederikssund.dinapoteker.dk"
    URLs_318_selenium = ['https://www.dinapoteker.dk/a/frederikssund/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/frederikssund//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/frederikssund//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/frederikssund//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/frederikssund//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/frederikssund//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/frederikssund//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_318 = seltuot.dinapoteker_selenium(URLs_318_selenium)

    for i in fetched_data_318:
        i.append(pharmacy_url_318)
    medication.extend(fetched_data_318)

    # Friheden apotek
    pharmacy_url_319 = "friheden.dinapoteker.dk"
    URLs_319_selenium = ['https://www.dinapoteker.dk/a/friheden/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/friheden//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/friheden//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/friheden//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/friheden//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/friheden//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/friheden//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_319 = seltuot.dinapoteker_selenium(URLs_319_selenium)

    for i in fetched_data_319:
        i.append(pharmacy_url_319)
    medication.extend(fetched_data_319)

    # Gilleleje apotek
    pharmacy_url_320 = "hornbaek.dinapoteker.dk"
    URLs_320_selenium = ['https://www.dinapoteker.dk/a/hornbaek/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/hornbaek//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/hornbaek//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/hornbaek//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/hornbaek//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/hornbaek//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/hornbaek//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_320 = seltuot.dinapoteker_selenium(URLs_320_selenium)

    for i in fetched_data_320:
        i.append(pharmacy_url_320)
    medication.extend(fetched_data_320)

    # Hammershoej apotek
    pharmacy_url_321 = "hammershoej.dinapoteker.dk"
    URLs_321_selenium = ['https://www.dinapoteker.dk/a/hammershoej/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/hammershoej//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/hammershoej//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/hammershoej//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/hammershoej//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/hammershoej//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/hammershoej//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_321 = seltuot.dinapoteker_selenium(URLs_321_selenium)

    for i in fetched_data_321:
        i.append(pharmacy_url_321)
    medication.extend(fetched_data_321)

    # Hobro apotek
    pharmacy_url_322 = "hobro.dinapoteker.dk"
    URLs_322_selenium = ['https://www.dinapoteker.dk/a/hobro/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/hobro//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/hobro//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/hobro//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/hobro//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/hobro//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/hobro//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_322 = seltuot.dinapoteker_selenium(URLs_322_selenium)

    for i in fetched_data_322:
        i.append(pharmacy_url_322)
    medication.extend(fetched_data_322)

    # Hundige apotek
    pharmacy_url_323 = "hundige.dinapoteker.dk"
    URLs_323_selenium = ['https://www.dinapoteker.dk/a/hundige/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/hundige//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/hundige//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/hundige//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/hundige//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/hundige//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/hundige//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_323 = seltuot.dinapoteker_selenium(URLs_323_selenium)

    for i in fetched_data_323:
        i.append(pharmacy_url_323)
    medication.extend(fetched_data_323)

    # Hvidovre stationsapotek
    pharmacy_url_324 = "hvidovre.dinapoteker.dk"
    URLs_324_selenium = ['https://www.dinapoteker.dk/a/hvidovrestation/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/hvidovrestation//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/hvidovrestation//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/hvidovrestation//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/hvidovrestation//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/hvidovrestation//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/hvidovrestation//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_324 = seltuot.dinapoteker_selenium(URLs_324_selenium)

    for i in fetched_data_324:
        i.append(pharmacy_url_324)
    medication.extend(fetched_data_324)

    # Hoersholm apotek
    pharmacy_url_325 = "hoersholm.dinapoteker.dk"
    URLs_325_selenium = ['https://www.dinapoteker.dk/a/hoersholm/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/hoersholm//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/hoersholm//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/hoersholm//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/hoersholm//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/hoersholm//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/hoersholm//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_325 = seltuot.dinapoteker_selenium(URLs_325_selenium)

    for i in fetched_data_325:
        i.append(pharmacy_url_325)
    medication.extend(fetched_data_325)

    # Kalundborg apotek
    pharmacy_url_326 = "kalundborg.dinapoteker.dk"
    URLs_326_selenium = ['https://www.dinapoteker.dk/a/kalundborg/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/kalundborg//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/kalundborg//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/kalundborg//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/kalundborg//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/kalundborg//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/kalundborg//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_326 = seltuot.dinapoteker_selenium(URLs_326_selenium)

    for i in fetched_data_326:
        i.append(pharmacy_url_326)
    medication.extend(fetched_data_326)

    # Kastrup apotek
    pharmacy_url_327 = "kastrup.dinapoteker.dk"
    URLs_327_selenium = ['https://www.dinapoteker.dk/a/kastrup/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/kastrup//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/kastrup//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/kastrup//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/kastrup//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/kastrup//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/kastrup//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_327 = seltuot.dinapoteker_selenium(URLs_327_selenium)

    for i in fetched_data_327:
        i.append(pharmacy_url_327)
    medication.extend(fetched_data_327)

    # Korsoer apotek
    pharmacy_url_328 = "korsoer.dinapoteker.dk"
    URLs_328_selenium = ['https://www.dinapoteker.dk/a/korsoer/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/korsoer//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/korsoer//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/korsoer//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/korsoer//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/korsoer//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/korsoer//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_328 = seltuot.dinapoteker_selenium(URLs_328_selenium)

    for i in fetched_data_328:
        i.append(pharmacy_url_328)
    medication.extend(fetched_data_328)

    # Koege torvets apotek
    pharmacy_url_329 = "koegetorvets.dinapoteker.dk"
    URLs_329_selenium = ['https://www.dinapoteker.dk/a/koegetorvets/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/koegetorvets//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/koegetorvets//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/koegetorvets//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/koegetorvets//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/koegetorvets//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/koegetorvets//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_329 = seltuot.dinapoteker_selenium(URLs_329_selenium)

    for i in fetched_data_329:
        i.append(pharmacy_url_329)
    medication.extend(fetched_data_329)

    # Nykøbing F. Svane Apotek
    pharmacy_url_330 = "slotsbryggen.dinapoteker.dk"
    URLs_330_selenium = ['https://www.dinapoteker.dk/a/slotsbryggen/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/slotsbryggen//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/slotsbryggen//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/slotsbryggen//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/slotsbryggen//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/slotsbryggen//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/slotsbryggen//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_330 = seltuot.dinapoteker_selenium(URLs_330_selenium)

    for i in fetched_data_330:
        i.append(pharmacy_url_330)
    medication.extend(fetched_data_330)

    # Odense apoteket oernen
    pharmacy_url_331 = "oernen.dinapoteker.dk"
    URLs_331_selenium = ['https://www.dinapoteker.dk/a/oernen/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/oernen//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/oernen//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/oernen//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/oernen//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/oernen//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/oernen//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_331 = seltuot.dinapoteker_selenium(URLs_331_selenium)

    for i in fetched_data_331:
        i.append(pharmacy_url_331)
    medication.extend(fetched_data_331)
    
    # Odense bolbro apotek
    pharmacy_url_332 = "bolbro.dinapoteker.dk"
    URLs_332_selenium = ['https://www.dinapoteker.dk/a/bolbro/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/bolbro//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/bolbro//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/bolbro//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/bolbro//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/bolbro//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/bolbro//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_332 = seltuot.dinapoteker_selenium(URLs_332_selenium)

    for i in fetched_data_332:
        i.append(pharmacy_url_332)
    medication.extend(fetched_data_332)

    # Rungsted apotek
    pharmacy_url_333 = "rungsted.dinapoteker.dk"
    URLs_333_selenium = ['https://www.dinapoteker.dk/a/rungsted/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/rungsted//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/rungsted//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/rungsted//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/rungsted//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/rungsted//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/rungsted//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_333 = seltuot.dinapoteker_selenium(URLs_333_selenium)

    for i in fetched_data_333:
        i.append(pharmacy_url_333)
    medication.extend(fetched_data_333)

    # Steno apotek
    pharmacy_url_334 = "steno.dinapoteker.dk"
    URLs_334_selenium = ['https://www.dinapoteker.dk/a/steno/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/steno//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/steno//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/steno//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/steno//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/steno//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/steno//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_334 = seltuot.dinapoteker_selenium(URLs_334_selenium)

    for i in fetched_data_334:
        i.append(pharmacy_url_334)
    medication.extend(fetched_data_334)

    # Sydhavnsapoteket
    pharmacy_url_335 = "sydhavns.dinapoteker.dk"
    URLs_335_selenium = ['https://www.dinapoteker.dk/a/sydhavns/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/sydhavns//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/sydhavns//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/sydhavns//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/sydhavns//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/sydhavns//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/sydhavns//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_335 = seltuot.dinapoteker_selenium(URLs_335_selenium)

    for i in fetched_data_335:
        i.append(pharmacy_url_335)
    medication.extend(fetched_data_335)

    # Soeborg apotek
    pharmacy_url_336 = "dinapoteker.dk/a/soeborg"
    URLs_336_selenium = ['https://www.dinapoteker.dk/a/soeborg/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/soeborg//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/soeborg//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/soeborg//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/soeborg//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/soeborg//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/soeborg//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_336 = seltuot.dinapoteker_selenium(URLs_336_selenium)

    for i in fetched_data_336:
        i.append(pharmacy_url_336)
    medication.extend(fetched_data_336)

    # Soenderbro apotek
    pharmacy_url_337 = "soenderbro.dinapoteker.dk"
    URLs_337_selenium = ['https://www.dinapoteker.dk/a/soenderbro/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/soenderbro//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/soenderbro//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/soenderbro//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/soenderbro//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/soenderbro//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/soenderbro//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_337 = seltuot.dinapoteker_selenium(URLs_337_selenium)

    for i in fetched_data_337:
        i.append(pharmacy_url_337)
    medication.extend(fetched_data_337)

    # Vallensbaek apotek
    pharmacy_url_338 = "vallensbaek.dinapoteker.dk"
    URLs_338_selenium = ['https://www.dinapoteker.dk/a/vallensbaek/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/vallensbaek//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/vallensbaek//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/vallensbaek//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/vallensbaek//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/vallensbaek//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/vallensbaek//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_338 = seltuot.dinapoteker_selenium(URLs_338_selenium)

    for i in fetched_data_338:
        i.append(pharmacy_url_338)
    medication.extend(fetched_data_338)

    # Vejen apotek
    pharmacy_url_339 = "dinapoteker.dk/a/vejen"
    URLs_339_selenium = ['https://www.dinapoteker.dk/a/vejen/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/vejen//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/vejen//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/vejen//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/vejen//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/vejen//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/vejen//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_339 = seltuot.dinapoteker_selenium(URLs_339_selenium)

    for i in fetched_data_339:
        i.append(pharmacy_url_339)
    medication.extend(fetched_data_339)

    # Vejen trolde apotek
    pharmacy_url_340 = "dinapoteker.dk/a/trolde"
    URLs_340_selenium = ['https://www.dinapoteker.dk/a/trolde/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/trolde//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/trolde//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/trolde//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/trolde//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/trolde//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/trolde//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_340 = seltuot.dinapoteker_selenium(URLs_340_selenium)

    for i in fetched_data_340:
        i.append(pharmacy_url_340)
    medication.extend(fetched_data_340)

    # Viborg loeve apotek
    pharmacy_url_341 = "viborg.dinapoteker.dk"
    URLs_341_selenium = ['https://www.dinapoteker.dk/a/viborg/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/viborg//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/viborg//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/viborg//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/viborg//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/viborg//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/viborg//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_341 = seltuot.dinapoteker_selenium(URLs_341_selenium)

    for i in fetched_data_341:
        i.append(pharmacy_url_341)
    medication.extend(fetched_data_341)

    # Oeresunds apotek
    pharmacy_url_342 = "oeresunds.dinapoteker.dk"
    URLs_342_selenium = ['https://www.dinapoteker.dk/a/oeresunds/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/oeresunds//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/oeresunds//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/oeresunds//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/oeresunds//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/oeresunds//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/oeresunds//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_342 = seltuot.dinapoteker_selenium(URLs_342_selenium)

    for i in fetched_data_342:
        i.append(pharmacy_url_342)
    medication.extend(fetched_data_342)

    # Oesterbro apotek
    pharmacy_url_343 = "oesterbro.dinapoteker.dk"
    URLs_343_selenium = ['https://www.dinapoteker.dk/a/oesterbro/ipren-200-mg-p6366',
                         'https://www.dinapoteker.dk/a/oesterbro//panodil-500-mg-blister-p12445',
                         'https://www.dinapoteker.dk/a/oesterbro//pantoprazol-20-mg-krka-1-p4178',
                         'https://www.dinapoteker.dk/a/oesterbro//voltaren-forte-23-2-mg-g-1-p51188',
                         'https://www.dinapoteker.dk/a/oesterbro//alnok-10-mg-1-p6037',
                         'https://www.dinapoteker.dk/a/oesterbro//otrivin-menthol-ukonserveret-1-p12770',
                         'https://www.dinapoteker.dk/a/oesterbro//mildison-lipid-10-mg-g-0-p43108']

    fetched_data_343 = seltuot.dinapoteker_selenium(URLs_343_selenium)

    for i in fetched_data_343:
        i.append(pharmacy_url_343)
    medication.extend(fetched_data_343)

    # Apopro online apotek
    pharmacy_url_344 = "apopro.dk"
    URLs_344_normi = ['https://apopro.dk/ipren-200-mg-20-stk-filmovertrukne-tabletter-184963',
                      'https://apopro.dk/panodil-500-mg-haandkoeb-apoteksforbeholdt-20-stk-filmovertrukne-tabletter-409193',
                      'https://apopro.dk/pantoprazol-krka-20-mg-haandkoeb-apoteksforbeholdt-14-stk-enterotabletter-102887',
                      'https://apopro.dk/voltaren-forte-232-mgg-100-g-gel-559165',
                      'https://apopro.dk/alnok-10-mg-30-stk-filmovertrukne-tabletter-170251',
                      'https://apopro.dk/otrivin-menthol-ukonserveret-1-mgml-10-ml-naesespray-oploesning-423414',
                      'https://apopro.dk/mildison-lipid-10-mgg-haandkoeb-apoteksforbeholdt-15-g-creme-486750']

    fetched_data_344 = nt.apopro(URLs_344_normi)

    for i in fetched_data_344:
        i.append(pharmacy_url_344)
    medication.extend(fetched_data_344)

    # Gazelle online apotek
    pharmacy_url_345 = "webapoteket.dk"
    URLs_345_normi = ['https://www.webapoteket.dk/sygdom-og-symptomer/smertestillende/ipren-tabletter-p-184963',
                      'https://www.webapoteket.dk/sygdom-og-symptomer/smertestillende/panodil-tabletter-p-409193',
                      'https://www.webapoteket.dk/sygdom-og-symptomer/mave-og-tarmproblemer/mavesyre-og-halsbrand/pantoprazol-krka-p-102887',
                      'https://www.webapoteket.dk/sygdom-og-symptomer/smertestillende/voltaren-forte-gel-p-559165',
                      'https://www.webapoteket.dk/sygdom-og-symptomer/allergi/tabletter-mod-allergi/alnok-tabletter-p-170251',
                      'https://www.webapoteket.dk/sygdom-og-symptomer/forkoelelse/naesespray/otrivin-menthol-naesespray-p-423414',
                      'https://www.webapoteket.dk/sygdom-og-symptomer/hudproblemer/eksem/mildison-lipid-creme-p-486750']

    fetched_data_345 = nt.gazelle(URLs_345_normi)

    for i in fetched_data_345:
        i.append(pharmacy_url_345)
    medication.extend(fetched_data_345)

    # Kolding loeve apotek
    pharmacy_url_346 = "kolding-jernbanegade.dinapoteker.dk"
    URLs_346_selenium = ['https://kolding-jernbanegade.dinapoteker.dk/ipren-200-mg-p6366',
                         'https://kolding-jernbanegade.dinapoteker.dk/panodil-500-mg-blister-p12445',
                         'https://kolding-jernbanegade.dinapoteker.dk/pantoprazol-20-mg-krka-1-p4178',
                         'https://kolding-jernbanegade.dinapoteker.dk/voltaren-forte-23-2-mg-g-1-p51188',
                         'https://kolding-jernbanegade.dinapoteker.dk/alnok-10-mg-1-p6037',
                         'https://kolding-jernbanegade.dinapoteker.dk/otrivin-menthol-ukonserveret-1-p12770',
                         'https://kolding-jernbanegade.dinapoteker.dk/mildison-lipid-10-mg-g-0-p43108']

    fetched_data_346 = seltuot.dinapoteker_selenium(URLs_346_selenium)

    for i in fetched_data_346:
        i.append(pharmacy_url_346)
    medication.extend(fetched_data_346)

    # Noerrebro apotek
    pharmacy_url_347 = "ugleapotek.dk"
    URLs_347_normi = ['https://ugleapotek.dk/produkt/ipren-200-mg/',
                      'https://ugleapotek.dk/produkt/panodil-500-mg-blister/',
                      'https://ugleapotek.dk/produkt/pantoprazol-20-mg-krka/',
                      'https://ugleapotek.dk/produkt/voltaren-forte-232-mg-g-3/',
                      'https://ugleapotek.dk/produkt/alnok-10-mg-2/',
                      'https://ugleapotek.dk/produkt/otrivin-menthol-ukonserveret-1/',
                      'https://ugleapotek.dk/produkt/mildison-lipid-10-mg-g-3/']

    fetched_data_347 = nt.ugleapotek(URLs_347_normi)

    for i in fetched_data_347:
        i.append(pharmacy_url_347)
    medication.extend(fetched_data_347)
    
    # Ringsted apotek
    pharmacy_url_348 = "ringsted.dinapoteker.dk"
    URLs_348_selenium = ['https://ringsted.dinapoteker.dk/ipren-200-mg-p6366',
                         'https://ringsted.dinapoteker.dk/panodil-500-mg-blister-p12445',
                         'https://ringsted.dinapoteker.dk/pantoprazol-20-mg-krka-1-p4178',
                         'https://ringsted.dinapoteker.dk/voltaren-forte-23-2-mg-g-1-p51188',
                         'https://ringsted.dinapoteker.dk/alnok-10-mg-1-p6037',
                         'https://ringsted.dinapoteker.dk/otrivin-menthol-ukonserveret-1-p12770',
                         'https://ringsted.dinapoteker.dk/mildison-lipid-10-mg-g-0-p43108']

    fetched_data_348 = seltuot.dinapoteker_selenium(URLs_348_selenium)

    for i in fetched_data_348:
        i.append(pharmacy_url_348)
    medication.extend(fetched_data_348)
