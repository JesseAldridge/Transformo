
from pprint import pprint

def pretty_xml(lines):
  s = lines[0]
  i = 1
  while i < len(xml_string):
    ch = xml_string[i]
    
    if ch == "<":
      new_child, inc = xml_string_to_list(xml_string[i:])
      list_root.append(new_child)
      i += inc + 1
    elif ch == ">":
      return list_root, i
    else:
      list_root[0] += ch
      i += 1
  return [s]