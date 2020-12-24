import pandas as pd
import imageio 
import re
import numpy as np
import os
from pathlib import Path
from skimage import color
import class_maps
import sys

class ViennaNote:
    
    def __init__(self, fn, typ):
        attr = fn.split('-')
        
        if typ == 'test':
            ROOT = './data/originals-test/'
        elif typ == 'train':
            ROOT = './data/transformations-resized/'
        else:
            sys.exit()
            
        self.type = attr[0]
        self.time = attr[1]
        self.pitch = attr[2]
        imfile = imageio.imread(ROOT + fn)
        self.image = color.rgb2gray(imfile) / 255
        
    def resize_image(self, width, height):
        pass
    
class InputData:
    
    ROOT = './data/transformations-resized/' 
    
    def __init__(self, path = ROOT):
        self.files = [file for file in os.listdir(path) if os.path.isfile(path + file) and file[0:4] == 'note']
        self.objs = [ViennaNote(f, 'train') for f in self.files]
                
    def training_images(self, path = ROOT):
        images = [o.image for o in self.objs]
        return(np.array(images))
    
    def training_labels_pitch(self, path = ROOT):
        notes = [o.pitch for o in self.objs]
        labels = [map_pitch(pitch) for pitch in notes]
        return(np.array(labels))
    
    
class TestData:
    
    ROOT = './data/originals-test/' 
    
    def __init__(self, path = ROOT):
        self.files = [file for file in os.listdir(path) if os.path.isfile(path + file) and file[0:4] == 'note']
        self.objs = [ViennaNote(f, 'test') for f in self.files]
                
    def training_images(self, path = ROOT):
        images = [o.image for o in self.objs]
        return(np.array(images))
    
    def training_labels(self, path = ROOT):
        notes = [o.pitch for o in self.objs]
        labels = [map_pitch(pitch) for pitch in notes]
        return(np.array(labels))