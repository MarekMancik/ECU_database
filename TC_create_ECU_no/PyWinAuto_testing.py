from pywinauto import Application
import time

app = Application().start("notepad.exe")
dlg = app.UntitledNotepad

dlg.edit.type_keys("Ahoj, Jak se máš", with_spaces=True)

dlg.type_keys("^s")
time.sleep(1)

save_dlg = app.window(title='Save As')
save_dlg.wait('visible')
save_dlg.Edit.set_text("example.txt")

save_dlg.Save.click()

dlg.close()

app.window(title='Notepad').wait('visible', timeout=10)
app.Notepad.DontSave.click()