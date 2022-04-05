print("""
**************************

KULLANICI GİRİŞİ

**************************""")
my_name="thoynk"
my_password="250917"
giris_hakki=3



while True:
    username = input("Kullanıcı Adınız:")
    password = input("Şifreniz:")


    if (username==my_name) and (password!=my_password):
        print("Şifreniz hatalı.")
        giris_hakki -= 1

    elif (username!=my_name) and (password==my_password):
        print("Hatalı kullanıcı adı.")
        giris_hakki -= 1

    elif (username!=my_name) and (password!=my_password):
        print("şifre ve kullanıcı adınız yanlış")

    elif (username == my_name) and (my_password == password):
        print("Programa başarılı bir şekilde giriş yaptınız.")
        break

    if giris_hakki==0:
        print("Giriş hakkınız bitti.")
        break
