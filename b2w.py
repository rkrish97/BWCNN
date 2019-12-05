import os,os.path,time,re
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from gtts import gTTS

langx="en"

def playx(jjj):
    global langx
    try:
        tts = gTTS(text=jjj, lang=langx)
        tts.save("xxx.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("xxx.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
    except Exception as e:
        pass

def b2w_mapit(w):
    global langx
    words={}
    #             1     2    3     4      5       6        7
    words["en"]=["Yes","No","Hi","I am","Good","Thanks","How are you?"] #English
    words["el"]=["Ναι", "Όχι", "Γεια σου", "Είμαι", "Καλό", "Ευχαριστώ", "Πώς είσαι?"]
    words["es"]=["Sí", "No", "Hola", "Yo soy", "Bueno", "Gracias","Cómo estás?"]#spanish
    words["ar"] = ["نعم" , "لا" , "مرحبا" , "أنا" , "بخير" , "شُكْرًا","كيف حالُك؟"]#Arabic
    words["fr"]=["Oui", "Non", "Bonjour", "Je suis", "Bien", "Merci","Comment vas-tu?"]#French
    words["zh-Hans"] = ["是","否","嗨","我很","好","谢谢","你好吗?"]#chinese
    words["hi"] = ["हाँ", "नहीं", "हाय", "मैं हूँ", "अच्छा", "धन्यवाद","क्या हाल है?"]#Hidni
    words1=words[langx]
    words2=["1","101","10101","1010101","101010101","10101010101","1010101010101"]

    r="NONE"
    for i in range(0,len(words1)):
        if w==words2[i] or w=="0"+words2[i] or w==words2[i]+"0" or w=="0"+words2[i]+"0":
            r=words1[i]+""
        elif len(w)<=1 or int(w)==0:
            r=""
    return r

def b2w():
    execution_path = os.getcwd()
    im_path=execution_path #+ "/imx"
    final_s=""
    while True:
        #os.system("clear")
        #time.sleep(0.10)
        jjj=""
        pppp='log/log.txt'
        if os.path.exists(pppp)!= True:
            continue
        else:
            with open(pppp, 'r') as f:
                inix=0
                try:
                    x=f.readline()
                    #print(x)
                    #print("")
                    matcher= re.compile(r'(.)\1*')
                    x=[match.group() for match in matcher.finditer(x)]
                    #print(x)
                    #print("")
                except:
                    x=""

                w=""
                for u in x:
                    
                    if inix==0:
                        space = ""
                    else:
                        space =" "
                
                    if len(u)>=15 and u[0]=='1':
                        if len(w)==0:
                            space=""
                        sss=space+b2w_mapit(w)+"."
                        #print(w+"=["+b2w_mapit(w)+"] STOP")
                        ##print(sss, end = '')
                        jjj=jjj+sss
                        ##app.setLabel("x", jjj)
                        w=""
                    elif  len(u)>=15 and u[0]=='0' and len(w)!=0:
                        sss=space+b2w_mapit(w)
                        #print(w+"=["+b2w_mapit(w)+"] DIV")
                        ##print(sss, end = '')
                        jjj=jjj+sss
                        w=""
                        inix=1
                    else:
                        w=w+u[0]
        if final_s != jjj and jjj!="":
            print(jjj)
            #playx(jjj)
            final_s=jjj

b2w()
