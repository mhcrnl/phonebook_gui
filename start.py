import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()


    def basicGUI(self):
        # Creating the Panel to hold the stuff
        panel = wx.Panel(self)

        # Create the menu bar
        menuBar = wx.MenuBar()

        # Menu Items
        fileButton = wx.Menu()
        editButton = wx.Menu()

        # Buttons in File Menu
        exitItem = fileButton.Append(wx.ID_CLOSE, 'Exit', 'status message')

        # Buttons in Edit Menu
        copyItem = editButton.Append(wx.ID_COPY, 'Copy')

        # Adding Menu Items to menuBar
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

        # Initializing the menuBar
        self.SetMenuBar(menuBar)

        # Binding the quitProgram function to the exit button
        self.Bind(wx.EVT_MENU, self.quitProgram, exitItem)

        # Setting the title of the window
        self.SetTitle('Epic Window')

        # Making the window actually show up
        self.Show(True)

    def quitProgram(self, e):
        self.Close()


def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()



main()