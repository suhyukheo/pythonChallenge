import bz2
# compress(bytes) : bytes 압축하기 
# decompress(bytes) bytes 압축풀기
# 앞에 b를 붙여주면 뒤에오는 객체를 문자열이 아닌 바이트로 읽어달라
un=b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
un_de =  bz2.decompress(un)
pw_de = bz2.decompress(pw)
print(f"un:{un_de.decode('utf-8')}\npw:{pw_de.decode('utf-8')}")