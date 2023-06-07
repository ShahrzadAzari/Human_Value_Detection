import pandas as pd
import os

labels = os.listdir("../data/clean")

for label in labels:
    df = pd.read_csv(f"../data/clean/{label}/{label}.tsv", sep='\t')

    # replace extra characters with whitespace
    df['Premise'] = df['Premise'].replace('"', '')
    df['Premise'] = df['Premise'].replace("'", '')
    df['Premise'] = df['Premise'].replace(",", '')
    df['Premise'] = df['Premise'].replace('!', '.')
    df['Premise'] = df['Premise'].replace('?', '.')
    df.to_csv(f"../data/clean/{label}/{label}.tsv",sep="\t", header=True, index=False)
    