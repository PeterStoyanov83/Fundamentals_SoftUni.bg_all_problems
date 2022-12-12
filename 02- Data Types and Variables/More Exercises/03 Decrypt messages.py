key = int(input())
leinght_of_message = int(input())
decoded_message = ''

for letter in range(1, leinght_of_message +1 ):
    input_letter = input()

    decoded_message += chr(key + ord(input_letter))

print(decoded_message)

"""
3. Decrypting Messages

On the first line, you will receive a key (integer). On the second line, you will receive n – the number 
of lines, which will follow. On the next n lines – you will receive a lower and an uppercase letter per line.

You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.

Examples

Input   Output        

3       SoftUni         
7                     
P                            
l                       
c                       
q                       
R                       
k                       
f          
"""