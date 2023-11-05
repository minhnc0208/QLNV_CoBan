class NhanVienBanHang:
    def __init__(self, maNV, hoTen, luongCB, soSanPham):
        self.maNV = maNV
        self.hoTen = hoTen
        self.luongCB = luongCB
        self.soSanPham = soSanPham

    def tinhLuong(self):
        return self.luongCB + self.soSanPham * 18_000

