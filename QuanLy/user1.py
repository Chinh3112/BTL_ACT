import re
import os
import hashlib
user_list=[]
class User():
    id_user=None
    name=None
    email=None
    password=None
    admin=None
    # phone=None
    def __init__(self,id_user,name,email,password,admin):
        self.id_user=id_user
        self.name=name
        self.password=password
        self.email=email
        self.admin=admin
        # self.phone=phone
    def dangki(self):
        user=self.id_user+","+self.name+","+self.email+","+self.password+","+self.admin+"\n"
        with open('../user/list_user.csv','a') as f:
            f.write(user)
    # def edit(self):
    #     with open('user/list_user.csv','r+') as f:

    def delete(self):
        pass
def loadfile_user():
    files=os.listdir('../user')
    if 'list_user.csv' not in files:
        print("Thu muc khong ton tai")
        return
    with open('../user/list_user.csv','r') as f:
        line=f.readline()
        while line:
            user1={}
            if line.endswith("\n"):
                line=line[0:len(line)-1]
            line=line.split(",")
            user1["id_user"]=line[0]
            user1["name"]=line[1]
            user1["password"]=line[2]
            user1["email"]=line[3]
            user1["admin"]=line[4]
            user_list.append(user1)
            line=f.readline()
loadfile_user()
def check_admin(id):
    for user in user_list:
        if id==user["id_user"]:
            return user["admin"]

def check_id(id=None):
    if id==None:
        id=print("Vui long nhap lai ID:")
    for user in user_list:
        if id==user["id_user"]:
            return id

def tao_taikhoan():
    user1={}
    id_user=input("Nhap ID cua ban:")
    check=check_id(id_user)
    while check is not None:
        id_user=input("ID da ton tai.Nhap ID khac:")
        check=check_id(id_user)
    user1["id_user"]=id_user
    user1["name"]=input("Nhap ten cua ban:")
    password=input("Nhap password:")
    re_password=input("Xac nhan lai mk:")
    while password!=re_password:
        password=input("Nhap password:")
        re_password=input("Xac nhan lai mk:")
    user1["password"]=hashlib.sha256(password.encode()).hexdigest()
    user1["email"]=input("Nhap email cua ban:")
    user1["admin"]=input("NHap quyen admin (1/0):")
    nhanvien=User(user1["id_user"],user1["name"],user1["password"],user1["email"],user1["admin"])
    nhanvien.dangki()
    print("Ban da tao tai khoan thanh cong")
    user_list.append(user1)
def check_password(id,password):
    #de kiem tra xem pass minh nhap co trung voi pass trong du lieu
    password_hash=hashlib.sha256(password.encode()).hexdigest()
    for user in user_list:
        if user["id_user"]==id:
            if user["password"]==password_hash:
                return 1
# tao_taikhoan()
def dangnhap():
    id_user=input("Hay nhap ID cua ban de dang nhap:")
    check=check_id(id_user)
    while check is None:
        id_user=input("ID chua ton tai.Nhap lai ID:")
        check=check(id_user)
    password=input("Vui long nhap mat khau cua ban:")
    check_pass=check_password(id_user,password)
    while check_pass is None:
        password=input("Sai mat khau.vui long nhap lai:")
        check_pass=check_password(id_user,password)
    print("Ban da dang nhap THANH CONG")
    for user in user_list:
        if id_user==user["id_user"]:
            return user
# dangnhap()
def sua():
    id_user=input("Nhap ID user ban muon sua:")
    check=check_id(id_user)
    while check is None:
        id_user=input("ID chua ton tai.Nhap lai:")
        check=check_id(id_user)
    for user in user_list:
        if user["id_user"]==id_user:
            print("+=============================+")
            print("|Nhap 1 de sua ten            |")
            print("|Nhap 2 de sua mat khau       |")
            print("|Nhap 3 de sua email          |")
            print("|NHap 4 de sua quyen truy cap |")
            print("|NHap E de thoat              |")
            print("+=============================+")
            x=input("Ban muon sua:")
            while x:
                if x.upper()=="1":
                    user["name"]=input("THay doi ten cua ban.Hay nhap ten moi:")
                if x.upper()=="2":
                    password=input("Thay doi mat khau cua ban.Hay nhap mat khau moi:")
                    user["password"]=hashlib.sha256(password.encode()).hexdigest()
                if x.upper()=="3":
                    user["email"]=input("THay doi email cua ban.Hay nhap email moi:")
                if x.upper()=="4":
                    user["admin"]=input("Thay doi quyen truy cap:")
                if x.upper()=="E":
                    break
                x=input("Ban muon sua:")
    print(user_list)
    with open('../user/list_user.csv','r+') as f:
        f.truncate()
    for user in user_list:
        print(user)
        nhanvien=User(user["id_user"],user["name"],user["password"],user["email"],user["admin"])
        nhanvien.dangki()
        
# sua()
def xoa():
    id_user=input("Nhap Id ban muon xoa:")
    check=check_id(id_user)
    while check is None:
        id_user=input("ID chua ton tai.Nhap lai ID ban muon xoa:")
        check=check_id(id_user)
    with open('../user/list_user.csv','r+') as f:
        f.truncate()
    i=0
    for user in user_list:
        if id_user==user["id_user"]:
            del user
            continue
        str_to_save=User(user["id_user"],user["name"],user["password"],user["email"],user["admin"])
        str_to_save.dangki()
        i=i+1
