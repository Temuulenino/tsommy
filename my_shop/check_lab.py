from lab8 import app
from html.parser import HTMLParser
class Links(HTMLParser):
 def handle_starttag(self, tag, attrs):
  for k,v in attrs:
   if k in ('href','src') and v.startswith('/'): urls.add(v)
client=app.test_client()
urls=set()
for path in ['/', '/store', '/product', '/product/2', '/product/3', '/cart', '/hello', '/hello/Bat']:
 r=client.get(path); assert r.status_code==200,(path,r.status_code)
 Links().feed(r.get_data(as_text=True))
 print('OK',path)
for path in sorted(urls):
 assert client.get(path).status_code==200,path
assert 'Сайн уу, дэлхий!' in client.get('/hello').get_data(as_text=True)
assert 'Сайн уу, Bat!' in client.get('/hello/Bat').get_data(as_text=True)
assert client.get('/product/999').status_code==404
assert '&lt;script&gt;' in client.get('/hello/%3Cscript%3E').get_data(as_text=True)
print('PASS: all pages, internal links, static assets, greetings, escaping and missing product.')
