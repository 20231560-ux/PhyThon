# Đọc file chứa từ điển mật mã
def load_key(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        return eval(data)  # chuyển chuỗi thành dict


# Mã hóa file
def encode_file(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    result = ""
    for ch in text:
        if ch in key:
            result += key[ch]
        else:
            result += ch

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print("✅ Đã mã hóa xong →", output_file)


# Giải mã file
def decode_file(input_file, output_file, key):
    # đảo key
    decode_key = {v: k for k, v in key.items()}

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    result = ""
    for ch in text:
        if ch in decode_key:
            result += decode_key[ch]
        else:
            result += ch

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print("✅ Đã giải mã xong →", output_file)


# ================= MENU =================
print("=== CHƯƠNG TRÌNH MÃ HÓA FILE ===")
print("1. Mã hóa")
print("2. Giải mã")

choice = input("Chọn: ")

key = load_key("key.txt")

if choice == "1":
    encode_file("input.txt", "encoded.txt", key)
elif choice == "2":
    decode_file("encoded.txt", "decoded.txt", key)
else:
    print("❌ Lựa chọn không hợp lệ")