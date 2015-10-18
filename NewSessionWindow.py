import wx
__author__ = 'Will'

ID_NAME_STRING = 0
ID_HOST_STRING = 1
ID_PASSWORD_STRING = 2
ID_SUBMIT_BUTTON = 3
ID_SSH_STRING = 4
ID_QUIT = 5


class myPrompt(wx.Dialog):

    def __init__(self, parent, title):
        super(myPrompt, self).__init__(parent, title=title, size=(500, 300))

        self.Centre()
        self.Show(True)

        # define panes and sizers
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(rows=4, cols=2, vgap=9, hgap=25)

        # add buttons and text boxes
        name_label = wx.StaticText(panel, label='NAME:')
        self.name_string = wx.TextCtrl(panel, id=ID_NAME_STRING)
        name_label.SetBackgroundColour('white')

        host_label = wx.StaticText(panel, label='HOST')
        self.host_string = wx.TextCtrl(panel, id=ID_HOST_STRING)
        host_label.SetBackgroundColour('white')

        password_label = wx.StaticText(panel, label='PASSWORD')
        self.password_string = wx.TextCtrl(panel, id=ID_PASSWORD_STRING)
        password_label.SetBackgroundColour('white')

        self.submit_button = wx.Button(panel, wx.ID_OK, label='SUBMIT', size=(70, 30))
        self.cancel_button = wx.Button(panel, id=ID_QUIT, label='CANCEL', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnQuit, id=ID_QUIT)

        # add widgets to sizer and expand the text boxes
        fgs.AddMany([(name_label, 1, wx.EXPAND), (self.name_string, 1, wx.EXPAND),
                     (host_label, 1, wx.EXPAND), (self.host_string, 1, wx.EXPAND),
                     (password_label, 1, wx.EXPAND), (self.password_string, 1, wx.EXPAND),
                     self.submit_button, self.cancel_button ])

        fgs.AddGrowableCol(1)
        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)

        self.Maximize()
        self.Restore()

    def OnQuit(self, event):
        self.Destroy()


def main():
    print '***begin testing***'
    ex = wx.App()
    myPrompt(None, title='test')
    ex.MainLoop()


if __name__ == '__main__':
    main()
