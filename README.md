# BioNLP Workshop

BioNLP 2023 and Shared Tasks @ ACL 2023: https://aclweb.org/aclwiki/BioNLP_Workshop. 

Paper: VBD-NLP at BioLaySumm Task 1: Explicit and Implicit Key Information Selection for Lay Summarization on Biomedical Long Documents](https://github.com/phanxuanphucnd/BioNLP-2023/blob/main/docs/VBD-NLP%20at%20BioLaySumm%20Task%201:%20Explicit%20and%20Implicit%20Key%20Information%20Selection%20for%20Lay%20Summarization%20on%20Biomedical%20Long%20Documents.pdf)

We achieved the **Third Rank** in the shared task (and the **Second Rank** excluding the baseline submission of the organizers). 

The performance on the private-test set of our best system and compared with the top-ranked systems: Top-1 (MDC), Top-2 (Baselines) reported in the shared task leaderboard.

|                          | R-1 &uarr;   | R-2 &uarr;   | R-L &uarr;    | BERTScore &uarr;   | FKGL &darr;   | DCRS &darr;   | BARTScore &uarr;   |
|--------------------------|:------------:|:------------:|:-------------:|:------------------:|:-------------:|:-------------:|:------------------:|
| Top-1 *(MDC)*            |    0.4822    |  **0.1553**  |    0.4485     |     **0.8707**     |    12.9370    |    10.2058    |      -1.1771       |
| Top-2 *(Baseline)*       |    0.4696    |    0.1445    |    0.4371     |       0.8642       |  **12.0694**  |    10.2487    |    **-0.8305**     |
| Our Approach             |  **0.4829**  |    0.1469    |  **0.4502**   |       0.8571       |    12.2923    |  **10.0862**  |      -1.7357       |
| Our Approach<br/>(PLOS)  |    0.4853    |    0.1711    |    0.4473     |       0.8617       |    14.8063    |    11.5870    |      -1.3791       |
| Our Approach<br/>(eLife) |    0.4805    |    0.1227    |    0.4532     |       0.8526       |    9.7781     |    8.5854     |      -2.0924       |


## Dataset & pre-trained models

- Processed data & pre-trained models: [https://drive.google.com/file/d/1MhI4RRKCnwPC2txCSSaYCsaLk28uIuWO/view?usp=sharing](https://drive.google.com/file/d/1MhI4RRKCnwPC2txCSSaYCsaLk28uIuWO/view?usp=sharing)

- Raw Dataset: 
  - Train: [https://drive.google.com/file/d/1FFfa4fHlhEAyJZIM2Ue-AR6Noe9gOJOF/view?usp=share_link](https://drive.google.com/file/d/1FFfa4fHlhEAyJZIM2Ue-AR6Noe9gOJOF/view?usp=share_link)    
  - Private-Test: [https://drive.google.com/file/d/1qHogbSW99UfhdbpFUhP6buDix5-8B2HC/view?usp=sharing](https://drive.google.com/file/d/1qHogbSW99UfhdbpFUhP6buDix5-8B2HC/view?usp=sharing)


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
