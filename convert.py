import os


for t in range(18):
    for i in range(10):
    
        filenumber0 = str(t)
        filenumber1 = str(i)
        string = "sox new_audio" + filenumber0+filenumber1 +".wav -b 16 newaudio"+ filenumber0+filenumber1 +".wav"
        os.system(string)

        