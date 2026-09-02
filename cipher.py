first_lower = "abcdefghijklmn"
second_lower = "opqrstuvwxyz"
first_upper = "ABCDEFGHIJKLM"
second_upper = "NOPQRSTUVWXYZ"
digits = "0123456789"

shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))


def encrypt_file(shift1, shift2, input_path, output_path):
    with open(input_path, 'r') as f:
        raw_text = f.read()
        
    for char in raw_text:
        if char.islower():
            if char in first_lower:
            if char in second_lower:
        elif char.isupper():
        elif char.isdigit():
        else:
            pass

def decrypt_file(shift1, shift2, input_path, output_path):

def verify_file(original_path, decrypted_path):