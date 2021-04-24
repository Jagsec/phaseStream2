import math
from operator import xor

def scan_file():
    encrypted_message = []
    with open ("output.txt", "r") as encrypted_file:
        for line in encrypted_file:
            encrypted_message.append(line.strip())
    return encrypted_message

def get_pairs(encrypted_message):
    index = 0
    pairs = []
    while index < len(encrypted_message):
        current_line = encrypted_message
        pairs.append(current_line[index] + current_line[index+1])
        index += 2
    return pairs

def convert_hex_to_binary(hex_number):
    res = "{0:08b}".format(int(hex_number, 16))
    return res

def convert_pairs(pairs):
    converted_pairs = []
    for pair in pairs:
        binary = convert_hex_to_binary(pair)
        converted_pairs.append(binary)
    return converted_pairs

def xor_encrypt(value, key):
    res = xor(int(value), key)
    return res

def convert_decimal_to_binary(decimal_number):
    res = format(decimal_number, '08b')
    return res

def convert_binary_to_decimal(binary_number):
    binary_number = str(binary_number)
    res = int(binary_number,2)
    return res

def convert_decimal_to_ascii_value(decimal_number):
    res = chr(decimal_number)
    return res

def concatenate_pairs(pairs):
    encrypted_binary_message = ""
    for pair in pairs:
        encrypted_binary_message += pair
    return encrypted_binary_message

def divide_in_segments(encrypted_binary, cut_length):
    segments = []
    message_length = len(encrypted_binary)
    last_cut = cut_length
    first_cut = 0
    while last_cut < message_length:
        segments.append(encrypted_binary[first_cut: last_cut])
        first_cut += cut_length
        last_cut += cut_length
    segments.append(encrypted_binary[first_cut:-1])
    return segments

def encrypt_decrypt_message(original_message, message_segments, key):
    new_message = ""
    for segment in message_segments:
        new_segmented_message = divide_in_segments(segment, 8)
        for new_segment in new_segmented_message:
            decimal_segment = convert_binary_to_decimal(new_segment)
            print(decimal_segment)
            new_message += convert_decimal_to_ascii_value(xor_encrypt(decimal_segment, key))
    if new_message.startswith("CHTB"):
        print(f"Flag found! {original_message} key {key}\n")

def write_to_txt_file(string, filename):
    with open(filename, "a") as results_file:
        results_file.write(string)

all_messages = scan_file()
for key in range(0,256):
#key = 470188516729
    for message in all_messages:
        pairs = get_pairs(message)
        converted_pairs = convert_pairs(pairs)
        encrypted_binary_message = concatenate_pairs(converted_pairs)
        segments = divide_in_segments(encrypted_binary_message, 8)
        encrypt_decrypt_message(message, segments, key)
"""encrypted = "2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904"
key = "0110110101111001011010110110010101111001"
      #0110110101111001011010110110010101111001 
pairs = get_pairs(encrypted)
converted_pairs = convert_pairs(pairs)
encrypted_binary_message = concatenate_pairs(converted_pairs)
segments = divide_in_segments(encrypted_binary_message, len(key))
encrypt_decrypt_message(encrypted, segments, key)"""