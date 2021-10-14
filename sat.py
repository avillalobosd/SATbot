#AGREGAR EN EL SISTEMA PATH LA RUTA DE CHROME

# CORRE ESTO PRIMERO EN EL CMD
# chrome.exe --remote-debugging-port=9250 --user-data-dir="C:/chromedriver2"
#INICIAR SESION EN LA WEBAPP EN LA PANTALLA QUE SE ABRIO
from tkinter import *
from tkinter import ttk
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import threading  
from io import BytesIO
import win32clipboard
from PIL import Image
switch = True  
# os.system('clear')
# from firebase import Firebase



#### CONGIRUACION PANTALLA DE WEB APP
opts = Options()
opts.add_experimental_option('debuggerAddress', 'localhost:9222')
driver = webdriver.Chrome(options=opts)
# driver = webdriver.Chrome()
# driver = webdriver.Chrome()

def comprobante():
    codigo_postal=driver.find_element_by_xpath('//*[@id="LugarExpedicion"]')
    codigo_postal.click()
    codigo_postal.send_keys(Keys.CONTROL, 'a')
    # time.sleep(1)
    codigo_postal.send_keys("66220")
    # time.sleep(1)
    botonSiguiente=driver.find_element_by_xpath('//*[@id="Complementos"]')
    botonSiguiente.click()

def complementos():
    registroPatronal=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Emisor_RegistroPatronal"]')
    registroPatronal.click()
    registroPatronal.send_keys(Keys.CONTROL, 'a')
    # time.sleep(1)
    if(f.get()==2):
        registroPatronal.send_keys("314909")
        # time.sleep(1)
    if(f.get()==3):
        registroPatronal.send_keys("314908")
        # time.sleep(1)
    RFCPatron=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Emisor_RfcPatronOrigen"]')
    RFCPatron.click()
    RFCPatron.send_keys(Keys.CONTROL, 'a')
    # time.sleep(1)
    if(f.get()==2):
        RFCPatron.send_keys("FIA030509UT8")
        # time.sleep(1)
    if(f.get()==3):
        RFCPatron.send_keys("FIA030509UE7")
        # time.sleep(1)
    # time.sleep(1)
    ## ENTIDAD SNCF
    try:
        origenRecurso=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Emisor_EntidadSNCF_OrigenRecurso"]')
        origenRecurso.click()
        origenRecurso.send_keys("IP")
        origenRecurso.send_keys(Keys.RETURN)
    except Exception:
        EntidadSNFC=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Emisor_EntidadSNCF_Activo"]')
        EntidadSNFC.click()
        ##ORIGEN RECURSO
        origenRecurso=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Emisor_EntidadSNCF_OrigenRecurso"]')
        origenRecurso.click()
        origenRecurso.send_keys("IP")
        origenRecurso.send_keys(Keys.RETURN)

