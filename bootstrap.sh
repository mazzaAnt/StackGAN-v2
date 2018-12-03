#!/bin/sh

wget http://www.symcernos.com/projectCU/birds.zip 
unzip -q birds.zip -d 'data/'
wget http://www.vision.caltech.edu/visipedia-data/CUB-200-2011/CUB_200_2011.tgz
tar -xzf CUB_200_2011.tgz -C data/birds
wget http://www.symcernos.com/projectCU/birds_3stages.zip
unzip -q birds_3stages.zip -d 'models/'
ROOT=./data/birds/CUB_200_2011/images/
ls $ROOT | while read dir; do cp ${ROOT}/${dir}/* TEMP_IMAGES; done
pip install tensorboard-pytorch python-dateutil easydict pandas torchfile PyHamcrest
mkdir -p "code/birds_output"  TEMP_IMAGES
python ./a-PyTorch-Tutorial-to-Image-Captioning.files/create_input_files.py 
