import pandas
#nacitam csv 
jmena = pandas.read_csv('jmena100.csv', encoding = 'utf-8')
#vybiram jmena bez pozadovaneho puvodu
bez_has_puvodu = jmena[~jmena['původ'].isin(['hebrejský', 'aramejský', 'slovanský'])][['jméno', 'četnost']]
#prevadim na list
bez_has_puvodu_list = bez_has_puvodu.values.tolist()
#tvorim list pouze s cetnostmi jmen
cetnosti = [cetnost[1] for cetnost in bez_has_puvodu_list]
#scitam vsechny cetnosti dohromady
soucet_cetnosti = sum(cetnosti)
#vypocitavam procentualni zastoupeni danych jmen v CZ
zastoupeni_jmen = (100 / 10629798) * soucet_cetnosti
print(f'{round(zastoupeni_jmen)}%')