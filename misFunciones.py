import os # para la gestion de las rutas
import shutil # para la gestion de ficheros
import xbmc #para kodi
import xbmcgui #para la interfaz grafica
import pyxbmct #para la interfaz grafica avanzada basada en xbmcgui
import xbmcaddon #para los addon de kkodi
import time #para usar la fecha del sistema




#### definimos escribe para para mostrar los textos
escribe = xbmcaddon.Addon().getLocalizedString

#Definimos dos variables globales con las rutas
rutaKeymaps = "definiendo rutaKeymaps"
rutaResources = "definiendo rutaResources"



#### Esta funcion crea la ventana negra
#### Sirve para comprobar los botones que funcionan

def crearVentanaNegra():
	#creamos una clase de tipo window
	#para definir en el onAction que extraiga los codigos de los botones
	class ventanaNegra(xbmcgui.Window):
		def __init__(self):
			self.contador = 1
			self.maxIntentos = 5

		def onAction(self, action):
			code = action.getButtonCode()
			identificador = action.getId()
			xbmcgui.Dialog().ok("Reconociendo botones ", "Boton reconocido " + str(self.contador) + "/" +str(self.maxIntentos) + "\nCodigo boton " + str(code) + "\nIdentificador boton: " + str(identificador))
			self.contador += 1
			if self.contador > self.maxIntentos:
				self.close()
			elif code == 61467:
				self.close()

	miVentanaNegra = ventanaNegra()
	titulo = xbmcgui.ControlLabel (300, 100, 700, 50, "COMPROBANDO LOS BOTONES DEL MANDO A DISTANCIA")
	miVentanaNegra.addControl(titulo)
	textBox = xbmcgui.ControlTextBox(300, 200, 500, 200, textColor="0xFFFFFFFF")
	textBox.setVisible(True)
	miVentanaNegra.addControl(textBox)
	textBox.setText("Toque las teclas de su mando a distancia para comprobar que son reconocidos por el sistema\n\nLa pantalla se cerrara automaticamente tras " + str(miVentanaNegra.maxIntentos) + " botones reconocidos")
	miVentanaNegra.doModal()




#Hacemos esta funcion para poder pasar la variables de la ruta del keymaps
#Tambien se posiciona en ella con chdir
def verRutaKeymaps():
	global rutaKeymaps
	#control, para verificar el correcto valor de rutaKeymaps
	#xbmcgui.Dialog().ok("VerRuta Keymaps function", rutaKeymaps)
	os.chdir(rutaKeymaps)
	#control, para verificar el correcto valor de ruta de la posicion en la que estamos
	#xbmcgui.Dialog().ok("get ruta keymaps en la function", os.getcwd())
	return rutaKeymaps


#Hacemos esta funcion para poder pasar la variable de la ruta de los resources
#Tambien se posiciona en ella con chdir
def verRutaResources():
	global rutaResources
	#control, para verificar el correcto valor de rutaResources
	#xbmcgui.Dialog().ok("VerRuta Resources function", rutaResources)
	os.chdir(rutaResources)
	#control, para verificar el correcto valor de ruta de la posicion en la que estamos
	#xbmcgui.Dialog().ok("get ruta resources en la function", os.getcwd())
	return rutaResources


