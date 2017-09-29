# -*- coding: utf-8 -*-
# Importa bibliotecas
import serial
import time
import threading
# ******************************************

class SerialCom(threading.Thread):
    def __init__(self,porta):
        threading.Thread.__init__(self)
        self.porta = porta
        self.ser = serial.Serial(self.porta-1)
        self.start()

    def callback(self):
        self._stop()

    def run(self):
        self.Comandos()

    def Comandos(self):
        CR = '\r'

        self.LerVolt =              ':READ?'
        self.Acesso =               ':SYST:REM'
        self.Liberar =              ':SYST:LOC'
        self.Reset =                '*RST'
        self.Limpar =               '*CLS'
        self.SCAN =                 ':ROUT:SCAN '        # acrescentar no final o canal que deseja scanear, exemplo: 'ROUT:SCAN (@101)'
        self.MON =                  ':ROUT:MON:CHAN '    # acrescentar no final o canal que deseja APENAS monitorar no display, exemplo: 'ROUT:MON:CHAN (@102)'
        self.MON_STATE =            ':ROUT:MON:STATE ON'
        self.ConfgVolt =            ':CONF:VOLT:DC'
        self.CON =                  ':CONF'
        self.Volt =                 ':VOLT'
        self.DC =                   ':DC'

##        self.ConfiguraVolt = [':ROUT:SCAN (@101)',\
##                              ':CONF:TEMP TC,K,(@101)',\
##                              'ROUT:MON:STATE ON']
    def Conectar(self):
        self.ser.baudrate = 115200
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.parity = serial.PARITY_NONE
        self.ser.timeout = 0.01
        if not self.ser.isOpen():
            self.ser.open()
        try:
            self.Enviar(self.Acesso)
            return True
        except:
            return False

    def Desconectar(self):
        self.ser.close()

    def LimpaTxRx(self):
        self.ser.flushInput()
        self.ser.flushOutput()

    def Enviar(self,comando):
        self.LimpaTxRx()
        ajuste = comando + '\r\n'
        self.ser.write(ajuste.encode('utf-8'))

    def Ler(self,n):
        try:
            leitura = self.ser.read(n)
            leitura = leitura.decode('utf-8')
            leitura = leitura.replace('\r\n','')
        except:
            leitura = ''

        return leitura

    def Ler_Temp(self):
        self.Enviar(self.LerVolt)
        time.sleep(.5)
        resp = self.Ler(15)
        return resp
       
    def Scan(self,canal):               
        try:
            string=str(canal)
            value = self.SCAN + '(@10'+string+')'
            self.Enviar(value)
            return True
        except:
            return False

    def Monitor(self, canal):
        try:
            string=str(canal)
            value = self.MON + '(@10'+string+')'
            self.Enviar(value)
            return True
        except:
            return False

##    def Coleta(self):               
##        try:
##            self.Enviar(self.LerVolt)
##            time.sleep(.45)
##            dado = self.Ler(200)
##            return float(dado)
##        except:
##            dado = ''
##            return dado

    def Coleta(self):
        try:
            self.Enviar(self.LerVolt)
            time.sleep(.1)
            valor = self.Ler(200)
            return valor
        except:
            return False
        
    
