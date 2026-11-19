import random
import string

def generate_otp(length):
    # string.digits gives us '0123456789'
    digits = string.digits 
    otp = ""
    
    # Loop 'length' amount of times to build the OTP
    for _ in range(length):
        otp += random.choice(digits)
        
    return otp

print("--- OTP Generator ---")
try:
    otp_length = int(input("Enter the length of OTP to generate (e.g., 4 or 6): "))
    if otp_length <= 0:
        print("Please enter a positive number.")
    else:
        print(f"Your {otp_length}-digit OTP is: {generate_otp(otp_length)}")
except ValueError:
    print("Invalid input. Please enter a whole number.")