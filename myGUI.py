import wx, sqlite3

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))
        panel = wx.Panel(self)











app = wx.App()
frame = Frame('Magical GUI')
frame.Show()
app.MainLoop()