# BioNLP Workshop

BioNLP 2023 and Shared Tasks @ ACL 2023: https://aclweb.org/aclwiki/BioNLP_Workshop.

We achieve the **Third Rank** in the shared task (and the **Second Rank** excluding the baseline submission of the organizers).

The performance on the private-test set of our best system and compared with the top-ranked systems: Top-1 (MDC), Top-2 (Baselines) reported in the shared task leaderboard.

|                          | R-1 &uarr; | R-2 &uarr; | R-L &uarr;  | BERTScore &uarr; | FKGL &darr; | DCRS &darr; | BARTScore &uarr; |
|--------------------------|------------|------------|-------------|------------------|-------------|-------------|------------------|
| Top-1 *(MDC)*            | 0.4822     | **0.1553** | 0.4485      | **0.8707**       | 12.9370     | 10.2058     | -1.1771          |
| Top-2 *(Baseline)*       | 0.4696     | 0.1445     | 0.4371      | 0.8642           | **12.0694** | 10.2487     | **-0.8305**      |
| Our Approach             | **0.4829** | 0.1469     | **0.4502**  | 0.8571           | 12.2923     | **10.0862** | -1.7357          |
| Our Approach<br/>(PLOS)  | 0.4853     | 0.1711     | 0.4473      | 0.8617           | 14.8063     | 11.5870     | -1.3791          |
| Our Approach<br/>(eLife) | 0.4805     | 0.1227     | 0.4532      | 0.8526           | 9.7781      | 8.5854      | -2.0924          |



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
