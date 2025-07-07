#!/bin/bash
export VOLUME=$PWD/data # share a volume with the Docker container to avoid downloading weights every run
export IMAGE_URL=ghcr.io/huggingface/text-generation-inference:3.2.0
export EXTERNAL_PORT=8081
export INTERNAL_PORT=80
export HF_TOKEN=$TOKEN

# MODELS
export DTYPE=float16
export ORGANIZATION=leoitcode
export MODEL_1_HF_ID=$ORGANIZATION/resume-critique-llama3_1_8b-tt_lora-model_1_20k-adapter-rev_3
export MODEL_2_HF_ID=$ORGANIZATION/resume-critique-llama3_1_8b-tt_lora-model_2_20k-adapter-rev_1
export MODEL_3_HF_ID=$ORGANIZATION/resume-critique-llama3_1_8b-tt_lora-model_3_2k-adapter-rev_3
export MODEL_4_HF_ID=$ORGANIZATION/resume-critique-llama3_1_8b-tt_lora-model_4_20k-adapter-rev_1
export MODEL_5_HF_ID=$ORGANIZATION/resume-critique-llama3_1_8b-tt_lora-model_5_20k-adapter-rev_1
export MODEL_6_HF_ID=$ORGANIZATION/resume-critique-llama3_1_8b-tt_lora-model_4_2k-adapter-rev_2

docker compose up
