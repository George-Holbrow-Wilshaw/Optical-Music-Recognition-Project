import pandas as pd
import imageio 
import re

class primusSequence:
    def __init__(self, folder, image, semantic):
        self.image = imageio.imread("./data/package_aa/" + folder + "/" + folder + ".png")
        self.semantic = open("./data/package_aa/" + folder + "/" + folder + ".semantic").read()
    
    def get_labels(self):
        notes = re.findall(r'note\-(.+?)\_', self.semantic)
        return(notes)
        

def join_images_labels(labels, images):
    pairs = dict()
    for l, i in zip(labels, images):
        pairs[l] = i   
    return(pairs)
