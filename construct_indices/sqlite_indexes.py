#!/usr/bin/env python3
import sqlite3
import gzip
import json
from tqdm import tqdm

def create_db(filename):
    con = sqlite3.connect(filename.replace('.json.gz', '.db'))
    cur = con.cursor()
    cur.execute("CREATE TABLE documents(id CHAR(50), start INT, end INT, PRIMARY KEY (id))")
    
    for k,v in tqdm(json.load(gzip.open(filename, 'rt')).items()):
        cur.execute("INSERT INTO documents VALUES (?, ?, ?);", (k, v['start'], v['end']))

    con.commit()
    cur.close()
    con.close()

    con = sqlite3.connect(filename.replace('.json.gz', '.db'))
    cur = con.cursor()
    # From https://github.com/phiresky/sql.js-httpvfs
    cur.execute("pragma journal_mode = delete;")
    cur.execute("pragma page_size = 1024;")
    cur.execute("vacuum;")
    con.commit()
    cur.close()
    con.close()

if __name__ == '__main__':
    #create_db('static/indexes/ms-marco.json.gz')
    #create_db('static/indexes/argsme.json.gz')
    #create_db('static/indexes/antique.json.gz')
    #create_db('static/indexes/cranfield.json.gz')
    #create_db('static/indexes/vaswani.json.gz')
    #create_db('static/indexes/ir-lab-jena-leipzig-wise-2023.json.gz')
    #create_db('static/indexes/ir-lab-jena-leipzig-wise-2023-validation.json.gz')
    create_db('static/indexes/ir-lab-jena-leipzig-sose-2023.json.gz')
    
    
