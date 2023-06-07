import pandas as pd

arguments_training = pd.read_csv("../data/raw/initial/arguments-training.tsv", sep='\t')
labels_training = pd.read_csv("../data/raw/initial/labels-training.tsv", sep='\t')

# join arguments and labels based on 'Argument ID'
training_df = pd.merge(arguments_training, labels_training, on='Argument ID', how='inner')

# delete unrelated labels columns
training_df = training_df.drop(columns=[
    'Self-direction: thought', 'Self-direction: action', 'Stimulation',
    'Hedonism', 'Face', 'Security: personal', 'Security: societal',
    'Tradition', 'Conformity: rules', 'Conformity: interpersonal',
    'Humility', 'Benevolence: caring', 'Benevolence: dependability',
    'Universalism: concern', 'Universalism: nature',
    'Universalism: tolerance', 'Universalism: objectivity'
])

# only keep rows which has at least one of chosen labels
training_df = training_df[(
    (training_df['Achievement'] == 1) |
    (training_df['Power: dominance'] == 1) |
    (training_df['Power: resources'] == 1)    
)]

# save training_df
training_df.to_csv("../data/raw/initial/training.tsv", sep="\t", header=True, index=False)

# seperate data based on their labels

# in_favor_of_achievement_df -> achievement_P
in_favor_of_achievement_df = training_df[(
    (training_df['Achievement'] == 1) & (training_df['Stance'] == "in favor of"))]
in_favor_of_achievement_df.to_csv("../data/raw/label_seperated/achievement_P/achievement_P.tsv",
    sep="\t", header=True, index=False)


# against_achievement_df -> achievement_N
against_achievement_df = training_df[(
    (training_df['Achievement'] == 1) & (training_df['Stance'] == "against"))]
against_achievement_df.to_csv("../data/raw/label_seperated/achievement_N/achievement_N.tsv",
    sep="\t", header=True, index=False)
against_achievement_df.to_csv("../data/clean/achievement_N/achievement_N.tsv",
    sep="\t", header=True, index=False)

# in_favor_of_power_dominance_df -> power_dominance_P
in_favor_of_power_dominance_df = training_df[(
    (training_df['Power: dominance'] == 1) & (training_df['Stance'] == "in favor of"))]
in_favor_of_power_dominance_df.to_csv("../data/raw/label_seperated/power_dominance_P/power_dominance_P.tsv",
    sep="\t", header=True, index=False)
in_favor_of_power_dominance_df.to_csv("../data/clean/power_dominance_P/power_dominance_P.tsv",
    sep="\t", header=True, index=False)

# against_power_dominance_df -> power_dominance_N
against_power_dominance_df = training_df[(
    (training_df['Power: dominance'] == 1) & (training_df['Stance'] == "against"))]
against_power_dominance_df.to_csv("../data/raw/label_seperated/power_dominance_N/power_dominance_N.tsv",
    sep="\t", header=True, index=False)
against_power_dominance_df.to_csv("../data/clean/power_dominance_N/power_dominance_N.tsv",
    sep="\t", header=True, index=False)

# in_favor_of_power_resources_df -> power_resources_P
in_favor_of_power_resources_df = training_df[(
    (training_df['Power: resources'] == 1) & (training_df['Stance'] == "in favor of"))]
in_favor_of_power_resources_df.to_csv("../data/raw/label_seperated/power_resources_P/power_resources_P.tsv",
    sep="\t", header=True, index=False)
in_favor_of_power_resources_df.to_csv("../data/clean/power_resources_P/power_resources_P.tsv",
    sep="\t", header=True, index=False)

# against_power_resources_df -> power_resources_N
against_power_resources_df = training_df[(
    (training_df['Power: resources'] == 1) & (training_df['Stance'] == "against"))]
against_power_resources_df.to_csv("../data/raw/label_seperated/power_resources_N/power_resources_N.tsv",
    sep="\t", header=True, index=False)
against_power_resources_df.to_csv("../data/clean/power_resources_N/power_resources_N.tsv",
    sep="\t", header=True, index=False)
