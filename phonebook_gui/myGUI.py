import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))
        panel = wx.Panel(self)

        # ******************************************************************
        # ******************* Menu Bar Creation ****************************
        # ******************************************************************

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


        # ******************************************************************
        # ******************* Layout Setup *********************************
        # ******************************************************************

        # Setting up UI for adding a new contact area
        wx.StaticBox(panel, label="Add a new contact", pos=(20,40), size=(300,200))

        # creating add new contact labels and text boxes
        wx.StaticText(panel, label="First Name:", pos=(40,70))
        self.cFName = wx.TextCtrl(panel, size=(150, -1), pos=(150, 70))
        wx.StaticText(panel, label="Last Name:", pos=(40,110))
        self.cLName = wx.TextCtrl(panel, size=(150, -1), pos=(150, 110))
        wx.StaticText(panel, label="Phone Number:", pos=(40,150))
        self.cPhone = wx.TextCtrl(panel, pos=(150, 150), size=(150,-1))
        wx.StaticText(panel, label="Email Address:", pos=(40,190))
        self.cEmail = wx.TextCtrl(panel, size=(150, -1), pos=(150, 190))

        # Setting up the table to display information
        self.listCtrl = wx.ListCtrl(panel, size=(300, 400), pos=(350, 40), \
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        # Adding columns to the table
        self.listCtrl.InsertColumn(0, "ID")
        self.listCtrl.InsertColumn(1, "First Name")
        self.listCtrl.InsertColumn(2, "Last Name")



        # ******************************************************************
        # ******************* Buttons Creation *****************************
        # ******************************************************************

        # Save Button
        saveBtn = wx.Button(panel, label="Add Contact", pos=(180,250))
        # Delete Button
        deleteBtn = wx.Button(panel, label="Delete Contact", pos=(50, 250))




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
frame = Frame('Basic Contact List')
frame.Show()
app.MainLoop()