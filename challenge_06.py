import zipfile

f = zipfile.ZipFile("C:\\Users\\user\\Downloads\\channel.zip")
nothing = '90052'
count =0 
while True:
    a = f.read(nothing+'.txt').decode()
    next_nothing = a.split('is')
    try:
     nothing = next_nothing[1][1:len(next_nothing[1])]
     print(f.getinfo(nothing+'.txt').comment.decode(),end="")
    except:
        print(next_nothing)
        break
    #Collext the comments? 
    #zip 파일에는 주석이 있습니다. 이를 불러오는 코드 
    #print(f.getinfo(nothing+'.txt').comment.decode(),end="")