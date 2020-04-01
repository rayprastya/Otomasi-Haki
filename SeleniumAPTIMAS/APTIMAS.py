from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import XLUtils
import numpy as np
import time
import os

from utils import get_project_root


rootPath = os.path.abspath(get_project_root())
usernameInput = ''
passwordInput = ''

print ("Masukan username : ")
usernameInput=input()
print ("Masukan password : ")
passwordInput=input()

# In[contoh user login]
# if usernameInput == '':
#     usernameInput = '0416048803'
# if passwordInput == '':
#     passwordInput = 'poltekpos2019'

driver = webdriver.Chrome()
driver.get('https://aptimas.poltekpos.ac.id/login')

#Rubah Username dan pass sesuai Dosennya masing masing
#Ini menggunakan Akun Pak Fachri
username = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[1]/input')
username.send_keys(usernameInput)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(passwordInput)
#-------------------------------------------------------

login = driver.find_element_by_xpath('//*[@id="loginBtn"]')
login.click()

haki = driver.find_element_by_xpath('//*[@id="haki"]/a')
haki.click()

time.sleep(2)
pengajuan = driver.find_element_by_xpath('//*[@id="hakcipta"]/a')
pengajuan.click()

jenishaki = driver.find_element_by_xpath('//*[@id="select2-jenis_haki-container"]')
jenishaki.click()

#Pilih Salah Satu
time.sleep(2)
jenishakibuku = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
jenishakibuku.send_keys('Buku' u'\ue007')

#time.sleep(2)
#jenishakiprogram = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
#jenishakiprogram.send_keys('Program Komputer' u'\ue007')
#-----------------------------------------------------------------------

path='SeleniumAPTIMAS/aptimas.xlsx'

rows=XLUtils.getRowCount(path,'Sheet1')

count = 0

for r in range(2,rows+1):
    judul=XLUtils.readData(path,"Sheet1",r,1)
    uraian=XLUtils.readData(path,"Sheet1",r,2)
    tanggal=XLUtils.readData(path,"Sheet1",r,3)
    negara=XLUtils.readData(path,"Sheet1",r,4)
    kota=XLUtils.readData(path,"Sheet1",r,5)
    keterangan=XLUtils.readData(path,"Sheet1",r,6)
    fileciptaan=XLUtils.readData(path,"Sheet1",r,7)
    ktp=XLUtils.readData(path,"Sheet1",r,8)
    pernyataan=XLUtils.readData(path,"Sheet1",r,9)
    pengalihan=XLUtils.readData(path,"Sheet1",r,10)
    alamat=XLUtils.readData(path,"Sheet1",r,11)

    if judul:
        driver.find_element_by_xpath('//*[@id="judul"]').send_keys(judul)
        driver.find_element_by_xpath('//*[@id="uraian_singkat"]').send_keys(uraian)
        driver.find_element_by_xpath('//*[@id="tgl_pertama_umumkan"]').send_keys(tanggal)
        driver.find_element_by_xpath('//*[@id="negara_pertama_umumkan"]').send_keys(negara)
        driver.find_element_by_xpath('//*[@id="kota_pertama_umumkan"]').send_keys(kota)
        driver.find_element_by_xpath('//*[@id="keterangan"]').send_keys(keterangan)

        uploadfileciptaan = driver.find_element_by_xpath('//*[@id="file_ciptaan"]')
        uploadfileciptaan.send_keys(str(rootPath) + "/SeleniumAPTIMAS/FileCiptaan/"+str(fileciptaan)+".pdf")

        uploadktp = driver.find_element_by_xpath('//*[@id="ktp"]')
        uploadktp.send_keys(str(rootPath) + "/SeleniumAPTIMAS/FileKTP/"+str(ktp)+".pdf")

        uploadpernyataan = driver.find_element_by_xpath('//*[@id="file_pernyataan"]')
        uploadpernyataan.send_keys(str(rootPath) + "/SeleniumAPTIMAS/FilePernyataan/"+str(pernyataan)+".pdf")

        uploadpengalihan = driver.find_element_by_xpath('//*[@id="file_pengalihan"]')
        uploadpengalihan.send_keys(str(rootPath) + "/SeleniumAPTIMAS/FilePengalihan/"+str(pengalihan)+".pdf")

        driver.find_element_by_xpath('//*[@id="team1"]/div[2]/div/input').send_keys(alamat)

        kirim = driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div/div[1]/div/div[2]/form/button')
        kirim.click()

# haki = driver.find_element_by_xpath('//*[@id="haki"]/a')
# haki.click()

# pengajuan = driver.find_element_by_xpath('//*[@id="hakcipta"]/a')
# pengajuan.click()

exec(open("./Haki-otomatis-master/main.py").read()) 

