"""

-[x] decided not to get abstracts if full texts not available (will just exclude based on this criteria--just going to create problems, as abstracts are written differently and I will frequently not be able to extract full context due to short length of abstract)
-[x] record what could be returned (or error message if nothing could be returned)
-[x] error handling (e.g. in case a request is rejected due to server overload rather than lack of texts). Am now logging these, if there are any http 429 exceptions (exceed wiley rate limit) then I'll handle these afterwards 
-[x] I will extract metadata from Web of Science ref entries (much easier as they are structured consistently)
"""
from pyminer import Miner
import os
import requests
import shutil
import csv
import pandas as pd
import random

doi_filename = '/home/joshua/Downloads/output.csv'
with open(doi_filename, 'r') as f:
    reader = csv.reader(f)
    content = list(reader)

doi_list = [row[28] for index, row in enumerate(content) if index > 0]
random.shuffle(doi_list) # shuffle list of dois-- will reduce load on a given publisher's server
# log type of full text returned or error message if none returned
output_log = pd.DataFrame(None, index=range(len(doi_list)*4), columns=['doi', 'output_code'])
m = Miner(mailto = os.environ.get('EMAIL'), tdmkey = os.environ.get('CROSSREF_API_KEY'))
exts = ['pdf', 'xml', 'html', 'txt']
log_count = 0
for i in range(len(doi_list)):
    x = m.search(ids = doi_list[i])
    for ext in exts:
        try:
            out = x.fetch(type = ext)
            shutil.move(out[0].path, '/home/joshua/Downloads/func3d_texts/{}.{}'.format(doi_list[i].rsplit('/', 1)[-1], ext))
            output_log.loc[log_count] = [doi_list[i], ext]
            log_count += 1
            break
        except (ValueError, IndexError): # link not available for ext type
            output_log.loc[log_count] = [doi_list[i], '{} is na'.format(ext)]
            log_count += 1
            continue
        except requests.exceptions.HTTPError as e:
            output_log.loc[log_count] = [doi_list[i], e.response.status_code]
            log_count += 1
            continue

output_log = output_log.drop(output_log.index[log_count:])
output_log.to_csv('/home/joshua/Downloads/func3d_texts/output_log.csv', sep=',')
