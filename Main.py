

# PHẦN YÊU CẦU: Xây dựng 5 hàm và 2 Class
# 5 hàm: 
    # tinh_tuoi_MSSV
    # get_email_MSSV
    # tinh_thang_MSSV
    # tinh_luong_MSSV
    # tinh_thuong_MSSV
# 2 class:
    # VienChuc_TENSV
    # HopDong_HODEM

def tinh_tuoi_MSSV(namsinh):
    return 2021 - int(namsinh)
def get_email_MSSV(ten):
    s = ten.split()
    email =''
    email += s[len(s)-1]
    for i in range(len(s)-2 , -1, -1):
        email += s[i][0]
    email += '@gmail.com'
    return email

def tinh_thang_MSSV(thang , nam):
    return (2021 - int(nam))*12 - int(thang ) + 12

def tinh_luong_MSSV(month, year):
    HSL = 2.34
    LuongCoSo = 1.49  
    if (tinh_thang_MSSV(month,year)<12) :
        return HSL*0.85*LuongCoSo
    elif (tinh_thang_MSSV(month,year)>=12 and tinh_thang_MSSV(month,year)<48):
        return HSL*LuongCoSo
    else:
        HSL += (tinh_thang_MSSV(month,year)/3)*0.33 
        return HSL*LuongCoSo

def tinh_thuong_MSSV(month,year,finish_level):
    if (tinh_thang_MSSV(month,year)<12):
        return 0
    else:
        HSThuong = 0
        if (finish_level == 1):
            HSThuong = 0.8
        elif (finish_level == 2):
            HSThuong = 1
        elif (finish_level == 3):
            HSThuong = 1.2
        else:
            HSThuong = 1.5
        return tinh_luong_MSSV(month,year)*HSThuong

class HopDong_HODEM:
    def __init__(self, month, year, type):
        self.month = month  #tháng gia nhập
        self.year = year    #năm gia nhập
        self.type = type    #loại hợp đồng (tập sự/chính thức/vô thời hạn)

class VienChuc_TENSV:
    
    def __init__(self, ten, namsinh, gioitinh, hopdong):
        self.ten = ten
        self.namsinh = namsinh
        self.gioitinh = gioitinh
        self.email = get_email_MSSV(self.ten)
        self.tuoi = tinh_tuoi_MSSV(self.namsinh)
        self.hopdong = hopdong
    def __str__(self):
        return self.ten +" "+ self.namsinh +" "+self.gioitinh +" "+str(self.hopdong.month)
     

 # ví dụ
# vc2 = VienChuc_TENSV("giang the an", "1999", "nam")
# vc3 = VienChuc_TENSV("pho long an", "2003", "nam")



    
# PHẦN THAO TÁC:

    #Phần 1: Nhập liệu
vc1 = VienChuc_TENSV("pham minh thang", "2001", "nam", HopDong_HODEM(2,2001,""))

    #Phần 2, #Phần 3:
lst = []
lst.append(vc1)
# lst.append(vc2)
# lst.append(vc3)
lst.sort(key=lambda x : x.namsinh,reverse= True) # sắp xếp theo độ tuổi giảm dần
for i in lst:
    print (i)

    #Phần 4:

    #Phần 5:
    





# Sap xep dua theo do tuoi 
# input(arr)
# output(arr da sap xep)

# Top K
# input(array)
# output( (array 2 luu K ptu lon nhat cua array)