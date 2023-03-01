from urllib.request import urlopen 
import pickle

banner = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
banner = pickle.loads(banner)

ret =''

for a in banner:
  for b in a:
    char = b[0]
    for c in range(b[1]):
      print(char,end="")
  print("\n")