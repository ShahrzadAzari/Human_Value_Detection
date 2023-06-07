#!/usr/bin/python

import pandas as pd
import os

labels = os.listdir("../data/raw/label_seperated")

for label in labels:
    df = pd.read_csv(f"../data/raw/label_seperated/{label}/{label}.tsv", sep='\t')

    # replace extra characters with whitespace
    df['Premise'] = df['Premise'].str.replace('"', '')
    df['Premise'] = df['Premise'].str.replace("'", '')
    df['Premise'] = df['Premise'].str.replace(",", '')
    df['Premise'] = df['Premise'].str.replace('!', '.')
    df['Premise'] = df['Premise'].str.replace('?', '.')
    df.to_csv(f"../data/clean/{label}/{label}.tsv",sep="\t", header=True, index=False)
    