def decoding(data):
    decoding = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ''
    return decoding