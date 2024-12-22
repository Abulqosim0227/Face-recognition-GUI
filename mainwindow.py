import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
import resource
# from model import Model
from out_window import Ui_OutputDialog


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("mainwindow.ui", self)

        self.runButton.clicked.connect(self.runSlot)

        self._new_window = None
        self.Videocapture_ = None

    def refreshAll(self):
        """
        Set the text of lineEdit once it's valid
        """
        self.Videocapture_ = "0"  # This is set to '0', which can represent the default webcam (ensure that it's handled correctly)

    @pyqtSlot()
    def runSlot(self):
        """
        Called when the user presses the Run button
        """
        print("Clicked Run")
        self.refreshAll()
        print(self.Videocapture_)
        ui.hide()  # Hide the main window
        self.outputWindow_()  # Create and open new output window

    def outputWindow_(self):
        """
        Create new window for visual output of the video in GUI
        """
        self._new_window = Ui_OutputDialog()
        self._new_window.show()

        # Ensure Videocapture_ is an integer or valid video source
        video_source = int(self.Videocapture_)  # Convert the capture source to an integer (0 for webcam)
        self._new_window.startVideo(video_source)  # Pass the integer value to the startVideo method

        print("Video Played")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
