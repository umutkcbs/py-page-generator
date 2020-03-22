#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

dosya = input("Dosya ismi giriniz... ")
dosyaadi = dosya + ".html"

baslik = input("Sayfa basligini giriniz... ")

f = open(dosyaadi, "w+")
f.write("<head>" + '<meta name="viewport" content="width=device-width">' + '<link rel="stylesheet" type="text/css" href="style.css">' + "\n" + "<title>" + baslik + "</title>" + "</head>" + "\n")

for i in range(1881):
    print("1) Buyuk metin ekle")
    print("2) Ufak metin ekle")
    print("3) Resim ekle")
    print("4) Sonlandir")

    secim = input("Eklenecek bileseni seciniz...")

    if secim == "1":
        h1 = input("Buyuk basligi giriniz... ")
        f.write("<h1>" + h1 + "</h1>" + "\n")
    elif secim == "2":
        p = input("Ufak metni giriniz... ")
        f.write("<p>" + p + "</p>" + "\n")
    elif secim == "3":
        adres = input("Resim adresini giriniz... ")
        f.write('<img src="' + adres + '" />' + "\n")
    elif secim == "4":
        f.close()
        break
    else:
        print("Lutfen gecerli bir secenek giriniz.")
