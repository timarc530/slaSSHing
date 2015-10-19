import wx
__author__ = 'Will'

ID_NAME_STRING = 0
ID_HOST_STRING = 1
ID_PASSWORD_STRING = 2
ID_SUBMIT_BUTTON = 3
ID_SSH_STRING = 4
ID_QUIT = 5
ID_OPEN = 6


class myPrompt(wx.Dialog):

    def __init__(self, parent, title):
        super(myPrompt, self).__init__(parent, title=title, size=(500, 400))
        wx.EVT_CLOSE(self, self.OnQuit)
        self.Centre()
        self.Show(True)

        # define panes and sizers
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')
        hbox = wx.BoxSizer(wx.VERTICAL)
        fgs_name_and_host = wx.FlexGridSizer(rows=8, cols=3, vgap=9, hgap=25)
        fgs_key_file = wx.FlexGridSizer(rows=4, cols=3, vgap=9, hgap=25)
        fgs_control_buttons = wx.FlexGridSizer(rows=1, cols=2, vgap=9, hgap=25)

        # add buttons and text boxes
        name_label = wx.StaticText(panel, label='NAME')
        self.name_string = wx.TextCtrl(panel, id=ID_NAME_STRING)

        host_label = wx.StaticText(panel, label='HOST')
        self.host_string = wx.TextCtrl(panel, id=ID_HOST_STRING)

        self.rb_pw = wx.RadioButton(panel, size=(10, 10), style=wx.RB_GROUP)
        self.rb_key = wx.RadioButton(panel, size=(10, 10))
        password_label = wx.StaticText(panel, label='PASSWORD')
        self.password_string = wx.TextCtrl(panel, id=ID_PASSWORD_STRING)

        self.key_button = wx.Button(panel, id=ID_OPEN, label='SELECT KEY', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnKeyOpen, id=ID_OPEN)
        self.key_label = wx.StaticText(panel, label='path to key file')

        self.rb_RSA = wx.RadioButton(panel, label='RSA', size=(10, 10), style=wx.RB_GROUP)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnKeyTypeSet, id=self.rb_RSA.GetId())
        self.rb_DSA = wx.RadioButton(panel, label='DSA', size=(10, 10))
        self.Bind(wx.EVT_RADIOBUTTON, self.OnKeyTypeSet, id=self.rb_DSA.GetId())
        self.rb_ECDSA = wx.RadioButton(panel, label='ECDSA', size=(10, 10))
        self.Bind(wx.EVT_RADIOBUTTON, self.OnKeyTypeSet, id=self.rb_ECDSA.GetId())
        self.key_type = self.rb_RSA.GetLabelText()

        self.submit_button = wx.Button(panel, wx.ID_OK, label='SUBMIT', size=(70, 30))
        self.cancel_button = wx.Button(panel, id=ID_QUIT, label='CANCEL', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnQuit, id=ID_QUIT)

        # add widgets to sizer and expand the text boxes
        fgs_name_and_host.AddMany([(0, 0), (name_label, 1, wx.EXPAND), (self.name_string, 1, wx.EXPAND),
                                   (0, 0), (host_label, 1, wx.EXPAND), (self.host_string, 1, wx.EXPAND),
                                   self.rb_pw, (password_label, 1, wx.EXPAND), (self.password_string, 1, wx.EXPAND)])
        fgs_key_file.AddMany([self.rb_key, self.key_button, (self.key_label, 1, wx.EXPAND),
                             (0, 0), (0, 0), (self.rb_RSA, 1, wx.EXPAND),
                             (0, 0), (0, 0), (self.rb_DSA, 1, wx.EXPAND),
                             (0, 0), (0, 0), (self.rb_ECDSA, 1, wx.EXPAND)])
        fgs_control_buttons.AddMany([self.submit_button, self.cancel_button])

        fgs_name_and_host.AddGrowableCol(2)

        hbox.Add(fgs_name_and_host, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        hbox.Add(fgs_key_file, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        hbox.Add(fgs_control_buttons, proportion=1, flag=wx.ALL | wx.EXPAND, border=20)
        panel.SetSizer(hbox)

        # lame hack for getting it to draw correctly
        self.SetSize((self.GetSize().width, self.GetSize().height+1))
        self.SetSize((self.GetSize().width, self.GetSize().height-1))

    def OnKeyTypeSet(self, event):
        self.key_type = event.EventObject.GetLabelText()

    def OnKeyOpen(self, event):
        fileDialog = wx.FileDialog(self, "Open key file", "", "", "PEM files (*.pem)|*.pem|Text files (*.txt)|*.txt",
                                   wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if fileDialog.ShowModal() == wx.ID_CANCEL:
            fileDialog.Destroy()

        self.key_label.SetLabelText(fileDialog.GetPath())

    def OnQuit(self, event):
        self.Destroy()


def main():
    print '***begin testing***'
    ex = wx.App()
    myPrompt(None, title='test')
    ex.MainLoop()


if __name__ == '__main__':
    main()
