
import os, threading, sys
from os.path import expanduser, join

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from win32api import GetSystemMetrics


save_path = expanduser(join('~', '.transform'))
def transform_window():
  # Before text on the left; after on the right.  Controls in between.
  window, main_layout = QWidget(), QHBoxLayout()
  window.setLayout(main_layout)
  before_edit, after_edit = main_edits = [QPlainTextEdit() for _ in range(2)]
  for edit in main_edits:  setup(edit)
  window.main_edits = main_edits
  window.scroll_area = scroll_area = QScrollArea()
  window.scroll_box = scroll_box = QWidget()
  window.control_layout = control_layout = QVBoxLayout()
  scroll_box.setLayout(control_layout)
  main_layout.addWidget(before_edit, 1)
  main_layout.addWidget(scroll_area)
  main_layout.addWidget(after_edit, 1)
  try:
    with open(save_path) as f:  text = f.read()
  except IOError:  pass
  before_edit.setPlainText(text)
  
  # If the before text is modified, save the changes.  Setup the edits.
  def on_text_change():
    def save():
      with open(save_path, 'w') as f:  f.write(before_edit.toPlainText())
    if v.t:  v.t.cancel()
    v.t = threading.Timer(1, save)
    v.t.start()
  before_edit.connect(before_edit, SIGNAL('textChanged()'), on_text_change)
  return window

def setup(edit):
  # Give the edit a grey background and a font relative to screen size.
  edit.setStyleSheet("* { background-color: rgb(203,208,191) }")
  if os.name == 'nt':
    font_name, font_size = ['DejaVu Sans Mono', 13]
    screen_width = GetSystemMetrics(0)
    if screen_width <= 1024:  font_size = 8
  else:
    font_name, font_size = ['Monospace', 13]
  font = QFont(font_name)
  font.setPointSize(font_size)
  edit.setFont(font)
  
class v:  t = None
  
if __name__ == '__main__':
  app = QApplication(sys.argv)
  widget = transform_window()
  hlayout = QHBoxLayout()
  for button in [QPushButton(), QPushButton()]:  hlayout.addWidget(button)
  widget.control_layout.addLayout(hlayout)
  widget.resize(1400,600)
  widget.show()
  app.exec_()