def no_lowercase(t):
    low = 'abcdefghijklmnopqrstuvwxyz'*2
    for ch in t:
        if ch in low:
            return False
    return True

def no_uppercase(t):
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
    for ch in t:
        if ch in up:
            return False
    return True

def no_number(t):
    num = '0123456789'*2
    for ch in t:
        if ch in num:
            return False
    return True

def no_symbol(t):
    other = '''"`~!@#$%^&*()-_=+[]{}\|;:,<>./\"'''
    for ch in t:
        if ch in other:
            return False
    return True

def character_repetition(t):
    for i in range(len(t)-3):
        if len(set(t[i:i+4])) == 1:
            return True
    return False

def number_sequence(t):
    num = '0123456789'*2
    for i in range(len(t)-3):
        if t[i:i+4] in (num or num[::-1]):
            return True
    return False

def letter_sequence(t):
    low = 'abcdefghijklmnopqrstuvwxyz'*2
    for i in range(len(t)-3):
        if (t[i:i+4].lower() in low) or (t[i:i+4].lower() in low[::-1]):
            return True
    return False

def keyboard_pattern(t):
    pattern1 = '!@#$%^&*()_+'*2
    pattern2 = 'QWERTYUIOP'*2
    pattern3 = 'ASDFGHJKL'*2
    pattern4 = 'ZXCVBNM'*2
    for i in range(len(t)-3):
        if (t[i:i+4].upper() in pattern1) or (t[i:i+4].upper() in pattern1[::-1]) or (t[i:i+4].upper() in pattern2) or (t[i:i+4].upper() in pattern2[::-1]) or (t[i:i+4].upper() in pattern3) or (t[i:i+4].upper() in pattern3[::-1]) or (t[i:i+4].upper() in pattern4) or (t[i:i+4].upper() in pattern4[::-1]):
            return True
    return False

passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append('Less than 8 characters')
if no_lowercase(passw):
    errors.append('No lowercase letters')
if no_uppercase(passw):
    errors.append('No uppercase letters')
if no_number(passw):
    errors.append('No numbers')
if no_symbol(passw):
    errors.append('No symbols')
if character_repetition(passw):
    errors.append('Character repetition')
if number_sequence(passw):
    errors.append('Number sequence')
if letter_sequence(passw):
    errors.append('Letter sequence')
if keyboard_pattern(passw):
    errors.append('Keyboard pattern')

if len(errors) == 0:
    print('OK')
else:
    print('\n'.join(errors))