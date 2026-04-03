def write_personal_info(filename='setInfo.txt'):
    """Nhập thông tin cá nhân và ghi vào file."""
    try:
        name = input('Nhập tên: ').strip()
        age = input('Nhập tuổi: ').strip()
        email = input('Nhập email: ').strip()
        skype = input('Nhập skype: ').strip()
        address = input('Nhập địa chỉ: ').strip()
        workplace = input('Nhập nơi làm việc: ').strip()

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Tên: {name}\n")
            f.write(f"Tuổi: {age}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Skype: {skype}\n")
            f.write(f"Địa chỉ: {address}\n")
            f.write(f"Nơi làm việc: {workplace}\n")

        print(f'Da luu thong tin vao file "{filename}"')
    except Exception as e:
        print('Loi khi ghi file:', e)


def read_personal_info(filename='setInfo.txt'):
    """Đọc thông tin từ file và hiển thị."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()

        if not content:
            print(f'File "{filename}" rỗng.')
            return

        print('--- Noi dung file ---')
        print(content)
        print('--- Ket thuc ---')
    except FileNotFoundError:
        print(f'Khong tim thay file "{filename}". Vui long chay write_personal_info truoc.')
    except Exception as e:
        print('Loi khi doc file:', e)


if __name__ == '__main__':
    print('Bai 4: luu va doc thong tin ca nhan')
    while True:
        print('\nLua chon:')
        print('1. Nhap va luu thong tin ca nhan')
        print('2. Doc thong tin tu file')
        print('3. Thoat')
        choice = input('Chon (1/2/3): ').strip()

        if choice == '1':
            write_personal_info()
        elif choice == '2':
            read_personal_info()
        elif choice == '3':
            print('Ket thuc.')
            break
        else:
            print('Lua chon khong hop le. Vui long chon 1, 2 hoac 3.')
