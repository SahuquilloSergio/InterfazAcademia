import gi
import sqlite3 as dbapi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Interfaz Academia")
        self.set_border_width(10)
        self.set_default_size(300, 300)

        notebook = Gtk.Notebook()
        self.add(notebook)

        cajaExterior = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        notebook.append_page(cajaExterior, Gtk.Label("Gestion de Alumnado"))

        # Caja Principal que contiene los diferentes box para los botones, labels, etc...
        boxPrincipal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        cajaExterior.pack_start(boxPrincipal, True, False, 0)

        # Caja que contiene los botones Añadir, Consultar y Borrar
        boxBotones = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_start(boxBotones, True, False, 0)

        self.btnEngadir = Gtk.Button("Engadir")
        self.btnEngadir.connect("clicked", self.on_btnAñadir_clicked)
        boxBotones.pack_start(self.btnEngadir, True, False, 0)

        self.btnConsultar = Gtk.Button("Consultar")
        self.btnConsultar.connect("clicked", self.on_btnConsultarClicked)
        boxBotones.pack_start(self.btnConsultar, True, False, 0)

        self.btnBorrar = Gtk.Button("Borrar")
        self.btnBorrar.connect("clicked", self.on_btnBorrar_clicked)
        boxBotones.pack_start(self.btnBorrar, True, False, 0)

        # Caja con Etiquetas1
        boxLabel1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_start(boxLabel1, True, False, 0)

        self.lblNombre = Gtk.Label("Nombre:")
        boxLabel1.pack_start(self.lblNombre, True, False, 0)

        self.lblApellidos = Gtk.Label("Apellidos:")
        boxLabel1.pack_start(self.lblApellidos, True, False, 0)

        self.lblDni = Gtk.Label("DNI:")
        boxLabel1.pack_start(self.lblDni, True, False, 0)

        # Caja con Entradas de Texto1
        boxEntry1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_start(boxEntry1, True, False, 0)

        self.entryNombre = Gtk.Entry()
        boxEntry1.pack_start(self.entryNombre, True, False, 0)

        self.entryApelidos = Gtk.Entry()
        boxEntry1.pack_start(self.entryApelidos, True, False, 0)

        self.entryDni = Gtk.Entry()
        self.entryDni.set_max_length(9)
        boxEntry1.pack_start(self.entryDni, True, False, 0)

        # Caja con Etiquetas2
        boxLabel2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_start(boxLabel2, True, False, 0)

        self.lblEdad = Gtk.Label("Edad:")
        boxLabel2.pack_start(self.lblEdad, True, False, 0)

        self.lblCurso = Gtk.Label("Curso:")
        boxLabel2.pack_start(self.lblCurso, True, False, 0)

        self.lblRepetidor = Gtk.Label("Repetidor:")
        boxLabel2.pack_start(self.lblRepetidor, True, False, 0)

        # Caja con Entradas de Texto2
        boxEntry2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_end(boxEntry2, True, False, 0)

        self.entryEdad = Gtk.Entry()
        self.entryEdad.set_max_length(2)
        boxEntry2.pack_start(self.entryEdad, True, False, 0)

        name_store = Gtk.ListStore(int, str)
        name_store.append([1, "1º Primaria"])
        name_store.append([2, "2º Primaria"])
        name_store.append([3, "3º Primaria"])
        name_store.append([4, "4º Primaria"])
        name_store.append([5, "5º Primaria"])
        name_store.append([6, "6º Primaria"])
        name_store.append([7, "1º ESO"])
        name_store.append([8, "2º ESO"])
        name_store.append([9, "3º ESO"])
        name_store.append([10, "4º ESO"])
        name_store.append([11, "1º Bachillerato"])
        name_store.append([12, "2º Bachillerato"])
        name_store.append([13, "Universidad"])
        name_store.append([14, "FP Basica"])
        name_store.append([15, "FP Media"])
        name_store.append([16, "FP Superior"])

        self.name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)

        self.name_combo.set_entry_text_column(1)
        boxEntry2.pack_start(self.name_combo, True, False, 0)

        self.chkRepetidor = Gtk.CheckButton()
        boxEntry2.pack_start(self.chkRepetidor, True, False, 0)

        self.boxSecundario = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        cajaExterior.pack_end(self.boxSecundario, False, False, 0)

        self.botonOcultar = Gtk.Button("Cerrar Consulta")
        self.botonOcultar.connect("clicked", self.on_botonOcultar_clicked)
        self.boxSecundario.pack_end(self.botonOcultar, True, False, 0)

        self.people_list_store = Gtk.ListStore(str, str, str, str, str, str)


        conexion = dbapi.connect("basedatosAlumnos.dat")  # nos conectamos a la base de datos
        cursor = conexion.cursor()  # cursor para trabajar con la base de datos

        for item in cursor.execute("select * from alumnos"):
            self.people_list_store.append(list(item))

        self.people_tree_view = Gtk.TreeView(self.people_list_store)

        for i, col_title in enumerate(["Nombre", "Apellidos", "Dni", "Edad", "Curso", "Repetidor"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Make column sortable and selectable
            column.set_sort_column_id(i)

            self.people_tree_view.append_column(column)

        # Handle selection
        selected_row = self.people_tree_view.get_selection()
        selected_row.connect("changed", self.item_selected)

        self.boxSecundario.pack_start(self.people_tree_view, True, True, 0)




        # Pagina 2
        paxina2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        paxina2.set_border_width(8)
        notebook.append_page(paxina2, Gtk.Label("Cursos y Tarifas"))

        box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        paxina2.pack_start(box1, True, False, 0)

        labelCombo = Gtk.Label("Asignaturas")
        box1.pack_start(labelCombo, True, True, 0)
        cmbAsignaturas = Gtk.ComboBoxText()
        cmbAsignaturas.connect("changed", self.on_cmbAsignaturas_changed)




        cmbAsignaturas.set_entry_text_column(0)
        for asignatura in cursor.execute("select asignatura from asignaturas"):

            cmbAsignaturas.append_text(asignatura[0])

        box1.pack_start(cmbAsignaturas, True, True, 0)


        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        paxina2.pack_start(box2, True, False, 0)

        labelDia = Gtk.Label("Dia")
        box2.pack_start(labelDia, True, True, 0)

        self.entryDia = Gtk.Entry()
        box2.pack_start(self.entryDia, True, True, 0)


        box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        paxina2.pack_start(box3, True, False, 0)

        labelProfesor = Gtk.Label("Profesor")
        box3.pack_start(labelProfesor, True, True, 0)

        self.entryProfesor = Gtk.Entry()
        box3.pack_start(self.entryProfesor, True, True, 0)

        box4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        paxina2.pack_start(box4, True, False, 0)

        labelPrecio = Gtk.Label("Precio")
        box4.pack_start(labelPrecio, True, True, 0)

        self.entryPrecio = Gtk.Entry()
        box4.pack_start(self.entryPrecio, True, True, 0)














        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_btnConsultarClicked(self, boton):
        self.boxSecundario.show()

        """conexion = dbapi.connect("basedatosAlumnos.dat")  # nos conectamos a la base de datos
        cursor = conexion.cursor()  # cursor para trabajar con la base de datos


        self.people_list_store.clear()
        for item in cursor.execute("select * from alumnos"):
            self.people_list_store.append(list(item))"""
        self.actualizar_modelo()

    def on_btnAñadir_clicked(self, button):
        conexion = dbapi.connect("basedatosAlumnos.dat")  # nos conectamos a la base de datos
        cursor = conexion.cursor()  # cursor para trabajar con la base de datos
        nombre = self.entryNombre.get_text()
        apelidos = self.entryApelidos.get_text()
        dni = self.entryDni.get_text()
        edad = self.entryEdad.get_text()
        curso = self.name_combo.get_active()
        repetidor = str
        if (nombre == ""):
            print("Nombre no valido")
        else:
            if (self.chkRepetidor.get_active()):
                repetidor = "si"
            else:
                repetidor = "no"
            try:
                cursor.execute(
                    "insert into alumnos values('" + str(nombre) + "','" + str(apelidos) + "','" + str(dni) + "','" + str(
                        edad) + "','" + str(curso) + "','" + str(repetidor) + "')")
                conexion.commit()
                self.actualizar_modelo()


            except dbapi.DatabaseError as erroInsercion:
                print("Erro na insercion de datos: " + str(erroInsercion))

            else:
                print("Comando executado correctamente")

    def item_selected(self, selection):
        model, row = selection.get_selected()
        if row is not None:
            print("Nombre: ", model[row][0])
            print("Apellidos: ", model[row][1])
            print("DNI: ", model[row][2])
            print("Edad: ", model[row][3])
            print("Curso: ", model[row][4])
            print("Repetidor: ", model[row][5])
            print("")
            self.dni = model[row][2]

    def initial_show(self):
        window.show_all()

    def actualizar_modelo(self):
        conexion = dbapi.connect("basedatosAlumnos.dat")  # nos conectamos a la base de datos
        cursor = conexion.cursor()  # cursor para trabajar con la base de datos

        self.people_list_store.clear()
        for item in cursor.execute("select * from alumnos"):
            self.people_list_store.append(list(item))

    def on_botonOcultar_clicked(self, boton):
        self.boxSecundario.hide()

    def on_btnBorrar_clicked(self, boton):
        conexion = dbapi.connect("basedatosAlumnos.dat")  # nos conectamos a la base de datos
        cursor = conexion.cursor()  # cursor para trabajar con la base de datos
        print(self.dni)

        cursor.execute("delete from alumnos where dni='"+self.dni+"'")
        conexion.commit()

        self.actualizar_modelo()




    def on_cmbAsignaturas_changed(self, combo):
        conexion = dbapi.connect("basedatosAlumnos.dat")  # nos conectamos a la base de datos
        cursor = conexion.cursor()  # cursor para trabajar con la base de datos

        texto = combo.get_active_text()
        print(texto)

        try:
            asignaturas = cursor.execute("select dia, profesor, precio from asignaturas where asignatura='"+texto+"'")
            for dato in asignaturas:
                print(dato[0])
                print(dato[1])
                print(dato[2])
                self.entryDia.set_text(dato[0])
                self.entryProfesor.set_text(dato[1])
                self.entryPrecio.set_text(dato[2])

        except AttributeError:
            print("No hay ningún item seleccionado.")




window = FiestraPrincipal()
window.connect("delete-event", Gtk.main_quit)
window.initial_show()
Gtk.main()
