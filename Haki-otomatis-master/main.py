import Haki


name=[0] * 3
address=[0] * 3
city=[0] * 3
zip_code=[0] * 3
province=[0] * 3


print ("Masukan Judul : ")
title=input()
print ("Masukan deskripsi : ")
decription=input()
print ("Masukan tanggal Dibuat : (format 2020-01-12)")
date=input()

print("Untuk Berapa Orang ?")
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
 
jalan=Haki.EHaki(title, decription, date, name, address, city, zip_code, province, people)
jalan.web()
jalan.permohonan_baru()
jalan.data_pencipta()
jalan.pemegang_hak_cipta()
jalan.lampiran()