def encode(text, mapping):
    """Encode the text using the provided mapping dictionary."""
    return ''.join(mapping.get(ch, ch) for ch in text)


def decode(text, mapping):
    """Decode the text using the reverse mapping dictionary."""
    reverse_mapping = {v: k for k, v in mapping.items()}
    return ''.join(reverse_mapping.get(ch, ch) for ch in text)


def main():
    mapping = {
        'a': '!',
        'b': '@',
        'c': '#',
        'd': '$',
        'e': '%',
        'f': '^',
        'g': '&',
        'h': '*',
        'i': '(',
        'j': ')',
        'k': '-',
        'l': '+',
        'm': '=',
        'n': '{',
        'o': '}',
        'p': '[',
        'q': ']',
        'r': ':',
        's': ';',
        't': '"',
        'u': "'",
        'v': '<',
        'w': '>',
        'x': ',',
        'y': '.',
        'z': '?'
    }

    print('Chương trình mã hóa / giải mã văn bản')
    print('1. Mã hóa')
    print('2. Giải mã')
    choice = input('Chọn 1 hoặc 2: ').strip()

    if choice not in {'1', '2'}:
        print('Lựa chọn không hợp lệ.')
        return

    text = input('Nhập văn bản: ')

    if choice == '1':
        result = encode(text, mapping)
        print('Kết quả mã hóa:', result)
    else:
        result = decode(text, mapping)
        print('Kết quả giải mã:', result)


if __name__ == '__main__':
    main()
