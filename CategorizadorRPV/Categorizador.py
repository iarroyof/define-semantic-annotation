# coding=utf-8
import csv, re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity

"""
    Titulo: Clasificador de definiciones.
    Autor: Ramon Pantoja Velasco.
    Descripcion: Por medio de un ,csv de definiciones, un .csv de Acepciones de wikipedia y un .csv con las definiciones de las acpeciones de      wikipedia el programa asignara un grupo a esas definiciones por medio de la comparacion con las acepciones antes mencionadas y dara como resultados la relacion en un diccionario guardado en un .txt
	Versión: 1.6
    
"""
"""
	El main debe ser modificado en los parametros que recibe para mandar algunas opciones al invocar este programa desde otro, los cuales son:
	dirección de los archivos .csv , porcentaje minimo de relacion expresado en decimales ente 0 y 1, el número de opcion de las 6 disponibles, la minima
	 similitud para la relación y la dirección completa donde se guardará el archivo final.
	
"""
def main():
    """
	Aquí se definen las listas que serán las principales en el programa.
	listaefiniciones almacena las definiciones que se obtienen de Describe.
	listaWiki almacena las definiciones que provee wikipedia
	listaAcepciones almacena las ascepciones de wikipedia
	listaSimilitud almacena el porcentaje de relacion que se establece entre los vectores de wikipedia y de definiciones de Describe
	listaWiki2 almacena el id que asocia la definicion de wikipedia con la ascepcion
	listaAcepciones2 almacena el id de cada ascepcion
	
    """
    listaDefiniciones = []
    listaWiki = []
    listaAcepciones = []
    listaSimilitud = []
    listaWiki2 = []
    listaAcepciones2 = []
    """
	Se definen las variables para manejar la direccion de los archivos, serán sustituidos por los parametros que se manden en el main
	cuando el programa esté trabajando junto al sistema para el que fue creado.
    """
    archivoDefiniciones = 'Boundary.csv'
    archivoWiki = 'wikiBoundary.csv'
    archivoAcepciones = 'Acepciones.csv'
    opc = 7
    minimaSimilitud = 0.1
    """
	Se asignan los valores a las listas por medio de funciones que leen el archivo .csv que reciben de parametro.
	
    """
    listaDefiniciones = crearListaDefiniciones(archivoDefiniciones)
    listaWiki = crearListaDefiniciones(archivoWiki)
    listaWiki2 = crearListaWiki2(archivoWiki)
    listaAcepciones = crearListaAcepciones(archivoAcepciones)
    listaAcepciones2 = crearListaAcepciones2(archivoAcepciones)
    """
	El siguiente while junto con los print y las opciones solamente son para probar el funcionamiento del programa, deberan de eliminarse o deshabilitarse
	al momento de unirlo con el sistema para el que fue creado.
    """
    while(opc != 0):
        print "Elija la forma en la que quiere el resultado"
        print "1.TFIDF unigrama"
        print "2.TFIDF bigrama"
        print "3.TFIDF trigrama"
        print "4.Sin TFIDF unigrama"
        print "5.Sin TFIDF bigrama"
        print "6.Sin TFIDF trigrama"
        print "0.Salir"
        opc = int(input("Digite:"))
        """
			Los siguientes if anidados son para seleccionar las direfentes acciones:
			opc = 1.- Realiza la clasificación con TFIDF para unigramas.
			opc = 2.- Realiza la clasificación con TFIDF para bigramas.
			opc = 3.- Realiza la clasificación con TFIDF para trigramas.
			opc = 4.- Realiza la clasificación sin TFIDF para unigramas.
			opc = 5.- Realiza la clasificación sin TFIDF para bigramas.
			opc = 6.- Realiza la clasificacion sin TFIDF para trigramas.
			opc = 0.- Es sólo en casi de usarse de manera manual, sirve para terminar el programa.
			else.- En caso de ser de forma manual para asegurarnos de que el usuario introduzca una opción valida.
		"""
		#Las siguientes opciones son muy similares y solo cambia considerando lo que mencioné arriba, así que solo comentaré la primera.
        if(opc == 1):
			#Se crea un objeto de la clase TfidfVectorizer con los parametros importantes de analyzer en palabras e idioma inglés.
            vectorizador = TfidfVectorizer(sublinear_tf=True,max_df=0.5,analyzer='word',stop_words='english')
			#Se crea una matriz con los vectores al transformar la listaDefiniciones con TFIDF y se asigna a vectorDefiniciones, así mismo se crea un vocabulario que se guarda en el objeto vectorizador.
            vectorDefiniciones = vectorizador.fit_transform(listaDefiniciones).toarray()
			#Se crea un objeto de la clase TfidfVectorizer con los parametros importantes de analyzer en palabras e idioma inglés, y como vocabulario el que se creó para vectorizador.
            vectorizadorWiki = TfidfVectorizer(sublinear_tf=True,max_df=0.5,analyzer='word',stop_words='english' ,vocabulary=vectorizador.vocabulary_)
			#Se crea una matriz con los vectores al transformar la listaWiki con TFIDF y se asigna a vectorWiki.
            vectorWiki = vectorizadorWiki.fit_transform(listaWiki).toarray()
			#Se crea la lista con la relación entre las definiciones y acepciones.
            listaRelacion = generarRelacion(vectorDefiniciones, vectorWiki, minimaSimilitud)
			#Se crea una lista con el porcentaje de similitud de los vectores.
            listaSimilitud = generarSimilitud(vectorDefiniciones, vectorWiki)
			#Genera el reporte final de relacion de acpeciones y definiciones.
            generarDic(listaRelacion, listaSimilitud, listaAcepciones, listaAcepciones2, listaWiki, listaWiki2, listaDefiniciones, "ResultadoTFIDFUnigrama.txt")
        elif(opc == 2):
			# Lo mismo que en el caso anterior pero con el nuevo parametro ngram_range = (2,2) para hacer el analisis con bigramas
            vectorizador = TfidfVectorizer(sublinear_tf=True,max_df=0.5,analyzer='word',stop_words='english',ngram_range = (2,2))
            vectorDefiniciones = vectorizador.fit_transform(listaDefiniciones).toarray()
			# Lo mismo que en el caso anterior pero con el nuevo parametro ngram_range = (2,2) para hacer el analisis con bigramas
            vectorizadorWiki = TfidfVectorizer(sublinear_tf=True,max_df=0.5,analyzer='word',stop_words='english', vocabulary=vectorizador.vocabulary_,ngram_range = (2,2))
            vectorWiki = vectorizadorWiki.fit_transform(listaWiki).toarray()
            listaRelacion = generarRelacion(vectorDefiniciones, vectorWiki, minimaSimilitud)
            listaSimilitud = generarSimilitud(vectorDefiniciones, vectorWiki)
            generarDic(listaRelacion, listaSimilitud, listaAcepciones, listaAcepciones2, listaWiki, listaWiki2, listaDefiniciones,  "ResultadoTFIDFBigrama.txt")
        elif(opc == 3):
			# Lo mismo que en el caso 1 pero con el nuevo parametro ngram_range = (3,3) para hacer el analisis con trigramas
            vectorizador = TfidfVectorizer(sublinear_tf=True,max_df=0.5,analyzer='word',stop_words='english', ngram_range = (3,3))
            vectorDefiniciones = vectorizador.fit_transform(listaDefiniciones).toarray()
			# Lo mismo que en el caso 1 pero con el nuevo parametro ngram_range = (3,3) para hacer el analisis con trigramas
            vectorizadorWiki = TfidfVectorizer(sublinear_tf=True,max_df=0.5,analyzer='word',stop_words='english' ,vocabulary=vectorizador.vocabulary_, ngram_range = (3,3))
            vectorWiki = vectorizadorWiki.fit_transform(listaWiki).toarray()
            listaRelacion = generarRelacion(vectorDefiniciones, vectorWiki, minimaSimilitud)
            listaSimilitud = generarSimilitud(vectorDefiniciones, vectorWiki)
            generarDic(listaRelacion, listaSimilitud, listaAcepciones, listaAcepciones2, listaWiki, listaWiki2, listaDefiniciones,  "ResultadoTFIDFTrigrama.txt")
        elif(opc == 4):
			#Lo mismo que la opcion 1 pero ahora se usa CountVectorizer sustituyendo a TfidfVectorizer, se hará el analisis sin TFIDF
            vectorizador = CountVectorizer(max_df=0.5,analyzer='word',stop_words='english')
            vectorDefiniciones = vectorizador.fit_transform(listaDefiniciones).toarray()
            vectorizadorWiki = CountVectorizer(max_df=0.5,analyzer='word',stop_words='english',vocabulary=vectorizador.vocabulary_)
            vectorWiki = vectorizadorWiki.fit_transform(listaWiki).toarray()
            listaRelacion = generarRelacion(vectorDefiniciones, vectorWiki, minimaSimilitud)
            listaSimilitud = generarSimilitud(vectorDefiniciones, vectorWiki)
            generarDic(listaRelacion, listaSimilitud, listaAcepciones, listaAcepciones2, listaWiki, listaWiki2, listaDefiniciones,  "ResultadoUnigrama.txt")
        elif(opc == 5):
			#Lo mismo que en la opcion 4 pero con el parametro ngram_range = (2,2) para hacer el analisis sin TFIDF y para bigramas
            vectorizador = CountVectorizer(max_df=0.5,analyzer='word',stop_words='english',ngram_range=(2,2))
            vectorDefiniciones = vectorizador.fit_transform(listaDefiniciones).toarray()
            #Lo mismo que en la opcion 4 pero con el parametro ngram_range = (2,2) para hacer el analisis sin TFIDF y para bigramas
            vectorizadorWiki = CountVectorizer(max_df=0.5,analyzer='word',stop_words='english',vocabulary=vectorizador.vocabulary_,ngram_range=(2,2))
            vectorWiki = vectorizadorWiki.fit_transform(listaWiki).toarray()
            listaRelacion = generarRelacion(vectorDefiniciones, vectorWiki, minimaSimilitud)
            listaSimilitud = generarSimilitud(vectorDefiniciones, vectorWiki)
            generarDic(listaRelacion, listaSimilitud, listaAcepciones, listaAcepciones2, listaWiki, listaWiki2, listaDefiniciones,  "ResultadoBigrama.txt")
        elif(opc == 6):
			#Lo mismo que en la opcion 4 pero con el parametro ngram_range = (3,3s) para hacer el analisis sin TFIDF y para trigramas
            vectorizador = CountVectorizer(max_df=0.5,analyzer='word',stop_words='english',ngram_range=(3,3))
            vectorDefiniciones = vectorizador.fit_transform(listaDefiniciones).toarray()
			#Lo mismo que en la opcion 4 pero con el parametro ngram_range = (3,3) para hacer el analisis sin TFIDF y para trigramas
            vectorizadorWiki = CountVectorizer(max_df=0.5,analyzer='word',stop_words='english',vocabulary=vectorizador.vocabulary_,ngram_range=(3,3))
            vectorWiki = vectorizadorWiki.fit_transform(listaWiki).toarray()
            listaRelacion = generarRelacion(vectorDefiniciones, vectorWiki,minimaSimilitud)
            listaSimilitud = generarSimilitud(vectorDefiniciones, vectorWiki)
            generarDic(listaRelacion, listaSimilitud, listaAcepciones, listaAcepciones2, listaWiki, listaWiki2, listaDefiniciones,  "ResultadoTrigrama.txt")
        elif(opc == 0):
            print "Termina el programa"
        else:
            print "Error, elija una opcion valida"

    """Nombre de la función: crearListaDefiniciones
	Descripción:Recibe la ruta del archivo de Definiciones en .csv y genera la lista que se utilizará de definiciones
	Versión:1.0
	Autor:Ramón Pantoja Velasco
	Parámetros:archivoCsv.- Direccion del archivo de definiciones
	Retorno:listaDefiniciones.- Lista que guarda las definiciones obtenidas del archivo .csv
	
    """
