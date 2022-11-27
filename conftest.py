import time

from pywinauto import Desktop, Application
import pytest


@pytest.fixture(scope="function")
def dlg():
    app = Application(backend="uia").start('calc.exe')
    dlg = Desktop(backend="uia").Калькулятор
    time.sleep(1)
    yield dlg
    dlg.child_window(auto_id="Close", control_type="Button").click()