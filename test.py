import re
def removeSpecialChar(string):
  p = re.compile('[a-zA-Z0-9]')
  return ''.join(p.findall(string))

def gcd(a,b):
  if a % b == 0:
    return b
  else:
    return gcd(b,a%b)
  
def lcm(a,b):
  return a*b // gcd(a,b)
    

string1 = "aFDF#^&$%SFSDsd^~#+_gsd2@#%"
print(removeSpecialChar(string1))