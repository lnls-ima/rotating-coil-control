# -*- coding: utf-8 -*-
"""
Created on 04/10/2013
Versão 1.0
@author: Ariane Taffarello
"""
# Importa bibliotecas
import time
import visa

# ******************************************
# Comunicacao GPIB
class GPIB(object):
    def __init__(self):
        try:
            self.Comandos()
        except:
            return None

    def Conectar(self,address):
        try:
            aux = 'GPIB::'+str(address)
            self.inst = visa.instrument(aux.encode('utf-8'))
            self.inst.timeout = 1
            return True
        except:
            return False

    def Comandos(self):
        try:
            CR = '\r'
            self.LerVolt = ':READ?'
            self.Reset = '*RST'
            self.Limpar = '*CLS'
            self.ConfiguraVolt = ':CONF:VOLT:DC AUTO'
            return True
        except:
            return False
        
    def Enviar(self,comando):
        try:
            self.inst.write(comando)
            return True
        except:
            return False

    def Ler(self):
        try:
            leitura = self.inst.read()
        except:
            leitura = ''

        return leitura

    def Config(self):
        try:
            self.Enviar(self.Limpar)
            self.Enviar(self.Reset)
            self.Enviar(self.ConfiguraVolt)
            return True
        except:
            return False

    def Coleta(self):
        try:
            self.Enviar(self.LerVolt)
            dado = self.Ler()
            return dado
        except:
            dado = ''
            return dado
        
