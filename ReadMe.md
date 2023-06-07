## SemEval 2023 Task 4

### ValueEval
Identification of Human Values behind Arguments.

### Dataset
The dataset has total of 5393 annotated arguments.  
After extracting the values which we want to classify, there remains 2188 arguments which are seperated by their labels in data/clean directory.  
There is also dataset seperated by words and sentence in data/wordbroken and data/sentencebroken directory.  

### Value Taxonomy (Labels)
We chose 3 values from 20 values available:
- Achievement
- Power: dominance
- Power: resources.

### Argument Corpus
The annotated corpus in tab-separated value format. Contains the following files for the different dataset splits:

    arguments-<split>.tsv: Each row corresponds to one argument
        Argument ID: The unique identifier for the argument
        Conclusion: Conclusion text of the argument
        Stance: Stance of the Premise towards the Conclusion; one of "in favor of", "against"
        Premise: Premise text of the argument
    labels-<split>.tsv: Each row corresponds to one argument
        Argument ID: The unique identifier for the argument
        Other: Each other column corresponds to one value category, with a 1 meaning that the argument resorts to the value category and a 0 that not

### Run
I wrote a python script named run.py which allows any user to run each part of this project seperately.
