"""Yil berilgan. kabisa yili deb 4 ga karrali yillarga aytiladi. Lekin 100 ga karrali yillar ichida faqat 400 ga karrali
bo'lganlari kabisa yili hisoblanadi. Masalan 300, 1300 va 1900 kabisa yili emas. 1200 va 2000 kabisa yili."""

year = int(input("Yil kiriting: "))

check = (year % 100 == 0)
check1 = check % 400 == 0 and year % 4 == 0

print(check1)