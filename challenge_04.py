from urllib.request import urlopen 
q ='12345'
count=0
def check_url(query):
    response = urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={query}')
    a = str(response.read())
    print(a)
    a_list =a.split("is")
    ret_query = a_list[1][1:len(a_list[1])-1]
    return ret_query
  
for i in range(1000):
  if count == 85:
    q = check_url(8022)
  elif count==140:
    q = check_url(63579)
  else:
    q =check_url(q)
  count +=1
  