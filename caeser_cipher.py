import string


def c_cipher(word, mode="encrypt"):
    word = word.lower()
    alpha = string.ascii_lowercase
    alpha_list = []
    for ch in alpha:
        alpha_list.append(ch)
    print(alpha_list)
    reverse_list = alpha_list.copy()
    reverse_list.reverse()
    print(reverse_list)
    cypher = dict(zip(alpha_list, reverse_list))
    decrypt = dict(zip(alpha_list, reverse_list))
    encrypted_msg = ""
    if mode == "encrypt":
        for ch in word:
            encrypted_msg += cypher[ch]

    else:
        for ch in word:
            encrypted_msg += decrypt[ch]
    return encrypted_msg


print(c_cipher("tivt", "decrypt"))
