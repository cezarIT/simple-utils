import config
from tkinter import *
import os
import subprocess
import pyowm
class weather():
	"""погода"""
	def start(self):	
		root = Tk()
		root.title('OpenWeatherMap')
		#
		def star():
			owm = pyowm.OWM(config.token) 
			observation = owm.weather_at_place(config.citi)
			w = observation.get_weather()
			weat.set(w)
		#
		weat = StringVar()
		#
		but = Button(root, text = 'Узнать погоду', bg = 'green', command = star)
		w = Label(root, bg = 'white', textvariable = weat)
		#
		w.pack()
		but.pack()
		#
		root.mainloop()
#
#
#
class pycalc():
	def start(self):
		'''калькулятор на питоне'''
		root = Tk('')
		root.title('калькулятор')
		root.geometry('100x150+500+300')
		#комманды
		def clic2():
		    data1.set(data11.get() - data21.get())
		def clic():
		    data1.set(data11.get() + data21.get())
		def deli():
		    data1.set(data11.get() / data21.get())
		def amn():
		    data1.set(data11.get() * data21.get())
		#переменные
		data11 =IntVar()
		data11.set('1')
		data21 =IntVar()
		data21.set('2')
		data1 =IntVar()
		data1.set('0')
		#кнопки
		button = Button(root, text = '+',bg = 'green' , command = clic)
		button2 = Button(root, text = '-',bg = 'red', command = clic2)
		button3 = Button(root, text = '/',bg = 'yellow', command = deli )
		button4 = Button(root, text = '*',bg = 'white', command = amn)
		#виджеты
		entry = Entry(root, textvariable = data11)
		entry2 = Entry(root, textvariable = data21)
		label = Label(root, textvariable = data1)
		#расмещение виджетов
		label.grid(row=0, column= 0, columnspan= 4)
		entry.grid(row=1, column= 1, columnspan= 4)
		entry2.grid(row=2, column= 1, columnspan= 4)
		#расмещение кнопки
		button.grid(row=3, column= 2)
		button2.grid(row=3, column= 3)
		button3.grid(row=4, column= 2)
		button4.grid(row=4, column= 3)
		#
		root.mainloop()
#
#
#
class Note():
	def start(self):
		'''заметка'''
		root = Tk()
		root.title('Заметка')
		root.geometry('215x210+500+250')
		#
		def re():
			data2.set(config.note)	
		def wet():
			config.note = data2.get()
			
		def ex():
			root.destroy() 
		#
		data2 = StringVar()
		data2.set('text')
		#
		button1 = Button(root, text = 'чтение', bg = 'green', command = re)
		button2 = Button(root, text = 'перезапись', bg = 'yellow', command = wet)
		kill = Button(root, text = 'EXIT', bg = 'red', command = ex)
		#
		entry = Entry(root, textvariable = data2)
		#
		entry.pack()
		#
		button1.pack()
		button2.pack()
		kill.pack()
		#
		root.mainloop()
#
#
#
class osa():
	def start(self):
		'''менэджер системы'''
		root = Tk()
		root.title('OS meneger')
		#
		def osgetid():
		    i = os.getpid()
		    data23.set('ID Процессора: '+ str(i))
		def ossystem():
		    cm  = data23.get()
		    ic = os.system(cm)
		    if ic == 0:
		        data3.set('Команда выполнена')
		    else:
		        data3.set('Команда не выполнена, код ошибки: ' + str(ic))
		def pathexists():
		    pat = data23.get()
		    ip = os.path.exists(pat)
		    if ip == True:
		       data3.set("Путь указывает на сущиствуещий файл или путь")
		    elif ip == False:
		       data3.set("Путь указывает на не сущиствуещий файл или путь")
		def getctime():
		    try:
		        it = data23.get()
		        ti = os.path.getctime(it)
		        data3.set('Время создания файла (Windows), время последнего изменения файла (Unix) :' + str(ti))
		    except:
		        data23.set('Не удается найти указанный файл')
		def kill():
		    root.destroy()
		def cl():
		    data23.set('')
		#
		data23 = StringVar()
		data23.set('none')
		data3 = StringVar()
		data3.set('OS meneger')
		#
		vvod = Entry(root, bg = 'green', textvariable = data23 )
		vvyvod = Label(root, bg = 'yellow', textvariable = data3 )
		#
		b2 = Button(root, text = 'ID поцессора', command = osgetid)
		b3 = Button(root, text = 'Выполнени команды CMD', command = ossystem)
		b4 = Button(root, text = 'Сущиствует ли файл|путь', command = pathexists)
		b5 = Button(root, text = 'Время создания|изменения файла', command = getctime)
		b6 = Button(root, text = 'Выход',bg = 'red' , command = kill)
		b7 = Button(root, text = 'очистить экран', command = cl)
		#
		vvod.grid(row=0, column= 0, columnspan= 3)
		vvyvod.grid(row=1, column= 0, columnspan= 3)
		#
		b2.grid(row=2, column= 1)
		b3.grid(row=2, column= 2)
		b4.grid(row=3, column= 0)
		b5.grid(row=3, column= 1)
		b6.grid(row=5, column= 1)
		b7.grid(row=3, column= 2)
		#
		root.mainloop()