def datosPersona():
    # time.sleep(2)
    ##CURP
    CURP=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_Curp"]')
    CURP.click()
    CURP.send_keys(Keys.CONTROL, 'a')
    # time.sleep(1)
    if(r.get()==1):
        CURP.send_keys("NAMY641209MNLVRL01")
    if(r.get()==2):
        CURP.send_keys("VIDA850702HNLLLB03")
    if(r.get()==3):
        CURP.send_keys("LOEV790927HNLPSC01")
    if(r.get()==4):
        CURP.send_keys("SIRR850911HNLFDB06")
    if(r.get()==5):
        CURP.send_keys("FAMJ660619HTSZRL02")
    if(r.get()==6):
        CURP.send_keys("AAMA490819HNLRRL08")
    if(r.get()==7):
        CURP.send_keys("OIMJ600419HDGRRS06")
    if(r.get()==8):
        CURP.send_keys("LEGF761030HNLNNR01")
    ##NUMERO SEGURO SOCIAL
    NSS=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_NumSeguridadSocial"]')
    NSS.click()
    NSS.send_keys(Keys.CONTROL, 'a')
    if(r.get()==1):
        NSS.send_keys("8")
    if(r.get()==2):
        NSS.send_keys("21")
    if(r.get()==3):
        NSS.send_keys("13")
    if(r.get()==4):
        NSS.send_keys("39")
    if(r.get()==5):
        NSS.send_keys("29")
    if(r.get()==6):
        NSS.send_keys("34")
    if(r.get()==7):
        NSS.send_keys("40")
    if(r.get()==8):
        NSS.send_keys("35")
    ##FECHA INICIO RELACION LABORAL
    FIRL=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_FechaInicioRelLaboral"]')
    FIRL.click()
    FIRL.send_keys(Keys.CONTROL, 'a')
    # time.sleep(1)
    if(r.get()==1):
        FIRL.send_keys("2000-01-15")
    if(r.get()==2):
        FIRL.send_keys("2008-03-01")
    if(r.get()==3):
        FIRL.send_keys("2004-03-22")
    if(r.get()==4):
        FIRL.send_keys("2014-06-16")
    if(r.get()==5):
        FIRL.send_keys("2009-09-01")
    if(r.get()==6):
        FIRL.send_keys("2010-09-16")
    if(r.get()==7):
        FIRL.send_keys("2017-10-02")
    if(r.get()==8):
        FIRL.send_keys("2013-06-01")
    # time.sleep(1)
    # ANTGUEDAD
    antig=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_Antig_edad"]')
    antig.click()
    antig.send_keys(Keys.CONTROL, 'a')
    # time.sleep(1)
    if(r.get()==1):
        antig.send_keys("P20Y1M15D")
    if(r.get()==2):
        antig.send_keys("P12Y1M15D")
    if(r.get()==3):
        antig.send_keys("P16Y1M15D")
    if(r.get()==4):
        antig.send_keys("P6Y1M15D")
    if(r.get()==5):
        antig.send_keys("P11Y1M15D")
    if(r.get()==6):
        antig.send_keys("P10Y1M15D")
    if(r.get()==7):
        antig.send_keys("P3Y1M15D")
    if(r.get()==8):
        antig.send_keys("P7Y1M15D")
    # time.sleep(1)
    # TIPO DE CONTRATO
    TC=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_TipoContrato"]')
    TC.click()
    TC.send_keys("01")
    # time.sleep(1)
    TC.send_keys(Keys.RETURN)
    # time.sleep(1)
    #SINDICALIZADO
    Sindicato=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_Sindicalizado"]')
    Sindicato.click()
    if(r.get()==6 or r.get()==7 or r.get()==4):
        Sindicato.send_keys("No")
        # time.sleep(1)
        Sindicato.send_keys(Keys.RETURN)
    else:
        Sindicato.send_keys("Sí")
        # time.sleep(1)
        Sindicato.send_keys(Keys.RETURN)
    # time.sleep(1)
    ##TIPO DE JORNADA
    jornada=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_TipoJornada"]')
    jornada.click()
    jornada.send_keys("01")
    # time.sleep(1)
    jornada.send_keys(Keys.RETURN)
    # time.sleep(1)
    ##TIPO DE REGIMEN
    regimen=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_TipoRegimen"]')
    regimen.click()
    regimen.send_keys("02")
    regimen.send_keys(Keys.RETURN)
    ##NUMERO DE EMPLEADO
    noEmp=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_NumEmpleado"]')
    noEmp.click()
    noEmp.send_keys(Keys.CONTROL, 'a')
    time.sleep(1)
    if(r.get()==1):
        noEmp.send_keys("8")
    if(r.get()==2):
        noEmp.send_keys("21")
    if(r.get()==3):
        noEmp.send_keys("13")
    if(r.get()==4):
        noEmp.send_keys("39")
    if(r.get()==5):
        noEmp.send_keys("29")
    if(r.get()==6):
        noEmp.send_keys("34")
    if(r.get()==7):
        noEmp.send_keys("40")
    if(r.get()==8):
        noEmp.send_keys("35")
    time.sleep(1)
    ## DEPARTAMENTO
    dep=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_Departamento"]')
    dep.click()
    if(r.get()==2 or r.get()==4):
        dep.send_keys("SISTEMAS")
    if(r.get()==1 or r.get()==6 or r.get()==8):
        dep.send_keys("CUENTAS POR COBRAR")
    if(r.get()==3):
        dep.send_keys("CONTABILIDAD")
    if(r.get()==5):
        dep.send_keys("COORDINACION")
    if(r.get()==7):
        dep.send_keys("DIRECCION")
    ## PUESTO
    puesto=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_Puesto"]')
    puesto.click()
    puesto.send_keys(Keys.CONTROL, 'a')
    # time.sleep(1)
    if(r.get()==1):
        puesto.send_keys("CAJERA RECEPCIONISTA")
    if(r.get()==2):
        puesto.send_keys("COORDINADOR DE SISTEMAS")
    if(r.get()==3):
        puesto.send_keys("COORDINADOR DE CONTABILIDAD")
    if(r.get()==4):
        puesto.send_keys("ANALISTA DE SISTEMAS")
    if(r.get()==5):
        puesto.send_keys("COORDINADOR GENERAL")
    if(r.get()==6):
        puesto.send_keys("COORDINADOR DE CUENTAS POR COBRAR")
    if(r.get()==7):
        puesto.send_keys("DIRECTOR")
    if(r.get()==8):
        puesto.send_keys("ANALISTA DE SISTEMAS")
    # RIESGO PUESTO
    riesgo=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_RiesgoPuesto"]')
    riesgo.click()
    # time.sleep(1)
    riesgo.send_keys(1)
    riesgo.send_keys(Keys.RETURN)
    ## PERIODICIDAD
    periodicidad=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_PeriodicidadPagoLookUp"]')
    periodicidad.click()
    periodicidad.send_keys("04")
    # time.sleep(1)
    periodicidad.send_keys(Keys.RETURN)
    ##BANCO
    banco=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_Banco"]')
    banco.click()
    banco.send_keys("012")
    banco.send_keys(Keys.RETURN)
    ##SALARIO DIARIO INTEGRADO
    salario=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_SalarioDiarioIntegrado"]')
    salario.click()
    salario.send_keys(Keys.CONTROL, 'a')
    salario.send_keys("1")
    ##CLAVE ENTIDAD FEDERATIVA
    cef=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_Receptor_ClaveEntFed"]')
    cef.click()
    cef.send_keys("NLE")
    cef.send_keys(Keys.RETURN)

