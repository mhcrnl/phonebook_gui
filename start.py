import wx

class windowClass(wx.Frame):
    def __init__(self, parent, title):
        super(windowClass, self).__init__(parent, title=title, size=(400, 400))

        # Setting the window to open in a different location
        # self.Move((800,350))
        self.Centre()


        self.Show()

app = wx.App()
windowClass(None, title='epic window')
app.MainLoop()


