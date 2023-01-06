import random
import email.utilis
import smtplib # send mail from sender to user
server = smtplib.SMTP('smtp.gmail.com',587)
server .starttls()
server.login('ankitnarkhede102@gmail.com',"hypa wyeq dbow plwh")
otp = ''.join ([str(random.randint(0,9))for i in range(4)])
msg = 'hello,your otp is '+str(otp)
vr = msg
rc = str(input("Enter receiver's mail: "))
server.sendmail('ankitnarkhede102@gmail.com',str(rc),msg)
server.quit()
print(otp)
temp = str(input("Enter received OTP: "))
if(otp==temp):
    print("Verified..!!")
else:
    print(" not verified")