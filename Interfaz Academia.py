import gi
import sqlite3 as dbapi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Interfaz Academia")
        self.set_border_width(10)

        notebook = Gtk.Notebook()
        self.add(notebook)

        cajaExterior = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=6)
        notebook.append_page(cajaExterior, Gtk.Label("Gestion de Alumnado"))

        #Caja Principal que contiene los diferentes box para los botones, labels, etc...
        boxPrincipal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        cajaExterior.pack_start(boxPrincipal,True, False, 0)

        #Caja que contiene los botones Añadir, Consultar y Borrar
        boxBotones = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_start(boxBotones, True, False, 0)

        self.btnEngadir = Gtk.Button("Engadir")
        boxBotones.pack_start(self.btnEngadir, True, False, 0)

        self.btnConsultar = Gtk.Button("Consultar")
        self.btnConsultar.connect("clicked", self.on_btnConsultarClicked)
        boxBotones.pack_start(self.btnConsultar, True, False, 0)

        self.btnBorrar = Gtk.Button("Borrar")
        boxBotones.pack_start(self.btnBorrar, True, False, 0)


        #Caja con Etiquetas1
        boxLabel1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_start(boxLabel1, True, False, 0)

        self.lblNombre = Gtk.Label("Nombre:")
        boxLabel1.pack_start(self.lblNombre, True, False, 0)

        self.lblApellidos = Gtk.Label("Apellidos:")
        boxLabel1.pack_start(self.lblApellidos, True, False, 0)

        self.lblDni = Gtk.Label("DNI:")
        boxLabel1.pack_start(self.lblDni, True, False, 0)

        #Caja con Entradas de Texto1
        boxEntry1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_start(boxEntry1, True, False, 0)

        self.entryNombre = Gtk.Entry()
        boxEntry1.pack_start(self.entryNombre, True, False, 0)

        self.entryApelidos = Gtk.Entry()
        boxEntry1.pack_start(self.entryApelidos, True, False, 0)

        self.entryDni = Gtk.Entry()
        self.entryDni.set_max_length(9)
        boxEntry1.pack_start(self.entryDni, True, False, 0)

        #Caja con Etiquetas2
        boxLabel2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxPrincipal.pack_start(boxLabel2, True, False, 0)

        self.lblEdad = Gtk.Label("Edad:")
        boxLabel2.pack_start(self.lblEdad, True, False, 0)

        self.lblCurso = Gtk.Label("Curso:")
        boxLabel2.pack_start(self.lblCurso, True, False, 0)

        self.lblRepetidor = Gtk.Label("Repetidor:")
        boxLabel2.pack_start(self.lblRepetidor, True, False, 0)

        #Caja con Entradas de Texto2
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

        name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)

        name_combo.set_entry_text_column(1)
        boxEntry2.pack_start(name_combo, True, False, 0)

        self.chkRepetidor = Gtk.CheckButton()
        boxEntry2.pack_start(self.chkRepetidor, True, False, 0)


        boxSecundario = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing= 6)
        cajaExterior.pack_end(boxSecundario, False, False, 0)

        boxBotones2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxSecundario.pack_start(boxBotones2, False, False, 0)

        self.mostrarBd = Gtk.TreeView()





        #Pagina 2
        paxina2 = Gtk.Box()
        paxina2.set_border_width(8)
        paxina2.add(Gtk.Label("HOLA, soy COCO"))
        notebook.append_page(paxina2, Gtk.Label("Gestion de Material"))


        self.connect("destroy", Gtk.main_quit)
        self.show_all()



    def on_btnConsultarClicked(self, boton):
        conexion = dbapi.connect("basedatosAlumnos.dat")  # nos conectamos a la base de datos
        cursor = conexion.cursor()  # cursor para trabajar con la base de datos

        cursor.execute("""select * from alumnos""")

        for rexistro in cursor.fetchall():

            print("Nome: " + rexistro[0])
            print("Apelidos: " + rexistro[1])
            print("Dni: " + rexistro[2])
            print("Edad: " + rexistro[3])
            print("Curso: " + rexistro[4])
            print("Repetidor: " + rexistro[5] + "\n")


#try:
    #conexion = dbapi.connect("basedatosAlumnos.dat")  # nos conectamos a la base de datos
    #cursor = conexion.cursor()  # cursor para trabajar con la base de datos

#except dbapi.DatabaseError as erroConexion:  # tratamiento de excepcion
    #print("Erro ao crear a conexión")

#else:
    #print("A base de datos ten o obxecto: " + str(conexion))

# CODIGO DE CREACION DE LA BASE DE DATOS.Executar só unha vez

#try:

