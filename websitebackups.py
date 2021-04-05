
import urllib
import urllib2

URL = "www.mypersonalhoneypotclickheretobefound.com"
U = "backups"
P = "TSNJYWEJHB&hkjshfjg3rhjfsnafhjtg&U@e83eh87Jhhd6"



params = {'param1': 'value1'}

req = urllib2.Request("http://someurl", urllib.urlencode(params))
res = urllib2.urlopen(req)

data = res.read()
