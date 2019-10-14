import requests
import orodja
import re


#for i in range(0,167):
#    orodja.pripravi_imenik(f'zajeti_podatki/{i+1}. stran')
#    orodja.shrani_spletno_stran(f'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?view=detailed&sort=desc&page={i}', f'zajeti_podatki/{i+1}. stran.html')

with open('zajeti_podatki/1. stran.html') as f:
    vsebina = f.read()

vzorec = (
    r'<span class="title numbered">\n' #začetek
    r'\s*(?P<stevilka>\d+.)\n' #zaporedna številka igre
    r'\s*</span>\n' #filc
    r'\s*\n'
    r'\s*<a href="(?P<url_do_igre>/game/.*/.*)" class="title">\n' # url za kasneje, ga bo treba kombinitati z www.metascore.com
    r'\s*.*\n'
    r'\s*(?P<naslov> \w.*)\n' # naslov
    r'\s*.*\n' # filc h3
    r'\s*.*\n' #filc a
    r'\s*' # filc blank
    r'.*\n' #filc clamp
    r'\s*\n' # filc blank
    r'\s*<span>(?P<Datum_izdaje>.+)<.*\n'

)

count = 0
for zadetek in re.finditer(vzorec, vsebina):
    print(zadetek.groupdict())
    count += 1
print(count)