import urllib.request

url = 'https://docs.python.org/ja/3/howto/urllib2.html'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    print(res.read())