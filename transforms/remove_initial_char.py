
def remove_initial_char(lines):
  new_lines = []
  for line in lines:
    new_lines.append(line[1:] if line else "")
  return new_lines