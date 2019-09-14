import os
import json
import loaihanghoa
import hoadon

danhsachhanghoa=[]
def loadfile_hanghoa():
    files=os.listdir("../danhmuc")
    if "hanghoa.csv" not in files:
        return
    with open('../danhmuc/hanghoa.csv','r') as f:
        line=f.readline()
        while line:
            str_to_read=line.split(",")
            if len(str_to_read)>1:
                hanghoa={}
                hanghoa["id"]=str_to_read[0]
                hanghoa["ten"]=str_to_read[1]
                hanghoa["giaban"]=str_to_read[2]
                id_loaihh=str_to_read[3]
                if id_loaihh.endswith("\n"):
                    id_loaihh=id_loaihh[0:len(id_loaihh)-1]
                hanghoa["id_loaihanghoa"]=id_loaihh
                danhsachhanghoa.append(hanghoa)
            line=f.readline()
loadfile_hanghoa()
def tao_hanghoa():
    data={}
    data["id"]=input("Nhap id hang hoa:")
    tim_idhanghoa=kiemtra_hanghoa(id)
    if tim_idhanghoa is not None:
        print("Id hang hoa da ton tai,xin moi chon chuc nang khac")
    data["ten"]=input("Vui long nhap ten hang hoa:")
    data["giaban"]=input("Vui long nhap gia ban:")
    id_loaihanghoa=input("Vui long id loai san pham cua hang hoa:")
    id_loaihanghoa_daco=loaihanghoa.kiemtra_loaihanghoa(id_loaihanghoa)
    #trả về 1 nếu tồn tại id đó r,trả về none nếu chưa tồn tại id đó
    while id_loaihanghoa_daco is None:
        for id_loai in loaihanghoa.danhsachloaihanghoa:
            print(id_loai)
        id_loaihanghoa=input("Vui long id loai san pham cua hang hoa111:")
        id_loaihanghoa_daco=loaihanghoa.kiemtra_loaihanghoa(id_loaihanghoa)
    data["id_loaihanghoa"]=id_loaihanghoa
    danhsachhanghoa.append(data)
    with open('../danhmuc/hanghoa.csv','a') as f:
        str_to_save=data["id"]+","+data["ten"]+","+data["giaban"]+","+data["id_loaihanghoa"]+"\n"
        data=f.write(str_to_save)
def kiemtra_hanghoa(id=None):
    if id is None:
        id=input("Vui long nhap id:")
    for hanghoa in danhsachhanghoa:
        if hanghoa["id"]==id:
            return hanghoa
#end kiem tra hang hoa
def xem_hanghoa():
    print("+{:-^4}+{:-<10}+{:-<10}+{:-^10}+".format('','','',''))
    print("|{:^4}|{:^10}|{:^10}|{:^10}|".format('id','ten','giaban','id_loaihh'))
    for hanghoa in danhsachhanghoa:
        print("|{:^4}|{:^10}|{:^10}|{:^10}|".format(hanghoa["id"],hanghoa["ten"],hanghoa["giaban"],hanghoa["id_loaihanghoa"]))
    print("+{:-^4}+{:-<10}+{:-<10}+{:-^10}+".format('','','',''))
#end xem hang hoa
        
def hanghoa_banra():
    hanghoaban={}
    for hanghoa in danhsachhanghoa:
        hanghoaban[hanghoa["ten"]]=0
    for data in hoadon.danhsachhoadon:
        for data1 in data["danhsach_hanghoa"]:
            for hanghoa in danhsachhanghoa:
                if data1["ten"]==hanghoa["ten"]:
                    hanghoaban[hanghoa["ten"]]+=data1["soluong"]
    return hanghoaban
def hanghoa_banchay():
    hanghoaban=hanghoa_banra()
    # print(hanghoaban)
    gtr_max=hanghoaban[danhsachhanghoa[0]["ten"]]
    gtr_min=hanghoaban[danhsachhanghoa[0]["ten"]]
    for hh in hanghoaban:
        if gtr_max<hanghoaban[hh]:
            gtr_max=hanghoaban[hh]
        if gtr_min>hanghoaban[hh]:
            gtr_min=hanghoaban[hh]
    for hh in hanghoaban:
        if gtr_max==hanghoaban[hh]:
            print(hh+" ban dc nhieu nhat trong thang.Tong ban duoc:"+str(gtr_max))
        if gtr_min==hanghoaban[hh]:
            print(hh+" ban dc it nhat trong thang.Tong ban duoc:"+str(gtr_min))
def loaihang_bannhieu():
    loaihang_banra=[]
    hanghoaban=hanghoa_banra()
    for loai in loaihanghoa.danhsachloaihanghoa:
        loaihang={}
        loaihang["tenloai"]=loai["ten_loaihang"]
        loaihang["doanhthu"]=0
        loaihang["soluong"]=0
        for hanghoa in danhsachhanghoa:
            if loai["id"]==hanghoa["id_loaihanghoa"]:
                #kiem tra hanghoa nao co id_loai==id  cua loai hanghoa thi them vao dict cua loai hang do
                for i in hanghoaban:
                    if i==hanghoa["ten"]:
                        loaihang["doanhthu"]+=int(hanghoaban[i])*int(hanghoa["giaban"])
                        loaihang["soluong"]+=int(hanghoaban[i])
                        # hanghoaban[i] tra ve tong so luong cua hang hoa do trong hoadon
                        # print(loaihang["hanghoa"])
        loaihang_banra.append(loaihang)
    max_doanhthu=0
    max_soluong=0
    for loai in loaihang_banra:
        if max_doanhthu<loai["doanhthu"]:
            max_doanhthu=loai["doanhthu"]
        if max_soluong<loai["soluong"]:
            max_soluong=loai["soluong"]
    for loai in loaihang_banra:
        if max_doanhthu==loai["doanhthu"]:
            print(loai["tenloai"]+" co doanh thu cao nhat trong thansg voi :"+str(loai["doanhthu"]))
        if max_soluong==loai["soluong"]:
            print(loai["tenloai"] +" co so luong hang ban ra nhieu nhat trong thang:"+str(loai["soluong"]))
    # print(loaihang_banra)
