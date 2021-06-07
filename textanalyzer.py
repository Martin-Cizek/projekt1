'''
author = Martin Cizek 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
ODDEL = 80*'-'
CREDENTIALS = {'bob':'123', 'ann':'pass123','mike':'password123', 'liz':'pass123'}

#prihlaseni uzivatele
login = input('Zadej jmeno uzivatele: ')
pwd = input(f'Zadej heslo pro uzivatele {login}: ')
print(ODDEL)

#overeni uzivatele
if not((login in CREDENTIALS.keys()) and (CREDENTIALS[login]==pwd)):    
    print('Nespravne uzivatelske jmeno nebo heslo. Ukoncuji program.')
    exit()

#uvitani uzivatele a zobrazeni vyberu textu
print('')
print(f'Ahoj {login}, vitej v programu Text Analyzer!')
print(f'Vyber si prosim jeden z nasledujicich {len(TEXTS)} ukazkovych textu k provedeni analyzy:')
print('')
for i in range(len(TEXTS)):
    print(f'{i+1}: {TEXTS[i]}')
    print(ODDEL)
    print('')
#volba textu k analyze
print(f'Povolene volby jsou 1 - {len(TEXTS)}. 0 - konec')
while not((selection:=int(input('Tvuj vyber: '))) in range(1,len(TEXTS)+1)):
    if selection==0:
        print('Ukoncuji program.')
        exit()
    else:
        print(f'Opakuj zadani. Povolene volby jsou 1 - {len(TEXTS)}')

print(ODDEL)
print(f'Analyzuji text c. {selection}...')
print('')

#nacteni stringu k analyze, jeho ocisteni a rozdeleni do listu slov
selection-=1
str_in = str(TEXTS[selection]).replace('\n','').replace('\r','').replace('-',' ').strip()
words = str_in.split(' ')
for i in range(len(words)):
    words[i] = words[i].strip('.,"').strip("'")

#pocet slov
N_words = len(words)

#inicializace pocitadel
N_titlecase_words = 0
N_uppercase_words = 0
N_lowercase_words = 0
N_numbers = 0
numbers_sum = 0

#inicializace slovniku delek slov
wrd_lengths=dict()

#analyza textu
for wrd in words:
    wrd_len = len(wrd)
    wrd_lengths[wrd_len]=wrd_lengths.setdefault(wrd_len, 0)+1
    if wrd.istitle():
        N_titlecase_words += 1 
    elif wrd.isupper():
        N_uppercase_words += 1
    elif wrd.islower():
        N_lowercase_words += 1
    elif wrd.isnumeric():
        N_numbers += 1
        numbers_sum += int(wrd)

#serazeni slovniku delek slov od nejkratsiho po nejdelsi
wrd_lengths = dict(sorted(wrd_lengths.items()))

#zobrazeni vysledku
print(f'Pocet slov v textu: {N_words}')
print(f'Pocet slov zacinajicich velkym pismenem: {N_titlecase_words}')
print(f'Pocet slov psanych velkymi pismeny: {N_uppercase_words}')
print(f'Pocet slov psanych malymi pismeny: {N_lowercase_words}')
print(f'Pocet cisel: {N_numbers}')
print(f'Soucet vsech cisel: {numbers_sum}')

#*** Vystup do tabulky ***
#maximalni sirka prostredniho sloupce
max_count = max(wrd_lengths.values())
#format radku tabulky
fmt_string_row= "{:>4} {:<" + str(max_count) + "} {:<4}"
#format zahlavi tabulky
fmt_string_hdr= "{:>4} {:^" + str(max_count) + "} {:<4}"
#vypis zahlavi a radku tabulky
print(ODDEL)
print(fmt_string_hdr.format('LEN|','OCCURENCES','|NR.'))
print(ODDEL)
for wrd_len in wrd_lengths.keys():   
    print(fmt_string_row.format(f'{wrd_len}|',wrd_lengths[wrd_len]*'*',f'|{wrd_lengths[wrd_len]}'))
