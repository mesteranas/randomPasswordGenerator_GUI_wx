import pyperclip
import wx
import string
import random

class main(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="Random Password Generator",size=(500,500))
		self.panel = wx.Panel(self) 
 
		self.label_1 = wx.StaticText(self.panel, label="Random Password Length:", pos=(10,20))
		self.txt_1 = wx.SpinCtrl(self.panel, -1, min=5, max=10000000, initial = 10)
		self.button_1 = wx.Button(self.panel,label="&Generate", pos=(250,20))
		self.button_1.Bind(wx.EVT_BUTTON, self.Generate)
		self.label_2 = wx.StaticText(self.panel, label="Generate Password:", pos=(10,50))
		self.txt_2 = wx.TextCtrl(self.panel, value="",style=wx.TE_MULTILINE+wx.HSCROLL+wx.TE_READONLY, pos=(150,50))
		copy= wx.Button(self.panel, -1, "&copy")
		self.Show()
		self.Bind(wx.EVT_BUTTON, lambda event: 		pyperclip.copy(self.txt_2.Value), copy)
	def Generate(self, event):
		length = int(self.txt_1.GetValue()) 
		alphabet = string.ascii_letters + string.digits
		password = ''.join(random.choice(alphabet) for i in range(length))
		self.txt_2.SetValue(password)
app=wx.App()
w=main()
w.Show()
app.MainLoop()