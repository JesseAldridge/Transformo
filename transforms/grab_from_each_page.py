
from grab import grab
from download_page import download_page

def grab_from_each_page(lines, re_):
  new_lines = []
  for line in lines:
    new_lines.append(grab(download_page(line), re_))    
  return new_lines
  
if __name__ == '__main__':
  print grab_from_each_page(['http://google.com'], 'google')