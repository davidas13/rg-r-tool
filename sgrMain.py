import sys
import os
import maya.cmds as cmds
import pymel.core as pm
sys.dont_write_bytecode = True

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------

# Function replace sep '\' to '/'
def rePath(path):
    sep = os.path.sep
    if sep != '/':
        path = path.replace(sep, '\\')
    return path

# main filepath
MAIN_PATH = rePath('C:\Users\david.agung\Documents\gsa_tool')       # Edit Path
# UI path
UI_PATH = os.path.join(MAIN_PATH, 'res/views')      # Edit path

# UI filepaths
mainWindowUi = os.path.join(UI_PATH, 'main_window.ui')
mainWidgetUI = os.path.join(UI_PATH, 'main_widget.ui')       # Edit variable name (main*) & Edit (main_*)(.ui)

# ui filepath
WIN_TITLE = 'Main'
WIN_OBJECT_NAME = 'mainMain'


# Set up access Lib
if MAIN_PATH not in sys.path:
    sys.path.append(MAIN_PATH)

# ----------------------------------------------------------------------
# Main script
# ----------------------------------------------------------------------

# import module Qt.py (bindings)
from lib.Qt import QtWidgets
from lib.Qt import QtCore
from lib.Qt import QtCompat
from lib.Qt import QtGui

class Main(QtWidgets.QMainWindow):      # Edit class name
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)      # Edit class object name

        self.setWindowTitle(WIN_TITLE)
        self.setObjectName(WIN_OBJECT_NAME)

        self.setWindowFlags(QtCore.Qt.Window)
        self.setProperty("saveWindowPref", True)


        # load UIs
        self.mainWindowWidget = QtCompat.load_ui(mainWindowUi)
        self.mainWidget = QtCompat.load_ui(mainWidgetUI)        # edit variable (self.main*)

        self.mainWindowWidget.verLayout.addWidget(self.mainWidget)      # edit variable (self.main*)

        self.setCentralWidget(self.mainWindowWidget)

        self.initUi()

    def initUi(self):
        pass

    def test(self):
        print('test')

# ----------------------------------------------------------------------
# Run Tool
# ----------------------------------------------------------------------

def _maya_delete_ui():
    """Delete existing UI in Maya"""
    if cmds.window(WIN_OBJECT_NAME, q=True, exists=True):
        cmds.deleteUI(WIN_OBJECT_NAME)      # Delete window

def _maya_main_window():
    """Return Maya's main window"""
    for obj in QtWidgets.qApp.topLevelWidgets():
        if obj.objectName() == 'MayaWindow':
            return obj
    raise RuntimeError('Could not find MayaWindow instance')

def main():
    # Edit variable main (Optional)
    _maya_delete_ui()
    main = GsaMain(parent=_maya_main_window())
    main.setProperty("saveWindowPref", True)
    main.show()


if __name__ == "__main__":
    main()