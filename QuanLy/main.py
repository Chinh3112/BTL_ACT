import loaihanghoa
import hanghoa
import hoadon
import user1
import customer
import tonkho

def menu_hanghoa():
    while True:
        print("=================MENU================+")
        print("|Chon THH de tao hang hoa            |")
        print("|Chon XHH de xem hang hoa            |")
        print("|Chon TLH de tao loai hang hoa       |")
        print("|Chon XLH de xem loai hang hoa       |")
        print("|Chon C de tao hoa don               |")
        print("|Chon D de nhap hang hoa vao kho     |")
        print("|Chon R de xem thong tin hoa don     |")
        print("|Chon TK de xem thong ke             |")
        print("=====================================+")
        # end menu
        x=input("=> chon chuc nang:")
        print("=> ban da chon chuc nang:",x)
        if x.upper()=="D":
            tonkho.nhapkho()
        if x.upper() == 'TLH':
            loaihanghoa.tao_loaihanghoa()
        if x.upper()=='THH':
            hanghoa.tao_hanghoa()
        if x.upper()=='XHH':
            hanghoa.xem_hanghoa()
        if x.upper()=='XLH':
            loaihanghoa.xem_loaihh()
        if x.upper()=='C':
            hoadon.tao_hoadon()
        if x.upper()=='R':
            hoadon.in_hoadon()
        if x.upper()=='TK':
            while True:
                print("+============================================================+")
                print("|Chon T de tinh tong doanh thu                               |")
                print("|CHon A de tinh tong hang hoa ban ra                         |")
                print("|Chon BC de xem hang hoa ban nhanh va cham nhat trong thang  |")
                print("|Chon KH de xem khach hang nao mua nhieu nhat                |")
                print("|Chon LH de xem loai hang nao ban nhieu nhat                 |")
                # print("|Chon DTN de xem ngay nao co doanh thu nhieu nhat trong thang|")
                print("|CHon K de xem hang hoa nao con ton trong kho                 ")
                print("|Chon E de thoat khoi thong ke                               |")
                print("+============================================================+")
                y=input("Nhap thong ke ban muon:")
                print("ban da chon chuc nang "+y)
                if y.upper()=="K":
                    tonkho.hanghoa_trongkho()
                if y.upper()=='T':
                    print("Tong doanh thu:",hoadon.total["tong_doanhthu"])
                if y.upper()=='A':
                    print("Tong hang hoa ban ra:",hoadon.total["tong_hanghoa"])
                if y.upper()=='BC':
                    hanghoa.hanghoa_banchay()
                if y.upper()=='LH':
                    hanghoa.loaihang_bannhieu()
                if y.upper()=="KH":
                    customer.khach_vip()
                if y.upper()=='E':
                    break
        if x.upper()=='E':
            break
def main():
    while True:
        print("Xin chao ! Vui long dang nhap:")
        seller=user1.dangnhap()
        # print(seller)
        if seller is not None:
            while True:
                print("+=================================+")
                print("|Nhap DK de tao tai khoan         |")
                print("|Nhap ED de sua tai khoan user    |")
                print("|Nhap DE de xoa tai khoan         |")
                print("|Nhap HH de lam viec voi hang hoa |")
                print("|Nhap E de thoat                  |")
                print("+=================================+")
                x=input("Chon chuc nang:")
                print("Ban da cho chuc nang "+x)
                if x.upper()=="DK":
                    check_adm=user1.check_admin(seller["admin"])
                    if check_adm is None:
                        print("Ban chua duoc cap quyen de su dung chuc nang nay.Vui long chon chuc nang khac")
                    else:
                        user1.tao_taikhoan()
                if x.upper()=="ED":
                    check_adm=user1.check_admin(seller["admin"])
                    if check_adm is None:
                        print("Ban chua duoc cap quyen de su dung chuc nang nay.Vui long chon chuc nang khac")
                    else:
                        user1.sua()
                if x.upper()=="DE":
                    check_adm=user1.check_admin(seller["admin"])
                    if check_adm is None:
                        print("Ban chua duoc cap quyen de su dung chuc nang nay.Vui long chon chuc nang khac")
                    else:
                        user1.xoa()
                if x.upper()=="HH":
                    menu_hanghoa()
                if x.upper()=="E":
                    break
        d=input("De dang xuat.Nhap Exit de dang xuat.")
        if d.upper()=="D":
            print("Tam biet! Hen gap lai.")
            return
main()