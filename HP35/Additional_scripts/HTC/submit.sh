#!/bin/bash

# change path if needed
cp ./HP35_data.tar.gz ./
tar xzvf HP35_data.tar.gz
rm HP35_data.tar.gz

mkdir new_trained_models
mkdir new_trained_models/{1..5}

python train.py

tar -czvf new_trained_models.tar.gz new_trained_models

rm *.npy
