# -*- coding: utf-8 -*-
import serial

class arduino:
	def __init__(self):
		self.port = ""


	def conect(self):

		speed = 9600
		numPort = 0
		door = False

		while door == False:
			try:
				self.port = "/dev/ttyACM%d" % numPort
				self.conection = serial.Serial(self.port,speed,timeout=5)
				print("Arduino conected! Porta: /dev/ttyACM%d \n" % numPort)
				door = True
				return True
			except:
				if numPort <=10:
					numPort = numPort + 1
				else:
					print("Conect arduino")
					numPort = 0
					door = True


	def state(self,on = True):
		try:
			if on == True:
				self.conection.write("1")

			else:
				self.conection.write("0")

		except:
			print("conect arduino")

	def timer(self, hours, minutes, seconds):
	
		self.conection.write("H%sEM%sES%sE" % (int(hours), int(minutes), int(seconds)))

		left = False
		while left==False:
			self.data= (self.conection.readline().strip())
			if self.data == "OK":
				left = True


			else:
				print(self.data)
