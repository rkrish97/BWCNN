import imageai
import h5py
import os
os.environ['CUDA_VISIBLE_DEVICES']='0'

execution_path = os.getcwd()
im_path=execution_path + "/imx"

from imageai.Prediction.Custom import ModelTraining
model_trainer2 = ModelTraining()
model_trainer2.setModelTypeAsResNet()
model_trainer2.setDataDirectory(im_path)
model_trainer2.trainModel(num_objects=2, num_experiments=100, enhance_data=True, batch_size=16, show_network_summary=True,transfer_from_model=execution_path+"/model_ex-055_acc-0.992638.h5", initial_num_objects=2, save_full_model=True)
