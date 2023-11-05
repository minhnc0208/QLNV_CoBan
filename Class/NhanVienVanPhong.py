class NhanVienVanPhong:
    def __init__(self, maNV, hoTen, luongCB, soNgayLamViec):
        self.maNV = maNV
        self.hoTen = hoTen
        self.luongCB = luongCB
        self.soNgayLamViec = soNgayLamViec

    def tinhLuong(self):
        return self.luongCB + self.soNgayLamViec * 150_000