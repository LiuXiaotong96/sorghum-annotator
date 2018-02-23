import numpy as np
from operator import attrgetter
import SegTool
class Segmap():
    def __init__(self, segmap):
        self.segmap = segmap
        self.sorghumMap = segmap[:,:,0]
        self.stemMap = segmap[:,:,1]
        self.leafMap = segmap[:,:,2]
        self.sorghumList = []
    def solveDependcy(self):
        pass
    def newSorghum(self, clickX, clickY):
        if len(self.sorghumList) == 0:
            sorghumId = 1
        else:
            sorghumId = max(self.sorghumList, key=attrgetter('sorghumId')).sorghumId + 1
    def modifyStem(self, clickX, clickY, mode='add', ):




class Sorghum():
    def __init__(self, sorghumId):
        self.sorghumId = sorghumId
        self.stemId = sorghumId
        self.leafIdList = []


