cipher = input("please enter a cypher code:  ")
shift = int(input("please input a shift value from 1 to 25:  "))

message = ""
final_message = ""
for ch in cipher:
    for i in range(shift):
        if ch.isalpha() == False:
            message = message + ch
        elif ch == chr(90):
            ch = chr(65)
            message = message + ch
        elif ch == chr(122):
            ch = chr(97)
            message = message + ch
        else:
            ch = chr(ord(ch)+1)
            message = message + ch
    for ch in message[-1]:
        final_message = final_message + ch
        message =""
print(final_message)



