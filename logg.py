import os, time
# funcion logg file ID link time music or video y error
# crear archivo si no existe
# add data to archivo
def add_data_log(error):
	hora = time.strftime("%X")
	filename = '\\logger.dat'
	ruta = os.getcwd()
	file = open(ruta + filename, "a", encoding="ISO-8859-1")
	file.write(hora+ os.linesep)
	file.write(error+os.linesep)
	file.write("###############################################################################################"+os.linesep)
	file.close()
# talves crear un archivo por ID
# add_data_log(error)