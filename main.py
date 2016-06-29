from __future__ import print_function

import requests
from django.utils import html

if __name__ == '__main__':
  print('Hello world')
  r = requests.get('http://www.srcclr.com', allow_redirects=False)
  print(r.url)
  print(r.headers)
  print(r.text)
  requests.sessions.SessionRedirectMixin.resolve_redirects
  x = "<html><body>HELLO HTML WORLD</body></html>"
  print(x)
  y = html.strip_tags(x)
  print(y)
