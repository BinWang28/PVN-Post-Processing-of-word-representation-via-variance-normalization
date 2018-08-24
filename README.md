# PVN-Post-Processing-of-word-representation-via-variance-normalization

PVN code for paper:
Post-Processing of Word Representations via Variance Normalization and Dynamic Embedding

### Procedure

1. Provide the word representation file as txt format.
For example: https://nlp.stanford.edu/projects/glove/
You can just choose the following one.
  https://nlp.stanford.edu/data/glove.6B.zip
2. Edit the path from PNV.sh

    BASELINE_PATH=./sgns.words
    
    RESULT_PATH=./sgns.word.processed
    
If you are going to use vector other than 300 dimensions. Please change it from pvn.py.
3. Run PNV.sh file.

I also put the evaluation for word similarity in the same folder. You can have a easy test.

### Here is some results: (same with our paper)
sgns file from our paper: 
Figure1.png

Results for GloVe(downloaded from office website, glove.6B.zip):
Figure2.png


### For details about PNV - Post-Processing via Variance Normalization, please look into the paper:

https://arxiv.org/abs/1808.06305

If you are going to use this method, please cite our paper.
