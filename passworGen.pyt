import random
import string
def genarate_password(lenght):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    all_characters = lowercase+uppercase+digits+symbols
    
    password = ''.join(random.choice(all_characters) for _ in range(lenght))
    
    return password



while True:
    try:
        length = int(input("Enter the deired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer> ")
        else:
            break
    except ValueError:
        print("Please enter a valid integer. ")
        
password = genarate_password(length)
print(f"\nYour generated password is : {password}")