###############################################
#### COMPROBAMOS SSOO Y CARGAMOS VARIABLES ####
###############################################
#Hacemos una funcion para verificar el SSOO y aplicar las rutas adecuadas
def verificarSSOO():
	#indicamos que hacen referencia a las variables globales
	global rutaKeymaps
	global rutaResources

	#Verificamos que se encuentran archivos y comprobamos el ssoo en el que estamos
	ventanaProgreso(30, "INICIANDO PROGRAMA", "Verificando Sistema Operativo...")
	####################
	#### para linux ####
	####################
	#Comprovamos la ruta, y definimos variables con las rutas correctas
	# ruta de keymaps de usuario 
	# ruta de resources del addon
	if os.path.exists("/home/c/.kodi/userdata/keymaps/"):
		#xbmcgui.Dialog().ok("INICIANDO PROGRAMA", "Sistema Operativo detectado:\nAplicando configuracion linux")
		ventanaProgreso(30, "Sistema Operativo Detectado", "Aplicando configuracion Linux...")
		rutaKeymaps = "/home/c/.kodi/userdata/keymaps/"
		rutaResources = "/home/c/.kodi/addons/script.hdmi-cec.control.remoto/resources/"
	
	########################
	#### para raspberry ####
	########################
	#Comprovamos la ruta, y definimos variables con las rutas correctas
	# ruta de keymaps de usuario 
	# ruta de resources del addon
	elif os.path.exists("/storage/.kodi/userdata/keymaps/"):
		#xbmcgui.Dialog().ok("INICIANDO PROGRAMA", "Sistema Operativo detectado:\nAplicando configuracion Raspberry Pi")
		ventanaProgreso(30, "Sistema Operativo Detectado", "Aplicando configuracion Raspberry Pi...")
		rutaKeymaps = os.chdir("/storage/.kodi/userdata/keymaps/")
		rutaResources = os.chdir("/home/c/.kodi/addons/script.hdmi-cec.control.remoto/resources/templates")

	# Mostramos mensaje de error sino coinciden las rutas
	else:
		xbmcgui.Dialog().ok("INICIANDO PROGRAMA", "ERROR - no se ha detectado un sistema operativo compatible")



# Esta funcion sirve para crear la ventana de progreso
# que muestra una animacion con el porcentaje cargado
def ventanaProgreso(tiempo, titulo, texto):
	miVentanaProgreso = xbmcgui.DialogProgress()
	miVentanaProgreso.create(titulo)
	segundos = 0
	porcentage = 0
	incremento = int(100 / tiempo)
	while segundos < tiempo:
		segundos += 1
		porcentage = incremento * segundos
		miVentanaProgreso.update(porcentage, texto)
		xbmc.sleep(100)







#Esta funcion crea la ventana del mando a distancian en la 
# que muestra los botones que son configurables
def ventanaMando1():
	ventanaMando = pyxbmct.AddonDialogWindow("La configuracion de los botones del mando a distancia son:" )
	ventanaMando.setGeometry(800, 600, 3, 3)
	botonCerrar2 = xbmcgui.ControlButton( 575, 650, 150, 50, "    Cerrar")
	ventanaMando.addControl(botonCerrar2)
	ventanaMando.connect(botonCerrar2, ventanaMando.close)
	ventanaMando.setFocus(botonCerrar2)
	imagen3 = xbmcgui.ControlImage(325, 130, 650, 450, rutaResources + "images_remote_controls/botonesMandoSamsung1.jpg")
	imagen3.setVisible(True)
	ventanaMando.addControl(imagen3)
	ventanaMando.doModal()



#definimos una funcion que crea la ventana de la opcion 1 del menu principal
#QUE ES HDMI CEC
#llama a la funcion crearVentana

#definimos la funcion crear ventana, que devuelve la ventana
#para que la pueda utilizar la funcion que la llama
def crearVentana(nombre, titulo):
	nombre = pyxbmct.AddonDialogWindow(titulo)
	nombre.setGeometry(800, 700, 3, 3)
	botonCerrar = xbmcgui.ControlButton( 575, 650, 150, 50, "    Cerrar")
	nombre.addControl(botonCerrar)
	nombre.connect(botonCerrar, nombre.close)
	nombre.setFocus(botonCerrar)
	return nombre
	

#Esta funcion sirve para crear una ventana de texto
#llama a la funcion crearVentana que le retorna la ventana
#Se crea un cuadro de texto en el que se le define el texto
def crearVentanaTexto(nombre, titulo, texto):
	nuevaVentana = crearVentana(nombre, titulo)
	textBox = xbmcgui.ControlTextBox(300, 100, 600, 600, textColor="0xFFFFFFFF")
	textBox.setVisible(True)
	nuevaVentana.addControl(textBox)
	textBox.setText(texto)
	#texto.setText(escribe(30004) + "\n\n" + escribe(30005) + "\n\n" + escribe(30006) + "\n\n" + escribe(30007))
	nuevaVentana.doModal()


