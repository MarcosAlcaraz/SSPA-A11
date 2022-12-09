from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from manager import Manager
from particula import Particula
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.manager = Manager()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id = 0

        # Cuando el botón pushbutton es presionado, ejecuta la función click_agregar
        # self.ui.mostrar.clicked.connect(self.click_mostrar)
        self.ui.insertar_inicio.clicked.connect(self.click_insertar_inicio)
        self.ui.insertar_final.clicked.connect(self.click_insertar_final)
        self.ui.randomPushButton.clicked.connect(self.random)

        self.ui.OrdenarAscendenteID_pushbutton_2.clicked.connect(self.accionMostrarTablaSBID)
        self.ui.OrdenarAscendenteVelocidad_pushbutton_2.clicked.connect(self.accionMostrarTablaSBS)
        self.ui.OrdenarDescendenteDistancia_pushbutton_2.clicked.connect(self.accionMostrarTablaSBD)

        self.ui.accionAbrir.triggered.connect(self.accionAbrirArchivo)
        self.ui.accionGuardar.triggered.connect(self.accionGuardarArchivo)

        self.ui.Buscar_pushbutton.clicked.connect(self.accionBuscar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    @Slot()
    def dibujar(self):
        pen = QPen()

        for particula in self.manager:
            pen.setWidth(2)
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)
            self.scene.addEllipse(particula.origenX, particula.origenY, 5, 5, pen)
            self.scene.addEllipse(particula.destinoX,  particula.destinoY, 5, 5, pen)
            self.scene.addLine(particula.origenX, particula.origenY,  particula.destinoX, particula.destinoY, pen)

    @Slot()
    def accionMostrarTabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen X", "Origen Y", "Destino X",
                   "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.manager))

        fila = 0
        for particula in self.manager:
            id_widget = QTableWidgetItem(str(particula.id))
            origenX_widget = QTableWidgetItem(str(particula.origenX))
            origenY_widget = QTableWidgetItem(str(particula.origenY))
            destinoX_widget = QTableWidgetItem(str(particula.destinoX))
            destinoY_widget = QTableWidgetItem(str(particula.destinoY))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(fila, 0, id_widget)
            self.ui.tabla.setItem(fila, 1, origenX_widget)
            self.ui.tabla.setItem(fila, 2, origenY_widget)
            self.ui.tabla.setItem(fila, 3, destinoX_widget)
            self.ui.tabla.setItem(fila, 4, destinoY_widget)
            self.ui.tabla.setItem(fila, 5, velocidad_widget)
            self.ui.tabla.setItem(fila, 6, red_widget)
            self.ui.tabla.setItem(fila, 7, green_widget)
            self.ui.tabla.setItem(fila, 8, blue_widget)
            self.ui.tabla.setItem(fila, 9, distancia_widget)

            fila += 1

    @Slot()
    def accionMostrarTablaSBID(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen X", "Origen Y", "Destino X",
                   "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.manager))

        fila = 0
        array = []

        for particula in self.manager:
            array.append(particula)

        array.sort(key=lambda particula: particula.id, reverse=False)

        self.ui.lista_particulas.clear()
        for particula in array:
            self.ui.lista_particulas.insertPlainText(str(particula))

        for particula in array:
            id_widget = QTableWidgetItem(str(particula.id))
            origenX_widget = QTableWidgetItem(str(particula.origenX))
            origenY_widget = QTableWidgetItem(str(particula.origenY))
            destinoX_widget = QTableWidgetItem(str(particula.destinoX))
            destinoY_widget = QTableWidgetItem(str(particula.destinoY))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(fila, 0, id_widget)
            self.ui.tabla.setItem(fila, 1, origenX_widget)
            self.ui.tabla.setItem(fila, 2, origenY_widget)
            self.ui.tabla.setItem(fila, 3, destinoX_widget)
            self.ui.tabla.setItem(fila, 4, destinoY_widget)
            self.ui.tabla.setItem(fila, 5, velocidad_widget)
            self.ui.tabla.setItem(fila, 6, red_widget)
            self.ui.tabla.setItem(fila, 7, green_widget)
            self.ui.tabla.setItem(fila, 8, blue_widget)
            self.ui.tabla.setItem(fila, 9, distancia_widget)

            fila += 1

    @Slot()
    def accionMostrarTablaSBS(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen X", "Origen Y", "Destino X",
                   "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.manager))

        fila = 0
        array = []

        for particula in self.manager:
            array.append(particula)

        array.sort(key=lambda particula: particula.velocidad, reverse=False)

        self.ui.lista_particulas.clear()
        for particula in array:
            self.ui.lista_particulas.insertPlainText(str(particula))

        for particula in array:
            id_widget = QTableWidgetItem(str(particula.id))
            origenX_widget = QTableWidgetItem(str(particula.origenX))
            origenY_widget = QTableWidgetItem(str(particula.origenY))
            destinoX_widget = QTableWidgetItem(str(particula.destinoX))
            destinoY_widget = QTableWidgetItem(str(particula.destinoY))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(fila, 0, id_widget)
            self.ui.tabla.setItem(fila, 1, origenX_widget)
            self.ui.tabla.setItem(fila, 2, origenY_widget)
            self.ui.tabla.setItem(fila, 3, destinoX_widget)
            self.ui.tabla.setItem(fila, 4, destinoY_widget)
            self.ui.tabla.setItem(fila, 5, velocidad_widget)
            self.ui.tabla.setItem(fila, 6, red_widget)
            self.ui.tabla.setItem(fila, 7, green_widget)
            self.ui.tabla.setItem(fila, 8, blue_widget)
            self.ui.tabla.setItem(fila, 9, distancia_widget)

            fila += 1

    @Slot()
    def accionMostrarTablaSBD(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen X", "Origen Y", "Destino X",
                   "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.manager))

        fila = 0
        array = []

        for particula in self.manager:
            array.append(particula)

        array.sort(key=lambda particula: particula.distancia, reverse=True)

        self.ui.lista_particulas.clear()
        for particula in array:
            self.ui.lista_particulas.insertPlainText(str(particula))

        for particula in array:
            id_widget = QTableWidgetItem(str(particula.id))
            origenX_widget = QTableWidgetItem(str(particula.origenX))
            origenY_widget = QTableWidgetItem(str(particula.origenY))
            destinoX_widget = QTableWidgetItem(str(particula.destinoX))
            destinoY_widget = QTableWidgetItem(str(particula.destinoY))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(fila, 0, id_widget)
            self.ui.tabla.setItem(fila, 1, origenX_widget)
            self.ui.tabla.setItem(fila, 2, origenY_widget)
            self.ui.tabla.setItem(fila, 3, destinoX_widget)
            self.ui.tabla.setItem(fila, 4, destinoY_widget)
            self.ui.tabla.setItem(fila, 5, velocidad_widget)
            self.ui.tabla.setItem(fila, 6, red_widget)
            self.ui.tabla.setItem(fila, 7, green_widget)
            self.ui.tabla.setItem(fila, 8, blue_widget)
            self.ui.tabla.setItem(fila, 9, distancia_widget)

            fila += 1

    @Slot()
    def accionBuscar(self):
        id = self.ui.buscar_lineedit.text()
        bandera = False

        for particula in self.manager:
            if str(id) == str(particula.id):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origenX_widget = QTableWidgetItem(str(particula.origenX))
                origenY_widget = QTableWidgetItem(str(particula.origenY))
                destinoX_widget = QTableWidgetItem(str(particula.destinoX))
                destinoY_widget = QTableWidgetItem(str(particula.destinoY))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenX_widget)
                self.ui.tabla.setItem(0, 2, origenY_widget)
                self.ui.tabla.setItem(0, 3, destinoX_widget)
                self.ui.tabla.setItem(0, 4, destinoY_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                bandera = True

                return
        if not bandera:
            QMessageBox.warning(self, "Particula no encontrada", f'La particula con el ID " {id} " no fue encontrada')

    @Slot()
    def accionAbrirArchivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.manager.abrir(ubicacion):
            self.click_mostrar()
            self.accionMostrarTabla()
            self.dibujar()
            QMessageBox.information(
                self, "Abrir archivo", "Archivo abierto Exitosamente : " + ubicacion)
        else:
            QMessageBox.critical(
                self, "Error", "No se puede abrir el archivo : " + ubicacion)

    @Slot()
    def accionGuardarArchivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar Archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.manager.guardar(ubicacion):
            QMessageBox.information(
                self, "Archivo Guardado", "Guardado Exitoso : " + ubicacion)
        else:
            QMessageBox.critical(
                self, "Error", "Archivo no Guardado : " + ubicacion)

    @Slot()
    def click_insertar_inicio(self):
        self.id += 1
        aux = Particula(self.id, self.ui.ox.value(), self.ui.oy.value(), self.ui.dx.value(), self.ui.dy.value(
        ), self.ui.velocidad.value(), self.ui.red.value(), self.ui.green.value(), self.ui.blue.value())
        self.manager.agregarInicio(aux)
        self.click_mostrar()
        self.accionMostrarTabla()
        self.dibujar()

    @Slot()
    def click_insertar_final(self):
        self.id += 1
        aux = Particula(self.id, self.ui.ox.value(), self.ui.oy.value(), self.ui.dx.value(), self.ui.dy.value(), self.ui.velocidad.value(), self.ui.red.value(), self.ui.green.value(), self.ui.blue.value())
        self.manager.agregarFinal(aux)
        self.click_mostrar()

    @Slot()
    def click_mostrar(self):
        self.ui.lista_particulas.clear()
        self.ui.lista_particulas.insertPlainText(str(self.manager))

    @Slot()
    def random(self):
        self.id += 1

        ox =  randint(0, 500)
        oy = randint(0, 500)
        dx = randint(0, 500)
        dy = randint(0, 500)
        velocidad = randint(0, 999)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        aux = Particula(self.id, ox, oy, dx, dy, velocidad, red, green, blue)
        self.manager.agregarFinal(aux)
        self.click_mostrar()
        self.dibujar()
        self.accionMostrarTabla()
