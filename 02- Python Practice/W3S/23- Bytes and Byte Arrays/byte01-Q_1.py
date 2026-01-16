def byte_converter(string,encoding):
    return string.encode(encoding)

list_of_encoding = ['utf-8','utf-16','ascii']

def all_encode(stri):
    for encode in list_of_encoding:
        print(encode +" -> "+str(byte_converter(stri,encode)))

all_encode("How are you?")