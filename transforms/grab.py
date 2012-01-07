
import re

def grab(s, re_):
  return '\n'.join([match.group() for match in re.finditer(re_, s)])
    
if __name__ == '__main__':
  print grab('<a href="foo_url">foo text</a>', 'href="(.+)"')