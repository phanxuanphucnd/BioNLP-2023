# BioNLP Workshop

BIONLP 2023 and Shared Tasks @ ACL 2023: https://aclweb.org/aclwiki/BioNLP_Workshop

## How to use

- STEP 1: 

Make sure the data for all splits are available (processing of the training sets might take several minutes):

```shell
>>> python -m factorsum.data prepare_dataset data/PLOS plos

>>> python -m factorsum.data prepare_dataset data/eLife elife
```

- STEP 2:

Run the training script as follows:

```shell
>>> bash plos_run_train.sh

>>> bash elife_run_train.sh

```

- STEP 3: 

Inference as follows:

```shell
>>> plos_infer.sh

>>> elife_infer.sh
```