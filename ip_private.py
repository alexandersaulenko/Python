import re

def is_ip_private(ip):

     # https://en.wikipedia.org/wiki/Private_network

     priv_lo = re.compile("^127\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
     priv_24 = re.compile("^10\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
     priv_20 = re.compile("^192\.168\.\d{1,3}.\d{1,3}$")
     priv_16 = re.compile("^172.(1[6-9]|2[0-9]|3[0-1]).[0-9]{1,3}.[0-9]{1,3}$")

     res = priv_lo.match(ip) or priv_24.match(ip) or priv_20.match(ip) or priv_16.match(ip)
     return res is not None


print(is_ip_private("127.0.0.1"))
