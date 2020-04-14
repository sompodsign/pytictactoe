import re

def testPasswordStrength(password):

    eightCharsLongRegex = re.compile(r'[\w\d\s\W\D\S]{8,}')
    upperCaseRegex = re.compile(r'[A-Z]+')
    lowerCaseRegex = re.compile(r'[a-z]+')
    oneOrMoreDigitRegex = re.compile(r'\d+')

    if not eightCharsLongRegex.search(password):
        return False
    elif not upperCaseRegex.search(password):
        return False
    elif not lowerCaseRegex.search(password):
        return False
    elif not oneOrMoreDigitRegex.search(password):
        return False

    return True

if __name__ == "__main__":
    password = '594'
    print(testPasswordStrength(password))