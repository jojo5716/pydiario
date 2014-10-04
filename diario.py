# -*- coding: utf-8 -*-
from datetime import datetime
import os

class Diario():
    def __init__(self, texto, redmine):
        self.hoy = datetime.today()
        self.texto = texto
        self.ruta = '/Users/jonathanrodriguez/'

        if not redmine:
            redmine = 'No tiene tarea asignada.'

        self.redmine = redmine

    def existe_dia(self, nombre):
        libreta = fichero = open('%s%s'%(self.ruta, nombre), "r")
        for linea in libreta.readlines():
            if linea.startswith('@'):
                fecha = linea.split('@')[1]
                fecha =  fecha.replace('_','')
                fecha = fecha.split('-')
                mes = fecha[1]
                dia = fecha[2]
                if (self.hoy.month == int(mes) and
                    self.hoy.day == int(dia)):
                    return True
        return False


    def guardar_diario(self):
        nombre = "diario-%s.txt"%self.hoy.month

        libreta = fichero = open('%s%s'%(self.ruta, nombre), "a")
        existe = self.existe_dia(nombre)
        if self.texto or self.redmine:
            if not existe:
                libreta.write('@ ____________________________ %s \n\n'%self.hoy.strftime('%Y-%m-%d'))

            libreta.write('#### \n')
            libreta.write('# \n')
            libreta.write('# \t \t Titulo: %s \n'%self.texto)
            libreta.write('# \t \t Redmine: %s \n'%self.redmine)
            libreta.write('# \t \t Hora: %s\n'%self.hoy.strftime('%H:%M:%S'))
            libreta.write('# \n')
            libreta.write('#### \n \n \n')
            libreta.close()
            print 'Diario actualizado.'
        else:
            print 'Sin guardar.'



texto = raw_input(u'Que anecdota ha pasado? ')
redmine = raw_input(u'Localizador redmine: ')
d = Diario(texto, redmine)
d.guardar_diario()