def crearListaDefiniciones(archivoCsv):
    listaDefiniciones = []
    #Se abre el archivo para lectura.
    with open(archivoCsv, 'rb') as csvfile:
        #Se crea un objeto para leer el archivo.
        lecturaDefiniciones = csv.DictReader(csvfile)
        #Se recorre cada linea del archivo para obtener la información.
        for row in lecturaDefiniciones:
            #Se guarda la información en la lista.
            listaDefiniciones.append(row['definicion'].lower())
	return listaDefiniciones
    """Nombre de la función: generarRelacion
	Descripción: Realiza la comparacion de los vectores de definiciones y acepciones de wikipedia con la funcion cosine_similarity, se obtiene la lista de la
				relacion
	Versión:1.0
	Autor:Ramón Pantoja Velasco
	Parámetros: vectorDefiniciones.- Vector obtenido de la listaDefiniciones al transformarla ya sea con o sin TFIDF, vectorWiki.- Vector obtenido de la lista
				de acepciones de wikipedia debes ser obtenida de la misma forma que listaDefiniciones, minimaSimilitud.- Valor entre 0 y 1 que define la
				minima similitud para la relacion definicion->acepcion de Wikipedia.
	Retorno:listaRelacion.- Lista con la relacion de definicion->acepcion
	
    """
