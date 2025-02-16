def user_info(ism,familiya,tyil,tjoy,email='',telraqam='',joriyyil=2024):
   """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili,
   tug'ilgan joyi, email manzili va telefon raqamini qabul qilib,
   lug'at ko'rinishida qaytaruvchi funksiya yozing.
   Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling
   (masalan, tel.raqam, el.manzil)
   Yuqoridagi funksiyani while yordamida bir necha bor chaqiring,
   va mijozlar degan ro'yxatni shakllantiring.
   Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
   """
   user = {
   'ism':ism,
   'familiya':familiya,
   'tyil':tyil,
   'tjoy':tjoy,
   'email':email,
   'telraqam':telraqam,
   'yosh':joriyyil-tyil
   }
   return user

#create while loop which is collect klient info
mijozlar = []
while True:
   print("Klient malumotlarini kiriting:\n>>>")
   m_ism = input("Mijoz ismini kiriting:\n>>>").lower()
   m_familiya = input("Mijoz familiyasini kiriting:\n>>>").lower()
   m_tyil = int(input("Mijoz tugilgan yilini kiriting:\n>>>"))
   m_tjoy = input("Mijoz tugilgan joyini kiriting:\n>>>").lower()
   m_email = input("Mijoz emailini kiriting:\n>>>").lower()
   m_telraqam = input("Mijoz tel raqamini kiriting:\n>>>")
   mijozlar.append(user_info(m_ism,m_familiya,m_tyil,m_tjoy,m_email,m_telraqam))
   javob = input("yana mijoz qoshasizmi?(ha/yo'q)\n>>>").lower()
   if javob != 'ha':
      break
   else: continue

print("\n\nBizning mijozlar:\n>>>")
n = len(mijozlar)
for r in range(n):
   n=mijozlar[r]['ism'].upper()
   sn=mijozlar[r]['familiya'].upper()
   ty=mijozlar[r]['tyil']
   tj=mijozlar[r]['tjoy'].title()
   age=mijozlar[r]['yosh']
   e_mail = mijozlar[r]['email']
   teln=mijozlar[r]['telraqam']
   print(f"{n} {sn} - {ty}da {tj}da tug'ilgan. \nHozirda {age} yoshda.\nEmaili:{e_mail},Telefon raqami - {teln}")
