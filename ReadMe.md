# Dataset for Touché / SemEval 2023 Task 4; ValueEval: Identification of Human Values behind Arguments.
The dataset has total of 9324 annotated arguments.

# Value Taxonomy
The value-categories.json describes the 20 value categories of this task through examples. Format:
{
  "<value category>": {
    "<level 1 value>": [
      "<exemplary effect a corresponding argument might target>",
      ...
    ], ...
  }, ...
}

# Argument Corpus
The annotated corpus in tab-separated value format. Contains the following files for the different dataset splits:
    arguments-<split>.tsv: Each row corresponds to one argument
        Argument ID: The unique identifier for the argument
        Conclusion: Conclusion text of the argument
        Stance: Stance of the Premise towards the Conclusion; one of "in favor of", "against"
        Premise: Premise text of the argument
    labels-<split>.tsv: Each row corresponds to one argument
        Argument ID: The unique identifier for the argument
        Other: Each other column corresponds to one value category, with a 1 meaning that the argument resorts to the value category and a 0 that not

# Argument Meta-information
    meta-arguments-a.tsv: Each row corresponds to one argument (IDs starting with A) from the IBM-ArgQ-Rank-30kArgs
        Argument ID: The unique identifier for the argument
        WA: the quality label according to the weighted-average scoring function
        MACE-P: the quality label according to the MACE-P scoring function
        stance_WA: the stance label according to the weighted-average scoring function
        stance_WA_conf: the confidence in the stance label according to the weighted-average scoring function
    meta-arguments-c.tsv: Each row corresponds to one argument (IDs starting with C) from the Chinese question-answering website Zhihu
        Argument ID: The unique identifier for the argument
        Conclusion Chinese: The original chinese conclusion statement
        Premise Chinese: The original chinese premise statement
        URL: Link to the original statement the argument was taken from
    meta-arguments-d.tsv: Each row corresponds to one argument (IDs starting with D) from https://www.groupdiscussionideas.com
        Argument ID: The unique identifier for the argument
        URL: Link to the topic the argument was taken from
    meta-arguments-e.tsv: Each row corresponds to one argument (IDs starting with E) from the Conference for the Future of Europe
        Argument ID: The unique identifier for the argument
        URL: Link to the comment the argument was taken from
    meta-arguments-f.tsv: Each row corresponds to one argument (IDs starting with F). This file contains information on the 279 arguments in arguments-test-nahjalbalagha.tsv and 1047 additional arguments that were not labeled so far. This data was contributed by the language.ml lab (Doratossadat, Omid, Mohammad, Ehsaneddin) [1].
        Argument ID: The unique identifier for the argument
        Conclusion Farsi: Conclusion text of the argument in Farsi
        Stance Farsi: Stance of the Premise towards the Conclusion, in Farsi
        Premise Farsi: Premise text of the argument in Farsi
        Conclusion English: Conclusion text of the argument in English (translated from Farsi)
        Stance English: Stance of the Premise towards the Conclusion; one of "in favor of", "against"
        Premise English: Premise text of the argument in English (translated from Farsi)
        Source: Source text of the argument; one of "Nahj al-Balagha" [2], "Ghurar al-Hikam wa Durar ak-Kalim" [3]; their Farsi translations were used
        Method: How the premise was extracted from the source; one of "extracted" (directly taken), "deduced"; the conclusion are deduced
    meta-arguments-g.tsv: Each row corresponds to one argument (IDs starting with G) from the New York Times
        Argument ID: The unique identifier for the argument
        URL: Link to the article the argument was taken from
        Internet Archive timestamp: Timestamp of the article's version in the Internet Archive that was used
