from PyQt5.QtWidgets import QMessageBox

def show_error_message( message):
        error_message = QMessageBox()
        error_message.setIcon(QMessageBox.Critical)
        error_message.setWindowTitle("Error")
        error_message.setText(message)
        error_message.setStandardButtons(QMessageBox.Ok)
        error_message.exec_()

def show_success_message(message):
    success_message = QMessageBox()
    success_message.setIcon(QMessageBox.Information)
    success_message.setWindowTitle("Success")
    success_message.setText(message)
    success_message.setStandardButtons(QMessageBox.Ok)
    success_message.exec()