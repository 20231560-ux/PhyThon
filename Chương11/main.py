import sqlite3

def connect():
    return sqlite3.connect("nhansu.db")

# ➕ Thêm
def them():
    conn = connect()
    cur = conn.cursor()

    cccd = input("CCCD: ")
    hoten = input("Họ tên: ")
    ngaysinh = input("Ngày sinh: ")
    gioitinh = input("Giới tính: ")
    diachi = input("Địa chỉ: ")

    try:
        cur.execute("INSERT INTO nhanvien VALUES (?, ?, ?, ?, ?)",
                    (cccd, hoten, ngaysinh, gioitinh, diachi))
        conn.commit()
        print("✔ Thêm thành công")

    except Exception as e:
        print("❌ Lỗi:", e)   # 👈 in lỗi thật ra

    conn.close()

# 📄 Hiển thị
def hienthi():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM nhanvien")

    for row in cur.fetchall():
        print(row)

    conn.close()

# 🔍 Tìm kiếm
def timkiem():
    conn = connect()
    cur = conn.cursor()

    key = input("Nhập từ khóa: ")

    cur.execute("""
    SELECT * FROM nhanvien
    WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
    """, (f"%{key}%", f"%{key}%", f"%{key}%"))

    for row in cur.fetchall():
        print(row)

    conn.close()

# ✏️ Sửa
def sua():
    conn = connect()
    cur = conn.cursor()

    cccd = input("Nhập CCCD cần sửa: ")

    hoten = input("Tên mới: ")
    ngaysinh = input("Ngày sinh mới: ")
    gioitinh = input("Giới tính mới: ")
    diachi = input("Địa chỉ mới: ")

    cur.execute("""
    UPDATE nhanvien
    SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
    WHERE cccd=?
    """, (hoten, ngaysinh, gioitinh, diachi, cccd))

    conn.commit()
    conn.close()

    print("✔ Đã sửa")

# ❌ Xóa
def xoa():
    conn = connect()
    cur = conn.cursor()

    cccd = input("Nhập CCCD cần xóa: ")

    cur.execute("DELETE FROM nhanvien WHERE cccd=?", (cccd,))
    conn.commit()

    conn.close()
    print("✔ Đã xóa")


# 🖥️ MENU (phải để ngoài cùng)
while True:
    print("\n===== MENU =====")
    print("1. Thêm")
    print("2. Hiển thị")
    print("3. Tìm kiếm")
    print("4. Sửa")
    print("5. Xóa")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        them()
    elif chon == "2":
        hienthi()
    elif chon == "3":
        timkiem()
    elif chon == "4":
        sua()
    elif chon == "5":
        xoa()
    elif chon == "0":
        break