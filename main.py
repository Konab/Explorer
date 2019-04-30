import sys # sys нужен для передачи argv в QApplication
import os # Отсюда нам понадобится методы для отображения содержимого директорий 

from PyQt5 import QtWidgets

# import design # Это наш конвертированный файл дизайна
from libs.uix import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	'''Example App
	Так как файл с дизайном будет польностью перезаписываться каждый раз 
	при изменении дизайна, создадим новый класс ExampleApp, который объединим
	с кодом дизайна для использования всех его функций
	
	Extends:
		QTWidgets.QMainWindow -- Доступ к виджетам
		design.Ui_MainWindow -- UI приложения
	'''
	dict_name = {'py': '🐍 Python: '}

	def __init__(self):
		'''Initialisation
		Это здесь нужно для доступа к переменным, методам
		и т.д. в файде design.py
		'''
		super().__init__()
		self.setupUi(self) # Это нужно для инициализации дизайна
		self.btnBrowse.clicked.connect(self.browse_folder) # Выполнить функцию browse_folder при нажатии на кнопку
		# btrBrowse -- имя объекта который определен в QTDesigner
		# clicked -- событие, которое мы хотим привязать. 
		# connect() -- метод, который привязывает событие к вызову переданное функции
		# self.browse_folder -- просто функция (метод)

	def browse_folder(self):
		'''Browse Folder
		Открывает интерфейс для выбора папки
		Выводит содержимое папки на экран
		'''
		self.listWidget.clear() # На случай если в списке уже есть элементы
		directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку')
		# Открыть диалог выбора директории и установить значение переменной
		# равной пути к выбранной дирректории

		if directory: # Не продолжать выполнение, если пользователь не выбрал директорию
			for file_name in sorted(os.listdir(directory)): # для каждого файла директории 
				if file_name[0] == '.':
					continue
				elif '.' in file_name:
					list_file_name = file_name.split('.')
					file_name = self.dict_name[list_file_name[1]] + file_name if list_file_name[1] in self.dict_name else '🗒 File: ' + file_name
				else:
					file_name = '📂 Directory: ' + file_name
				self.listWidget.addItem(file_name) # добавить файл в listWidget


def main():
	'''MAIN'''
	app = QtWidgets.QApplication(sys.argv) # Новый экземпляр QApplicatin 
	window = ExampleApp() # Создаем объект класса ExampleApp
	window.show() # Показывает окно
	app.exec_() # и запускаем приложение


if __name__ == '__main__': # Если мы запускаем файл напрямую, а не импортируем
	main() # Запускаем функцию main()