#Esta funcion crea la venta con los mandos en funcion de la marca de la television
def crearVentanaMandos(nombre, titulo, numeroMarca):
	nuevaVentana = crearVentana(nombre, titulo)


	imagen1 = xbmcgui.ControlImage(400, 130, 150, 450, rutaResources + "images_remote_controls/mandoLGOK.png")
	imagen1.setVisible(True)
	nuevaVentana.addControl(imagen1)

	imagen2 = xbmcgui.ControlImage(750, 130, 150, 450, rutaResources + "images_remote_controls/samsungOK.jpg")
	#imagen2 = xbmcgui.ControlImage(750, 130, 150, 450, "/home/c/.kodi/addons/script.valido/resources/images_remote_controls/mandoLGOK.png")
	imagen2.setVisible(True)
	nuevaVentana.addControl(imagen2)

	boton1 = xbmcgui.ControlButton(400, 600, 150, 50, "   Modelo 1")
	nuevaVentana.addControl(boton1)
	#llamamos a la funcion ventanaMando1 con el comando lambda
	nuevaVentana.connect(boton1, lambda: ventanaMando1())
			 
	boton2 = xbmcgui.ControlButton(750, 600, 150, 50, "   Modelo 2")
	nuevaVentana.addControl(boton2)
	#llamamos a la funcion ventanaMando2 con el comando lambda
	nuevaVentana.connect(boton2, lambda: ventanaMando1())

	botonCerrar = xbmcgui.ControlButton( 575, 650, 150, 50, "    Cerrar")
	nuevaVentana.addControl(botonCerrar)
	nuevaVentana.connect(botonCerrar, nuevaVentana.close)

	#definimos la navegabilidad entre los botones
	nuevaVentana.setFocus(boton1)
	boton1.controlRight(boton2)
	boton1.controlLeft(boton2)
	boton1.controlUp(botonCerrar)
	boton1.controlDown(botonCerrar)
	boton2.controlLeft(boton1)
	boton2.controlRight(boton1)
	boton2.controlUp(botonCerrar)
	boton2.controlDown(botonCerrar)
	botonCerrar.controlDown(boton1)
	botonCerrar.controlUp(boton1)
	botonCerrar.controlLeft(boton1)
	botonCerrar.controlRight(boton2)


	nuevaVentana.doModal()




### Esta funcion sirve para realizar los backups
#Comprueba que existe el fichero remote.xml, 
# si existe, hace backup y se anhade la fecha
# sino existe, lo crea y hace el backup anhadiendo la fecha
def hacerBackupRemoteXML():
	#Cogemos la fecha y hora, para anhadirselo al archivo de backup
	#Importamos time, para que permita utlizar las librerias
	fechaHoraActual = time.strftime("%y%m%d-%H%M")
	verRutaKeymaps()
	#si existe el fichero de remote.xml hacemos el backup
	if os.path.exists("remote.xml"):
		#ponemos este formato porque kodi utiliza los ficheros .xml
		shutil.copy("remote.xml", "remote.xml_" + fechaHoraActual)
		xbmcgui.Dialog().ok("Realizando Backup del remote.xml activo", "Encontrado el fichero de configuracion remote.xml\nHacemos backup con el nombre de: remote.xml_"+ fechaHoraActual)
	#Si no existe lo creamos y hacemos backup
	else:
		os.mknod("remote.xml")
		shutil.copy("remote.xml", "remote.xml_" + fechaHoraActual)
		xbmcgui.Dialog().ok("Realizando Backup del remote.xml activo", "No existe el fichero de configuracion.\nCreamos un fichero remote.xml por defecto\nHacemos backup con el nombre de: remote.xml_"+ fechaHoraActual)

