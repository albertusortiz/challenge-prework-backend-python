# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    
    list_lowercase = ""
    list_uppercase = ""

    is_lowercase = random.sample(string.ascii_lowercase, 5) #Getting 5 valors random in lowercase
    list_lowercase = list_lowercase.join(is_lowercase) #Joining valors
    is_uppercase = random.sample(string.ascii_uppercase,5) #Getting 5 valor random in uppercase
    list_uppercase = list_uppercase.join(is_uppercase) #Joining valors
    is_numbers = random.randint(100,999) #Getting a number of 3 characters between 100 and 999
    is_symbols = random.choice(SYMBOLS) #Getting one symbol random

    password_result = (list_lowercase + list_uppercase + str(is_numbers) + is_symbols) #Joining all variables

    return (random.sample(password_result, 14)) #Return pasdword_result scrambled

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
        # print (password) #Line for watch password random
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
