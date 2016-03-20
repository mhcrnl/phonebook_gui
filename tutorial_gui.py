import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()


    def basicGUI(self):
        # Creating the Panel to hold the stuff
        panel = wx.Panel(self)


        # DIALOG BOXES
        # Asking for user's name
        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome!', 'Michelle')
        if nameBox.ShowModal() == wx.ID_OK:
            userName = nameBox.GetValue()


        # Creating yes/no dialog box
        yesNoBox = wx.MessageDialog(None, 'Do you enjoy python?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()


        # Options box / multiple choice input (with only one allowed)
        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?', 'Color Question', \
                                             ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Pink', 'Black'])
        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        # ADDING ITEMS TO PANEL
        # Creating a textbox
        wx.TextCtrl(panel, pos=(3, 100), size=(150, 50))
        # static text
        basicText = wx.StaticText(panel, -1, 'Awesome Text', pos=(3, 3))
        basicText.SetForegroundColour(favColor)
        basicText.SetBackgroundColour('#ffffff')


        # CREATION OF MENU BAR AND ITEMS
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

        # Doing a thing with the yes/no ? answer
        if yesNoAnswer == wx.ID_NO:
            userName = 'Python Hater'


        # Setting the title of the window
        self.SetTitle('Welcome ' + userName)

        # Making the window actually show up
        self.Show(True)

    def quitProgram(self, e):
        self.Close()


def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()



main()