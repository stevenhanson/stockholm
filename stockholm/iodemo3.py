import os

print(os.name)
# uname windows上没有这个函数
# print(os.uname())

print(os.environ)
print(os.environ["PATH"])