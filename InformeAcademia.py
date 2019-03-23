import os

from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, Paragraph, TableStyle, Table)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from sqlite3 import dbapi2



bbdd = dbapi2.connect("basedatosAlumnos.dat")
cursor = bbdd.cursor()

#alumnos = cursor.execute("select * from alumnos")
asignaturas = cursor.execute("select * from asignaturas")

doc = SimpleDocTemplate("InformeTablas.pdf", pagesize=A4)
hojaEstilo = getSampleStyleSheet()
estilo = hojaEstilo['BodyText']

guion = []

cabezeraAlumnos = [['Nombre', 'Apellidos', 'DNI', 'Edad', 'Curso', 'Repetidor']]
for elemento in cursor.execute("select * from alumnos"):
    cabezeraAlumnos.append(elemento)

cabezeraAsignaturas = [['Asignatura', 'Dia', 'Profesor', 'Precio']]
for elemento in cursor.execute("select * from asignaturas"):
    cabezeraAsignaturas.append(elemento)

cadena="En este informe se encuentra todo los datos de la base de la aplicacion."+\
    "Los valores de las tablas son los presentes en la base de datos en el momento de la generacion del informe"+\
    "Cualquier modificación en la aplicación tras generar este documento hace que los datos entre el mismo y los mostrados en la aplicación no sean los mismos."
parrafo=Paragraph(cadena,estilo)
guion.append(parrafo)
guion.append(Spacer(0,20))


parrafo=Paragraph("Alumnos matriculados en la academia:",estilo)
guion.append(parrafo)
guion.append(Spacer(0,10))

tabla=Table(cabezeraAlumnos,colWidths=80,rowHeights=30)
tabla.setStyle(TableStyle(
    [
        ('BACKGROUND',(0,0),(-1,0),colors.darkred),
        ('TEXTCOLOR',(0,0),(-1,0),colors.white),
        ('BOX',(0,0),(-1,-1),1,colors.black),
        ('INNERGRID',(0,0),(-1,-1),1,colors.grey),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]
))

guion.append(tabla)
guion.append(Spacer(0,20))


parrafo=Paragraph("Asignaturas impartidas en la academia:",estilo)
guion.append(parrafo)
guion.append(Spacer(0,10))

tabla=Table(cabezeraAsignaturas,colWidths=80,rowHeights=30)
tabla.setStyle(TableStyle(
    [
        ('BACKGROUND',(0,0),(-1,0),colors.aliceblue),
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
        ('BOX',(0,0),(-1,-1),1,colors.black),
        ('INNERGRID',(0,0),(-1,-1),1,colors.grey),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]
))

guion.append(tabla)
guion.append(Spacer(0,20))

doc.build(guion)