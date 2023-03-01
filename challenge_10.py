import re
# r은 raw string의 의미를 가지며, 구체적인 의미는 \을 탈출 문자로 보지 않고, 그냥 아무 역할도 하지 않는 평범한 문자열로 간주하여 처리하겠다는 뜻이다.
#(\d) = 0~9 
new_ant='1'
idx=0
for i in range(30):
  ant = re.findall(r"(\d)(\1*)",new_ant)
  new_ant=''
  idx +=1
  for i in ant:
    new_ant+=str(len(i[1])+1)+i[0]
  print(f"len of idx:{idx} :{len(new_ant)}")