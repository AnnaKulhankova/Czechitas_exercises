soubor = open('karty.txt', 'r', encoding='utf-8')
karty = [radek.strip() for radek in soubor]
karty_split = [radek.split(" ") for radek in karty]
soubor.close()
import random
prvni_tah = random.choice(karty_split)
prvni_index = karty_split.index(prvni_tah)
del karty_split[prvni_index]

druhy_tah = random.choice(karty_split)
druhy_index = karty_split.index(druhy_tah)
del karty_split[druhy_index]

treti_tah = random.choice(karty_split)
treti_index = karty_split.index(treti_tah)
del karty_split[treti_index]

ctvrty_tah = random.choice(karty_split)

hodnoty = [prvni_tah[0], druhy_tah[0], treti_tah[0], ctvrty_tah[0]]
list_pro_soucet = [hodnoty.replace("kluk", "10") for hodnoty in hodnoty]
list_pro_soucet1 = [hodnoty.replace("dáma", "10") for hodnoty in list_pro_soucet]
list_pro_soucet2 = [hodnoty.replace("král", "10") for hodnoty in list_pro_soucet1]
list_pro_soucet3 = [hodnoty.replace("eso", "1") for hodnoty in list_pro_soucet2]
soucet = sum([int(hodnoty) for hodnoty in list_pro_soucet3])
print(f'tahy: {prvni_tah, druhy_tah, treti_tah, ctvrty_tah}, soucet:{soucet}')