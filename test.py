#coding:utf-8
import httplib, urllib
 
httpClient = None
try:
  params = urllib.urlencode({'name': 'Maximus', 'addr': "GZ"})
  headers = {"Content-type": "application/x-www-form-urlencoded"
          , "Accept": "text/plain"}
 
  httpClient = httplib.HTTPConnection("localhost", 8080, timeout=30)
  httpClient.request("POST", "/test0.html", params, headers)
 
  response = httpClient.getresponse()
  print response.status
  print response.reason
  print response.read()
  print response.getheaders() #获取头信息
except Exception, e:
  print e
finally:
  if httpClient:
    httpClient.close()