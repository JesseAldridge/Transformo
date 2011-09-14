
def cpp_to_py(lines):
  new_lines = []
  for old_line in lines:
    new_line = old_line
    
    if [s for s in ["{", "}"] if new_line.strip() == s]:
      continue
    
    for s in ["const ", "double ", "uint *", "uint ", "int ", ";", 
          "void ", "&", "} ", "bool "]:
      new_line = new_line.replace(s, "")
      
    for f, r in [["::", "."], ["this", "self"], ["->", "."], [" {", ":"],
           ["!", "not "], ["true", "True"], ["false", "False"]]:
      new_line = new_line.replace(f, r)
  
    if new_line.startswith("#include"):
      lch, rch = ("<", ">") if "<" in old_line else ('"', '"')
      new_line = "import " + old_line.split(lch)[1].split(rch)[0]
      
    if new_line.endswith(".h"):
      new_line = new_line[:-2]
      
    new_lines.append(new_line)
  return new_lines