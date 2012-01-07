
import re

def build_list(lines, s):
  regex = s
  new_lines = []
  for line in lines:  
    match = re.search(regex, line)
    if match:  new_lines.append(match.group(0))
  return new_lines
  
if __name__ == '__main__':
  print build_list(['foo', 'bar', 'baz'], '[a-z]a[a-z]')