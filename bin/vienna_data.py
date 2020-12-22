import pandas as pd
import imageio 
import re
import numpy as np
import os
from pathlib import Path
import tensorflow as tf

def map_pitch(pitch):
    
    m = {"a": 0,
         "h": 1,
         "c1": 2,
         "d1": 3,
         "e1": 4,
         "f1": 5,
         "g1": 6,
         "a1": 7,
         "h1": 8,
         "c2": 9,
         "d2": 10,
         "e2": 11,
         "f2": 12,
         "g2": 13,
         "a2": 14,
         "h2": 15,
         "c3": 16,
         "other": 17}
    
    return(m[pitch])

class ViennaNote:
    
    def __init__(self, fn):
        attr = fn.split('-')
        self.type = attr[0]
        self.time = attr[1]
        self.pitch = attr[2]
        self.image = imageio.imread('./data/originals-resized/' + fn)
        
    def resize_image(self, width, height):
        pass
    
class InputData:
    
    ROOT = './data/originals-resized/' 
    
    def __init__(self, path = ROOT):
        self.files = [file for file in os.listdir(path) if os.path.isfile(path + file) and file[0:4] == 'note']
        self.objs = [ViennaNote(f) for f in self.files]
                
    def training_images(self, path = ROOT):
        images = [o.image for o in self.objs]
        return(np.array(images) / 255)
    
    def training_labels(self, path = ROOT):
        notes = [o.pitch for o in self.objs]
        labels = [map_pitch(pitch) for pitch in notes]
        return(np.array(labels))