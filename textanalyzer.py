'''
author = Martin Cizek 
'''
#----------------------------------------------------------------------------
import re
import string
#----------------------------------------------------------------------------

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
#----------------------------------------------------------------------------
ODDEL = 80*'-'
CREDENTIALS = {'bob':'123', 'ann':'pass123','mike':'password123', 'liz':'pass123'}
#----------------------------------------------------------------------------
#prevedeni stringu na integer s odchycenim chyby
#pri odchycene chybe vraci defaultni hodnotu defaultv
def str2intdef(int_str, defaultv):
    try:
        i=int(int_str)
    except ValueError:
        i=defaultv
    return i

#----------------------------------------------------------------------------
#ocisteni stringu od jinych znaku nez jsou pismena, cislice a mezery
def clean_text(text_in):
    text_clean = ''.join(ch for ch in text_in 
                        if ch in (string.digits + string.ascii_letters + ' ')).strip()
    return text_clean

#----------------------------------------------------------------------------
#analyza listu slov
def analyze_words(words_in):
    #inicializace pocitadel
    N_words = 0  
    N_titlecase_words = 0   #pocet slov zacinajicich velkym pismenem
    N_uppercase_words = 0   #pocet slov psanych velkymi pismeny
    N_lowercase_words = 0   #pocet slov psanych malymi pismeny
    N_numbers = 0           #pocet cisel v textu
    numbers_sum = 0         #soucet cisel v textu
    wrd_lengths=dict()
    #analyza textu
    for wrd in words_in:
        wrd_len = len(wrd)
        #pokud je slovo delsi nez 0 znaku, provedeme analyzu a zapocitame ho
        if (wrd_len>0):
            N_words += 1
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
    
    dict_out = dict();
    dict_out['N_words'] = N_words
    dict_out['N_titlecase_words'] = N_titlecase_words
    dict_out['N_uppercase_words'] = N_uppercase_words
    dict_out['N_lowercase_words'] = N_lowercase_words
    dict_out['N_numbers'] = N_numbers
    dict_out['numbers_sum'] = numbers_sum
    dict_out['wrd_lengths'] = wrd_lengths    
    return dict_out
#----------------------------------------------------------------------------    

#funkce main
def text_analyzer_main():
    #prihlaseni uzivatele
    login = input('Zadej jmeno uzivatele: ')
    pwd = input(f'Zadej heslo pro uzivatele {login}: ')
    print(ODDEL)
    
    #overeni uzivatele
    if not((login in CREDENTIALS.keys()) and (CREDENTIALS[login]==pwd)):    
        print('Nespravne uzivatelske jmeno nebo heslo. Ukoncuji program.')
        exit()
    
    #uvitani uzivatele a zobrazeni vyberu textu
    num_texts=len(TEXTS)
    
    print('')
    print(f'Ahoj {login}, vitej v programu Text Analyzer!')
    print(f'Vyber si prosim jeden z nasledujicich {num_texts} ukazkovych textu k provedeni analyzy:')
    print('')
    
    for i in range(num_texts):
        print(f'{i+1}: {TEXTS[i]}')
        print(ODDEL)
        print('')
    
    #volba textu k analyze    
    print(f'Povolene volby jsou 1 - {num_texts}. 0 - konec')
    while not((selection:=str2intdef(input('Tvuj vyber: '),-1)) in range(1,num_texts+1)):
        if selection==0:
            print('Ukoncuji program.')
            exit()
        else:
            print(f'Opakuj zadani. Povolene volby jsou 1 - {num_texts}')
    
    print(ODDEL)
    print(f'Analyzuji text c. {selection}...')
    print('')
    
    selection-=1    
    
    #nacteni stringu k analyze, jeho ocisteni a rozdeleni do listu slov
    str_clean = clean_text(TEXTS[selection])
    
    #rozdeleni stringu do listu slov, odeleovacem je mezera
    #re.split si poradi i s vicenasobnymi mezerami a neprida do listu slova o delce 0 znaku    
    words = re.split(' +',str_clean)
        
    #analyza listu slov    
    wrd_analysis = analyze_words(words)
        
    #kontrolni vypisy
    #print(f'Ocisteny string s textem:\n{str_clean}\n')
    #print(f'List jednotlivych slov:\n{words}\n')
    #print(f'Vysledek analyzy:\n{wrd_analysis}\n')
        
    #zobrazeni vysledku
    print(f"Pocet slov v textu: {wrd_analysis['N_words']}")
    print(f"Pocet slov zacinajicich velkym pismenem: {wrd_analysis['N_titlecase_words']}")
    print(f"Pocet slov psanych velkymi pismeny: {wrd_analysis['N_uppercase_words']}")
    print(f"Pocet slov psanych malymi pismeny: {wrd_analysis['N_lowercase_words']}")
    print(f"Pocet cisel: {wrd_analysis['N_numbers']}")
    print(f"Soucet vsech cisel: {wrd_analysis['numbers_sum']}\n")
    
    #pokud text obsahuje alespon 1 slovo, zobrazime tebulku
    if (wrd_analysis['N_words']>0):    
        #*** Vystup do tabulky ***
        #maximalni sirka prostredniho sloupce
        max_count = max(wrd_analysis['wrd_lengths'].values())
        #format radku tabulky
        fmt_string_row= "{:>4} {:<" + str(max_count) + "} {:<4}"
        #format zahlavi tabulky
        fmt_string_hdr= "{:>4} {:^" + str(max_count) + "} {:<4}"
        #vypis zahlavi a radku tabulky
        print(ODDEL)
        print(fmt_string_hdr.format('LEN|','OCCURENCES','|NR.'))
        print(ODDEL)
        for wrd_len in wrd_analysis['wrd_lengths'].keys():   
            print(fmt_string_row.format(f'{wrd_len}|', 
                wrd_analysis['wrd_lengths'][wrd_len]*'*', 
                f"|{wrd_analysis['wrd_lengths'][wrd_len]}"))


#----------------------------------------------------------------------------        
if __name__ == "__main__":
    text_analyzer_main()
