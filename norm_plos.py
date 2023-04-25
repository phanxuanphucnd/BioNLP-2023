# -*- coding: utf-8 -*-
# Copyright (c) 2023 by Phuc Phan


import pickle
import os, sys, json

type = sys.argv[1]

with open('./results/PLOS/generated_predictions.pkl', 'rb') as f:
    data = pickle.load(f)

print(len(data))

with open(f'./results/{type}/plos.txt', 'w', encoding='utf-8') as f:
    for dt in data:
        dt = dt.replace('\n', ' ')
        f.writelines(f"{dt}\n")