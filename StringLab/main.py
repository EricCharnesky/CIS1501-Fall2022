def encrypt(string, stride):
    scrambled_string = ''

    for index in range(stride):
        scrambled_string += string[index::stride]

    encrypted_string = ''
    for index in range(len(scrambled_string)):
        encrypted_string += chr(ord(scrambled_string[index]) + index)

    return encrypted_string


def decrypt(encrypted_string, stride):
    decrypted_string = ''
    for index in range(len(encrypted_string)):
        decrypted_string += chr(ord(encrypted_string[index]) - index)

    chunks = []
    current_stride_chunk_start = 0

    for index in range(stride):
        count_of_characters_in_stride = 0
        current_index = index
        while current_index < len(decrypted_string):
            count_of_characters_in_stride += 1
            current_index += stride
        chunks.append(decrypted_string[current_stride_chunk_start:current_stride_chunk_start+count_of_characters_in_stride])
        current_stride_chunk_start += count_of_characters_in_stride

    original = ''

    for index in range(len(chunks[0])):
        for chunk in chunks:
            if index < len(chunk):
                original += chunk[index]

    return original

print(encrypt("ABCDEFG", 2))
# ACEBD
# ADGEH

print(decrypt("ADGEHKL", 2))

print(encrypt("ABCDEFG", 3))
# ACEBD
# ADGEH

print(decrypt("AEIEIHL", 3))
