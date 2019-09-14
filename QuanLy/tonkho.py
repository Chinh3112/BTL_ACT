import hanghoa
import os
import hoadon
# import loaihanghoa

danhsach_tonkho=[]
def load_hangtonkho():
    files=os.listdir('../danhmuc')
    if 'hangtonkho.csv' not in files:
        return
    with open('../danhmuc/hangtonkho.csv','r') as f:
        line=f.readline()
        while line:
            danhsach={}
            if line.endswith("\n"):
                line=line[0:len(line)-1]
            line=line.split(",")
            danhsach["ten"]=line[0]
            danhsach["soluong"]=line[1]
            danhsach_tonkho.append(danhsach)
            line=f.readline()
load_hangtonkho()
def update_hangtonkho():
    with open('../danhmuc/hangtonkho.csv','r+') as files:
        files.truncate()
    with open('../danhmuc/hangtonkho.csv','a') as f:
        for hang_tonkho in danhsach_tonkho:
            str_to_save=hang_tonkho["ten"]+","+str(hang_tonkho["soluong"])+"\n"
            f.write(str_to_save)

#de nhap so luong hang hoa vao kho
def nhapkho():
    ten_hanghoa=input("Nhap ten loai hang hoa ban muon nhap:")
    check=hoadon.check_tenhanghoa(ten_hanghoa)
    while check is None:
        ten_hanghoa=input("Ban NHap sai ten hang hoa.Xin moi nhap lai:")
        check=hoadon.check_tenhanghoa(ten_hanghoa)
    soluong=input("Nhap so luong hang hoa:")
    for hang_hoa in danhsach_tonkho:
        if ten_hanghoa==hang_hoa["ten"]:
            hang_hoa["soluong"]=int(soluong)+int(hang_hoa["soluong"])
    update_hangtonkho()
# nhapkho()
# print(danhsach_tonkho)
def ban_hanghoa(ten,soluong):
    #khi nhap hoa don,danh sach se tu dong tru di hang hoa do va luu vao kho
    for hang_hoa in danhsach_tonkho:
        if ten==hang_hoa["ten"]:
            hang_hoa["soluong"]=int(hang_hoa["soluong"])-int(soluong)
    update_hangtonkho()
def hanghoa_trongkho():
    print("----Danh sach hang ton kho----")
    print("+{:-^9}+{:-^20}+".format('',''))
    print("|{:^9}|{:^20}|".format('Ten','So luong con lai'))
    print("+{:-^9}+{:-^20}+".format('',''))
    for hang_hoa in danhsach_tonkho:
        print("|{:^9}|{:^20}|".format(hang_hoa["ten"],hang_hoa["soluong"]))
        print("+{:-^9}+{:-^20}+".format('',''))