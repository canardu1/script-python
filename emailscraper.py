import urllib
import urllib.request
import re
import certifi
import ssl

sites = ["http://list_of_sites.com",]

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

for site in sites:
	f = urllib.request.urlopen(site, context=ssl_context)
	s = f.read().decode('latin1')
	emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
    
	newemails = list(set(emails))
	print(newemails)
