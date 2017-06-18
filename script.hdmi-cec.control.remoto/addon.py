import os
import sys
import shutil
import traceback
import xbmc
#import utils
#from xbmcgui import Dialog
import xbmcgui
#from editor import Editor
#la libreria pyxbmct anhade funcionalidades que para la gui y se basa en xbmcgui
import pyxbmct
import time
import xbmcplugin
import misFunciones
from misFunciones import crearVentanaNegra, verRutaResources, verRutaKeymaps, verificarSSOO, crearVentanaMandos, crearVentanaTexto, ventanaMando1, escribe, hacerBackupRemoteXML

# para funciones especiales como el string para traducir
import xbmcaddon



verificarSSOO()




#control, para verificar el correcto funcionamiento de verRutaKeymaps y verRutaResources
#xbmcgui.Dialog().ok("mostrar funcion return keymapsdesde addons", verRutaKeymaps())
#xbmcgui.Dialog().ok("mostrar funcion return resources desde addon ", verRutaResources() )

#Declaramos listados de marcas y tipos de HDMI-CEC y de modelos de television
listadoMarcas = ["Samsung", "LG", "Hitachi", "Panasonic", "Philips", "Pioneer", "Sony", "Toshiba"]
listadoMarcasHDMICEC = ["Samsung - Anynet +" , "LG - SimpLink", "Hitachi - HDMI-CEC", "Panasonic - HDAVI / EZ-Sync / Viera Link", "Philips - EasyLink", "Pioneer - Kuro Enlace", "Sony - Bravia Sync", "Toshiba - CE-Link / Enlace Regza"]
listadoModelosSamsung = ["Serie KS9800 - Compatible", "Serie KS9500 - Compatible", "Serie KS9000 - Compatible", "Serie KS8000 - Compatible", "Serie KS7500 - Compatible",  "Serie KS7000 - Compatible", "Serie KU6640 - Compatible" , "Serie KU6510 - Compatible", "Serie KU6450 - Compatible", "Serie KU6400 - Compatible" , "Serie KU6000 - Compatible", "Serie KU6300 - Compatible", "Serie K6300 - Compatible", "Serie K5500 - Compatible"]
listadoModelosLG = ["Serie UH950V - Compatible", "Serie UH850V - Compatible", "Serie UH770V - Compatible", "Serie UH750V - Compatible", "Serie UH668V - Compatible", "Serie UH661V - Compatible", "Serie UH650V - Compatible" ]




##########################################################
################# MENU PRINCIPAL #########################
##########################################################

