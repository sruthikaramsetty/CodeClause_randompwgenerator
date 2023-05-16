import random
lower="qwertyuiopasdfghjklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLMNBVCXZ"
numbers="0123456789"
symbols="!@#$%^&*()"
string=lower+upper+numbers+symbols
length=10
password="".join(random.sample(string,length))
print("Your new password is"+password)
