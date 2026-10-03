from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QWidget

from ui_files_python.configurate_camera import Ui_CameraConfig


class CameraServerConnectionInterface(QDialog):
    _port_regex: QRegularExpression = QRegularExpression("[\\d]+")
    ui: Ui_CameraConfig

    def __init__(self, parent: QWidget | None = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_CameraConfig()
        self.ui.setupUi(self)
        self.ui.invalid_input_error_label.hide()

        self.ui.camera_width.setValidator(QRegularExpressionValidator(self._port_regex))
        self.ui.camera_height.setValidator(QRegularExpressionValidator(self._port_regex))

        # Varsayılanlar burada: ui_files ayrı bir depo, oradaki .ui dosyasına
        # dokunmadan değerleri kendi kodumuzda tutuyoruz.
        self.ui.server_ip_input.setPlaceholderText("10.0.0.193:9999")
        self.ui.camera_width.setPlaceholderText("1280")
        self.ui.camera_height.setPlaceholderText("720")
