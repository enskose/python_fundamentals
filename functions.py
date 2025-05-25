# Fonksiyonlar, kodu tekrar tekrar yazmamak için kullanılır.

#* "def" yazarak fonksiyon oluşturuyoruz.
#* Fonksiyonlara istersek dışarıdan bilgi (parametre) verebiliriz.
#* Fonksiyonlar bazen bize bir sonuç (return) döndürebilir.
'''
def fonksiyon_adi(parametre1, parametre2):
    #* Burada fonksiyonun yapmasını istediğimiz işlemleri yazıyoruz
    return parametre1 + parametre2

#* Fonksiyonu çağırırken adını ve gerekli bilgileri yazıyoruz:
sonuc = fonksiyon_adi(3, 5)
print(sonuc)  #* Burada ekrana 8 yazdırılır

'''

'''
def exponentiation_exp_2(x):
    result = x ** 2
    print("Raised to the power of 2:", result)
    return result

exponentiation_exp_2(5)
'''

'''
#* Fonksiyonlar, kodu daha düzenli ve tekrar kullanılabilir hale getirir.
def wage(w_hours):
    return w_hours * 20

def bonus(w_hours):
    return wage(w_hours) + 50

print("Wage for 8 hours:", wage(8), "Bonus:", bonus(8))

'''
#* _________________________________________________________________________________________________ *# 

'''
def plus_five(x):
    return x + 5

def m_by_3(y):
    return plus_five(y) * 3

result = m_by_3(5)
print(result)  

'''


def main():
    x = int(input("Bir sayı giriniz: "))
    print("Karesi:", square(x))
    
def square(n):
    return pow(n, 2)

main()