DATASET='plos'

python scripts/run_summarization.py \
    --model_name_or_path "GanjinZero/biobart-v2-base" \
    --tokenizer_name "GanjinZero/biobart-v2-base" \
    --do_train \
    --do_eval \
    --output_dir output/"${DATASET}" \
    --per_device_eval_batch_size=8 \
    --overwrite_output_dir \
    --train_file "data/PLOS/train.csv" \
    --validation_file "data/PLOS/val.csv" \
    --text_column article \
    --summary_column lay_summary \
    --generation_max_length 500 \
    --generation_num_beams 4