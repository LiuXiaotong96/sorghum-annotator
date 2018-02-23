import os
import wx
from scipy import misc
import numpy as np
class DataModel():

    def __init__(self, imageRoot, segmapRoot):
        self.imageRoot = imageRoot
        self.segmapRoot = segmapRoot
        self.imageNameList = os.listdir(self.imageRoot);
        self.imageList = []
        self.segmapList = []

    def getImageList(self):
        for name in self.imageNameList:
            im = misc.imread(os.path.join(self.imageRoot, name))
            self.imageList.append(im)
    def getImageByIdx(self, idx):
        return misc.imread(os.path.join(self.imageRoot, self.imageNameList[idx]))

    def getSegmapByIdx(self, idx):
        if not os.path.isfile(os.path.join(self.segmapRoot, self.imageNameList[idx])):
            image = misc.imread(os.path.join(self.imageRoot, self.imageNameList[idx]))
            segmap = np.zeros(image.shape)
            misc.imsave(os.path.join(self.segmapRoot, self.imageNameList[idx]), segmap)
        else:
            segmap = misc.imread(os.path.join(self.segmapRoot, self.imageNameList[idx]))
        return segmap

    def saveSegmap(self,segmap, name):
        pass

    def npyToBitmap(self, image):
        image = image[:,:,0:3]
        print(image.shape)
        if len(image.shape) == 2:
            height, width = image.shape
        if len(image.shape) == 3:
            height, width,_ = image.shape
        bitmapImage = wx.Image(width,height)
        bitmapImage.SetData( image.tostring())
        return bitmapImage