
import os, inspect, sys
from os.path import join, splitext

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from transform_window import transform_window


def transform_controls(filename, control_layout, main_edits):
  # Import the transform func.  Make a button.  Inspect the arguments.
  func_name = splitext(filename)[0]
  exec('from jca.tools.transform.transforms.%s import %s as func' %
     (func_name, func_name))
  parm_edits = []
  button = QPushButton(func_name.replace("_", " "))
  arg_names = inspect.getargspec(func)[0]

  # Add appropriate widgets.  Connect the button to a caller.
  if len(arg_names) > 1:
    parm_edits = [ParmEdit(button) for _ in range(len(arg_names) - 1)]
    [edit.setMaximumSize(50, 20) for edit in parm_edits]
    layout = QHBoxLayout()
    for widget in [button] + parm_edits:  layout.addWidget(widget)
    control_layout.addLayout(layout)
  else:  control_layout.addWidget(button)
  button.connect(button, SIGNAL("clicked()"),
           create_caller(func, arg_names[0], main_edits, parm_edits))

def create_caller(func, arg_name, main_edits, parm_edits):
  # Create a function which will pass the gui parms to the transformer func.
  if parm_edits is None:  parm_edits = []
  def call_func():
    start = unicode(main_edits[0].toPlainText())
    if arg_name == 'lines':  start = start.splitlines()
    parm_edits_ = [unicode(edit.text()) for edit in parm_edits]
    result = func(start, *parm_edits_)
    if arg_name == 'lines':  result = '\n'.join(result)
    main_edits[1].setPlainText(result)
  return call_func
  
# A line edit associated with a button.  Click the button on hit return.
class ParmEdit(QLineEdit):
  def __init__(self, button, *args, **kwargs):
    self.button = button
    QLineEdit.__init__(self, *args, **kwargs)
  def keyPressEvent(self, event):
    key = event.key()
    if key == Qt.Key_Return or key == Qt.Key_Enter:  self.button.click()
    QLineEdit.keyPressEvent(self, event)

# Create a window with two big edits.  Add controls for the transforms between.
app = QApplication(sys.argv)
window = transform_window()
window.resize(1400, 600)
transforms_dir = 'transforms'
for root, dirs, files in os.walk(transforms_dir):
  for filename in [file for file in files if file.endswith('.py') and
           not file == '__init__.py']:
    transform_controls(filename, window.control_layout, window.main_edits)
window.scroll_area.setWidget(window.scroll_box)
window.show()
app.exec_()