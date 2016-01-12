# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

from gluon.tools import Mail

#########################################################################
## La función index es la actividad por default que hacen todas las aplicaciones
## Este index no hace nada en la parte lógica, su vista solo son dos enlaces para
## que el usuario seleccione el modo en el que quiere trabajar
#########################################################################
"""
Nombre de la función: index
Descripción: Retorna las variables locales
Versión: 1.0
Autor: Antonio Nuñez
Retorno: locals() - Las variables locales del programa, se usan en la vista
Vista relacionada: default/index.html
"""
def index():
    return locals()

#########################################################################
## La función user se encarga de las operaciones que están relacionadas con:
## Registrarse, entrar al sistema, recuperar contraseñas.
#########################################################################
"""
Nombre de la función: user
Descripción: Crea las diferentes interfaces para la administración de cuentas
Versión: 1.2
Autor: Antonio Nuñez
Retorno: dict(form=auth()) - Un formulario para la que el usuario ponga sus datos de registro/login
Vista relacionada: default/user.html
"""
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    ## configure auth policy
    mail = auth.settings.mailer #Ajustes del mail
    mail.settings.server = 'smtp.gmail.com:587' #Servidor que se usará
    mail.settings.sender = 'define.gil@gmail.com' #Correo desde el cual se enviarán las notificaciones
    mail.settings.login = 'define.gil:defineadmin' #Datos de acceso del correo
    auth.settings.registration_requires_verification = True
    auth.settings.login_after_registration = False
    auth.settings.registration_requires_approval = False
    auth.settings.reset_password_requires_verification = True
    auth.messages.verify_email = 'Click on the link http://' +     request.env.http_host +     URL(r=request,c='default',f='user',args=['verify_email']) +     '/%(key)s to verify your email'
    auth.messages.reset_password = 'Click on the link http://' +     request.env.http_host +     URL(r=request,c='default',f='user',args=['reset_password']) +     '/%(key)s to reset your password'
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
