
def keep_only_indented(lines):
  return [line.strip() for line in lines if line.lstrip() != line]