# La consulta se realiza entre comillas triples (modificar)

    #cursor.execute("create table alumnos (Nombre text,Apellidos text,Dni text, Edad text, Curso text, Repetidor text)")

#except dbapi.DatabaseError as erroSQL:
    #print("Erro na creacion da base de datos: " + str(erroSQL))

#else:
  #print("Base de datos creada corectamente")


#try:
    # Los comandos se ejecutan con comilla doble y simple para los datos
      #cursor.execute("insert into alumnos values ('Sergio', 'Sahuquillo', '12345678R', '20', '1ºDAM', 0)")
      #cursor.execute("insert into alumnos values ('Adrian', 'Brandariz', '17645678R', '25', '1ºASIR', 1)")
      #cursor.execute("insert into alumnos values ('Andrea', 'Cabezas', '12345418R', '28', '2ºDAM', 1)")

      #conexion.commit()

#except dbapi.DatabaseError as erroInsercion:
    #print("Erro na insercion de datos: " + str(erroInsercion))

#else:
    #print("Comando executado correctamente")










"""        Gtk.Window.__init__(self, title="Exemplo Gtk.TreeView")
        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        modelo = Gtk.ListStore(str, str, float, bool, str)
        self.filtro_categoria = modelo.filter_new()
        self.filtro_categoria.set_visible_func(self.categoria_filtro)
        self.parametro_filtro_categoria = None

        modelo.append(["Hotel Melia", "García Barbón 48", 75.38, True, '*'])
        modelo.append(["Hotel Galeones", "Avda Madrid", 80.88, False, '**'])
        modelo.append(["Hotel Baiha", "Paseo as avenidas 55", 60.38, True, '*****'])

        self.categoria = Gtk.ListStore(str)
        for estrelas in range(1, 6):
            self.categoria.append([estrelas * '*'])

        vista = Gtk.TreeView(model=self.filtro_categoria)  # modelo filtrado
        seleccion = vista.get_selection()
        seleccion.connect("changed", self.on_seleccion_changed)
        boxV.pack_start(vista, True, True, 0)

        celdaText = Gtk.CellRendererText()
        celdaText.set_property("editable", True)
        celdaText.connect("edited", self.on_celdaText_edited, modelo)
        columnaHotel = Gtk.TreeViewColumn('Aloxamento', celdaText, text=0)
        columnaHotel.set_sort_column_id(0)
        vista.append_column(columnaHotel)

        celdaText2 = Gtk.CellRendererText(xalign=1)
        columnaDir = Gtk.TreeViewColumn('Dirección', celdaText2, text=1)
        vista.append_column(columnaDir)

        celdaNum = Gtk.CellRendererProgress()
        columnaOcupacion = Gtk.TreeViewColumn('Ocupación', celdaNum, value=2)
        columnaOcupacion.set_sort_column_id(2)
        vista.append_column(columnaOcupacion)

        celdaMascotas = Gtk.CellRendererToggle()

        columnaMascotas = Gtk.TreeViewColumn('Mascotas', celdaMascotas, active=3)
        vista.append_column(columnaMascotas)

        celdaCategoria = Gtk.CellRendererCombo()
        celdaCategoria.set_property("editable", True)
        celdaCategoria.set_property("model", self.categoria)
        celdaCategoria.set_property("text-column", 0)
        celdaCategoria.set_property("has-entry", False)
        celdaCategoria.connect("edited", self.on_combo_edited, modelo)
        columnaCategoria = Gtk.TreeViewColumn('Categoria', celdaCategoria, text=4)
        vista.append_column(columnaCategoria)

        boxH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.txtHotel = Gtk.Entry()
        self.txtDireccion = Gtk.Entry()
        self.chkMascotas = Gtk.CheckButton()
        self.txtOcupacion = Gtk.Entry()
        self.cmbCategoria = Gtk.ComboBox(model=self.categoria)
        celdaCombo = Gtk.CellRendererText()
        self.cmbCategoria.pack_start(celdaCombo, True)
        self.cmbCategoria.add_attribute(celdaCombo, "text", 0)

        # Indicarlle que columna queremos mostrar
        boxH.pack_start(self.txtHotel, True, True, 0)
        boxH.pack_start(self.txtDireccion, True, True, 0)
        boxH.pack_start(self.chkMascotas, True, True, 0)
        boxH.pack_start(self.txtOcupacion, True, True, 0)
        boxH.pack_start(self.cmbCategoria, True, True, 0)
        btnEngadir = Gtk.Button(label="Engadir")
        btnEngadir.connect("clicked", self.on_btnEngadir_clicked, modelo)
        boxH.pack_start(btnEngadir, True, True, 0)

        boxV.pack_start(boxH, True, True, 0)

        boxHFiltro = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.cmbCategoriaF = Gtk.ComboBox(model=self.categoria)
        celdaComboF = Gtk.CellRendererText()
        self.cmbCategoriaF.pack_start(celdaComboF, True)
        self.cmbCategoriaF.add_attribute(celdaComboF, "text", 0)

        btnFiltrar = Gtk.Button(label="Filtrar")
        btnFiltrar.connect("clicked", self.on_btnFiltrar_clicked)

        boxHFiltro.pack_end(btnFiltrar, False, False, 0)
        boxHFiltro.pack_end(self.cmbCategoriaF, False, False, 0)
        boxV.pack_start(boxHFiltro, True, True, 0)

        self.add(boxV)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


    def on_combo_edited(self, control, fila, texto, modelo):
        modelo[fila][4] = texto


    def on_btnEngadir_clicked(self, control, modelo):
        fila = self.cmbCategoria.get_active_iter()
        datos = [self.txtHotel.get_text(), self.txtDireccion.get_text(), float(self.txtOcupacion.get_text()),
                 self.chkMascotas.get_mode(), self.cmbCategoria.get_model()[fila][0]]
        modelo.append(datos)  # Engadir o recollido dos controis


    def on_seleccion_changed(self, seleccion):
        modelo, punteiro = seleccion.get_selected()
        if punteiro is not None:
            self.txtHotel.set_text(modelo[punteiro][0])
            self.txtDireccion.set_text(modelo[punteiro][1])
            self.txtOcupacion.set_text(str(modelo[punteiro][2]))
            self.chkMascotas.set_active(modelo[punteiro][3])
            categorias = self.cmbCategoria.get_model()
            # Non funcionaaaaa, REVISAR
            i = 0
            for categoria in categorias:

                if modelo[punteiro][4] == categoria[0]:
                    self.cmbCategoria.set_active(i)
                i = i + 1


    def on_celdaText_edited(self, control, punteiro, texto, modelo):
        modelo[punteiro][0] = texto


    def on_btnFiltrar_clicked(self, control):
        punteiro = self.cmbCategoriaF.get_active_iter()
        print("Filtrando os hoteis da categoria: ", self.cmbCategoriaF.get_model()[punteiro][0])
        self.parametro_filtro_categoria = self.cmbCategoriaF.get_model()[punteiro][0]
        self.filtro_categoria.refilter()


    def categoria_filtro(self, modelo, punteiro, datos):
        if self.parametro_filtro_categoria is None:
            return True
        else:
            if modelo[punteiro][4] == self.parametro_filtro_categoria:
                return True
            else:
                return False




"""
"""
try:
    conexion = dbapi.connect("basedatos.dat")  # nos conectamos a la base de datos
    cursor = conexion.cursor()  # cursor para trabajar con la base de datos

except dbapi.DatabaseError as erroConexion:  # tratamiento de excepcion
    print("Erro ao crear a conexión")

else:
    print("A base de datos ten o obxecto: " + str(conexion))

# CODIGO DE CREACION DE LA BASE DE DATOS.Executar só unha vez

# try:

# La consulta se realiza entre comillas triples (modificar)

#  cursor.execute("create table alumnos (dni text,nome text,curso text)")

# except dbapi.DatabaseError as erroSQL:
#   print("Erro na creacion da base de datos: " + str(erroSQL))

# else:
#  print("Base de datos creada corectamente")

"""
"""
try:
    # Los comandos se ejecutan con comilla doble y simple para los datos
    #  cursor.execute("insert into alumnos values ('11111a','Miriam Bacelo','2ºDAM')")
    #  cursor.execute("insert into alumnos values ('66666B','Laura Diz','2ºDAM')")
    #  cursor.execute("insert into alumnos values ('788995a','Andrea Cabezas','2ºASIR')")

    conexion.commit()

except dbapi.DatabaseError as erroInsercion:
    print("Erro na insercion de datos: " + str(erroInsercion))

else:
    print("Comando executado correctamente")

dniAlumno = "11111a"
try:
    cursor.execute(""""""select * from alumnos"""""")
    # lista = cursor.fetchall()
    # print(type(lista))
    # cursor.execute("select * from alumnos where dni= '"+ dniAlumno + "'")
    # cursor.execute("select * from alumnos where dni= ?", (dniAlumno,))

    for rexistro in cursor.fetchall():
        print("Dni: " + rexistro[0])
        print("Nome: " + rexistro[1])
        print("Curso: " + rexistro[2] + """"\n"""")

except dbapi.DatabaseError as erroConsulta:
    print("Erro na consulta de datos: " + str(erroConsulta))"""






if __name__ == "__main__":

    FiestraPrincipal()
    Gtk.main()
