from model import *
import os
from bottle import run, template, redirect, static_file, get, post, request, static_file, route

dir = os.path.dirname(os.path.realpath(__file__))+"\\views\\"

#CSS in JS 
@get('/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root=dir)

@get('/<filename:re:.*\.js>')
def js(filename):
    return static_file(filename, root=dir)

###
@get('/')
def osnovna_stran():
    return template('izdelki.html', root=dir)

@get('/register')
def register():
    return template('registracija.html', root=dir)

@post('/register')
def do_register():
    username = request.forms.get('uid')
    password = request.forms.get('pwd')
    pwd_repeat = request.forms.get('pwd-repeat')
    email = request.forms.get('email')
    birthday = request.forms.get('birthday')
    address = request.forms.get('address')

    Uporabnik.registriraj_če_ne_obstaja(username, password, pwd_repeat, email, birthday, address)

    return template('izdelki.html', root=dir)

@get('/login')
def login():
    return template('prijava.html', root=dir) 

@post('/login')
def do_login():
    username = request.forms.get('uid')
    password = request.forms.get('pwd')

    pravilno = Uporabnik.prijavi(username, password)
    if pravilno == True:
        return template('izdelki.html', root=dir)
    else:
        return '<p>Uporabniško ime ali geslo ni pravilno</p>'

@get('/items')
def items():
    return template('izdelki.html', root=dir) 

run(debug=True, reloader=True)
