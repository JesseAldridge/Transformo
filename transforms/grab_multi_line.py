
import re

def grab_multi_line(s, re_):
  return '\n'.join([match for match in re.findall(re_, s, re.DOTALL)])
    
if __name__ == '__main__':
  print grab_multi_line('<a href="foo_url">foo text</a>', 'href="(.+)"')