def generarRelacion(vectorDefiniciones, vectorWiki, minimaSimilitud):
    listaRelacion = []
    i = 0
    #Se recorre el vector de definiciones.
    for valor in vectorDefiniciones:
        listaRelacion.append(0)
        j = 0
        valorMasAlto = 0
        #Se recorre el vector de Wikipedia.
        for valorWiki in vectorWiki:
            #Se calcula la distancia coseno para cada vector de wikipedia con los vectores de definiciones.
            result = cosine_similarity(valor, valorWiki)
            #Mantiene el resultado mayor guardado en la lista.
            if(result > valorMasAlto):
                #Asigna el ID de la definicion de wikipedia con que se relaciona la definicion, es + 1 porque empiezan en 1 los ID.
                listaRelacion[i] = j + 1
                valorMasAlto = result
            j = j + 1
        #En caso de ser menor a minimaSimilitud la similitud se asigna a no informativo.
        if(valorMasAlto < minimaSimilitud):
            listaRelacion[i] = 0
        i = i + 1
    return listaRelacion
    """Nombre de la función: generarSimilitud
	Descripción:Realiza la obtencion de el porcentaje de similitud de los vectores de definiciones y acepciones de wikipedia con la funcion
				cosine_similarity, se obtiene la lista de la similitud
	Versión:1.0
	Autor:Ramón Pantoja Velasco
	Parámetros: vectorDefiniciones.- Vector obtenido de la listaDefiniciones al transformarla ya sea con o sin TFIDF, vectorWiki.- Vector obtenido de la lista
				de acepciones de wikipedia debes ser obtenida de la misma forma que listaDefiniciones
	Retorno:listaSimilitud.- lista de procentaje de similitud coseno
	
    """    
