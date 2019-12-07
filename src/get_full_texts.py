"""

-[] still need to check for full text and get abstract if not available (or exclude if neither are available)                    
-[] record what could be returned (full text type, abstract only, nothing)
-[] error logging (e.g. in case a request is rejected due to server overload rather than lack of texts)
-[] metadata extraction (from crossref metadata or web of science reference info?)
-[] add rate limiting for wiley articles (max 60 in 5 minutes...might not matter if I randomize the order as the script is pretty slow, especially for wiley articles as they are only pdfs and involve redirects...can't hurt, maybe i just throw any dois that would exceed the limit into a list and then repeat through that list at the end with a sleep in between
"""
from pyminer import Miner
import os
import requests
from pathlib import Path
import shutil
import csv

doi_filename = '/home/joshua/Downloads/output.csv'
with open(doi_filename, 'r') as f:
    reader = csv.reader(f)
    content = list(reader)
doi_list = [row[28] for index, row in enumerate(content) if index > 0]

m = Miner(mailto = os.environ.get('EMAIL'), tdmkey = os.environ.get('CROSSREF_API_KEY'))
exts = ['pdf', 'xml', 'html', 'txt']
for i in range(len(doi_list)):
    x = m.search(ids = doi_list[i])
    for ext in exts:
        try:
            out = x.fetch(type = ext)
            shutil.move(out[0].path, '/home/joshua/Downloads/func3d_texts/{}.{}'.format(doi_list[i].rsplit('/', 1)[-1], ext))
            break
        except:
            continue
