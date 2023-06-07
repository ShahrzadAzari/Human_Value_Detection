import pandas as pd
import os

labels = os.listdir("../data/clean")

for label in labels:
    df = pd.read_csv(f"../data/clean/{label}/{label}.tsv", sep='\t')

    # create sentence broken data
    sentence_broken_df = df.copy()
    sentence_broken_df['Premise'] = list(filter(None, sentence_broken_df['Premise'].str.split('.')))
    sentence_broken_df.to_csv(f"../data/sentencebroken/{label}/{label}.tsv", sep="\t", header=True, index=False)
    
    # create word broken data
    word_broken_df = df.copy()
    word_broken_df['Premise'] =word_broken_df['Premise'].replace('.', '')
    word_broken_df['Premise'] = word_broken_df['Premise'].str.split(' ')
    word_broken_df.to_csv(f"../data/wordbroken/{label}/{label}.tsv", sep="\t", header=True, index=False)
