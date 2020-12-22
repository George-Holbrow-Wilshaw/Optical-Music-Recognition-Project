import pandas as pd
import imageio 
import re

class primusSequence:

    def __init__(self, folder, package):
        self.image = imageio.imread("./data/" + package + "/" + folder + "/" + folder + ".png")
        self.semantic = open("./data/" + package + "/" + folder + "/" + folder + ".semantic").read()
        self.labels = re.findall(r'note\-(.+?)\_', self.semantic)
        
    def flattened_image(self):
        im = self.image
        return(im.flatten())
                                    
        
def init_objs(dataset):
    
    if dataset == 'train':
        ROOT = './data/package_aa/'
        package = 'package_aa'
    elif dataset == 'validate':
        ROOT = './data/package_ab/'
        package = 'package_ab'

    folders = [directory for directory in os.listdir(ROOT) if os.path.isdir(ROOT+directory)]
    objs = []
    
    for f in folders:
        objs.append(primusSequence(f, package))
        
    return(objs)