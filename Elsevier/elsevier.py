from elsapy.elsclient import ElsClient
from elsapy.elsdoc import FullDoc
import json
import os
from tqdm import tqdm
import requests


def store_fulltext(idx, doi, path):
    doi_doc = FullDoc(doi=doi)
    if doi_doc.read(client):
        # print("doi_doc.title: ", doi_doc.title)
        doi_doc.write()
    else:
        print("Read document failed.")
    files = os.listdir(path)
    count = 0
    name = ''
    for fs in files:
        if fs.endswith('.json'):
            count += 1
            name = fs

    if count == 1:
        with open('data/'+name, encoding='utf-8') as file_obj:
            print(files[0])
            total = json.load(file_obj)
        if type(total['originalText']) == str:
            with open('data/' + str(idx) + '.txt', 'w', encoding='utf-8') as f:
                f.write(doi)
                f.write('\n')
                f.write(total['originalText'])
        os.remove(path + name)
    else:
        print(doi, 'something wrong')


con_file = open("config.json")
config = json.load(con_file)
con_file.close()
client = ElsClient(config['apikey'])
client.inst_token = config['insttoken']

with open('input your doi json path here', 'r', encoding='utf-8') as file_obj:
    elsevier = json.load(file_obj)

path = "input your path here"
already = os.listdir(path)


a_idx = []
for a in already:
    a_idx.append(int(a[:-4]))
print(len(a_idx))

for i, ed in enumerate(tqdm(elsevier)):
    store_fulltext(i, ed, path)