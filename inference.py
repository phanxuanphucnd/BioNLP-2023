# Coding: utf-8
# Copyright (c) 2023 by Phuc Phan

from factorsum.model import FactorSum

training_domain = 'arxiv'
model = FactorSum(model_name_or_path='./models/model-rs86h5g0_v0')
summary = model.summarize(
    "Cell-fate reprograming is at the heart of development , yet very little is known about the molecular mechanisms promoting or inhibiting reprograming in intact organisms . In the C . elegans germline , reprograming germ cells into somatic cells requires chromatin perturbation . These findings have wide implications , ranging from development to diseases associated with abnormal Notch signaling .  Cell-fate decisions are controlled , on the one hand , by intercellular signaling and , on the other hand , by intrinsic mechanisms such as epigenetic chromatin modifications . The Notch signaling pathway is a highly conserved and widespread signaling mechanism ( Artavanis-Tsakonas et al . , 1999; Greenwald and Kovall , 2013 ) , which has been implicated in key cell-fate decisions such as the decision between proliferation and differentiation ( Liu et al . Thus , we propose that the GLP-1Notch–dependent induction of UTX-1 facilitates reprograming by alleviating PRC2-mediated repression of alternative cell fates .  Germ cells can be converted into neuronal cells in intact C . elegans upon overexpression of the neuronal transcription factor CHE-1 , simply by depleting the chromatin modifier LIN-53 ( Tursun et al . , 2011; Patel et al . 022  In the C . elegans germline , GLP-1Notch signaling is essential for maintaining a pool of undifferentiated stem cells/progenitors . Here , we report an unexpected role of GLP-1Notch signaling in promoting cell fate reprograming . A fascinating possibility is that a regulatory principle described here could help explain the etiology of this and perhaps other human diseases linked to a pathological increase in Notch signaling .  Standard procedures were used to maintain animals . Worms ( RRID:WB_DL226 ) were grown at 25°C unless stated otherwise . All heat-shock and temperature-sensitive strains were kept at 15°C . Based on the observation of a clear and penetrant phenotype , gonads were scored in a second round according to the categories defined in the first round .", # a document string
    budget_guidance=200, # budget guidance in tokens
    source_token_budget=1000, # number of tokens to use from source document as content guidance
    verbose=True,
)
