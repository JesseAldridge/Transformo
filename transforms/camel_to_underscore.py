
def camel_to_underscore(lines):
  new_lines = []
  for line in lines:
    def go(line, index1, index2):
      if len(line) < 2 or index2 >= len(line):
        return line
      ch1 = line[index1]
      ch2 = line[index2]
      if ch1.islower() and ch2.isupper():
        line = line[:index2] + "_" + ch2.lower() + line[index2 + 1:]
      return go(line, index1 + 1, index2 + 1)
    new_line = go(line, 0, 1)
    new_lines.append(new_line)
  return new_lines
  
if __name__ == "__main__":
  print camel_to_underscore(["fooBar"])