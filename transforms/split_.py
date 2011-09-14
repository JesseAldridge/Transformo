
def split_(lines, ch):
  return ['\n'.join(line.split(ch)) for line in lines]

if __name__ == "__main__":
  print split_(["foo:bar:baz"], ":")