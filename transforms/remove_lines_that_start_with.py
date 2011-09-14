
def remove_lines_that_start_with(lines, ch):
  return [line for line in lines if line.lstrip(ch) == line]