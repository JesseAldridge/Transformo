
def remove_line_nums(lines):  
  new_lines = []
  for line in lines:
    split = line.split(' ', 1)
    if len(split) > 1 and is_number(split[0]):
      new_lines.append(split[1])
    elif is_number(line):
      continue
    else:
      new_lines.append(line)
  return new_lines
  
  
def is_number(s):
  try: 
    int(s)
    return True
  except ValueError:
    return False
    
if __name__ == "__main__":
  print remove_line_nums(["1 foo", "bar"])