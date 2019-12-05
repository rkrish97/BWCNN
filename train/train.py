import imageai
import h5py
import os

## Here choose your GPU
os.environ['CUDA_VISIBLE_DEVICES']='0'

execution_path = os.getcwd()
im_path=execution_path + "/imx"

from imageai.Prediction.Custom import ModelTraining
model_trainer2 = ModelTraining()

## Here choose which architecture you want to use
model_trainer2.setModelTypeAsSqueezeNet()
##model_trainer2.setModelTypeAsResNet()
##model_trainer2.setModelTypeAsInceptionV3()
##model_trainer2.setModelTypeAsDenseNet()

model_trainer2.setDataDirectory(im_path)
model_trainer2.trainModel(num_objects=2, num_experiments=1000, enhance_data=True, batch_size=16, show_network_summary=True, save_full_model=True)

