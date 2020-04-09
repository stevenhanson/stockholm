# try :
#     f = open("d:\\abc.txt","r")
#     print(f.read())
# finally:
#     if f:
#         f.close()


# with open("d:\\abc.txt", "r") as f:
#     print(f.read())

# r 读取模式  b按字节读取 
with open("d:\\abc.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        print(line.strip())


