Interfaz Academia
*****************

Esta es la documentacion de la Interfaz de la Academia

Descripcion
===========

La interfaz esta diseñada para un uso rapido e intuitivo de la misma
permitiendo al usuario realizar las tareas basicas de gestion
de la empresa en el menor tiempo posible

- Gestion de Personal
- Gestion de Servicios
- Generacion de Informes

Gestion de Personal
-------------------

La aplicacion permite la gestion completa(Insercion, consulta y eliminacion) del personal de la academia. Se piden 6 datos basicos de la persona, de los cuales, el DNI es clave única, y debe cubrirse siempre.

Gestion de Servicios
--------------------

El apartado de Gestion de Servicios permite consultar en todo momento, las asignaturas que se imparten,el dia, que profesor las imparte y el precio de las mismas

Generacion de Informes
----------------------

La aplicacion permite la generacion de 2 informes que contienen todos los datos almacenados en la base de datos. Un informe contiene todos los alumnos pertenecientes a la academia con todos los datos y el otro informe todas las asignaturas con los respectivos datos




Estructura de la base de datos
------------------------------

Tabla Alumnos
+++++++++++++

=== ====== ========= ==== ===== =========
DNI Nombre Apellidos Edad Curso Repetidor
--- ------ --------- ---- ----- ---------

=== ====== ========= ==== ===== =========


Tabla Asignaturas
+++++++++++++++++

========= === ======== ======
Asgnatura Dia Profesor Tarifa
--------- --- -------- ------

========= === ======== ======


Bibliografia
++++++++++++
`DeveloperGnome <https://developer.gnome.org/gtk3/stable/>`_

.. note::
	Este proyecto se encuentra en la version 1.0, por lo que puede no contener todo lo esperado de un ERP

.. versionadded::
	1.0

Proximas Actualizaciones

* Modificacion de Alumnos
* Añadir Asignaturas(mediante interfaz)
* Impresion de Factura(simple y detallada) de un alumno


