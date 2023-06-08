#!/usr/bin/python

import pandas as pd
import os
import matplotlib.pyplot as plt

labels = os.listdir("../data/clean")

row_count_df = pd.DataFrame(columns=['row count'], index=labels)
sentence_count_df = pd.DataFrame(columns=['sentence count'], index=labels)
word_count_df = pd.DataFrame(columns=['word count'], index=labels)
unique_word_count_df = pd.DataFrame(columns=['unique word count'], index=labels)
common_unique_word_count_df = pd.DataFrame(columns=['common unique word count'], index=labels)
uncommon_unique_word_count_df = pd.DataFrame(columns=['uncommon unique word count'], index=labels)
most_frequent_uncommon_words_df = pd.DataFrame(columns=[f'word {i}' for i in range(1,11)], index=labels)

common_words = set()
word_dicts = []
for label in labels:
    clean_df = pd.read_csv(f"../data/clean/{label}/{label}.tsv", sep='\t')
    sentence_broken_df = pd.read_csv(f"../data/sentencebroken/{label}/{label}.tsv", sep='\t')
    word_broken_df = pd.read_csv(f"../data/wordbroken/{label}/{label}.tsv", sep='\t')
    
    # compute row count
    row_count_df.loc[label, "row count"] = len(clean_df.index)

    sentence_count = 0
    word_count = 0
    word_dict = {}
    for i, row in clean_df.iterrows():
        # compute Sentence Count
        sentence_count += len(list(filter(None, row['Premise'].split('.'))))

        row['Premise'] = row['Premise'].replace('.', '')
        # compute Word Count
        words = list(filter(None, row['Premise'].split(' ')))
        word_count += len(words)

        # compute Unique Word Count
        for word in words:
            if word_dict.__contains__(word):
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    word_dicts.append(word_dict)
    if len(common_words) == 0:
        common_words = set(word_dict)
    else:
        common_words = common_words.intersection(set(word_dict))

    sentence_count_df.loc[label, "sentence count"] = sentence_count
    word_count_df.loc[label, "word count"] = word_count
    unique_word_count_df.loc[label, "unique word count"] = len(word_dict)

row_count_df.to_csv(f"../stats/row_count.csv", sep="\t", header=True, index=True)
sentence_count_df.to_csv(f"../stats/sentence_count.csv", sep="\t", header=True, index=True)
word_count_df.to_csv(f"../stats/word_count.csv", sep="\t", header=True, index=True)
unique_word_count_df.to_csv(f"../stats/unique_word_count.csv", sep="\t", header=True, index=True)

sorted_words = []
for i, label in enumerate(labels):
    # compute Common Unique Word Count
    # compute Uncommon Unique Word Count
    common_unique_word_count = 0
    uncommon_unique_word_count = 0
    word_dict = word_dicts[i]
    for key, val in word_dict.items():
        if key in common_words:
            common_unique_word_count += 1
            word_dict[key] = 0
        else:
            uncommon_unique_word_count += 1

    common_unique_word_count_df.loc[label, "common unique word count"] = common_unique_word_count
    uncommon_unique_word_count_df.loc[label, "uncommon unique word count"] = uncommon_unique_word_count

    # compute 10 Most Frequent Uncommon Words
    sorted_word_dict = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)
    for j in range(1, 11):
        most_frequent_uncommon_words_df.loc[label, f'word{j}'] = sorted_word_dict[j-1][0]
        sorted_words.append(sorted_word_dict[j-1])

common_unique_word_count_df.to_csv(f"../stats/common_unique_word_count.csv", sep="\t", header=True, index=True)
uncommon_unique_word_count_df.to_csv(f"../stats/uncommon_unique_word_count.csv", sep="\t", header=True, index=True)
most_frequent_uncommon_words_df.to_csv(f"../stats/most_frequent_uncommon_words.csv", sep="\t", header=True, index=True)

# compute words histogram
sorted_words = sorted(sorted_words, key=lambda x:x[1], reverse=True)
names = []
values = []
for i in range(30):
    names.append(sorted_words[i][0])
    values.append(sorted_words[i][1])

plt.bar(range(30), values, tick_label=names)
plt.title(f"Most Frequent Uncommon Words", fontweight ="bold")
plt.xticks(rotation=60, ha='right')
plt.savefig("../stats/words_histogram.png")
