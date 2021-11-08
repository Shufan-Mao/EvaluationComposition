# EvaluationComposition

## About

This repostiory contains research code for evaluating the semantic relatedness scores between VPs and instruments predicted by distributional models trained on the corpus [MissingAdjunct](https://github.com/phueb/MissingAdjunct).

## Evaluations

All evaluations are pooled across model replications (random seed used to sample from the corpus), and items (VPS) of the same type.

### First-Rank

We assign a hit every time a model predicts that the correct instrument is the most related to a VP. 

### Intra-Instrument Variance

To test whether a model differntiates between two or more instruments that are equally correct (their rank should be tied), we use an anlysis of variance comparing the variance between predicted sematnic relatedness scores assigned to the correct instruments and scores sassigend to all other instruments.

## Compatibility

Developed on Ubuntu 18.04 and Python 3.7
