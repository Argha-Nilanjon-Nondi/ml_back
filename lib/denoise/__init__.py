from IPython import display as disp
import torch
import torchaudio
from denoiser import pretrained
from denoiser.dsp import convert_audio
from scipy.io import wavfile
import numpy as np
import random
from utility import filename_generator
import os

def remove_all_noise(filename):
    model = pretrained.dns64().cpu()
    wav, sr = torchaudio.load(filename)
    wav = convert_audio(wav.cpu(), sr, model.sample_rate, model.chin)
    with torch.no_grad():
         denoised = model(wav[None])[0]
         data=denoised.data.cpu().numpy()
         data=np.squeeze(data)
         new_filename=filename_generator(filename,text="denoised")
         saved_path=os.path.join(os.getcwd(),"audio/denoised/",new_filename)
         wavfile.write(saved_path,model.sample_rate,data)
         print("denoised",saved_path)
         return saved_path