import pandas as pd
import imageio 
import re

class primusSequence:

    def __init__(self, folder):
        self.image = imageio.imread("./data/package_aa/" + folder + "/" + folder + ".png")
        self.semantic = open("./data/package_aa/" + folder + "/" + folder + ".semantic").read()
        self.labels = re.findall(r'note\-(.+?)\_', self.semantic)
        
def join_images_labels(labels, images):
    pairs = dict()
    for l, i in zip(labels, images):
        pairs[l] = i   
    return(pairs)


