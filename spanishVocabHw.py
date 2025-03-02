import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

tema = input("Which tema: ")
df = pd.read_excel(f"file{tema}.xlsx")
df["Spanish Word"] = df["Spanish Word"].fillna("")

#Probably have to update excel file soon
while True:
    word = input("Enter in Spanish Word áéíóúñ (1 to stop): ")
    if word == "1":
        break

    #Synonym
    r = requests.get(f'https://www.spanishdict.com/thesaurus/{word}')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find_all('div', class_='oIApfSfD FKq1a5Ed')

    syn = []
    for x in s:
        name = str({None: ''}.get(x, x))
        clean_text = re.sub('<.*?>', '', name)
        syn.append(clean_text)
    print(f"\n\033[1mSynonyms\033[0m: {syn}")


    #Spanish Dict Def
    r = requests.get(f'https://www.spanishdict.com/translate/{word}')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find_all("a", class_="sddpPTrv")
    syn = []
    for x in s:
        name = str({None: ''}.get(x, x))
        clean_text = re.sub('<.*?>', '', name)
        syn.append(clean_text)

    

    print(f"\n\033[1mSpanish Dict Def\033[0m: {syn}")

    

    #Translate/Definition
    data_top = df.head()
    index = 0
    thing = False
    for row in range(len(df)):
        x = df.loc[row, "Spanish Word"]
        if(word in x):
            index = row
            thing = True
            break

    if(thing == False):
        print("Word not found in VHL (or you misspelled it)")
    else:
        print(f"\n\033[1mTranslation\033[0m: {df.loc[index, "English Definition"]}")
        print(f"\n\033[1mSpanish Definition\033[0m: {df.loc[index, "Spanish Definition"]}\n")


       
    



       



