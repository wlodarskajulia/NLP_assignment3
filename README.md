# Assignment 3 — Transformer Fine-tuning, Robustness, and Limitations

**Authors:** Julia Wlodarska (S5965780), Lara van den Broek (S5883288), Tessa van Staalduinen (S5999286)  

Training was performed on Google Colab using a T4 GPU. 
The notebook can also be run on CPU, but training can be significantly slower.

## Overview

This repository contains the implementation for Assignment 3, which focuses on fine-tuning a pretrained Transformer model for text classification, evaluating its performance, and analyzing its robustness.

We fine-tune a DistilBERT model for 4-class classification on the AG News dataset. In addition, we perform slice-based evaluations to assess robustness and provide an analysis of model limitations.

## Repository Structure
- notebooks/
    - transformer_finetuning.ipynb
    - slice_evaluation.ipynb
- README.md

## Setup instructions

1. Install dependencies (pip install -r requirements.txt)
2. Run transformer_main_finetuning.ipynb file.
3. Run slice_evaluation.ipynb file.