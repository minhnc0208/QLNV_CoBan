# Bản quyền của NguyenCaoMinh_22410082
from Class.NhanVienBanHang import NhanVienBanHang
from Class.NhanVienVanPhong import NhanVienVanPhong

#Cau 1
#Ham khoi tao nhan vien
def khoiTaoNhanVien():
    danhSachNhanVien = []
    # Thêm các nhân viên vào danh sách
    # Ví dụ:
    danhSachNhanVien.append(NhanVienVanPhong("NV001", "Nguyễn Văn A", 5000000, 20))
    danhSachNhanVien.append(NhanVienBanHang("NV002", "Trần Thị B", 4000000, 100))
    # Thêm các nhân viên khác tương tự
    return danhSachNhanVien

#Cau 2
#Ham xuat thong tin nhan vien
def xuatThongTinNV(nhanVien):
    print(f"Mã NV: {nhanVien.maNV}")
    print(f"Họ và tên: {nhanVien.hoTen}")
    print(f"Lương cơ bản: {nhanVien.luongCB} VND")
    print(f"Lương hằng tháng: {nhanVien.tinhLuong()} VND")
    print("----------")

#Cau 3
#Ham tinh luong nhan vien
def tinhLuongNhanVien(danhSachNhanVien):
    print("Tính lương cho tất cả nhân viên:")
    for nhanVien in danhSachNhanVien:
        print(f"Nhân viên: {nhanVien.maNV}")
        print(f"Lương hằng tháng: {nhanVien.tinhLuong()} VND")
        print("----------")

#Cau 4
#Ham tim nhan vien theo ma nhan vien
def timNhanVienTheoMa(maNV, danhSachNhanVien):
    for nhanVien in danhSachNhanVien:
        if nhanVien.maNV == maNV:
            return nhanVien
    return None

#Cau 5
#Ham tim nhan vien co luong cao nhat
def timNVCoLuongCaoNhat(danhSachNhanVien):
    maxLuong = max(nv.tinhLuong() for nv in danhSachNhanVien)
    for nv in danhSachNhanVien:
        if nv.tinhLuong() == maxLuong:
            return nv


#Cau 6
#Ham tim nhan vien ban hang luong thap nhat
def timNVBanHangLuongThapNhat(danhSachNhanVien):
    nhanVienBanHang = [nv for nv in danhSachNhanVien if isinstance(nv, NhanVienBanHang)]
    if not nhanVienBanHang:
        return None
    minLuong = min(nv.tinhLuong() for nv in nhanVienBanHang)
    for nv in nhanVienBanHang:
        if nv.tinhLuong() == minLuong:
            return nv


#Ham xuat danh sach nhan vien
def xuatDanhSachNhanVien(danhSachNhanVien):
    for nhanVien in danhSachNhanVien:
        xuatThongTinNV(nhanVien)

#Ham tim nhan vien theo ma
def timNhanVienTheoMa(maNV, danhSachNhanVien):
    for nhanVien in danhSachNhanVien:
        if nhanVien.maNV == maNV:
            return nhanVien
    return None

#Ham tim nhan vien co luong cao nhat
def timNVCoLuongCaoNhat(danhSachNhanVien):
    maxLuong = max(nv.tinhLuong() for nv in danhSachNhanVien)
    for nv in danhSachNhanVien:
        if nv.tinhLuong() == maxLuong:
            return nv

#Ham tim nhan vien ban hang luong thap nhat
def timNVBanHangLuongThapNhat(danhSachNhanVien):
    nhanVienBanHang = [nv for nv in danhSachNhanVien if isinstance(nv, NhanVienBanHang)]
    if not nhanVienBanHang:
        return None
    minLuong = min(nv.tinhLuong() for nv in nhanVienBanHang)
    for nv in nhanVienBanHang:
        if nv.tinhLuong() == minLuong:
            return nv

#Ham main
def main():
    danhSachNhanVien = []  # Khởi tạo danh sách trống

    while True:
        print("Menu:")
        print("1. Khởi tạo danh sách nhân viên")
        print("2. Xuất thông tin của tất cả nhân viên")
        print("3. Tính lương của tất cả nhân viên")
        print("4. Tìm nhân viên theo mã nhân viên")
        print("5. Tìm nhân viên có lương hằng tháng cao nhất")
        print("6. Tìm nhân viên bán hàng có lương thấp nhất")
        print("0. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            danhSachNhanVien = khoiTaoNhanVien()
            print("Đã khởi tạo danh sách nhân viên thành công.")
        elif choice == "2":
            if not danhSachNhanVien:
                print("Danh sách nhân viên trống. Vui lòng khởi tạo danh sách trước.")
            else:
                print("\nThông tin của tất cả nhân viên:")
                for nhanVien in danhSachNhanVien:
                    xuatThongTinNV(nhanVien)
        elif choice == "3":
            if not danhSachNhanVien:
                print("Danh sách nhân viên trống. Vui lòng khởi tạo danh sách trước.")
            else:
                tinhLuongNhanVien(danhSachNhanVien)
        elif choice == "4":
            maNV = input("Nhập mã nhân viên cần tìm: ")
            nhanVien = timNhanVienTheoMa(maNV, danhSachNhanVien)
            if nhanVien:
                print("Thông tin nhân viên:")
                xuatThongTinNV(nhanVien)
            else:
                print("Không tìm thấy nhân viên có mã", maNV)
        elif choice == "5":
            if not danhSachNhanVien:
                print("Danh sách nhân viên trống. Vui lòng khởi tạo danh sách trước.")
            else:
                nvLuongCaoNhat = timNVCoLuongCaoNhat(danhSachNhanVien)
                print("\nNhân viên có lương cao nhất:")
                xuatThongTinNV(nvLuongCaoNhat)
        elif choice == "6":
            if not danhSachNhanVien:
                print("Danh sách nhân viên trống. Vui lòng khởi tạo danh sách trước.")
            else:
                nvLuongThapNhat = timNVBanHangLuongThapNhat(danhSachNhanVien)
                if nvLuongThapNhat:
                    print("\nNhân viên bán hàng có lương thấp nhất:")
                    xuatThongTinNV(nvLuongThapNhat)
                else:
                    print("Không có nhân viên bán hàng trong danh sách.")
        elif choice == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


