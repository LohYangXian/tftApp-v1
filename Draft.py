import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #Add a title
        self.setWindowTitle("TFT Statistics Profile")

        #Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        #Create a Label
        my_label = qtw.QLabel("Enter your Summoner Name and select region to view TFT match statistics!")
        # Change the font size of label
        my_label.setFont(qtg.QFont("Helvetica",18))

        #Add label
        self.layout().addWidget(my_label)

        #Create entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("Summoner_Name")
        my_entry.setText("Enter your Summoner Name here")
        
        #Add the entry box
        self.layout().addWidget(my_entry)

        #Create dropbox
        my_dropbox = qtw.QComboBox()
        my_dropbox.addItem("Select Region")
        my_dropbox.addItem("na1")
        my_dropbox.addItem("br1")
        my_dropbox.addItem("eun1")
        my_dropbox.addItem("euw1")
        my_dropbox.addItem("jp1")
        my_dropbox.addItem("kr")
        my_dropbox.addItem("la1")
        my_dropbox.addItem("la2")
        my_dropbox.addItem("oc1")
        my_dropbox.addItem("ru")
        my_dropbox.addItem("tr1")
        self.layout().addWidget(my_dropbox)
        #my_dropbox.currentText() = my_region

        #Create a button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: "insert class for loading page here")

        #Add the button
        self.layout().addWidget(my_button)

        #Show the App
        self.show()
