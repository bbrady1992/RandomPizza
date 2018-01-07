from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject,  pyqtSlot
import sys
from os.path import basename
from pizza_ui import Ui_Form
from random import choice
from json import load

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
                'menus', filter = "*.json")
        if fname[0]:
            self.options_file = fname[0]
            self.ui.optionsLineEdit.setText(basename(self.options_file))

    @pyqtSlot('QString')
    def on_options_file_set(self, arg1):
        options = self.load_options(self.options_file)
        self.crusts, self.cheese_levels, self.sauces, self.sauce_levels, self.toppings = options
        self.ui.maxToppingsLineEdit.setText(str(len(self.toppings)))
        self.ui.toppingNumSelect.setMinimum(0)
        self.ui.toppingNumSelect.setMaximum(len(self.toppings))
        self.ui.toppingNumSelect.setValue(3)

    @pyqtSlot()
    def on_randomize_button_clicked(self):
        self.ui.toppingsListWidget.clear()
        num_toppings = self.ui.toppingNumSelect.value()
        crust = choice(self.crusts)
        cheese_level = choice(self.cheese_levels)
        sauce = choice(self.sauces)
        sauce_level = choice(self.sauce_levels)
        toppings = self.pick_toppings(self.toppings, num_toppings)
        self.ui.crustLineEdit.setText(crust)
        self.ui.cheeseLevelLineEdit.setText(cheese_level)
        self.ui.sauceLineEdit.setText(sauce)
        self.ui.sauceLevelLineEdit.setText(sauce_level)
        for t in toppings:
            self.ui.toppingsListWidget.addItem(t)

    @pyqtSlot()
    def clear_all_fields(self):
        self.ui.crustLineEdit.clear()
        self.ui.cheeseLevelLineEdit.clear()
        self.ui.sauceLineEdit.clear()
        self.ui.sauceLevelLineEdit.clear()
        self.ui.toppingsListWidget.clear()

    def __init__(self):
        super(PizzaApp, self).__init__()
        self.options_file = 'menus/Dominos.json'
        self.crusts = None
        self.cheese_levels = None
        self.sauces = None
        self.sauce_levels = None
        self.toppings = None
        self.init_ui()

    def init_ui(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        self.setup_connections()
        self.ui.optionsLineEdit.setText(basename(self.options_file))

    def pick_toppings(self, toppings, num_toppings):
        toppings = list(toppings)
        picked = []
        for top in range(0, num_toppings):
            random_topping = choice(toppings)
            picked.append(random_topping)
            toppings.remove(random_topping)
        return picked

    def load_options(self, file_name):
        options = load(open(file_name))
        crusts = options['crusts']
        cheese_levels = options['cheese level']
        sauces = options['sauce']
        sauce_levels = options['sauce level']
        toppings = options['toppings']
        return (crusts, cheese_levels, sauces, sauce_levels, toppings)

    def run(self):
        sys.exit(self.app.exec_())

    
if __name__ == "__main__":
    app = PizzaApp()
    app.run()
