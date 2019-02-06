
# coding: utf-8



import os
import json


carpeta = './tefs/'

files = [x for x in os.listdir(carpeta)]


def sdicts(lista):
    sdict_aliases = {}
    sdict_items = {}
    for i in lista:
        with open(carpeta+i,'r') as f:
            file = json.load(f)
        for x, y in file.items():
            sdict_aliases[x]=y
        sdict_items[i]=[x for x in file.keys()]    
        
    return sdict_aliases, sdict_items


with open('sdict_aliases.json','w') as f:
    json.dump(sdicts(files)[0], f, indent=4, ensure_ascii=False)

with open('sdict_items.json', 'w') as f:
    json.dump(sdicts(files)[1], f, indent=4, ensure_ascii=False)

