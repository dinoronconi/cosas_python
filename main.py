import modulo as A
import moduloN as B
import sys
import csv
import cx_Oracle
from datetime import datetime
import wx

import requests
from bs4 import BeautifulSoup

class VentanaEjemplo(wx.Frame):
    def __init__(self, parent, title):
        super(VentanaEjemplo, self).__init__(parent, title=title)
        self.SetPosition((10,10))
        self.Show(True)

class EjemploMenu(wx.Frame):
    def __init__(self, parent, title):
        super(EjemploMenu, self).__init__(parent, title=title)
        self.SetPosition((10,10))
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()

        archivo = wx.Menu()

        archivo.Append(wx.ID_FILE, '&Archivo')
        archivo.Append(wx.ID_EDIT, '&Editar')
        archivo.Append(wx.ID_SAVE, '&Guardar')
        archivo.Append(wx.ID_HELP, '&Ayuda')
        archivo.AppendSeparator()

        edit = wx.Menu()
        edit.Append(wx.ID_ANY, '&ZItem')
        edit.Append(wx.ID_ANY, '&XItem')
        edit.Append(wx.ID_ANY, '&WItem')

        archivo.AppendMenu(wx.ID_ANY, '&editar', edit)
        opcion = wx.MenuItem(archivo, wx.ID_ANY, '&Salir')
        archivo.AppendItem(opcion)
        self.Bind(wx.EVT_MENU, self.OnQuit, opcion)

        menubar.Append(archivo, '&Archivo')

        self.SetMenuBar(menubar)
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

class EjemploTexto(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.Center()

        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(3,2)

        self.textoU = wx.StaticText(self.panel, label="Usuario:")
        self.sizer.Add(self.textoU, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.textoP = wx.StaticText(self.panel, label="Password:")
        self.sizer.Add(self.textoP, pos=(1,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.textoR = wx.StaticText(self.panel, label="Respuesta:")
        self.sizer.Add(self.textoR, pos=(2,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        self.textoeditU = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoeditU, pos=(0,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.BOTTOM, border=5)
        self.textoeditP = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoeditP, pos=(1,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.BOTTOM, border=5)

        self.boton = wx.Button(self.panel, label="Log in", size=(50,25))
        self.sizer.Add(self.boton, pos=(3,3), span=(1,3), flag=wx.RIGHT|wx.BOTTOM)

        self.Bind(wx.EVT_BUTTON, self.Validar, self.boton)
        self.panel.SetSizerAndFit(self.sizer)

    def Validar(self, event):
        usuario = self.textoeditU.GetValue()
        password = self.textoeditP.GetValue()

        if usuario == 'dino' and password == 'dino':
            self.textoR.SetLabel('Ingreso habilitado')
            nv = NuevaVentana(None)
            nv.show()
        else:
            self.textoR.SetLabel('Ingreso denegado!')

class NuevaVentana(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self, -1)
        txt = wx.StaticText(panel, label="Entramos!")
        self.Show()

try:
    url = input("Ingresar URL: ")
    url = 'http://'+url
    print(url)
    r = requests.get('http://'+url)

    data = r.text
    soup = BeautifulSoup(data)
    print('Entro en el loop?')
    for link in soup.find_all('img', class_="attachment-home-post wp-post-image"):
        print('loop 1...')
        print(link.get('width'))


except Exception as e:
    print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))



""" 
    A.metodo()
    B.metodo()
    print(sys.path)

====================================
Interfaz gráfica

try:
    app = wx.App()
    frame = EjemploTexto(None)
    frame.Show()
    app.MainLoop()
exception
  
    if __name__ == '__main__':
        app = wx.App()
        VentanaEjemplo(None, title="Hola!")
        app.MainLoop()
        
   app = wx.App()
   frame = wx.Frame(None, -1, "Primera Ventana", size=(400,400))
   #  frame = wx.Frame(None, -1, "Primera Ventana", style=wx.MINIMIZE_BOX| wx.MAXIMIZE_BOX| wx.RESIZE_BORDER| wx.SYSTEM_MENU| wx.CAPTION, size=(400-400))
   frame.Show()

   app.MainLoop()
    =========================================
   Entrada-salida archivos de texto
    ===================
    doc = open("archivo_prueba.csv", "w")
    doc_csv_w = csv.writer(doc)

    today = datetime.today().strftime("%Y-%m-%d %H:%M")
    lista = ([today, "<<BOF>>"],["Dino", 16900140],["Pepe", 2456464],["Sasa", 3865745],["Memee", 4000012],[today, "<<EOF>>"])

    for line in lista:
      doc_csv_w.writerow(line)

    doc.close()
    
    =========================================
        doc = open("BD-Inmuebles.csv", "r")
    doc_csv_r = csv.reader(doc, delimiter=";")

    for(Referencia, FechaAlta, Tipo, Operacion, Provincia, Superficie, PrecioVenta, FechaVenta, Vendedor) in doc_csv_r:
        print(Referencia, FechaAlta,Provincia,Vendedor)

    doc.close()
    =========================================
    Acceso a base de datos Oracle
    ===================
        con = cx_Oracle.connect('dino/dino@127.0.0.1/orcl')

    print ("Conectado a Oracle "+con.version)

    cur = con.cursor()
    cur.execute('select * from ventas order by referencia')

    rows = cur.fetchall()

    for row in rows:
        print(row)
  #  for result in cur:
   #     print(result)
    cur.close()
    con.close()
"""