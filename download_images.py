#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import codecs
import pandas as pd
from argparse import ArgumentParser
from urllib import request
from tqdm import trange

parser = ArgumentParser()
parser.add_argument(
    'output_dirpath',
    type=str,
    help='output directory path'
)
parser.add_argument(
    'csv_filepath',
    type=str,
    help='csv filepath'
)
args = parser.parse_args()

header_names = ['Amazon ID (ASIN)', 'Filename', 'Image URL', 'Title', 'Author', 'Category ID',
                'Category']
with codecs.open(args.csv_filepath, mode='r', encoding='utf-8', errors='ignore') as f:
    csv = pd.read_csv(f, delimiter=",", header=None, names=header_names)

if not os.path.isdir(args.output_dirpath):
    os.makedirs(args.output_dirpath)

print('[Download images into "{}"]'.format(args.output_dirpath))
for i in trange(len(csv)):
    filename = csv.iloc[i]['Filename']
    category = csv.iloc[i]['Category']
    inner_output_dirpath = os.path.join(args.output_dirpath, category)
    if not os.path.isdir(inner_output_dirpath):
        os.mkdir(inner_output_dirpath)
    output_filepath = os.path.join(inner_output_dirpath, filename)
    
    url = csv.iloc[i]['Image URL']
    downloaded_img = request.urlopen(url)
    f = open(output_filepath, mode='wb')
    f.write(downloaded_img.read())
    downloaded_img.close()
    f.close()
