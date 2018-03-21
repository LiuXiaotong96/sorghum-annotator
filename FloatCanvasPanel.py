import wx
from wx.lib.floatcanvas import NavCanvas, FloatCanvas
import numpy
from scipy import misc
from DataModel import DataModel

class CanvasPanel(wx.lib.floatcanvas.NavCanvas.NavCanvas):
    def __init__(self, parent, BackgroundColor = "DARK SLATE BLUE"):
        #wx.Panel.__init__(self, *args, **kw)
        NavCanvas.NavCanvas.__init__(self, parent, Debug=1, BackgroundColor=BackgroundColor)
        self.mask = None
        self.mainImage = None
        #self.SetScrollRate(20, 20)
        self.maxWidth  = 3000
        self.maxHeight = 3000
        #self.SetVirtualSize((self.maxWidth, self.maxHeight))
        #self.Bind(wx.EVT_SIZE, self.OnSize)
        #self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Canvas.Bind(FloatCanvas.EVT_LEFT_DOWN, self.OnLeftDown)
        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(FloatCanvas.EVT_MOTION, self.OnMouseMove)
        #self.bmp = wx.Bitmap(28,28,32)
        #print(self.mask.IsOk())
        #self.bmp = self.MakeMask(self.mask, 32)
    def SetScale(self, xs, ys):
        super().SetScale(xs, ys)
        maxWidth = self.maxWidth  * xs
        maxHeight = self.maxHeight * ys
        self.SetVirtualSize(maxWidth, maxHeight)
    #def LoadImage(self, filename):
    #    Image = wx.Image(filename)
    #    self.Canvas.AddScaledBitmap(Image, (0,0), Height = Image.GetAlpha())
    def setImage(self, image):
        self.mainImage = image
        self.maxWidth = round(image.GetWidth()*1.2)
        self.maxHeight = round(image.GetHeight()*1.2)
    def setMask(self, mask):
        self.mask = mask
    def OnPaint(self, evt):
        print("OnPAint")
        dc = wx.PaintDC(self)
        dc = wx.BufferedDC(dc)
        self.PrepareDC(dc)
        #dc.SetUserScale(3.0, 3.0)
        dc.SetBackground(wx.Brush("WHITE"))
        dc.Clear()
        dc.SetBrush(wx.Brush("GREY", wx.BRUSHSTYLE_CROSSDIAG_HATCH))
        dc.DrawRectangle(0, 0, self.maxWidth, self.maxHeight)
        image= self.mainImage.AdjustChannels(1.0, 1.0, 1.0, 1.0)
        bitmap= wx.Bitmap(image)
        dc.DrawBitmap(bitmap, 0, 0, True)
        image= self.mask.AdjustChannels(20.0, 255.0, 255.0, 0.2)
        bitmap= wx.Bitmap(image)
        dc.DrawBitmap(bitmap, 0, 0, True)
        #dc.DrawBitmap(wx.Bitmap(self.mainImage),-1,-1,True)
        #dc.DrawBitmap(wx.Bitmap(self.mask), 25, 25, True)
    def OnLeftDown(self, evt):
        print(evt.GetPosition())
        if evt.Dragging():
            print('DRAGGING')
        return

    def OnLeftUp(self, evt):
        return

    def OnMouseMove(self, evt):
        if evt.Dragging():
            print('Dragging: %s', evt.Coords)
        return

    def OnSize(self, evt):
        self.Refresh()
    def OnEraseBackground(self, evt):
        pass
    def MakeMask(self, bitmap, alpha = 32):
        pixelData = wx.AlphaPixelData(bitmap)
        pixels = pixelData.GetPixels()
        for y in range(28):
            pixels.MoveTo(pixelData, 0, y)
            for x in range(28):
                pixels.Set(255,0,0,alpha)
                pixels.nextPixel()
        return bitmap

    def CalcGlobalPosition(self, posX, posY):
        x, y = self.CalcUnscrolledPosition(posX, posY)
        x = round(x / self.GetScaleX())
        y = round(y / self.GetScaleY())
        return (x, y)


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frm = wx.Frame(None, title="wx.Overlay Test", size=(450, 450))

    dataModel = DataModel('./images', './segmaps')
    segmap = dataModel.getSegmapByIdx(0)
    image = dataModel.getImageByIdx(0)
    imageBitmap = dataModel.npyToBitmap(image)
    segmapBitmap = dataModel.npyToBitmap(segmap)
    segmapBitmap = segmapBitmap.AdjustChannels(20.0, 255.0, 255.0, 0.2)
    # frm.SetDoubleBuffered(True)
    pnl = CanvasPanel(frm)
    print(imageBitmap.GetHeight(), ',' , imageBitmap.GetWidth())
    imageObj = pnl.Canvas.AddScaledBitmap(imageBitmap, (0, 0), Height = imageBitmap.GetHeight(), Position = 'bl')
    #pnl.Canvas.RemoveObject(imageObj, False)
    pnl.Canvas.AddScaledBitmap(segmapBitmap, (0, 0), Height = segmapBitmap.GetHeight(), Position = 'bl')
    #pnl.setImage(dataModel.npyToBitmap(image))
    #pnl.setMask(dataModel.npyToBitmap(segmap))
    frm.Show()
    app.MainLoop()