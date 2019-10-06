# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:46:27 2019

@author: MERT VE YASİN
"""

print("""                 ****************************
              
                        HESAP MAKİNESİ
                 
                 ****************************""")
while True:
    sayı1 = int(input("SAYI GİRİNİZ: "))
    
    islem_seciniz = int(input("İSLEM SEÇİNİZ: ")) 
    if(islem_seciniz == 1):
        sayı2 = int(input("SAYI GİRİNİZ: ")) 
        print(sayı1+sayı2)
    
    elif(islem_seciniz == 2): 
        sayı2 = int(input("SAYI GİRİNİZ: ")) 
        print(sayı1-sayı2) 
    elif(islem_seciniz == 3):
        sayı2 = int(input("SAYI GİRİNİZ: ")) 
        print(sayı1*sayı2) 
    elif(islem_seciniz == 4):
        sayı2 = int(input("SAYI GİRİNİZ: ")) 
        print(sayı1/sayı2) 
    elif(islem_seciniz == 5):
        print("KAPANIYOR...")
        break 