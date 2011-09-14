
def add_to_start(lines, s):
  new_lines = []
  for line in lines:
    new_line = s + line
    new_lines.append(new_line)
  print "new_lines: ", new_lines
  return new_lines
  
if __name__ == "__main__":
  print add_to_start(["foo", "  foo"], "  ")