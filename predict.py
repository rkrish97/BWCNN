import imageai
import h5py
from imageai.Prediction import ImagePrediction
import time
import os

def pre():
    execution_path = os.getcwd()
    im_path=execution_path #+ "/imx"

    os.system("rm log/"+"*.txt")
    #note please copy the name of the model that you want to use from /content/im6/models
    ################################################
    ##m_n="best-models/eye16-ResNet/model_ex-055_acc-0.992638.h5"
    ##m_n="best-models/eye8-DenseNet/model_ex-055_acc-0.992402.h5"
    #m_n="best-models/eye16-SqueezeNet/model_ex-001_acc-0.494081.h5"
    m_n="best-models/eye16-InceptionV3/model_ex-022_acc-0.992049.h5"
    ################################################
    from imageai.Prediction.Custom import CustomImagePrediction
    prediction = CustomImagePrediction()
    prediction.setModelPath(model_path=im_path+"/"+m_n)
    prediction.setJsonPath(model_json=im_path+"/best-models/model_class.json")
    prediction.loadFullModel(num_objects=2)

    pa=im_path+"/pic/"
    print("==================\n==== Welcome ====\n==================")
    while True:
        output=[]
        t1=time.time()
        uuu=-1
        ########################################
        sss=""
        for file in sorted(os.listdir(pa)):
            #if file.endswith(".jpg"):
            try:
                uuu=uuu+1
                image_path=pa+"/"+file
                t1x=time.time()
                results, probabilities = prediction.predictImage(image_input=image_path, result_count=1)
                t2x=time.time()
                print("Time-->",t2x-t1x)
                output.append(results)
                if results[0]=='close':
                    x="1"
                else:
                    x="0"
                sss=sss+x
                f= open('log/log.txt', 'a+')
                f.write("%s" % x)
                f.close()
                os.system("rm "+image_path)
                print(x)
            except:
                continue
        
        ########################################
        '''for file in sorted(os.listdir(pa)):
            #if file.endswith(".jpg"):
            try:
                uuu=uuu+1
                image_path=pa+"/"+file
                results, probabilities = prediction.predictImage(image_input=image_path, result_count=1)
                output.append(results)
                os.system("rm "+image_path)
                #print(image_path)
            except:
                continue
        sss=""
        with open('log/log.txt', 'a+') as f:
            for item in output:
                if item[0]=='close':
                    x="1"
                else:
                    x="0"
                sss=sss+x
                f.write("%s" % x)'''
        t2=time.time()
        if uuu>0:
            print("Time-->",t2-t1,"Files#",uuu )
    #print(item)
                #os.system("clear")
    #print("==================\n==== Welcome ====\n==================")
    #speak(sss)
    ##t2=time.time()
    ##print(t2-t1)
    #print(*output, sep='\n')
pre()
