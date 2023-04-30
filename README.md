Now the new repositories for updated sarcopenia evaluation model will be soon updated here: https://github.com/realzwu/sarcopenia-unet

# Cancer Informatics Project 1
Code for MRes Cancer Informatics Project 1

## Sequence for machine learning (train.py is working on google colab):

importnii.py - generator.py - train.py (dataset.py, utils.py, model.py) - log.py

### Environment settings:
```
apt-get update
apt-get intall python 3.10
pip install torch-xla
pip install -U git+https://github.com/albumentations-team/albumentations
pip install opencv-python-headless
```
### Then run:
```
python /content/drive/MyDrive/sarcopenia_zd2/train.py
```

## Sequence for statistics:

process-characteristics.py - characteristics-sarcopenia.py / Correlation.py / barplot.py / survival.py /  multivariate.py / univariate.py

## Segmentation data processing (remove non-muscle area):

please refer to Dr. Mitchell Chen: https://github.com/scat2801/sarc_tool
