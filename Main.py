from _typeshed import Self


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
    # def __init__(self,):
    #     self.
    pass

class HopDong_HODEM:
    pass
