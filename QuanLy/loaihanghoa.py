import os

danhsachloaihanghoa=[]
def loadfile_loaihanghoa():
    files=os.listdir('../danhmuc')
    if "loaihanghoa.csv" not in files:
        return
    
    with open('../danhmuc/loaihanghoa.csv','r') as f:
        line=f.readline()
        while line:
            str_to_read=line.split(",")
            if len(str_to_read)>1:
                loaihanghoa={}
                loaihanghoa["id"]=str_to_read[0]
                tenloai=str_to_read[1]
                if tenloai.endswith("\n"):
                    tenloai=tenloai[0:len(tenloai)-1]
                loaihanghoa["ten_loaihang"]=tenloai
                danhsachloaihanghoa.append(loaihanghoa)
            line=f.readline()
loadfile_loaihanghoa()
#end load
def tao_loaihanghoa():
    data={}
    id=input("Nhap id loai hang hoa:")
    kiemtra_id=kiemtra_loaihanghoa(id)
    if kiemtra_id is not None:
        print("id da ton tai,xin moi chon chuc nang khac")
        return
    data["id"]=id
    data["ten_loaihang"]=input("Vui long nhap ten loai hang hoa")
    danhsachloaihanghoa.append(data)
    str_to_save=data["id"]+","+data["ten_loaihang"]+"\n"
    with open('BTL/danhmuc/loaihanghoa.csv','a') as f:
        data=f.write(str_to_save)   
# end tao_loaihanghoa()
def kiemtra_loaihanghoa(id):
    if id is None:
        id=input("Vui long nhap id loai san pham:")
    for loaihanghoa in danhsachloaihanghoa:
        if loaihanghoa["id"]==id:
            return loaihanghoa
#end kiem tra loai hang hoa
def xem_loaihh():
    print("+{:-^4}+{:-<10}+".format('',''))
    print("|{:^4}|{:^10}|".format('id','ten_loai'))
    for loai_hanghoa in danhsachloaihanghoa:
        # print(hanghoa)
        print("|{:^4}|{:^10}|".format(loai_hanghoa["id"],loai_hanghoa["ten_loaihang"]))
    print("+{:-^4}+{:-<10}+".format('',''))
#end xem loai hang hoa
def loaihang_banchay():
    banchay=[]
    for loai in danhsachloaihanghoa:
        loaihang={}
        loaihang["ten"]=loai["ten_loaihang"]
        loaihang["soluong"]=0
        banchay.append(loaihang)
    
    # print(banchay)
# loaihang_banchay()