def concate_memory_view(m1,m2):
    return memoryview(bytes(m1)+bytes(m2))

str1 = b"Hello "
str2 = b"Hi"

memoryview1 = memoryview(str1)
memoryview2 = memoryview(str2)

concated_memory_view = concate_memory_view(memoryview1,memoryview2)

print(concate_memory_view)

print(bytes(concated_memory_view))