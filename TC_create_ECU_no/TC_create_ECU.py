from pywinauto.application import Application
import time

app = Application(backend="win32").connect(title_re=".*My Teamcenter - Teamcenter 12*")
dlg = app["My Teamcenter - Teamcenter 12"]

dlg.menu_select("File->New->Item")
dlg.wait("visible")
time.sleep(1)

dlg = app.NewItem

dlg.edit.type_keys("MPart")
window2 = app.Dialog
button2 = window2[u'&Next >']
button2.Click()