def generarSimilitud(vectorDefiniciones, vectorWiki):
    listaSimilitud = []
    i = 0
    #Recorre todos los valores en vectorDefiniciones.
    for valor in vectorDefiniciones:
        j = 0
        valorMasAlto = 0
        result = 0
        #Recorre todos los valores en vectorWiki.
        for valorWiki in vectorWiki:
            #Calcula la distancia coseno y almacena el resultado en result
            result = cosine_similarity(valor, valorWiki)
            #Guarda el valor más alto
            if(result > valorMasAlto):
                valorMasAlto = result
            j = j + 1
        #Guarda el valor en la lista.
        listaSimilitud.append(valorMasAlto)
    return listaSimilitud
    """Nombre de la función: crearListaAcepciones
	Descripción:Recibe la ruta del archivo de Acepciones en .csv y genera la lista que se utilizará de Acepciones, guardando unicamente el nombre de
				la acepción
	Versión:1.0
	Autor:Ramón Pantoja Velasco
	Parámetros:archivoCsv.- Direccion del archivo de acepciones
	Retorno:listaAcepciones.- Lista que guarda el nombre de las acepciones obtenidas del archivo .csv
	
    """
def crearListaAcepciones(archivoCsv):
    listaAcepciones = []
    with open(archivoCsv, 'rb') as csvfile:
        lectura = csv.DictReader(csvfile)
        for row in lectura:
            listaAcepciones.append(row["acepcion"])
	return listaAcepciones
    """Nombre de la función: crearListaAcepciones2
	Descripción:Recibe la ruta del archivo de Acepciones en .csv y genera la lista que se utilizará de Acepciones, guardando unicamente el id de
				la acepción
	Versión:1.0
	Autor:Ramón Pantoja Velasco
	Parámetros:archivoCsv.- Direccion del archivo de acepciones
	Retorno:listaAcepciones.- Lista que guarda el id de las acepciones obtenidas del archivo .csv
	
    """	
def crearListaAcepciones2(archivoCsv):
    listaAcepciones = []
    cont = 0
    with open(archivoCsv, 'rb') as csvfile:
        lectura = csv.DictReader(csvfile)
        for row in lectura:
            listaAcepciones.append(int(row["id"]))
	return listaAcepciones
    """Nombre de la función: crearListaWiki2
	Descripción:Recibe la ruta del archivo de Acepciones de Wikipedia en .csv y genera la lista que se utilizará de Wikipedia, guardando unicamente el id de
				la relacion de acepcion con definicion de wikipedia.
	Versión:1.0
	Autor:Ramón Pantoja Velasco
	Parámetros:archivoCsv.- Direccion del archivo de acepciones de Wikipedia
	Retorno:listaAcepciones.- Lista que guarda el id de las definiciones que relaciona con acepciones de wikipedia obtenidas del archivo .csv
	
    """
