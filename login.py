from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import sys
from modals import ModalLogin, CaptchaLogin


class Login(QWidget):
    #  def enterClicked(self):
    #         if login(self.login_edit.text(), self.password_edit.text()):
    #             self.modal = ModalLogin()
    #             self.modal.show()
    #             self.close()
    #         else:
    #             self.captchaModal = CaptchaLogin()
    #             self.captchaModal.show()
    def enterClicked(self):
            if self.login_edit.text() == "dalec" and self.password_edit.text() == "14":
                self.modal = ModalLogin()
                self.modal.show()
                self.close()
            else:
                self.captchaModal = CaptchaLogin()
                self.captchaModal.show()
    def __init__(self):
        super().__init__()
        #window settings
        self.setWindowTitle("Вход")
        self.setFixedSize(300, 400)
        #widgets
        self.login_lbl = QLabel("Введите логин:")
        self.password_lbl = QLabel("Введите пароль:")
        self.login_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.enter_btn = QPushButton("Вход")
        #widgets settings
        self.login_lbl.setObjectName('LabelLogin')
        self.password_lbl.setObjectName('LabelLogin')
        self.login_edit.setObjectName('LabelLogin')
        self.password_edit.setObjectName('LabelLogin')
        self.enter_btn.setObjectName('PushButtonLogin')
        self.login_edit.setPlaceholderText("Логин")
        self.password_edit.setPlaceholderText("Пароль")
        #handler events
        self.enter_btn.clicked.connect(self.enterClicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.login_lbl)
        vbox.addWidget(self.login_edit)
        vbox.addWidget(self.password_lbl)
        vbox.addWidget(self.password_edit)
        vbox.addWidget(self.enter_btn)
        self.setLayout(vbox)
     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = Login()
    loginWindow.show()
    app.exec()
