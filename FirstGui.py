import wx
class Frame(wx.Frame):
             def __init__(self):
                    wx.Frame.__init__(self, None, title ='hey world', size = (600, 500))
                    panel = wx.Panel(self)
                    button = wx.Button(panel, label = ' Exit' , size = (100, 50), pos = (100,50))
                    button.Bind(wx.EVT_BUTTON , self.Exit)
                    menuBar = wx.MenuBar()
                    fileEdit = wx.Menu()
                    fileExit = wx.Menu()
                    self.SetMenuBar(menuBar)
                    menuBar.Append(fileEdit , "Edit")
                    menuBar.Append(fileExit , "Exit")
                    self.CreateStatusBar()
                    fileExit.Append(wx.NewId(), 'Exit', ' click here to exit ')
                    fileExit.Bind(wx.EVT_MENU, self.Exit)
             def Exit(self , event):
                 self.Destroy()

app = wx.App()
frame = Frame()
frame.Show()
app.MainLoop()

            