## Creamos el menu principal sobre un While ##
while True:
	#Creamos menu, con todas las opciones, sobre una ventana de dialogo de seleccionar
	opcionMenuPrincipal = xbmcgui.Dialog().select(escribe(30003), ["0.-Acerca de este add-on", "1.-Que es HDMI-CEC", "2.-Comprueba si tu TV es compatible", "3.-Como configurar tu TV", "4.-Que son los KeyMaps", "5.-Administrar Backup remote.xml", "6.-Cargar Plantilla Preconfigurada", "7.-Botones configurables de tu mando a distancia", "8.-Comprueba tu mando a distancia", "9.-Configura los botones de tu mando a distancia"])    
	
	##########################################
	#### opcion 0.- acerca de este add-on ####
	##########################################
	if opcionMenuPrincipal == 0:
		xbmcgui.Dialog().ok(escribe(30001)	, escribe(30002))
    
	####################################
	#### opcion 1.- Que es HDMI-CEC ####
	####################################
	elif opcionMenuPrincipal == 1:
		crearVentanaTexto("ventanaOMP1", "1.- Que es HDMI-CEC",escribe(30004) + "\n\n" + escribe(30005) + "\n\n" + escribe(30006) + "\n\n" + escribe(30007))
    
	#####################################################
	#### opcion 2.- Comprueba si tu tv es compatible ####
	#####################################################
	elif opcionMenuPrincipal == 2:
		eligeMarca = xbmcgui.Dialog().select("2.-Comprueba si tu TV es compatible ", listadoMarcas)		
		if eligeMarca == 0:
			xbmcgui.Dialog().select("2.-Comprueba si tu TV Samsung es compatible", listadoModelosSamsung)
		elif eligeMarca == 1: 
			xbmcgui.Dialog().select("2.-Comprueba si tu TV LG es compatible", listadoModelosLG)
		else:
			xbmcgui.Dialog().ok("Informacion no disponible", "Informacion no disponible")

	
	##########################################		
	#### opcion 3.- Como configurar tu TV ####
	##########################################
	elif opcionMenuPrincipal == 3:
		eligeMarca = xbmcgui.Dialog().select("3.-Como configurar tu TV", listadoMarcasHDMICEC)
		if eligeMarca == 0:
			crearVentanaTexto("ventanaOMP3_0", "3.- Como configurar tu TV Samsung - Anynet +", "Para realizar la configuracion, sigue los siguientes pasos:\n\n1.- Acceder al menu Config\n2.- Seleccionar HDMI\n3.-Seleccionar Anynet+ (HDMI-CEC)\n4.- Marcar Si")
		elif eligeMarca == 1: 
			crearVentanaTexto("ventanaOMP3_1" ,"3.- Como configurar tu TV LG - SimpLink", "Para realizar la configuracion, sigue los siguientes pasos:\n\n1.- Pulsar el boton de Q.Menu\n2.- Seleccionar Advanced\n3.- Seleccionar General\n4.- Seleccionar SimpLink\n5.- Seleccionar On")		
		else:
			xbmcgui.Dialog().ok("Informacion no disponible", "Informacion no disponible")


	########################################
	#### opcion 4.- Que son los KeyMaps ####
	########################################
	elif opcionMenuPrincipal == 4:
		crearVentanaTexto("ventanaOMP4","4.-Que son los KeyMaps", "Los KeyMaps son unos ficheros de configuracion, para determinar la configuracion de las teclas.\n\nVamos a configurar el fichero remote.xml para poder modificar la configuracion de los botones del mando a distancia.\n\nDependiendo del modelo de TV se necesita una configuracion determinada para que funcionen todos los botones del mando a distancia")
		#xbmcgui.Dialog().ok("4.-Que son los KeyMaps", "Los KeyMaps son unos ficheros de configuracion, para determinar la configuracion de las teclas.\nVamos a configurar el fichero remote.xml para poder modificar la configuracion de los botones del mando a distancia.\nDependiendo del modelo de TV se necesita una configuracion determinada para que funcionen todos los botones de mando a distancia")

	###################################################
	#### opcion 5.- Administrar Backups remote.xml ####
	###################################################
	elif opcionMenuPrincipal == 5:
		opcionSubmenuBackup = xbmcgui.Dialog().select("5.-Administrar Backups fichero remote.xml", ["5.0.- Realizar Backup", "5.1.-Restaurar Backup", "5.2.-Borrar Backup" ] )
		
		###############################
		## 5.0.- submenu HacerBackup ##
		###############################
		if opcionSubmenuBackup == 0:
			verRutaKeymaps()
			#Devuelve la ruta donde estamos
			#ruta = os.getcwd()
			#La siguiente linea es de control, para ver la ruta
			#xbmcgui.Dialog().ok("", ruta)
			#llamamos a la funcion que gestiona los backups
			hacerBackupRemoteXML()

		##################################
		## 5.1 submenu Restaurar Backup	##
		##################################
		if opcionSubmenuBackup == 1:
			#Vamos a listar los ficheros para seleccionar el backup
			#vamos a la ruta donde estan los keymaps
			verRutaKeymaps()
			listadoFicheros = os.listdir(".")
			#eliminamos de la lista el fichero remote.xml, pues de este no queremos restaurar el backup
			listadoFicheros.remove("remote.xml")
			eligeBackup = xbmcgui.Dialog().select("6.-Restaurar Backup remote.xml - Elegir fichero", listadoFicheros)
			#Verificamos por si el usuario quiere hacer un backup de respaldo de la configuracion actual
			if xbmcgui.Dialog().yesno("6.-Hacer Backup del remote.xml", "Desea realizar Backup de remote.xml antes de continuar?."):
				hacerBackupRemoteXML()
			#linea de control para ver el elemento de la lista que seleccionamos
			#xbmcgui.Dialog().ok("Backup seleccionado", "Backup a restaurar seleccioando: " + str(eligeBackup)+ " " + listadoFicheros[eligeBackup])
			#Vamos a restaurar el fichero seleccionado
			shutil.copy( listadoFicheros[eligeBackup], "remote.xml")
			xbmcgui.Dialog().ok("Backup Restaurado", "Restaurado el Backup de " + listadoFicheros[eligeBackup] + " correctamente\nCopiada configuracion al fichero remote.xml")

		###############################
		## 5.2 submenu Borrar Backup ##
		###############################
		if opcionSubmenuBackup == 2:
			verRutaKeymaps()
			listadoFicheros = os.listdir(".")
			#eliminamos de la lista el fichero remote.xml, pues de este no queremos restaurar el backup
			listadoFicheros.remove("remote.xml")
			eligeBackupParaBorrar = xbmcgui.Dialog().select("5.2.-Borrar Backup - Elegir fichero", listadoFicheros)
			#Verificamos por si el usuario quiere hacer un backup de respaldo de la configuracion actual
			if xbmcgui.Dialog().yesno("5.2.-Borrar Backup", "Confirme si desea borrar el fichero " + listadoFicheros[eligeBackupParaBorrar]):
				os.remove(listadoFicheros[eligeBackupParaBorrar])
				xbmcgui.Dialog().ok("5.2.-Borrar Backup", "Ha borrado con exito el archivo: " + listadoFicheros[eligeBackupParaBorrar] )
		else:
			continue	

	####################################################
	#### opcion 6.- Cargar Plantilla Preconfigurada ####
	####################################################

	elif opcionMenuPrincipal == 6:
		#eligeMarca = xbmcgui.Dialog().select("6.-Cargar Plantilla Preconfigurada", listadoMarcasHDMICEC)
		os.chdir(verRutaResources() + "templates/")
		listadoFicheros = os.listdir(".")
		eligePlantilla = xbmcgui.Dialog().select("6.-Elegir Plantilla remote.xml - Elegir fichero", listadoFicheros)
		xbmcgui.Dialog().ok("6.- Cargar Plantilla", "Va a cargar la plantilla: " + listadoFicheros[eligePlantilla])
		if xbmcgui.Dialog().yesno("6.- Cargar Plantilla", "Desea realizar Backup de remote.xml antes de continuar?"):
			hacerBackupRemoteXML()
		shutil.copy(verRutaResources() + "templates/" + listadoFicheros[eligePlantilla], verRutaKeymaps() + "remote.xml")
		xbmcgui.Dialog().ok("Plantilla cargada", "La plantilla: " + listadoFicheros[eligePlantilla] + " \nha sido cargada correctamente como el remote.xml activo")

		



	#######################################################################
	#### opcion 7.- Ver el mapa de los botones de tu mando a distancia ####
	#######################################################################
	elif opcionMenuPrincipal == 7:
		eligeMarca = xbmcgui.Dialog().select("7.-Botones configurables de tu manndo a distancia", listadoMarcasHDMICEC)
		if eligeMarca == 0:
			crearVentanaMandos("ventanaOMP7", listadoMarcasHDMICEC[eligeMarca], eligeMarca)

		elif eligeMarca == 1: 
			crearVentanaMandos("ventanaOMP7", listadoMarcasHDMICEC[eligeMarca], eligeMarca)

#			xbmcgui.Dialog().ok("7.-Ver mapa de los botones de tu mando a distancia LG", "Selecciona tu modelo de mando:\nmodelo 1 \nmodelo 2\n moedelo 3")
		else:
			continue




	###################################################		
	#### opcion 8.- Comprueba tu mando a distancia ####
	###################################################
	elif opcionMenuPrincipal == 8:
		crearVentanaNegra()

	##################################################################
	#### opcion 9.- Configura los botones de tu mando a distancia ####
	##################################################################
	elif opcionMenuPrincipal == 9:
		xbmcgui.Dialog().yesno("9.-Configura los botones de tu mando a distancia", "Desea configurar los botones de tu mando a distancia")
	else:
		#hay que poner break para asegurar que sale de la funcion
		break
