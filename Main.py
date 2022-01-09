


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
    
    def __init__(self, ten, namsinh, gioitinh):
        self.ten = ten
        self.namsinh = namsinh
        self.gioitinh = gioitinh
        self.email = get_email_MSSV(self.ten)
        self.tuoi = tinh_tuoi_MSSV(self.namsinh)
    def __str__(self):
        return self.ten +" "+ self.namsinh +" "+self.gioitinh
     
vc1 = VienChuc_TENSV("pham minh thang", "2001", "nam")
vc2 = VienChuc_TENSV("giang the an", "2002", "nam")
vc3 = VienChuc_TENSV("pho long an", "2003", "nam")

lst = []
lst.append(vc1)
lst.append(vc2)
lst.append(vc3)
lst.sort(key=lambda x : x[1],reverse= False)
for i in lst:
    print (i)
class HopDong_HODEM:
    pass
# Sap xep dua theo do tuoi 
# input(arr)
# output(arr da sap xep)

# Top K
# input(array)
# output( (array 2 luu K ptu lon nhat cua array)