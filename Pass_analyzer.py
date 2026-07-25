password=input("Enter Password : ")

def check_password(password):
    Has_upper=False
    Has_lower=False
    Has_numbers=False
    Special_characters=False
    for ch in password:
        if ch.isupper():
            Has_upper=True
        elif ch.islower():
            Has_lower=True
        elif ch.isnumeric():
            Has_numbers=True
        elif  not ch.isalnum():
            Special_characters=True

    if(Has_upper==True and Has_lower==True and Has_numbers==True and Special_characters==True):
        print("Strong Password...!")
    else:
        print("week password")
        if len(password) >= 8:
                print("- Password must be at least 8 characters long")

        if not Has_upper:
                print("- Password must contain at least one uppercase letter")

        if not Has_lower:
                print("- Password must contain at least one lowercase letter")

        if not Has_numbers:
                print("- Password must contain at least one digit")
        if not Special_characters:
             print("-Password must contain atleast one special character ")
check_password(password)