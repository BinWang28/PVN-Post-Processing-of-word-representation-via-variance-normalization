#!/bin/sh

# PNV-post-processing via variance normalization:

BASELINE_PATH=./sgns.words
RESULT_PATH=./sgns.word.processed
PPA_dims=11

echo "PVN processing..."


python pvn.py ${BASELINE_PATH} ${RESULT_PATH} ${PPA_dims}
echo "PVN processing finished!"



# Evaluation:

echo "Original word representation result"
python2 ./word_sim/wordsim.py -l en -v ${BASELINE_PATH}

echo "Post-processed via PNA Word representation result"
python2 ./word_sim/wordsim.py -l en -v ${RESULT_PATH}