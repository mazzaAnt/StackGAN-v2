#!/bin/sh

wget http://www.symcernos.com/projectCU/birds.zip 
unzip -q birds.zip -d 'StackGAN-v2/data/'
wget http://www.vision.caltech.edu/visipedia-data/CUB-200-2011/CUB_200_2011.tgz
tar -xzf CUB_200_2011.tgz -C StackGAN-v2/data/birds
wget http://www.symcernos.com/projectCU/birds_3stages.zip
unzip -q birds_3stages.zip -d 'StackGAN-v2/models/'
ROOT=~/StackGAN-v2/data/birds/CUB_200_2011/images/
ls $ROOT | while read dir; do cp ${ROOT}/${dir}/* a-PyTorch-Tutorial-to-Image-Captioning/images/; done
ls $ROOT | while read dir; do cp ${ROOT}/../../text/${dir}/* a-PyTorch-Tutorial-to-Image-Captioning/images/; done
cp -r a-PyTorch-Tutorial-to-Image-Captioning/output StackGAN-v2/code/birds_output
pip install tensorboard-pytorch python-dateutil easydict pandas torchfile PyHamcrest
