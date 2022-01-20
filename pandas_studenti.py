import pandas
studenti1 = pandas.read_csv('studenti1.csv', encoding = 'utf-8')
studenti2 = pandas.read_csv('studenti2.csv', encoding = 'utf-8')

#1 spojuji csv do jednoho datasetu
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)

#2 zjistuji kolik studentu jiz nestuduje a kolik je dalkovych
nestuduje = studenti['ročník'].isnull()
nestudenti = nestuduje.to_list()
kolik_nestudenti = sum(nestudenti)
print(f'Jiz nestuduje:{kolik_nestudenti}')

dalkovi_serie = studenti['kruh'].isnull()
dalkovi_list = dalkovi_serie.to_list()
dalkovi = sum(dalkovi_list)
print(f'Pocet dalkovych studentu:{dalkovi}')

#3 cistim data o dalkove a jiz nestudujici studenty
cista_data = studenti.dropna()

#zjistuji pocet studentu v jednotlivych oborech
pocet_dle_oboru = cista_data.groupby('obor').count()
print(pocet_dle_oboru)

#prumerny prospech v kazdem oboru
prumerny_prospech = round(cista_data.groupby('obor')['prospěch'].mean())
print(prumerny_prospech)

#zjistuji pohlavi joinem s tabulkou jmen a koukam, jestli vic zen nebo muzu
jmena = pandas.read_csv('jmena100.csv', encoding='utf-8')
studenti_new = pandas.merge(cista_data, jmena, on=['jméno'])
zeny_a_muzi = studenti_new.groupby('pohlaví').count()
print(zeny_a_muzi)