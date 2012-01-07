
def add_to_end(lines, s):
  new_lines = []
  for line in lines:
    new_line = line + s
    new_lines.append(new_line)  
  return new_lines
  
if __name__ == "__main__":
  print add_to_end(["foo", "  bar"], " + ")