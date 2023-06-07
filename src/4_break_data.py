#!/usr/bin/python

import pandas as pd
import os

labels = os.listdir("../data/clean")

for label in labels:
    df = pd.read_csv(f"../data/clean/{label}/{label}.tsv", sep='\t')

    # create sentence broken data
    sentence_broken_df = df.copy()
    for i, row in sentence_broken_df.iterrows():
        sentence_broken_df.at[i, 'Premise'] = list(filter(None, row['Premise'].split('.')))
    sentence_broken_df.to_csv(f"../data/sentencebroken/{label}/{label}.tsv", sep="\t", header=True, index=False)
    
    # create word broken data
    word_broken_df = df.copy()
    word_broken_df['Premise'] = word_broken_df['Premise'].str.replace('.', '')
    for i, row in word_broken_df.iterrows():
        word_broken_df.at[i, 'Premise'] = list(filter(None, row['Premise'].split(' ')))
    word_broken_df.to_csv(f"../data/wordbroken/{label}/{label}.tsv", sep="\t", header=True, index=False)
