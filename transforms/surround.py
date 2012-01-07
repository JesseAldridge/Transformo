
import string

def surround(lines, s):
  new_lines = []
  for line in lines:
    init_white = line[:line.find(line.strip())]
    new_line = init_white + s + line.strip() + s
    new_lines.append(new_line)
  return new_lines
  
if __name__ == "__main__":
  print surround(["foo", "  foo"], "'")