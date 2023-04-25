python scripts/run_summarization.py \
    --model_name_or_path artifacts/eLife-best/checkpoint-13000-49.9065 \
    --do_predict \
    --output_dir ./results/eLife \
    --per_device_eval_batch_size 4 \
    --overwrite_output_dir \
    --predict_with_generate \
    --generation_max_length 512 \
    --generation_num_beams 4 \
    --val_max_target_length 512 \
    --max_source_length 1024 \
    --dataset_name data/infer/eLife \
    --dataset_config elife \
    --predict_split test

python norm_elife.py test