def crearListaWiki2(archivoCsv):
    listaWiki2 = []
    with open(archivoCsv, 'rb') as csvfile:
        lectura = csv.DictReader(csvfile)
        lista = []
        for row in lectura:
            listaWiki2.append(int(row["acepcion"]))
	return listaWiki2
    """Nombre de la función: generarDic
	Descripción:Recibe la lista de relacion, lista de similitud, lista de acepciones, lista de acepciones2, lista de wikipedia, lista de wikipedia2
				lista de definiciones y el nombre del archivo donde se guradará la salida.
	Versión:2.0

	Autor:Ramón Pantoja Velasco
	Parámetros: listaRelacion.- lista de la relación entre vectores de definiciones y de acepciones de wikipedia, listaSimilitud.- lista de la similitud entre
				los vectores de definiciones y de acepciones de wikipedia, listaAcepciones.- lista de nombre de cada acepcion, listaAcepciones2.- lista del id
				de cada acepcion, listaWiki.- lista de definiciones de wikipedia, listaWiki2.- lista de id que asocia las definiciones de wikipedia con las
				acepciones de wikipedia, listaDefiniciones.- lista de definiciones, nombreArchivo.- direccion y nombre del archivo donde se guardará la salida.
	
    """
def generarDic(listaRelacion, listaSimilitud, listaAcepciones, listaAcepciones2,listaWiki, listaWiki2, listaDefiniciones, nombreArchivo):
    #Se crea el objeto que permite la escritura del archivo.
    c = open(nombreArchivo, "wb")
    cont = 1
    dicc = {}
    diccionario = "{\'acepciones\':{"
    #Se recorre la lista de acepciones con los ID como base para acomodar por acepción.
    for acepcion in listaAcepciones2:
        contWiki = 0
        contArt = 1
        diccionario = diccionario + "\'" + listaAcepciones[cont - 1] + "\':{"     
        #se recorre la lista de id asociados de definiciones Wikipedia con las acepciones correspondientes.
        contAcepcionesWiki = 1
        for valor in listaWiki2:

            #Si los valores son iguales se procede a agregar una línea más al diccionario con la acepción y la definición
            if(acepcion == valor):
                diccionario = diccionario + "\'art" + str(contAcepcionesWiki) + "\':\"" + listaWiki[contWiki] + "\"," + "defs"  + ":{"
                contAcepcionesWiki = contAcepcionesWiki + 1
                cont2 = 0
                #Se crea una matriz para poder organizar por ranking de mayor a menor.
                matriz = []
                #Se recorre los elementos en la listaRelacion.
                for relacion in listaRelacion:

                    #Si el elemento en relacion es igual al contador significa que son la misma definicion por lo que se agrega a la lista.
                    if(relacion == cont):
                        
                        lista = []
                        #Se agrega el valor de similitud.
                        lista.append(float(listaSimilitud[cont2]))
                        #Se agrega la definición.
                        lista.append(listaDefiniciones[cont2])
                        #Se agrega a la matriz
                        matriz.append(lista)
                    cont2 = cont2 + 1
                #Se ordena la matriz por renglon para que sea organizada de mayor a menor.
                matriz.sort(reverse = True)
                contComas = True
                #Se agrega el contenido obtenido de la matriz al string
                contDefs = 1
                for lista in matriz:
                    if(contComas):
                        diccionario = diccionario + "\'Def_" + str(contDefs) + "\':(\"" + str(lista[0]) + "\",\"" + lista[1] + "\")"
                        contComas = False
                    else:
                        diccionario = diccionario + ",\'Def_" + str(contDefs) +"\':(\"" + str(lista[0]) + "\",\"" + lista[1] + "\")"
                    contDefs = contDefs + 1
                diccionario = diccionario + ","
                diccionario = diccionario + "}"
        diccionario = diccionario + "}"
        cont = cont + 1
    contNoInf = 0
    noInf = "}},\'noInformativo\':["
    boolComas = True
    #Se recorren todas las definiciones.
    for definicion in listaDefiniciones:
        #Si la definicion pertenece al grupo 0 de no informativo se guarda en el archivo como no informativo.
        if(listaRelacion[contNoInf] == 0):
            if(boolComas):
                noInf = noInf + definicion
                boolComas = False
            else:
                noInf = noInf + "," + definicion 
                contNoInf = contNoInf + 1
    diccionario = diccionario + noInf + "]}"
    c.write(diccionario)
if __name__ == '__main__':
    main()