def reciboNomina():
    ##TIPO DE NOMINA
    tNomina=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_TipoNomina"]')
    tNomina.click()
    tNomina.send_keys("O")
    tNomina.send_keys(Keys.RETURN)
    diasPagados=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_NumDiasPagados"]')
    diasPagados.click()
    diasPagados.send_keys(Keys.CONTROL, 'a')
    diasPagados.send_keys(15)
    fechaPago=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_FechaPago"]')
    fechaInicial=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_FechaInicialPago"]')
    fechaFinal=driver.find_element_by_xpath('//*[@id="Complemento_Nomina_FechaFinalPago"]')
    ##ENERO
    if(q.get()==1):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-01-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-01-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-01-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==2):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-01-31")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-01-31")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-01-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##FEBRERO
    if(q.get()==3):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-02-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-02-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-02-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==4):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-02-28")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-02-28")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-02-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##MARZO
    if(q.get()==5):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-03-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-03-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-03-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==6):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-03-31")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-03-31")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-03-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##ABRIL
    if(q.get()==7):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-04-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-04-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-04-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==8):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-04-30")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-04-30")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-04-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##MAYO
    if(q.get()==9):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-05-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-05-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-05-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==10):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-05-31")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-05-31")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-05-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##JUNIO
    if(q.get()==11):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-06-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-06-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-06-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==12):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-06-30")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-06-30")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-06-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##JULIO
    if(q.get()==13):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-07-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-07-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-07-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==14):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-07-31")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-07-31")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-07-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##AGOSTO
    if(q.get()==15):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-08-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-08-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-08-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==16):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-08-31")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-08-31")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-08-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##SEPTIEMBRE
    if(q.get()==17):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-09-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-09-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-09-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==18):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-09-30")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-09-30")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-09-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##OCTUBRE
    if(q.get()==19):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-10-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-10-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-10-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==20):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-10-31")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-10-31")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-10-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##NOVIEMBRE
    if(q.get()==21):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-11-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-11-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-11-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==22):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-11-30")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-11-30")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-11-16")
        fechaInicial.send_keys(Keys.RETURN)
    ##DICIEMBRE
    if(q.get()==23):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-12-15")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-12-15")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-12-01")
        fechaInicial.send_keys(Keys.RETURN)
    if(q.get()==24):
        fechaPago.click()
        fechaPago.send_keys(Keys.CONTROL, 'a')
        fechaPago.send_keys("2021-12-31")
        fechaPago.send_keys(Keys.RETURN)
        fechaFinal.click()
        fechaFinal.send_keys(Keys.CONTROL, 'a')
        fechaFinal.send_keys("2021-12-31")
        fechaFinal.send_keys(Keys.RETURN)
        fechaInicial.click()
        fechaInicial.send_keys(Keys.CONTROL, 'a')
        fechaInicial.send_keys("2021-12-16")
        fechaInicial.send_keys(Keys.RETURN)




    
def inicio():
    comprobante()
    complementos()
    datosPersona()
    reciboNomina()




root = Tk()
root.title('SAT BOT')
root.geometry("600x700")


# empleado=StringVar()
# empleado.set("Ninguno")
# tipo= OptionMenu(root, empleado,"Ninguno","Yolanda","Abelardo","Alan","Victor","Francisco","MaestroJesus","JoseArangua")
# tipo.grid(row=0,column=0)

