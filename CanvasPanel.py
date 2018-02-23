import wx
from wx.lib.floatcanvas import NavCanvas, FloatCanvas
import numpy
from scipy import misc

import wx

class CanvasPanel(wx.Window):
    def __init__(self, *args, **kw):
        wx.Panel.__init__(self, *args, **kw)
        self.mask = None
        self.mainImage = None
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

        #self.bmp = wx.Bitmap(28,28,32)
        #print(self.mask.IsOk())
        #self.bmp = self.MakeMask(self.mask, 32)
    def LoadImage(self, filename):
        Image = wx.Image(filename)
        self.Canvas.AddScaledBitmap(Image, (0,0), Height = Image.GetAlpha())
    def setImage(self, image):
        self.mainImage = image
    def setMask(self, mask):
        self.mask = mask
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc = wx.BufferedDC(dc)
        dc.SetBackground(wx.Brush("WHITE"))
        dc.Clear()
        dc.SetBrush(wx.Brush("GREY", wx.BRUSHSTYLE_CROSSDIAG_HATCH))
        windowsize= self.GetSize()
        dc.DrawRectangle(0, 0, windowsize[0], windowsize[1])
        print(self.mask)
        image= self.mainImage.AdjustChannels(1.0, 1.0, 1.0, 1.0)
        bitmap= wx.Bitmap(image)
        dc.DrawBitmap(bitmap, 0, 0, True)
        image= self.mask.AdjustChannels(1.0, 1.0, 1.0, 0.2)
        bitmap= wx.Bitmap(image)
        dc.DrawBitmap(bitmap, 0, 0, True)
        #dc.DrawBitmap(wx.Bitmap(self.mainImage),-1,-1,True)
        #dc.DrawBitmap(wx.Bitmap(self.mask), 25, 25, True)
    def OnLeftDown(self, evt):
        print(evt.GetPosition())
        return

    def OnLeftUp(self, evt):
        return

    def OnMouseMove(self, evt):
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


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frm = wx.Frame(None, title="wx.Overlay Test", size=(450, 450))
    # frm.SetDoubleBuffered(True)
    pnl = CanvasPanel(frm)
    frm.Show()
    app.MainLoop()