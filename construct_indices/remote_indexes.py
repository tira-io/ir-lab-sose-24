#!/usr/bin/env python3
import json
import os
from tqdm import tqdm
import urllib.request
from construct_indexes import parse_documents
import tempfile
import gzip


def download_url(url, output_path):
    """
    Download a file from a url to a local path.
    From https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads
    """
    class DownloadProgressBar(tqdm):
        def update_to(self, b=1, bsize=1, tsize=None):
            if tsize is not None:
                self.total = tsize
            self.update(b * bsize - self.n)

    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

def process(doc_index, remote_file):
    temp_dir = tempfile.TemporaryDirectory().name
    os.makedirs(temp_dir, exist_ok=True)
    temp_dir += '/documents.jsonl'
    download_url(remote_file, temp_dir)
    parsed_docs = parse_documents(temp_dir)

    with gzip.open(doc_index, 'wt') as f:
        f.write(json.dumps(parsed_docs))

if __name__ == '__main__':
    for doc_index, remote_file in tqdm(json.load(open('ui/src/document_indexes.json', 'r')).items()):
        if os.path.exists(doc_index):
            continue

        process(doc_index, remote_file)
