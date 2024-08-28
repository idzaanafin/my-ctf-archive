from string import printable

enc = b'\xd2\x95\xc2p\xa4S\xd5J=\xc0\x9a<b\r\xa7A\xea*<\x85s\xc6\xacG\xee\x87\rd\xb8^\xa9Z\rG\x8d;\x8aX\x8a\x00\x05\xda\x81D\xab.\x96\x93nCV\x1b\x9dQ\x89`)\xae\tTN\x7f\xd3\xc0\x82\xe8\r\xa33R\xac '
flag = "CJ2023{"
gdb.execute("b * 0x21f16f")
for x in range(len(enc)):
     for i in printable.encode():
        x = open("a", "w")
        x.write(flag + chr(i))
        x.close()
        gdb.execute("r < a")

        for j in range(len(flag)):
            gdb.execute("c")
            chk = int(gdb.selected_frame().read_register("al")) & 0xff
            if chk == enc[len(flag)]:
               flag += chr(i)
               print(flag)
               break
