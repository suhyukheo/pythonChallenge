text ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
ret =''
def isalpha(alpha):
  if ('A' <= alpha <= 'Z') or ('a' <= alpha <='z'):
    return  True
  else: 
    return False
  
for i in text:
  if isalpha(i):
      if ord(i)+2 > ord('z'):
         ret+=chr(((ord(i)+2)%ord('z'))+96)
      else:
         ret+=chr(ord(i)+2)
  else:
    ret+=i

print(ret)
 
url ='map'
ret= ''
for i in range(len(url)):
   ret += chr(ord(url[i])+2)
print(ret)