class HocVien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop
    
    def show_info(self):
        print(f"Tên: {self.ho_ten} | NS: {self.ngay_sinh} | Email: {self.email}")
        print(f"ĐT: {self.dien_thoai} | Địa chỉ: {self.dia_chi} | Lớp: {self.lop}\n")
    
    def change_info(self, dia_chi=None, lop=None):
        if dia_chi:
            self.dia_chi = dia_chi
        if lop:
            self.lop = lop

hv1 = HocVien("Phan Quốc Trình", "12/04/2005", "phanquoctrinh@email.com", "0999999999", "18 Nam Định", "CNNTT.14.4")
hv2 = HocVien("Nguyễn Việt Phong", "30/04/2005", "nguyenvietphong@email.com", "0888888888", "36 Thanh Hóa", "CNNTT.14.4")

hv1.show_info()
hv2.show_info()

hv1.change_info(dia_chi="HÀ NỘI", lop="CNNTT.14.4")
hv1.show_info()