r=IntVar()
r.set("1")
radioYola=Radiobutton(root, text="Yolanda Navarro", variable=r, value=1)
radioAbe=Radiobutton(root, text="Abelardo Villalobos", variable=r, value=2)
radioVictor=Radiobutton(root, text="Victor Lopez", variable=r, value=3)
radioAlan=Radiobutton(root, text="Alan Sifuentes", variable=r, value=4)
radioJulio=Radiobutton(root, text="Julio C. Faz", variable=r, value=5)
radioJose=Radiobutton(root, text="José Arangua", variable=r, value=6)
radioJesus=Radiobutton(root, text="Jesús Ortiz", variable=r, value=7)
radioFrancisco=Radiobutton(root, text="Francisco de Leon", variable=r, value=8)
##GRID
radioYola.grid(row=0,column=0,sticky=W)
radioAbe.grid(row=1,column=0,sticky=W)
radioVictor.grid(row=2,column=0,sticky=W)
radioAlan.grid(row=3,column=0,sticky=W)
radioJulio.grid(row=4,column=0,sticky=W)
radioJose.grid(row=5,column=0,sticky=W)
radioJesus.grid(row=6,column=0,sticky=W)
radioFrancisco.grid(row=7,column=0,sticky=W)

q=IntVar()
q.set("1")
radio1=Radiobutton(root, text="1a Enero", variable=q, value=1)
radio2=Radiobutton(root, text="2a Enero", variable=q, value=2)
radio3=Radiobutton(root, text="1a Febrero", variable=q, value=3)
radio4=Radiobutton(root, text="2a Febrero", variable=q, value=4)
radio5=Radiobutton(root, text="1a Marzo", variable=q, value=5)
radio6=Radiobutton(root, text="2a Marzo", variable=q, value=6)
radio7=Radiobutton(root, text="1a Abril", variable=q, value=7)
radio8=Radiobutton(root, text="2a Abril", variable=q, value=8)
radio9=Radiobutton(root, text="1a Mayo", variable=q, value=9)
radio10=Radiobutton(root, text="2a Mayo", variable=q, value=10)
radio11=Radiobutton(root, text="1a Junio", variable=q, value=11)
radio12=Radiobutton(root, text="2a Junio", variable=q, value=12)
radio13=Radiobutton(root, text="1a Julio", variable=q, value=13)
radio14=Radiobutton(root, text="2a Julio", variable=q, value=14)
radio15=Radiobutton(root, text="1a Agosto", variable=q, value=15)
radio16=Radiobutton(root, text="2a Agosto", variable=q, value=16)
radio17=Radiobutton(root, text="1a Septiembre", variable=q, value=17)
radio18=Radiobutton(root, text="2a Septiembre", variable=q, value=18)
radio19=Radiobutton(root, text="1a Octubre", variable=q, value=19)
radio20=Radiobutton(root, text="2a Octubre", variable=q, value=20)
radio21=Radiobutton(root, text="1a Noviembre", variable=q, value=21)
radio22=Radiobutton(root, text="2a Noviembre", variable=q, value=22)
radio23=Radiobutton(root, text="1a Diciembre", variable=q, value=23)
radio24=Radiobutton(root, text="2a Diciembre", variable=q, value=24)

##GRID
radio1.grid(row=0,column=1,sticky=W)
radio2.grid(row=1,column=1,sticky=W)
radio3.grid(row=2,column=1,sticky=W)
radio4.grid(row=3,column=1,sticky=W)
radio5.grid(row=4,column=1,sticky=W)
radio6.grid(row=5,column=1,sticky=W)
radio7.grid(row=6,column=1,sticky=W)
radio8.grid(row=7,column=1,sticky=W)
radio9.grid(row=8,column=1,sticky=W)
radio10.grid(row=9,column=1,sticky=W)
radio11.grid(row=10,column=1,sticky=W)
radio12.grid(row=11,column=1,sticky=W)
radio13.grid(row=12,column=1,sticky=W)
radio14.grid(row=13,column=1,sticky=W)
radio15.grid(row=14,column=1,sticky=W)
radio16.grid(row=15,column=1,sticky=W)
radio17.grid(row=16,column=1,sticky=W)
radio18.grid(row=17,column=1,sticky=W)
radio19.grid(row=18,column=1,sticky=W)
radio20.grid(row=19,column=1,sticky=W)
radio21.grid(row=20,column=1,sticky=W)
radio22.grid(row=21,column=1,sticky=W)
radio23.grid(row=22,column=1,sticky=W)
radio24.grid(row=23,column=1,sticky=W)


f=IntVar()
f.set("2")
radioF2=Radiobutton(root, text="EDUCACION", variable=f, value=2)
radioF3=Radiobutton(root, text="SERVIDORES", variable=f, value=3)
radioF2.grid(row=0,column=2,sticky=W)
radioF3.grid(row=1,column=2,sticky=W)


botonPrueba = Button(root, text="Iniciar", command=inicio)
botonPrueba.grid(row=0,column=3)
root.mainloop()