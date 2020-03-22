#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

dosya = input("File name... ")
dosyaadi = dosya + ".html"

baslik = input("Type page title... ")

f = open(dosyaadi, "w+")
f.write("<head>" + '<meta name="viewport" content="width=device-width">' + '<link rel="stylesheet" type="text/css" href="style.css">' + "\n" + "<title>" + baslik + "</title>" + "</head>" + "\n")

for i in range(1881):
    print("1) Add h1")
    print("2) Add p")
    print("3) Add image")
    print("4) Save")

    secim = input("Select component...")

    if secim == "1":
        h1 = input("Type h1... ")
        f.write("<h1>" + h1 + "</h1>" + "\n")
    elif secim == "2":
        p = input("Type paragraph... ")
        f.write("<p>" + p + "</p>" + "\n")
    elif secim == "3":
        adres = input("Type image address... ")
        f.write('<img src="' + adres + '" />' + "\n")
    elif secim == "4":
        f.close()
        break
    else:
        print("there is no such option.")
