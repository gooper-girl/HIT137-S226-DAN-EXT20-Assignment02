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

    encrypted_text = ""
        
    for char in raw_text:
        if char.islower():
            if char in first_lower:
                idx = first_lower.index(char)
                shift = shift1 * shift2
                new_idx = (idx + shift) % len(first_lower)
                new_char = first_lower[new_idx]
                encrypted_text += new_char

            elif char in second_lower:
                idx = second_lower.index(char)
                shift = shift1 + shift2
                new_idx = (idx - shift) % len(second_lower)
                new_char = second_lower[new_idx]
                encrypted_text += new_char

        elif char.isupper():
            if char in first_upper:
                idx = first_upper.index(char)
                shift = shift1
                new_idx = (idx - shift) % len(first_upper)
                new_char = first_upper[new_idx]
                encrypted_text += new_char

            elif char in second_upper:
                idx = second_upper.index(char)
                shift = shift2 ** 2
                new_idx = (idx + shift) % len(second_upper)
                new_char = second_upper[new_idx]
                encrypted_text += new_char

        elif char.isdigit():
            idx = digits.index(char)
            shift = shift1 - shift2
            new_idx = (idx + shift) % len(digits)
            new_char = digits[new_idx]
            encrypted_text += new_char

        else:
            encrypted_text += char

    with open(output_path, 'w') as f:
        f.write(encrypted_text)

def decrypt_file(shift1, shift2, input_path, output_path):
    with open(input_path, 'r') as f:
        raw_text = f.read()

    decrypted_text = ""
        
    for char in raw_text:
        if char.islower():
            if char in first_lower:
                idx = first_lower.index(char)
                shift = shift1 * shift2
                new_idx = (idx - shift) % len(first_lower)
                new_char = first_lower[new_idx]
                decrypted_text += new_char

            elif char in second_lower:
                idx = second_lower.index(char)
                shift = shift1 + shift2
                new_idx = (idx + shift) % len(second_lower)
                new_char = second_lower[new_idx]
                decrypted_text += new_char

        elif char.isupper():
            if char in first_upper:
                idx = first_upper.index(char)
                shift = shift1
                new_idx = (idx + shift) % len(first_upper)
                new_char = first_upper[new_idx]
                decrypted_text += new_char

            elif char in second_upper:
                idx = second_upper.index(char)
                shift = shift2 ** 2
                new_idx = (idx - shift) % len(second_upper)
                new_char = second_upper[new_idx]
                decrypted_text += new_char

        elif char.isdigit():
            idx = digits.index(char)
            shift = shift1 - shift2
            new_idx = (idx - shift) % len(digits)
            new_char = digits[new_idx]
            decrypted_text += new_char

        else:
            decrypted_text += char

    with open(output_path, 'w') as f:
        f.write(decrypted_text)

def verify_file(original_path, decrypted_path):
    with open(original_path, 'r') as f:
        original_text = f.read()

    with open(decrypted_path, 'r') as f:
        decrypted_text = f.read()

    if original_text == decrypted_text:
        print("The decrypted file matches the original.")

    else:
        print("The decrypted file does NOT match the original.")

encrypt_file(shift1, shift2, "raw_text.txt", "encrypted_text.txt")
decrypt_file(shift1, shift2, "encrypted_text.txt", "decrypted_text.txt")
verify_file("raw_text.txt", "decrypted_text.txt")