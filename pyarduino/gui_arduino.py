from Tkinter import *
from com_arduino import *
import time

user = arduino()

class window:
	def __init__(self,containerTop):

		if user.conect():
			self.frame1 = Frame(containerTop)
			self.frame1.pack()

			self.frame2 = Frame(containerTop)
			self.frame2.pack()

			self.frame3 = Frame(containerTop)
			self.frame3.pack()

			self.frame4 = Frame(containerTop)
			self.frame4.pack()

			self.frame5 = Frame(containerTop)
			self.frame5.pack()

			self.frame6 = Frame(containerTop)
			self.frame6.pack()

			self.frame7 = Frame(containerTop)
			self.frame7.pack()

			self.texto = Label(self.frame1, text =user.port + "\n" )
			self.texto.pack()

			self.hrText = Label(self.frame2, text="HORAS:       ")
			self.hrText.pack(side =LEFT)
			self.hrEnter =Entry(self.frame2, width = 5)
			self.hrEnter.pack(side=LEFT)

			self.minText = Label(self.frame3, text="MINUTOS:    ")
			self.minText.pack(side =LEFT)
			self.minEnter =Entry(self.frame3, width = 5)
			self.minEnter.pack(side=LEFT)

			self.secText = Label(self.frame4, text="SEGUNDOS: ")
			self.secText.pack(side =LEFT)
			self.secEnter =Entry(self.frame4, width = 5)
			self.secEnter.pack(side=LEFT)

			self.send = Button(self.frame5, text = "Programar !", background='blue')
			self.send.bind("<Button-1>", self.calc)
			self.send.pack(side =LEFT)

			self.state = Button(self.frame5, text = "ligar", background ='green')
			self.state.bind("<Button-1>", self.turnState)
			self.state.pack(side=LEFT)

			self.texto = Label(self.frame6, text =" " )
			self.texto.pack()

		else:
			self.frame1 = Frame(containerTop)
			self.frame1.pack()

			self.frame2 = Frame(containerTop)
			self.frame2.pack()

			self.frame3 = Frame(containerTop)
			self.frame3.pack()

			self.frame4 = Frame(containerTop)
			self.frame4.pack()

			self.frame5 = Frame(containerTop)
			self.frame5.pack()

			self.frame6 = Frame(containerTop)
			self.frame6.pack()

			self.frame7 = Frame(containerTop)
			self.frame7.pack()

			self.texto = Label(self.frame1, text="Conect Arduino")
			self.texto.pack()

			self.refresh = Button(self.frame2, text = "Refresh", background='green')
			self.refresh.bind("<Button-1>", self.conected)
			self.refresh.pack()



	def turnState(self, event):
		if self.state['text']=="ligar":
			self.state['text']="desligar"
			self.state['background'] = 'red'

			user.state()

		else:
			self.state['text']="ligar"
			self.state['background'] = 'green'

			user.state(False)

	def calc(self, event):
	
		self.texto['text'] = self.time()

		self.send2 = Button(self.frame7, text = "Iniciar !", background='red')
		self.send2.bind("<Button-1>", self.program)
		self.send2.pack(side =LEFT)

	def program(self, event):

		user.timer(self.hrEnter.get(),self.minEnter.get(),self.secEnter.get())
		self.send2.destroy()

	def conected(self, event):
		if user.conect():

			self.texto.destroy()
			self.refresh.destroy()

			self.hrText = Label(self.frame1, text="HORAS:       ")
			self.hrText.pack(side =LEFT)
			self.hrEnter =Entry(self.frame1, width = 5)
			self.hrEnter.pack(side=LEFT)

			self.minText = Label(self.frame2, text="MINUTOS:    ")
			self.minText.pack(side =LEFT)
			self.minEnter =Entry(self.frame2, width = 5)
			self.minEnter.pack(side=LEFT)

			self.secText = Label(self.frame3, text="SEGUNDOS: ")
			self.secText.pack(side =LEFT)
			self.secEnter =Entry(self.frame3, width = 5)
			self.secEnter.pack(side=LEFT)

			self.send = Button(self.frame4, text = "Programar !", background='blue')
			self.send.bind("<Button-1>", self.program)
			self.send.pack(side =LEFT)
			self.state = Button(self.frame4, text = "ligar", background ='green')
			self.state.bind("<Button-1>", self.turnState)
			self.state.pack(side=LEFT)

			self.texto = Label(self.frame5, text =" " )
			self.texto.pack()

			self.texto2 = Label(self.frame6, text =user.port)
			self.texto2.pack()

	def time(self):
		finalTime = self.hrEnter.get() + ":" + self.minEnter.get() + ":" + ":" + self.secEnter.get()
		conc = "De :" + time.strftime("Data:%d/%m/%Y as %H:%M:%S " + "\n" + "Tempo programado: " +  finalTime )

		return (conc)




raiz = Tk()
raiz.geometry("300x200")
window(raiz)
raiz.mainloop()