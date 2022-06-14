import numpy as np
import os
from pydub import AudioSegment
import soundfile

#program 2
#load noise sample 
#cut into 1 second pieces and save to new files

#THIS IS PROGRAM 2

directory = "/Users/lucbohmer/Downloads/Background_dataset/background_category"

time = [0,1001,2001,3001,4001,5001,6001,7001,8001,9001,10001] #miliseconds
t = 0

for file in sorted(os.listdir(directory)):
    filename = os.fsdecode(file)
    if filename.endswith(".wav"):
        p1 = AudioSegment.from_file(os.path.join(directory, filename),format="wav",frame_rate=44100, channels=2, sample_width=2)
        for i in range(10):
            newAudio = p1[time[i]:time[i+1]]
            filenumber0 = str(t)
            filenumber1 = str(i)
            newAudio.export('/Users/lucbohmer/Downloads/Background_dataset/background_category_samples/new_audio'+ filenumber0 + filenumber1 + '.wav', format="wav")
        t+=1
        continue
    else:
        continue

