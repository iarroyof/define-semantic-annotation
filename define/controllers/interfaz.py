# -*- coding: utf-8 -*-
from __future__ import division
#########################################################################
## La función inicio crea la vista inicial crea dos variables en apoyo
## Vista relacionada: interfaz/inicio.html
#########################################################################
"""
Nombre de la función: inicio
Descripción: Crea dos variables, una para mostrar el nombre del usuario y la otra para el email del usuario
Versión: 1.0
Autor: Antonio Nuñez
Retorno: locals() - Las variables locales del programa, se usan en la vista
Vista relacionada: interfaz/inicio.html
"""
@auth.requires_membership('Administrador')
def inicio():
    usuario_nombre = auth.user.first_name
    usuario_mail = auth.user.email
    return locals();

#########################################################################
## La función generaParticular genera el diccionarion que servirá para la
## salida json
#########################################################################
"""
Nombre de la función: generaParticular
Descripción: General el archivo json
Versión: 1.0
Autor: Antonio Nuñez
Retorno: salida - diccionario que se convertira en json
Vista relacionada: interfaz/inicio.html
"""
@auth.requires_membership('Administrador')
def generaParticular():
    salida = dict()
    relaciones = db(db.relacion.modo == "1").select()
    i = 0
    for relacion in relaciones:
        aux = dict()
        definicion_all = db(db.definicion.id == relacion['definicion_id']).select()[0]
        definicion = definicion_all['defi']
        termino_all = db(db.definicion.id == definicion_all['id']).select()[0]['termino_id']
        termino = db(db.termino.id == termino_all).select()[0]['ter']
        gruposPromedio = dict()
        grupos = db(db.relacion.id == relacion['id']).select()
        for grupo in grupos:
            gruposPromedio['grupo'] = db(db.grupo.id == grupo['grupo_id']).select()[0]['grup']
            gruposPromedio['promedio'] = getPromedio(grupo['grupo_id'])
        gruposKey = dict()
        for grupo in grupos:
            gruposKey['grupo'] = db(db.grupo.id == grupo['grupo_id']).select()[0]['grup']
            gruposKey['keywords'] = grupo['keywords']
        aux['id'] = relacion['id']
        aux['termino'] = termino
        aux['definicion'] = definicion
        aux['Grupo-Promedio'] = gruposPromedio
        aux['Grupo-Keywords'] = gruposKey
        salida[i] = aux
        i += 1
    return salida

#########################################################################
## La función getPromedio obtiene el promedio de los grados de certeza usados para
## un grupo
#########################################################################
"""
Nombre de la función: getPromedio
Descripción: Obtiene los promedios
Versión: 1.0
Autor: Antonio Nuñez
Retorno: El promedio
Vista relacionada: interfaz/inicio.html
"""
def getPromedio(idGrupo):
    grupos = db(db.relacion.grupo_id == idGrupo).select()
    suma = 0
    for grupo in grupos:
        suma = int(grupo['grado'])
    return float(suma / len(grupos))

#########################################################################
## La función generaGeneral genera el diccionarion que servirá para la
## salida json
#########################################################################
"""
Nombre de la función: generaGeneral
Descripción: General el archivo json
Versión: 1.0
Autor: Antonio Nuñez
Retorno: salida - diccionario que se convertira en json
Vista relacionada: interfaz/inicio.html
"""
@auth.requires_membership('Administrador')
def generaGeneral():
    salida = dict()
    relaciones = db(db.relacion.modo == "2").select()
    i = 0
    for relacion in relaciones:
        aux = dict()
        definicion_all = db(db.definicion.id == relacion['definicion_id']).select()[0]
        definicion = definicion_all['defi']
        termino_all = db(db.definicion.id == definicion_all['id']).select()[0]['termino_id']
        termino = db(db.termino.id == termino_all).select()[0]['ter']
        gruposPromedio = dict()
        grupos = db(db.relacion.id == relacion['id']).select()
        for grupo in grupos:
            gruposPromedio['grupo'] = db(db.grupo.id == grupo['grupo_id']).select()[0]['grup']
            gruposPromedio['promedio'] = getPromedio(grupo['grupo_id'])
        gruposKey = dict()
        for grupo in grupos:
            gruposKey['grupo'] = db(db.grupo.id == grupo['grupo_id']).select()[0]['grup']
            gruposKey['keywords'] = grupo['keywords']
        aux['id'] = relacion['id']
        aux['termino'] = termino
        aux['definicion'] = definicion
        aux['Grupo-Promedio'] = gruposPromedio
        aux['Grupo-Keywords'] = gruposKey
        salida[i] = aux
        i += 1
    return salida
