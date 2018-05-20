# !/usr/bin/env python3

import bibtexparser
import gscholar
import time 
with open('ref.bib') as bib:
    db = bibtexparser.load(bib)
ress =[]

for it in (db.entries):
    title = it['title']
    id = it['ID']
    title = title.strip('{}')
    succ = False 
    while not succ:
        try:    
            res = gscholar.query(title)
            time.sleep(10)
            succ = True
        except Exception as e:
            print(e) 
            # sleep(10) 
            break 
    if not succ: break 
    it_gs = bibtexparser.loads(res[0])   
    it_gs = it_gs.entries[0]
    # from IPython import embed; embed()
    it_gs['ID'] = id 

    ress.append(it_gs)
    print(it_gs)
    # break

from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

db = BibDatabase()
db.entries = ress 

writer = BibTexWriter()
with open('ref_clean.bib', 'w') as bibfile:
    bibfile.write(writer.write(db))
