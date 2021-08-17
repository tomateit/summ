# This is how the project is being developed

## 05 Aug 2021
1. The app was scaffolded.
2. Implementing baseline with ready-to-use third-party solutions.
    - Refer to notebook 1 in `notebooks/` directory.

## 06 Aug 2021
1. Research on common metrics and datasets.
    - Refer to notebook 0 in `notebooks/` directory.
2. Started to implement baseline solution.

## 07 Aug 2021
1. Implemented a baseline solution in notebook 2.
    - Very basic and need more comments (will do later).
    - Really have learned a lot in my drafts.

### 08 Aug 2021
1. Started implementing an extended solution with heuristics.
    - Turned out that most of ready-to-use tools are outdated and incompatible.
    - The third-party algorithm also does not perform well enough.
    - Nothing works for now, still a lot left to do.
2. Drafted hybrid approach on abstractive summarization model.

### 09 Aug 2021
1. Monday. I did some web-demo stuff bc I seemingly out of my schedule.
    - Note: as a former web dev I would never use current approach to writing a webapp, but for now the least possible action principle is on.
2. Some updates on metrics (third-party sources).

### 12 Aug 2021
1. Actual research and loading of datasets.

### 13 Aug 2021
1. Writing loader and parser for downloaded datasets.

### 14 Aug 2021
1. Loading more datasets for compression.
2. Separating WIP parts from extended solution into separate notebooks to make exeriments on.
3. First drafts on extended solution summarization part.

### 15 Aug 2021
1. Started grokking the reference code repo:
    - Forked it and dig into the code.
    - Got a grasp of file formats used there.
2. Started re-implementing it according to my needs, as long as I only like the idea:
    - All will be LaBSE based now.
    - I won't use BertExt, as the paper suggests :-\ .
    - Custom data pre-processing - the new model is not uncased, so why (the file in the current repo).
    - Implemented sentence scoring method (the paper requires) but as a surrogate (the file in the fork repo; I'm still indecisive on how to better structure this work).

### 16 Aug 2021
1. Gained a profound understanding of data preparation process required for the model. 
2. Did refactoring of the original code and wrote my own loader based on more transparent technologies:
    - Everything is named properly
    - Everything is consequetive, no repetitive looping and stuff like that
    - No fastNLP, only PyTorch Dataset
    - Rouge metric is python based, not some horrible perl solution

### 17 Aug 2021
1. Grocked the model. Rewrote it to be more concise and pretty.
2. Grocked the scheduler. Rewrote it based on native torch scheduler.
3. Grocked the loss (almost). Reimplemented it as a function.
4. Conclusion: 
    - i wrote a ton of code, yet it lacks integrity (probably will fail to run, IDK). 
    - gonna negotiate the APIs and ensure everything is vectorized and differentiable. 
    - i still wonder how I gonna train it lacking 8 T100 GPUs. Prbbly gonna try colab.