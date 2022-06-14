import numpy as np
import os
from pydub import AudioSegment
import random
import soundfile
import math


#program 1
#read random percentage of test files in a loop
#sample random noise sample
# mix the noise with the audio sample
#save new file to folder

#THIS IS PROGRAM 1

words = ["down","go","left","no","off","on","right","stop","up","yes"]

for element in words:

    directory = "/Users/lucbohmer/Documents/RU DataScience/Semester 2/ASR/keyword-transformer/data1/testing/" + element
    background_directory = "/Users/lucbohmer/Downloads/Background_dataset/background_category_samples"

    files = os.listdir(directory)#random.sample(os.listdir(directory), 48)
    for file in files:
        filename = os.fsdecode(file)
        background_file = random.choice(os.listdir(background_directory))
        background_file = os.fsdecode(background_file)
        if filename.endswith(".wav"):
            p1 = AudioSegment.from_wav(os.path.join(directory, filename))
            p2 = AudioSegment.from_wav(os.path.join(background_directory, background_file))
            #print(p1.dBFS-p2.dBFS)
            p2 = p2 + (p1.dBFS-p2.dBFS)#calculate SNR to dynamically level and mix the keyword and background noise, SNR ratio is set to 0
            #print(p1.dBFS-p2.dBFS)
            newAudio = p1.overlay(p2) 
            newAudio.export('/Users/lucbohmer/Documents/RU DataScience/Semester 2/ASR/keyword-transformer/data1/testing/' + element + '/' + filename, format="wav")
        
            continue
        else:
            continue 