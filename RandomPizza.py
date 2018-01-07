#!/usr/bin/python
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from os.path import basename
sys.path.append('ui')
from ui import Ui_Form
sys.path.append('resources')
from Pizza import Pizza

class PizzaApp(QObject):
    ###
    # Connections
    ###
    def setup_connections(self):
        self.ui.browseButton.clicked.connect(self.on_browse_button_clicked)
        self.ui.randomizeButton.clicked.connect(self.on_randomize_button_clicked)
        self.ui.optionsLineEdit.textChanged.connect(self.on_options_file_set)
        self.ui.optionsLineEdit.textChanged.connect(self.clear_all_fields)

    ###
    # Slots
    ###
    @pyqtSlot()
    def on_browse_button_clicked(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Select file',
                                                      'menus', filter='*.json')
        if fname[0]:
            self.pizza.options_file = fname[0]
            self.ui.optionsLineEdit.setText(basename(self.pizza.options_file))

    @pyqtSlot('QString')
    def on_options_file_set(self, arg1):
        options = self.pizza.load_options()
        max_toppings = len(self.pizza.options['toppings'])
        self.ui.maxToppingsLineEdit.setText(str(max_toppings))
        self.ui.toppingNumSelect.setMinimum(0)
        self.ui.toppingNumSelect.setMaximum(max_toppings)
        self.ui.toppingNumSelect.setValue(3)

    @pyqtSlot()
    def on_randomize_button_clicked(self):
        self.ui.toppingsListWidget.clear()
        self.pizza.num_toppings = self.ui.toppingNumSelect.value()
        self.pizza.randomize()
        self.populate_fields()

    @pyqtSlot()
    def clear_all_fields(self):
        self.ui.crustLineEdit.clear()
        self.ui.cheeseLevelLineEdit.clear()
        self.ui.sauceLineEdit.clear()
        self.ui.sauceLevelLineEdit.clear()
        self.ui.toppingsListWidget.clear()

    ###
    # Remaining methods
    ###
    def __init__(self):
        super(PizzaApp, self).__init__()
        self.pizza = Pizza()
        self.init_ui()

    def init_ui(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        self.setup_connections()
        self.ui.optionsLineEdit.setText(basename(self.pizza.options_file))

    def populate_fields(self):
        self.ui.crustLineEdit.setText(self.pizza.crust)
        self.ui.cheeseLevelLineEdit.setText(self.pizza.cheese_level)
        self.ui.sauceLineEdit.setText(self.pizza.sauce)
        self.ui.sauceLevelLineEdit.setText(self.pizza.sauce_level)
        for topping in self.pizza.toppings:
            self.ui.toppingsListWidget.addItem(topping)

    def run(self):
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = PizzaApp()
    app.run()
