def rep_char(count):
    print("-"*(count+2))
    print(" "+msg1)
    print(" "+msg2)
    print("-"*(count+2))
    
def draw_line_string(msg1, msg2):
    nstr= len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    return nstr

prompt= input("Input his/her name: ")
msg1= "Hello " + prompt+","
msg2="Welcome to Seoul."
count= draw_line_string(msg1, msg2)
rep_char(count)
