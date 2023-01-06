import os
import math
import random
import smtplib
# testing
import unittest
import re


def email_check(mail):
    compil = re.compile(r"""^([-a-z0-9_]+((\w)+[-a-z0-9_]+(\w)+)?)@[-a-z0-9_]+[.]([-a-z0-9_]+([.][-a-z0-9_]+)?)$""",
                        re.X)
    result = compil.search(mail)
    if result:
        length = mail.split('@')
        if len(length[0]) <= 128 and len(length[1]) <= 256:
            print(mail, 'correct' if not '-.' in length[1] and not '.-' in length[1] else 'Incorrect value')
            return result.group()
        else:
            print('Length string is not mathing')
    else:
        print('Incorrect data')
    return ""


class TestingEmail(unittest.TestCase):
    def setUp(self):
        self.mails = ["hardikachaudhari02@gmail.com", "shreyashsupe11@gmail.com", "hac2002@gmail.com"]
        print("hello")

    def test_EmailCheck(self):
        for i in self.mails:
            self.assertTrue(i == email_check(i), "INCORRECT Value")

    def tearDown(self):
        self.mails = [""]


def getOtp(value):
    digits = "0123456789"
    for i in range(d):
        Otp += digits[math.floor(random.random() * 10)]
    return Otp;


def login_id():
    i = input("Enter your email id")
    return i


if __name__ == '__main__':
    unittest.main()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    email_identity = login_id()
    s.login(email_identity, "dmtm smso zkdq maue")
    emailid = input("Enter your email: ")
    s.sendmail('&&&&&&&&&&&', emailid, msg)
    Otp_length = input("Provide the length of Otp:")
    Otp = getOtp(Otp_length);
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Verified")
    else:
        print("Please Check your OTP again")