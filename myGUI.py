import wx, sqlite3

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))
        panel = wx.Panel(self)

        # Create a Menu Bar
        menuBar = wx.MenuBar()
        # Create FileMenu as a menu option
        fileMenu = wx.Menu()
        # Add exitItem (Exit) as an option under File on MenuBar
        exitItem = fileMenu.Append(wx.NewId(), 'Exit')
        # Add fileMenu to actually show up on MenuBar
        menuBar.Append(fileMenu, 'File')
        # Setting the Menu Bar (Turning it on)
        self.SetMenuBar(menuBar)

        # Binding exitProgram action to exitItem
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)


    def exitProgram(self, event):
        # Creating yes/no dialog box
        yesNoBox = wx.MessageDialog(None, 'Are you sure you want to quit?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        if yesNoAnswer == wx.ID_NO:
            pass
        if yesNoAnswer == wx.ID_YES:
            # Terminate Program
            self.Destroy()





app = wx.App()
frame = Frame('Magical GUI')
frame.Show()
app.MainLoop()