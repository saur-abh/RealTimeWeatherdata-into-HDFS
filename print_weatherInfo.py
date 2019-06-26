import urllib2
response =urllib2.urlopen('http://api.apixu.com/v1/current.json?key=50e18156d7704eac99d93832191704&q&q=jaipur')
html = response.read()
print(html)
