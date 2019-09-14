import json
# print(1)
danhsachkhachhang=[]
danhsach_tenkhachhang=[]
class Customer():
    id_customer=None
    ten=None
    tongtien_thanhtoan=None
    soluong=None
    tiemnang=None
    def __init__(self,id_customer,ten,tongtien_thanhtoan,soluong,tiemnang):
        self.id_customer=id_customer
        self.ten=ten
        self.tongtien_thanhtoan=tongtien_thanhtoan
        self.soluong=soluong
        self.tiemnang=tiemnang
    def save(self):
        with open('../user/customer.csv','a') as f:
            str_to_save=self.id_customer+","+self.ten+","+self.tongtien_thanhtoan+","+self.soluong+","+self.tiemnang+"\n"
            f.write(str_to_save)
def load_khachhang():
    with open('../user/customer.csv','r') as f:
        line=f.readline()
        while line:
            khach={}
            if line.endswith("\n"):
                line=line[0:len(line)-1]
            line=line.split(",")
            khach["id_customer"]=line[0]
            khach["ten"]=line[1]
            danhsach_tenkhachhang.append(khach["ten"])
            khach["tongtien_thanhtoan"]=line[2]
            khach["soluong"]=line[3]
            khach["tiemnang"]=line[4]
            danhsachkhachhang.append(khach)
            line=f.readline()
load_khachhang()
# print(danhsach_tenkhachhang)
def update_khachhang():
    # print(1)
    list_khach=[]
    i=0
    for khachhang in danhsach_tenkhachhang:
        khach={}
        khach["id_customer"]=i
        i+=1
        khach["ten"]=khachhang
        khach["tongtien_thanhtoan"]=0
        khach["soluong"]=0
        khach["tiemnang"]=0
        list_khach.append(khach)
    # print(list_khach)
    with open('../user/customer.csv','r+') as f1:
        f1.truncate()
    danhsachkhachhang.clear()
    for khachhang in list_khach:
        with open('../danhmuc/hoadon/hoadon.txt','r') as f2:
            line=f2.readline()
            while line:
                line=line[0:len(line)-1]
                with open('../danhmuc/hoadon/'+line+'.json','r') as files:
                    data=json.load(files)
                    if data["nguoimua"]==khachhang["ten"]:
                        khachhang["tongtien_thanhtoan"]+=data["tongtien"]
                        if khachhang["tongtien_thanhtoan"]>500000:
                            khachhang["tiemnang"]=1
                        for hanghoa in data["danhsach_hanghoa"]:
                            khachhang["soluong"]+=hanghoa["soluong"]
                    # for danhsach_hanghoa in data["danhsach_hanghoa"]:
                line=f2.readline()
        danhsachkhachhang.append(khachhang)
        customer=Customer(str(khachhang["id_customer"]),khachhang["ten"],str(khachhang["tongtien_thanhtoan"]),str(khachhang["soluong"]),str(khachhang["tiemnang"]))
        customer.save()
# update_khachhang()
def khach_vip():
    update_khachhang()
    tongtien_max=danhsachkhachhang[0]["tongtien_thanhtoan"]
    soluong_max=danhsachkhachhang[0]["soluong"]
    for khachhang in danhsachkhachhang:
        if tongtien_max<khachhang["tongtien_thanhtoan"]:
            tongtien_max=khachhang["tongtien_thanhtoan"]
        if soluong_max<khachhang["soluong"]:
            soluong_max=khachhang["soluong"]
    for khachhang in danhsachkhachhang:
        if tongtien_max==khachhang["tongtien_thanhtoan"]:
            print(khachhang["ten"]+" tro thanh khach hang thanh toan nhieu nhat voi:"+str(khachhang["tongtien_thanhtoan"]))
        if soluong_max==khachhang["soluong"]:
            print(khachhang["ten"]+" tro thanh khach hang mua nhieu luong hang nhat voi:"+str(khachhang["soluong"]))
    