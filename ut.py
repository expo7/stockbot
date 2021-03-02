import pyotp
totp  = pyotp.TOTP("233164156555").now()
print("Current OTP:", totp)