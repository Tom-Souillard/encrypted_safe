import sys
import pytest
from PyQt5.QtWidgets import QApplication
from encrypted_safe.ui.mainwindow import MainWindow

@pytest.fixture(scope='session')
def app():
    app = QApplication(sys.argv)
    yield app
    app.quit()

def test_main_window(app):
    window = MainWindow()
    assert window.windowTitle() == "Encrypted Safe"  # Simple check to see if UI loads correctly
