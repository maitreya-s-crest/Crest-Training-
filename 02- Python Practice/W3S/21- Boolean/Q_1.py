def pass_verifier(pas):
    
    if len(pas) < 8 or len(pas) > 16:
        return False
    
    capital_word = any(i.isupper() for i in pas)
    small_word = any(i.islower() for i in pas)

    digit = any(i.isdigit() for i in pas)
    special_char = "!@#$%^&*()_+[]{}|;:,.<>?/"

    special_check = any( i in special_char for i in pas)

    return capital_word and small_word and digit and special_check



while True:
    password = input("Enter Password : ")

    if pass_verifier(password):
        print("Password is strong!!!")
        break
    else:
        print("Password is poor,Add another one!!")


