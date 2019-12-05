def do_a(x1):
	global axx,BSN
	y1=x0.split(':')
	if(len(y1)>1):
		print("batch size:",BSN)
		axx.append(BSN)
		y1[0]=y1[0].replace("Epoch 0","")
		print(y1[0])
		axx.append(y1[0])

def do_b(x1):
	global axx
	x1=x1.replace("e-","ee")
	y1=x1.split('-')
	if(len(y1)>1):
		'''		y1[2]=float(y1[2].replace("loss: ",""))
		y1[3]=float(y1[3].replace("acc: ",""))
		y1[4]=float(y1[4].replace("val_loss: ",""))
		y1[5]=float(y1[5].replace("val_acc: ",""))'''
		y1[2]=y1[2].replace("loss: ","").replace("ee","e-")
		y1[3]=y1[3].replace("acc: ","").replace("ee","e-")
		y1[4]=y1[4].replace("val_loss: ","").replace("ee","e-")
		y1[5]=y1[5].replace("val_acc: ","").replace("ee","e-")
		print("loss:",y1[2])
		print("acc:",y1[3])
		print("val_loss:",y1[4])
		print("val_acc:",y1[5])
		axx.append(y1[2])
		axx.append(y1[3])
		axx.append(y1[4])
		axx.append(y1[5])
		axx.append("#")
#sel="ResNet"
sel="ResNet-1000"
#sel="ResNet-transfer-itself"
#sel="transfer-res-of"
#sel="DenseNet"
#sel="InceptionV3"
#sel="SqueezeNet"
if sel=="ResNet-transfer-itself" or sel=="transfer-res-of" or sel=="DenseNet" or sel=="InceptionV3" or sel=="SqueezeNet":
	SSS=[8,16,32]
	MAXN=100
if sel=="ResNet":
	SSS=[1,2,4,8,16,32]
	MAXN=100
if sel=="ResNet-1000":
	SSS=[8,16,32]
	MAXN=500
for BSN in SSS:
	axx=[]
	if sel=="ResNet":
		filepath = './eye'+str(BSN)+'/nohup.out'
	if sel=="ResNet-1000":
		filepath = './eye'+str(BSN)+'-1000/nohup.out'
	if sel=="ResNet-transfer-itself":
		filepath = './transfer/to'+str(BSN)+'/nohup.out'
	if sel=="transfer-res-of":
		filepath = './transfer-res-of/to'+str(BSN)+'/nohup.out'
	if sel=="DenseNet":
		filepath = './compare/eye'+str(BSN)+'-DenseNet/nohup.out'
	if sel=="InceptionV3":
		filepath = './compare/eye'+str(BSN)+'-InceptionV3/nohup.out'
	if sel=="SqueezeNet":
		filepath = './compare/eye'+str(BSN)+'-SqueezeNet/nohup.out'
	#filepath = './'+str(BSN)+'.out'
	print(filepath)
	if BSN==1:
		BS="67919/67919"
	if BSN==2:
		BS="33960/33960"
	if BSN==4:
		BS="16980/16980"
	if BSN==8:
		BS="8490/8490"
	if BSN==16:
		BS="4245/4245"
	if BSN==32:
		BS="2123/2123"
	with open(filepath) as fp:
		cnt = 0
		while True:
			x0 = fp.readline().strip()
			if x0:
				if(x0.find("Epoch 0")!=-1):
					print(x0)
					do_a(x0)
					#axx.append(y1[0])
					#if(x0.find("did not improve from")==-1):
				if(x0.find(BS)!=-1):
					print(x0)
					do_b(x0)
					cnt=cnt+1
			if cnt==MAXN:
				break
	#outF = open(filepath+"-out.csv", "a+")
	outF = open("out_"+sel+".csv", "a+")
	outF.write("batch size,")
	outF.write("epoch,")
	#outF.write("time,")
	outF.write("loss,")
	outF.write("acc,")
	outF.write("val_loss,")
	outF.write("val_acc,\n")
	#outF.write("note,")
	#outF.write("model,")
	for i in axx:
		s=str(i).strip()
		if s=="#":
			outF.write("\n")
		else:
			outF.write(s)
			outF.write(",")
	outF.close()
