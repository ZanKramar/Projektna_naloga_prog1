import requests
import orodja
import  re
import csv
import json
seznam = []
vzorec = r';(?P<url>\game\.*);'

my_file = open('csvji/podatki.csv', mode='r', errors = 'ignore')
parsed_data = csv.reader(my_file)
for row in parsed_data:
    if row != []:
        seznam.append(row)
#print(seznam)
seznam_url = []
for i in seznam:
    seznam_url.append(i[1])
print(seznam_url)


stevec = 16700
for i in range(len(seznam_url)):
    u = 1
    v = i+30
    r = requests.get(f'https://www.metacritic.com{v}')
    with open(f'{v}_igra.html', 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')
            print(u)

