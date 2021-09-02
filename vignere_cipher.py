import re


def clean_text(text: str) -> str:
    res = text

    # Convert to lowercase
    res = res.lower()

    # Remove whitespace
    res.strip()

    # Remove number
    res = ''.join([i for i in res if not i.isdigit()])

    # Remove punctuation
    res = re.sub(r'[^\w\s]', '', res)

    return res


def generate_key_standard(plain_text: str, key: str) -> str:
    if(len(key) >= len(plain_text)):
        return key[:len(key)]

    full_key: str = key
    for i in range(len(plain_text) - len(key)):
        full_key += key[i % len(key)]

    return full_key


def generate_key_auto(plain_text: str, key: str) -> str:
    if(len(key) >= len(plain_text)):
        return key[:len(key)]

    full_key: str = key
    for i in range(len(plain_text) - len(key)):
        full_key += plain_text[i % len(key)]

    return full_key


def vignere_cipher_encrypt(plain_text: str, key: str) -> str:
    cipher_text = ""

    for i in range(len(plain_text)):
        curr_plain_text_num = ord(plain_text[i]) - ord('a')
        curr_key_text_num = ord(key[i]) - ord('a')
        curr_cipher_text_num = (curr_plain_text_num + curr_key_text_num) % 26

        cipher_text += alphabet[curr_cipher_text_num]

    return cipher_text


def vignere_cipher_decrypt(cipher_text: str, key: str) -> str:
    plain_text = ""

    for i in range(len(cipher_text)):
        curr_cipher_text_num = ord(cipher_text[i]) - ord('a')
        curr_key_text_num = ord(key[i]) - ord('a')
        curr_plain_text_num = (curr_cipher_text_num - curr_key_text_num) % 26

        plain_text += alphabet[curr_plain_text_num]

    return plain_text


def vignere_cipher_standard_encrypt(plain_text: str, key: str):
    clean_plain_text = clean_text(plain_text)
    full_key = generate_key_standard(clean_plain_text, clean_text(key))

    return vignere_cipher_encrypt(clean_plain_text, full_key), full_key


def vignere_cipher_auto_key_encrypt(plain_text: str, key: str):
    clean_plain_text = clean_text(plain_text)
    full_key = generate_key_auto(clean_plain_text, clean_text(key))

    return vignere_cipher_encrypt(clean_plain_text, full_key), full_key


def main():
    global alphabet
    alphabet = [chr(97 + i) for i in range(26)]

    plain_text = "simanalagi"
    key = "karel"

    cipher_text, full_key = vignere_cipher_standard_encrypt(plain_text, key)
    print(cipher_text)

    decrypt_text = vignere_cipher_decrypt(cipher_text, full_key)
    print(decrypt_text)

    cipher_text_2, full_key_2 = vignere_cipher_auto_key_encrypt(
        plain_text,
        key
    )
    print(cipher_text_2)

    decrypt_text = vignere_cipher_decrypt(cipher_text_2, full_key_2)
    print(decrypt_text)


if __name__ == "__main__":
    main()
