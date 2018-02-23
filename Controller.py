import SegTool
from View import View
from DataModel import DataModel
import wx
from wx.lib.evtmgr import eventManager
class Controller():
    def __init__(self):
        self.dataModel = DataModel('./images', './segmaps')
        self.dataModel.getImageList()

        self.app = wx.App()
        self.view = View(None)
        self.view.setFileNameList(self.dataModel.imageNameList)
        self.TOOL_STEM_NEW = 10
        self.TOOL_LEAF_NEW = 40
        self.TOOL_LEAF_ADD = 50
        self.TOOL_LEAF_MINUS = 60
        self.curTool = self.TOOL_STEM_NEW
        self.curImage = self.dataModel.getImageByIdx(0)
        self.curMask = self.dataModel.getSegmapByIdx(0)
        eventManager.Register(self.OnCanvasLeftDown, wx.EVT_LEFT_DOWN, self.view.canvasPanel)
        eventManager.Register(self.OnToolChange, wx.EVT_TOOL, self.view.verToolBar)
        self.init()
    def init(self):
        init_image = self.dataModel.npyToBitmap(self.curImage)
        init_mask = self.dataModel.npyToBitmap(self.curMask)
        self.view.canvasPanel.setImage(init_image)
        self.view.canvasPanel.setMask(init_mask)
        self.app.MainLoop()
    def changeTool(self, tool):
        self.curTool = tool
    def OnCanvasLeftDown(self, evt):
        self.view.SetStatusText(str(evt.GetPosition()))
        if self.curTool == self.TOOL_LEAF_NEW:
            # change segmap
            # save segmap
            # update canvas
            # TODO dont save segmap into file, only if user choose to do so. Need a attr in DataModel: modified_Segmap
            pass
        if self.curTool == self.TOOL_LEAF_ADD:
            pass
        if self.curTool == self.TOOL_LEAF_MINUS:
            pass



    def OnToolChange(self, evt):
        self.curTool = evt.GetId()


