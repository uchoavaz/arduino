from Tkinter import *

class initializer:
	def __init__(self):
		raiz = Tk()
		raiz.geometry("250x150")
		window(raiz)
		raiz.mainloop()

class window:
	def init(self, containerTop):
			self.frame1 = Frame(containerTop)
			self.frame1.pack()