#
#
#
class OF():
	def start(self):
		'''менедер офис'''
		root = Tk()
		root.title('|><|OFFICE|><|')
		root.geometry('250x250+500+250')
		def pp():
		    subprocess.call(config.pp)
		def ex():
		    subprocess.call(config.ex)
		def wr():
		    subprocess.call(config.mw)
		def qute():
		    root.destroy()
		button1 = Button(root, text = 'PowerPoint',bg = 'orange' , command = pp)
		button2 = Button(root, text = '___Excel__',bg = 'green', command = ex)
		button3 = Button(root, text = '___Word___',bg = 'blue', command = wr )
		button4 = Button(root, text = 'EXIT',bg = 'red' , command = qute)
		label = Label(root, text = '<<<|МЭНЕДЖЕР OFFICE|>>>')
		label.pack()
		button1.pack()
		button2.pack()
		button3.pack()
		button4.pack()
		root.mainloop()
#
#
#
class FTP():
	def start(self):
		'''открытие программ'''
		root = Tk()
		root.title('Teleport For Program')
		root.geometry('200x250+500+300')
		def z():
			subprocess.call('C:/Windows/System32/notepad.exe')
		def x():
			subprocess.call('C:/Windows/System32/calc.exe')
		def c():
			subprocess.call('C:/Windows/System32/control.exe')
		def v():
			subprocess.call('C:/Windows/System32/fsquirt.exe')
		#
		button = Button(root, text = 'notepad',bg = 'green' , command = z)
		button2 = Button(root, text = 'calc',bg = 'red', command = x)
		button3 = Button(root, text = 'панель упровление',bg = 'yellow', command = c )
		button4 = Button(root, text = 'bluetooth',bg = 'white', command = v)
		natpis = Label(root, text = 'Teleport For Program')
		natpis.pack()
		button.pack()
		button2.pack()
		button3.pack()
		button4.pack()
		root.mainloop()
#
#
#
class Basic():
	def start(self):
		'''меню'''
		root = Tk()
		root.title('util')
		root.geometry('150x200+500+300')
		#
		def os():
			sys = osa()
			sys.start()
		def tp():
			tpp = FTP()
			tpp.start()
		def of():
			of = OF()
			of.start()
		def TheNote():
			n = Note()
			n.start()
		def pyc():
			pc = pycalc()
			pc.start()
		def Wemap():
			mapw = weather()
			mapw.start()
		#
		bu1 = Button(root, bg = 'yellow', text = 'OSMen', command = os)
		bu2 = Button(root, bg = 'green', text = 'Prog', command = tp)
		bu3 = Button(root, bg = 'orange', text = 'Office', command = of)
		bu4 = Button(root, bg = 'purple', text = 'TheNote', command = TheNote)
		bu5 = Button(root, bg = 'red', text = 'PyCalc', command = pyc)
		bu6 = Button(root, bg = 'white', text = 'OpenWeatherMap API', command = Wemap)
		#
		bu1.pack()
		bu2.pack()
		bu3.pack()
		bu4.pack()
		bu5.pack()
		bu6.pack()
		#
		root.mainloop()
#
#
#
class stat():
	def start(self):
		'''проверка пороля'''
		window = Tk()
		window.geometry('150x110+500+300')
		window.title('ввод пороля')
		#
		data = IntVar()
		data.set('0')
		data2 = StringVar()
		code = config.code
		#
		def CodeProgramm():
			window.destroy()
			win = Basic()
			win.start()
		def open():
			if data.get() == code:   
				CodeProgramm()
			else:
				data2.set('пороль не верный')
		#
		button = Button(window, text = 'ввести пороль', command = open)
		entry = Entry(window, textvariable = data)
		label = Label(window, textvariable = data2)
		#
		button.pack()
		entry.pack()
		label.pack()
		window.mainloop()
'''запуск'''
lock = stat()
lock.start()