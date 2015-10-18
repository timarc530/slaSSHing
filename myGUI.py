import wx
import NewSessionWindow
__author__ = 'Will'

ID_INCOMING_TEXT = 0
ID_OUTGOING_TEXT = 1
ID_GET_BUTTON = 2
ID_SEND_BUTTON = 3
ID_SSH_STRING = 4


class GUI(wx.Frame):

    def __init__(self, parent, title):
        super(GUI, self).__init__(parent, title=title, size=(800, 600))

        self.Centre()
        self.Show(True)

        # define panes and sizers
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(rows=3, cols=2, vgap=9, hgap=25)

        # add buttons and text boxes
        self.ssh_string = wx.StaticText(panel, id=ID_SSH_STRING, label='SSH String goes here')
        self.ssh_string.SetBackgroundColour('white')
        self.incoming = wx.TextCtrl(panel, id=ID_INCOMING_TEXT, style=wx.TE_MULTILINE)
        self.outgoing = wx.TextCtrl(panel, id=ID_OUTGOING_TEXT, style=wx.TE_MULTILINE)

        get_button = wx.Button(panel, id=ID_GET_BUTTON, label='Get', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnGet, id=ID_GET_BUTTON)

        send_button = wx.Button(panel, id=ID_SEND_BUTTON, label='Send', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnSend, id=ID_SEND_BUTTON)

        # add widgets to sizer and expand the text boxes
        fgs.AddMany([(self.ssh_string, 1, wx.EXPAND), (0, 0),
                     (self.incoming, 1, wx.EXPAND), (self.outgoing, 1, wx.EXPAND),
                    get_button, send_button])
        fgs.AddGrowableRow(1)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)

        # menu bar code
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        nitem = fileMenu.Append(wx.ID_NEW, '&New Session', 'Quit application')
        fitem = fileMenu.Append(wx.ID_EXIT, '&Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        self.Bind(wx.EVT_MENU, self.OnNew, nitem)
        self.SetTitle('HACKATHON GUI')

    def OnGet(self, event):
        tx = 'new ssh string received'
        self.ssh_string.SetLabelText(tx)

    def OnSend(self, event):
        tx = self.outgoing.GetValue()
        if tx != '':
            print tx

    def OnNew(self, event):
        print 'new session'
        chooser = NewSessionWindow.myPrompt(None, title='Choose Session Parameters')
        if chooser.ShowModal() == wx.ID_OK:
            name_string = chooser.name_string
            host_string = chooser.host_string
            password_string = chooser.password_string
            print name_string.GetValue() + '@' + host_string.GetValue()
        else:
            chooser.Destroy()

    def OnQuit(self, event):
        print '***end testing***'
        self.Close()


def main():
    print '***begin testing***'
    ex = wx.App()
    GUI(None, title='test')
    ex.MainLoop()


if __name__ == '__main__':
    main()
