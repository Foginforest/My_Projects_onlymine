

def to_jaden_case(string):
    final_message = ''
    new_message = [i for i in string]
    for j in range(len(new_message)):
        if new_message[j] == ' ':
            new_message[j + 1] = str(new_message[j + 1].upper())
        if j == 0:
            new_message[j] = str(new_message[j].upper())
    for y in range(len(new_message)):
        final_message += new_message[y]
    print(final_message)



message = 'how can mirrors be real if our eyes aren\'t real'
to_jaden_case(string=message)