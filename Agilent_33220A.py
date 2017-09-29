# -*- coding: utf-8 -*-
"""
Created on 01/07/2013
Versão 3.0
@author: James Citadini
"""
# Importa bibliotecas
import time
import ctypes
import visa
import threading
# *******************************************

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
            self.Acesso = 'SYSTEM:REMOTE'
            self.Liberar = 'SYSTEM:LOCAl'
            self.ConfTipo = 'APPLY:PULSE'
            self.Impedancia = 'OUTPut:LOAD INFinity'
            self.SaidaOff = 'OUTPUT OFF'
            self.SaidaOn = 'OUTPUT ON'
            self.SetPeriodo = 'PULSE:PERIOD '
            self.SetLargura = 'PULSE:WIDTH 1e-6'
            self.SetNivelBaixo = 'VOLTAGE:LOW 0'
            self.SetNivelAlto = 'VOLTAGE:HIGH 5'
            self.SetOffset = 'VOLTAGE:OFFSET 2.5'
            self.SetPulseTransition = 'PULSE:TRANSITION 5e-9'            
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
            tmp = self.inst.read()
            leitura = tmp.split(',')
        except:
            leitura = ''

        return leitura

    def Config(self,PeriodoPulso):
        try:
            # Configuração do voltímetro Agilent 33220A
            self.Enviar('SYSTEM:REMOTE')
            self.Enviar('APPLY:PULSE')
            self.Enviar('OUTPut:LOAD INFinity')
            self.Enviar('OUTPUT OFF')
            self.Enviar('PULSE:PERIOD '+ str(PeriodoPulso))
            self.Enviar('PULSE:WIDTH 1e-6')
            self.Enviar('VOLTAGE:LOW 0')
            self.Enviar('VOLTAGE:HIGH 5')
            self.Enviar('VOLTAGE:OFFSET 2.5')
            self.Enviar('PULSE:TRANSITION 5e-9')
            time.sleep(1)
            return True
        except:
            return False

    
