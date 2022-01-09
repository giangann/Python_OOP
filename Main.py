def tinh_tuoi_MSSV(namSinh):
    return 2021 - int(namSinh)
def get_email_MSSV(ten):
    s = ten.split()
    email =''
    email += s[len(s)-1]
    for i in range(len(s)-2 , -1, -1):
        email += s[i][0]
    email += '@gmail.com'
    return email

def tinh_thang_MSSV(thang , nam):
    return (2021 - int(nam))*12 - int(thang )+ 12

