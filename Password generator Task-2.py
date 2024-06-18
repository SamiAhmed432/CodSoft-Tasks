import random                           #Random Module geneared by the system
import string 


print("Password Generator !!")

input=int(input("Enter password length"))

lowercase=string.ascii_lowercase     
uppercase=string.ascii_uppercase
number=string.digits
symbol=string.punctuation

char=lowercase+uppercase+number+symbol
temp=random.sample(char,input)
password=" ".join(temp)
print(password)

