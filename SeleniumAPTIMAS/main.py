import xlutils
import os
import APTIMAS

name=[0] * 3
address=[0] * 3
city=[0] * 3
zip_code=[0] * 3
province=[0] * 3


202
print ("Masukan tanggal Dibuat : (format 2020-01-12)")
date=input()

print("Untuk Berapa Orang ? (masukan angka)")
people=int(input())
for x in range (people):
    print (x)
    print ("Masukan Nama : ")
    name[x]=input()
    print("Masukan Alamat : ")
    address[x]=input()
    print("Masukan Kota : ")
    city[x]=input()
    print("Masukan Kode Pos :  (Wajib Angka !!!) ")
    zip_code[x]=input()
    print("Masukan Provinsi : (Wajib Huruf Kecil !!!)")
    province[x]=input()

print ("Masukan username APTIMAS anda: ")
username=input()
print ("Masukan password APTIMAS anda: ")
password=input()

#path ='SeleniumAPTIMAS/aptimas.xlsx'

path=os.getcwd()+"/Aptimas.xlsx"

jalan=APTIMAS.aptims(date, name, address, city, zip_code, province, people, username, password, path)
jalan.aptimas()
jalan.isian()
jalan.web()
jalan.permohonan_baru()
jalan.data_pencipta()
jalan.pemegang_hak_cipta()
jalan.lampiran()
jalan.status()
jalan.billing()