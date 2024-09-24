
def krazy(text):
    temp_list = []
    for i in range(len(text)):
        if i % 2:
            temp_list.append(text[i])
        else:
            temp_list.append(text[i].upper())
    temp_list.append('!')
    return ''.join(temp_list)

print(krazy('bruh'))