import os
import json
import datetime
import hanghoa
import customer
import tonkho

danhsachhoadon=[]
total={}
def load_hoadon():
    files=os.listdir('../danhmuc/hoadon')
    if 'hoadon.txt' not in files:
        return
    with open('../danhmuc/hoadon/hoadon.txt','r') as f:
        line=f.readline()
        total["tong_doanhthu"]=0
        total["tong_hanghoa"]=0
        while line:
            if line.endswith("\n"):
                line=line[0:len(line)-1]
            with open('../danhmuc/hoadon/'+line+'.json','r') as f1:
                data=json.load(f1)
                total["tong_doanhthu"]+=data["tongtien"]
                # print(total["tong_doanhthu"])
                for hh in data["danhsach_hanghoa"]:
                    total["tong_hanghoa"]+=hh["soluong"]
                danhsachhoadon.append(data)
            line=f.readline()
load_hoadon()


def max_HDS():
    with open('../danhmuc/hoadon/hoadon.txt','r') as f:
        line=f.readline()
        str_to_read="0000"
        while line:
            str_to_read=line.lstrip("HDS")
            # print(str_to_read)
            line=f.readline()
        str_to_read=str_to_read.lstrip("HDS")
        return str_to_read

def check_tenhanghoa(ten=None):
    if ten is None:
        ten=input("Xin moi nhap ten hang hoa:")
    for hh in hanghoa.danhsachhanghoa:
        # print(hh)
        if ten==hh["ten"]:
            return ten
# check_tenhanghoa()

def tao_hoadon():
    hoadon={}
    sohoadon=int(max_HDS())+1
    x=datetime.datetime.now()
    print("----Tao hoa don----")
    sohoadon=str(format(sohoadon,'04d'))
    hoadon["sohoadon"]=sohoadon
    hoadon["ngayhoadon"]=x.strftime("%x %X")
    hoadon["nguoimua"]=input("Hay nhap ten khach hang:")
    # luu ten khach,neu da co trong danh sach thif thoi,con neu k co trong danh sach thi luu vao
    i=1
    for ten_khach in customer.danhsach_tenkhachhang:
        if ten_khach==hoadon["nguoimua"]:
            break
        if i==len(customer.danhsach_tenkhachhang):
            customer.danhsach_tenkhachhang.append(hoadon["nguoimua"])
        i=i+1
    hoadon["tongtien_truocthue"]=0
    hoadon["thue"]=0.1
    hoadon["tongtien"]=0
    hoadon["danhsach_hanghoa"]=[]
    nhap_hanghoa=input("Ban co muon nhap hang hoa khong (y/n):")
    stt_hanghoa=1
    while nhap_hanghoa.upper()=="Y":
        danhsach_hanghoa={}
        danhsach_hanghoa["stt"]=stt_hanghoa
        stt_hanghoa+=1
        ten=input("Nhap ten hang hoa:")
        check=check_tenhanghoa(ten)
        while check is None:
            ten=input("xin moi nhap ten hang hoa:")
            check=check_tenhanghoa(ten)
        danhsach_hanghoa["ten"]=ten
        for hh in hanghoa.danhsachhanghoa:
            if hh["ten"]==ten:
                danhsach_hanghoa["donggia"]=int(hh["giaban"])
        danhsach_hanghoa["soluong"]=int(input("NHap so luong hang hoa:"))
        tonkho.ban_hanghoa(danhsach_hanghoa["ten"],danhsach_hanghoa["soluong"])
        danhsach_hanghoa["thanhtien"]=danhsach_hanghoa["soluong"]*danhsach_hanghoa["donggia"]
        hoadon["tongtien_truocthue"]+=danhsach_hanghoa["thanhtien"]
        hoadon["danhsach_hanghoa"].append(danhsach_hanghoa)
        nhap_hanghoa=input("Ban co muon nhap hang hoa khong (y/n):")
    hoadon["tongtien"]=hoadon["tongtien_truocthue"]*(1+hoadon["thue"])
    with open('../danhmuc/hoadon/hoadon.txt','a') as files:
        files.write("HDS"+hoadon["sohoadon"]+"\n")
    str_to_save="HDS"+hoadon["sohoadon"]+".json"
    with open('../danhmuc/hoadon/'+str_to_save,'w') as f:
        json.dump(hoadon,f)
    danhsachhoadon.append(hoadon)
    customer.update_khachhang()
# tao_hoadon()
def check_hoadon(filename):
    while not os.path.isfile('../danhmuc/hoadon/'+filename+'.json'):
        filename = input("nhap ten file can kiem tra:")
    return filename


def in_hoadon():
    filename=input("Nhap so hoa don ban muon xem:")
    kiemtra_hoadon=check_hoadon(filename)
    with open('../danhmuc/hoadon/'+ filename+ '.json') as f:
        data=json.load(f)
    # print(data)
    print("{:^40}".format('HOA DON MUA HANG'))
    print("So hoa don:",filename)
    print("Ngay hoa don:",data['ngayhoadon'])
    print("Khach hang:",data['nguoimua'])
    print("Tong tien truoc thue:",data['tongtien_truocthue'])
    print("Tong tien sau thue:",data['tongtien'])
    print("+{:-^9}+{:-^9}+{:-^9}+{:-^9}+{:-^9}+".format('','','','',''))
    print("|{:<9}|{:<9}|{:>9}|{:>9}|{:>9}|".format('STT','hang hoa','so luong','don gia','tong tien'))
    print("+{:-^9}+{:-^9}+{:-^9}+{:-^9}+{:-^9}+".format('','','','',''))
    for data1 in data["danhsach_hanghoa"]:
        print("|{:<9}|{:<9}|{:>9}|{:>9}|{:>9}|".format(data1["stt"],data1["ten"],data1["soluong"],data1["donggia"],data1["thanhtien"]))
        print("+{:-^9}+{:-^9}+{:-^9}+{:-^9}+{:-^9}+".format('','','','',''))
# print(danhsachhoadon)
