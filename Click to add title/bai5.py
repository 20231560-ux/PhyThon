import re


def count_words_in_file(filename='demo_file2.txt'):
    """Đếm số lượng xuất hiện của các từ trong file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f'File "{filename}" khong ton tai. Tao file mau va dem lai.')
        sample = 'Dem so luong tu xuat hien abc abc abc 12 12 it it eau t'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(sample)
        text = sample

    # Tách từ (giữ cả số), không phân biệt hoa thường
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    counts = {}
    for w in words:
        token = w.lower()
        counts[token] = counts.get(token, 0) + 1

    return counts


def main():
    filename = 'demo_file2.txt'
    counts = count_words_in_file(filename)

    if not counts:
        print('Khong co tu nao de dem.')
    else:
        print('Ket qua tra ve:')
        print(counts)


if __name__ == '__main__':
    main()
