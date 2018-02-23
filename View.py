# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wx.lib.evtmgr import eventManager
from CanvasPanel import CanvasPanel

###########################################################################
## Class MyFrame1
###########################################################################

class View ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 722,470 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        # Data goes here
        self.fileNameList = []

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.SetMenuBar( self.m_menubar1 )

        gbSizer1 = wx.GridBagSizer( 5, 5 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        self.horToolBar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
        self.horToolBar.AddSeparator()

        self.m_staticText1 = wx.StaticText( self.horToolBar, wx.ID_ANY, u"Threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.horToolBar.AddControl( self.m_staticText1 )
        self.thresholdSlider = wx.Slider( self.horToolBar, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
        self.thresholdSlider.Bind(wx.EVT_SLIDER, self.thresholdSliderChange)
        self.horToolBar.AddControl( self.thresholdSlider )
        self.thresholdTextCtrl = wx.TextCtrl( self.horToolBar, wx.ID_ANY, "thresholdTextCtrl", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
        self.thresholdTextCtrl.SetMaxLength( 2 )
        self.thresholdTextCtrl.Bind(wx.EVT_TEXT_ENTER, self.thresholdTextChange)
        self.horToolBar.AddControl( self.thresholdTextCtrl )
        self.horToolBar.Realize()
        gbSizer1.Add( self.horToolBar, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )

        self.verToolBar = wx.ToolBar( self, 2, wx.DefaultPosition, wx.DefaultSize, wx.TB_VERTICAL )
        self.stemAdd = self.verToolBar.AddRadioTool(10 , "stemAdd", wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ), wx.NullBitmap, wx.EmptyString,"New stem", None )
        self.stemMWAdd = self.verToolBar.AddRadioTool(20 , "stemMWAdd", wx.ArtProvider.GetBitmap( wx.ART_ADD_BOOKMARK, wx.ART_TOOLBAR ), wx.NullBitmap, wx.EmptyString, wx.EmptyString, None )
        #self.stemMWAdd = self.verToolBar.AddTool(20, "stemMWAdd", wx.ArtProvider.GetBitmap( wx.ART_ADD_BOOKMARK, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, "New", "Long help for 'New'", None)

        self.stemMWMinus = self.verToolBar.AddRadioTool(30 , "stemMWMinus", wx.ArtProvider.GetBitmap( wx.ART_DEL_BOOKMARK, wx.ART_TOOLBAR ), wx.NullBitmap, wx.EmptyString, wx.EmptyString, None )

        #self.verToolBar.AddSeparator()
        self.leafAdd = self.verToolBar.AddRadioTool(40 , "leafAdd", wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ), wx.NullBitmap, wx.EmptyString, wx.EmptyString, None )
        self.leafMWAdd = self.verToolBar.AddRadioTool(50 , "leafMWAdd", wx.ArtProvider.GetBitmap( wx.ART_ADD_BOOKMARK, wx.ART_TOOLBAR ), wx.NullBitmap, wx.EmptyString, wx.EmptyString, None )
        self.leafMWMinus = self.verToolBar.AddRadioTool(60 , "leafMWMinus", wx.ArtProvider.GetBitmap( wx.ART_DEL_BOOKMARK, wx.ART_TOOLBAR ), wx.NullBitmap, wx.EmptyString, wx.EmptyString, None )
        #self.verToolBar.AddSeparator()
        self.zoomIn = self.verToolBar.AddRadioTool(70 , "zoomIn", wx.ArtProvider.GetBitmap( wx.ART_FIND, wx.ART_TOOLBAR ), wx.NullBitmap, wx.EmptyString, wx.EmptyString, None )
        self.zoomOut = self.verToolBar.AddRadioTool(80 , "zoomOut", wx.ArtProvider.GetBitmap( wx.ART_FIND_AND_REPLACE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.EmptyString, wx.EmptyString, None )
        #self.verToolBar.InsertSeparator(3)
        #self.verToolBar.InsertSeparator(6)
        self.verToolBar.Realize()
        #self.verToolBar.Bind(wx.EVT_TOOL, self.OnTestTool)
        gbSizer1.Add( self.verToolBar, wx.GBPosition( 1, 0 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )

        self.canvasPanel = CanvasPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gbSizer1.Add( self.canvasPanel, wx.GBPosition( 1, 1 ), wx.GBSpan( 2, 1 ), wx.EXPAND |wx.ALL, 5 )
        self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

        self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Images" ), wx.VERTICAL )

        self.fileListBox = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, -1), self.fileNameList, 0 )
        sbSizer2.Add( self.fileListBox, 1, wx.ALL, 5 )


        self.m_panel2.SetSizer( sbSizer2 )
        self.m_panel2.Layout()
        sbSizer2.Fit( self.m_panel2 )
        self.m_panel3 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Annotation" ), wx.VERTICAL )

        self.m_treeCtrl1 = wx.TreeCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(150, -1), wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HAS_BUTTONS )
        self.root = self.m_treeCtrl1.AddRoot('Sorghum_1')
        self.m_treeCtrl1.SetItemData(self.root, ('key', 'value'))
        os = self.m_treeCtrl1.AppendItem(self.root, 'Leaf_1')
        self.m_treeCtrl1.Expand(self.root)
        sbSizer1.Add( self.m_treeCtrl1, 1, wx.ALL, 5 )


        self.m_panel3.SetSizer( sbSizer1 )
        self.m_panel3.Layout()
        sbSizer1.Fit( self.m_panel3 )
        self.m_splitter1.SplitHorizontally( self.m_panel2, self.m_panel3, 0 )
        gbSizer1.Add( self.m_splitter1, wx.GBPosition( 1, 2 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )


        gbSizer1.AddGrowableCol( 1 )
        gbSizer1.AddGrowableRow( 1 )

        self.SetSizer( gbSizer1 )
        self.Layout()

        #eventManager.Register(self.OnCanvasLeftDown, wx.EVT_LEFT_DOWN, self.canvasPanel)

        self.Centre( wx.BOTH )
        self.Show()
    def __del__( self ):
        pass
    def m_splitter1OnIdle( self, event ):
        self.m_splitter1.SetSashPosition( 0 )
        self.m_splitter1.Unbind( wx.EVT_IDLE )
    def thresholdTextChange(self, evt):
        threshold = self.thresholdTextCtrl.GetValue()
        self.thresholdSlider.SetValue(int(threshold))
    def thresholdSliderChange(self, evt):
        threshold = self.thresholdSlider.GetValue()
        self.thresholdTextCtrl.SetValue(str(threshold))
    def setFileNameList(self, fileNameList):
        self.fileNameList = fileNameList
        self.fileListBox.Set(self.fileNameList)
    def OnCanvasLeftDown(self, evt):
        self.SetStatusText(str(evt.GetPosition()))
    def OnTestTool(self, evt):
        print(str(evt.GetId()))





if __name__ == '__main__':
        app = wx.App()
        View(None)
        app.MainLoop()


