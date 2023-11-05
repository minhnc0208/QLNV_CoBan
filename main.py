# Bản quyền của NguyenCaoMinh_22410082
from Class.NhanVienBanHang import NhanVienBanHang
from Class.NhanVienVanPhong import NhanVienVanPhong

#Cau 1
#Ham khoi tao nhan vien
def khoiTaoNhanVien():
    danhSachNhanVien = []
    # Thêm các nhân viên vào danh sách
    # Ví dụ:
    try:
        danhSachNhanVien.append(NhanVienVanPhong("NV001", "Nguyễn Văn A", 5000000, 20))
        danhSachNhanVien.append(NhanVienBanHang("NV002", "Trần Thị B", 4000000, 100))
        danhSachNhanVien.append(NhanVienBanHang("NV003", "Nguyễn Cao Minh", 6000000, 800))
    except Exception as e:
        print(f"Có lỗi xảy ra trong lúc khởi tạo: {e}")
    # Thêm các nhân viên khác tương tự
    return danhSachNhanVien

#Cau 2
#Ham dem so luong nhan vien duoc xuat thanh cong
def xuatDanhSachNhanVien(danhSachNhanVien):
    count = 0 #Bien dem so luong nhan vien duoc xuat thanh cong
    try:
        print("\nThông tin của tất cả nhân viên:")
        for nhanVien in danhSachNhanVien:
            xuatThongTinNV(nhanVien)
            count += 1  # Tăng biến đếm sau mỗi lần xuất thông tin
    except Exception as e:
        print(f"Có lỗi xảy ra khi xuất danh sách nhân viên: {e}")
    else:
        print(f"Tổng số nhân viên được xuất: {count}")

#Ham xuat thong tin nhan vien
def xuatThongTinNV(nhanVien):
    try:
        print(f"Mã NV: {nhanVien.maNV}")
        print(f"Họ và tên: {nhanVien.hoTen}")
        print(f"Lương cơ bản: {nhanVien.luongCB} VND")
        print(f"Lương hằng tháng: {nhanVien.tinhLuong()} VND")
        print("----------")
    except Exception as e:
        print(f"Có lỗi xảy ra khi xuất thông tin nhân viên: {e}")

#Cau 3
#Ham tinh luong nhan vien
def tinhLuongNhanVien(danhSachNhanVien):
    try:
        print("Tính lương cho tất cả nhân viên:")
        for nhanVien in danhSachNhanVien:
            print(f"Nhân viên: {nhanVien.maNV}")
            print(f"Lương hằng tháng: {nhanVien.tinhLuong()} VND")
            print("----------")
    except Exception as e:
        print(f"Có lỗi xảy ra khi tính lương nhân viên: {e}")

#Cau 4
#Ham tim nhan vien theo ma nhan vien
def timNhanVienTheoMa(maNV, danhSachNhanVien):
    count = 0
    try:
        for nhanVien in danhSachNhanVien:
            if nhanVien.maNV == maNV:
                count += 1  # Tăng biến đếm sau mỗi lần tìm thấy nhân viên
                return nhanVien
        return None
    except Exception as e:
        print(f"Có lỗi xảy ra khi tìm nhân viên theo mã: {e}")
    return None

#Cau 5
#Ham tim nhan vien co luong cao nhat
def timNVCoLuongCaoNhat(danhSachNhanVien):
    try:
        maxLuong = max(nv.tinhLuong() for nv in danhSachNhanVien)
        for nv in danhSachNhanVien:
            if nv.tinhLuong() == maxLuong:
                return nv
    except Exception as e:
        print(f"Có lỗi xảy ra khi tìm nhân viên có lương cao nhất: {e}")
        return None

#Cau 6
#Ham tim nhan vien ban hang luong thap nhat
def timNVBanHangLuongThapNhat(danhSachNhanVien):
    try:
        nhanVienBanHang = [nv for nv in danhSachNhanVien if isinstance(nv, NhanVienBanHang)]
        if not nhanVienBanHang:
            return None
        minLuong = min(nv.tinhLuong() for nv in nhanVienBanHang)
        for nv in nhanVienBanHang:
            if nv.tinhLuong() == minLuong:
                return nv
    except Exception as e:
        print(f"Có lỗi xảy ra khi tìm nhân viên bán hàng có lương thấp nhất: {e}")
        return None

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
                xuatDanhSachNhanVien(danhSachNhanVien)
        elif choice == "3":
            if not danhSachNhanVien:
                print("Danh sách nhân viên trống. Vui lòng khởi tạo danh sách trước.")
            else:
                tinhLuongNhanVien(danhSachNhanVien)
        elif choice == "4":
            if not danhSachNhanVien:
                print("Danh sách nhân viên trống. Vui lòng khởi tạo danh sách trước.")
            else:
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
                if nvLuongCaoNhat:
                    print("\nNhân viên có lương cao nhất:")
                    xuatThongTinNV(nvLuongCaoNhat)
                else:
                    print("Không tìm thấy nhân viên nào.")
        elif choice == "6":
            if not danhSachNhanVien:
                print("Danh sách nhân viên trống. Vui lòng khởi tạo danh sách trước.")
            else:
                nvLuongThapNhat = timNVBanHangLuongThapNhat(danhSachNhanVien)
                if nvLuongThapNhat:
                    print("\nNhân viên bán hàng có lương thấp nhất:")
                    xuatThongTinNV(nvLuongThapNhat)
                else:
                    print("Không tìm thấy nhân viên bán hàng nào trong danh sách.")
        elif choice == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
