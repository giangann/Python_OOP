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

class VienChuc_TENSV:
    
    def __init__(self, ten, thangsinh, namsinh, gioitinh, hopdong, mucdo):
        self.ten = ten
        self.namsinh = namsinh
        self.gioitinh = gioitinh
        self.hopdong = hopdong
        self.mucdo = mucdo
        self.thangsinh = thangsinh
    tinh_tuoi_MSSV(self,thangsinh, namsinh)
    get_email_MSSV(self, ten)
    tinh_thang_MSSV(self,thangsinh, namsinh)

class HopDong_HODEM:
    pass

# Sap xep dua theo do tuoi 
# input(arr)
# output(arr da sap xep)

# Top K
# input(array)
# output( (array 2 luu K ptu lon nhat cua array)
