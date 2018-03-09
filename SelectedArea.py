import numpy as np
import logging
from SegTool import SegTool

class SelectedArea():
    MW_MODE_DEFAULT = 1
    MW_MODE_FOUR_POINT = 2
    MW_MODE_DIFF = 3
    TYPE_STEM = 1
    TYPE_LEAF = 2
    MODIFY_MODE_ADD = 1
    MODIFY_MODE_MINUS = 2
    def __init__(self, areaMask, type='stem', id=1):
        self.areaMask = np.array(areaMask)
        self.type = type
        self.id = id
        self.logger = logging.getLogger('SelectedArea')
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self.logger.addHandler(ch)
        #self.logger.debug('areaShape type: %s', self.areaMask.shape)

    def newArea(self, segmap, clickX, clickY, x2=0, y2=0, x3=0, y3=0, x4=0, y4=0, threshold = 50, mwMode=2, image = None):
        if self.type == SelectedArea.TYPE_STEM:
            if mwMode == SelectedArea.MW_MODE_FOUR_POINT:
                self.areaMask = SegTool.find_stem(segmap, clickX, clickY, x2, y2, x3, y3, x4, y4)
        elif self.type == SelectedArea.TYPE_LEAF:
            self.logger.debug('new leaf area from point:%d, %d. Threshold: %d', clickX, clickY, threshold)
            self.areaMask = SegTool.add_leaf(image, clickX, clickY, threshold, pointmap=segmap)
        self.logger.debug('new areaShape: %s', self.areaMask.shape)
    def modifyArea(self, id, segmap , image, clickX, clickY, threshold, mwMode = 1, opMode = 1):
        if self.type == SelectedArea.TYPE_STEM:
            # TODO
            pass
        elif self.type == SelectedArea.TYPE_LEAF:
            if mwMode == SelectedArea.MW_MODE_DEFAULT:
                is_nei = False
            elif mwMode == SelectedArea.MW_MODE_DIFF:
                is_nei = True
            else:
                self.logger.error('modifyArea has no mode: %s', mode)
            if opMode == SelectedArea.MODIFY_MODE_ADD:
                self.areaMask = SegTool.add_leaf(image, clickX, clickY, threshold, is_nei=is_nei, ID=id)
                #self.logger.debug('add leaf area from point:%s, %s. Threshold: %s', clickX, clickY, threshold)
            elif opMode ==SelectedArea.MODIFY_MODE_MINUS:
                self.areaMask = SegTool.minus_leaf(image, clickX, clickY, threshold, is_nei=is_nei, ID=id)
                #self.logger.debug('minus leaf area from point:%d, %d. Threshold: %d', clickX, clickY, threshold)
            else:
                self.logger.error('modifyArea has no opeate mode: %s', opMode)
        pass
    def lassoArea(self, id, segmap, clickList):
        self.logger.debug('Lasso calc start.')
        self.areaMask = SegTool.lasso(segmap, clickList)
        self.logger.debug('Lasso calc end.')
    def clear(self):
        self.areaMask.fill(0)
        self.id = 0
    def setId(self, id):
        self.id = id
        self.areaMask = self.areaMask.astype('bool') * id
        pass



