password =""

while password!= "123456":
    password = input("masukan password:")
    
    if password!= "123456":
       print("password salah,silahkan coba lagi")
    else:
        print("password benar")
    
print("password benar,login berhasil")