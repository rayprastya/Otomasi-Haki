from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import XLUtils
import numpy as np
from time import sleep
import os
from src.utils import get_project_root

class aptims(object):
    def __init__(self, date, name, address, city, zip_code, province, people, username, password, path):
        self.driver = webdriver.Chrome()
        #self.title = title
        #self.description = description
        self.date = date 
        self.name = name 
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.province = province
        self.people = people
        #self.rootPath = os.path.abspath(get_project_root())
        self.username = username
        self.password = password
        self.path = path

#usernameInput = ''
#passwordInput = ''

#print ("Masukan username APTIMAS anda: ")
#username=input()
#print ("Masukan password APTIMAS anda: ")
#password=input()

## In[contoh user login]
## if usernameInput == '':
##     usernameInput = '0416048803'
## if passwordInput == '':
##     passwordInput = 'poltekpos2019'
    def aptimas(self):
        self.driver.get('https://aptimas.poltekpos.ac.id/login')

#driver = webdriver.Chrome()
#driver.get('https://aptimas.poltekpos.ac.id/login')

#Rubah Username dan pass sesuai Dosennya masing masing
#Ini menggunakan Akun Pak Fachri
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[1]/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
#-------------------------------------------------------

        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="haki"]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="hakcipta"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="select2-jenis_haki-container"]').click()

#Pilih Salah Satu
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('Buku' u'\ue007')

#time.sleep(2)
#jenishakiprogram = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
#jenishakiprogram.send_keys('Program Komputer' u'\ue007')
#-----------------------------------------------------------------------
    def isian(self):

        rows=XLUtils.getRowCount(self.path,'Sheet1')

        count = 0

        for r in range(2,rows+1):
            judul=XLUtils.readData(self.path,"Sheet1",r,1)
            uraian=XLUtils.readData(self.path,"Sheet1",r,2)
            tanggal=XLUtils.readData(self.path,"Sheet1",r,3)
            negara=XLUtils.readData(self.path,"Sheet1",r,4)
            kota=XLUtils.readData(self.path,"Sheet1",r,5)
            keterangan=XLUtils.readData(self.path,"Sheet1",r,6)
            fileciptaan=XLUtils.readData(self.path,"Sheet1",r,7)
            ktp=XLUtils.readData(self.path,"Sheet1",r,8)
            pernyataan=XLUtils.readData(self.path,"Sheet1",r,9)
            pengalihan=XLUtils.readData(self.path,"Sheet1",r,10)
            alamat=XLUtils.readData(self.path,"Sheet1",r,11)

            if judul:
                self.driver.find_element_by_xpath('//*[@id="judul"]').send_keys(judul)
                self.driver.find_element_by_xpath('//*[@id="uraian_singkat"]').send_keys(uraian)
                self.driver.find_element_by_xpath('//*[@id="tgl_pertama_umumkan"]').send_keys(tanggal)
                self.driver.find_element_by_xpath('//*[@id="negara_pertama_umumkan"]').send_keys(negara)
                self.driver.find_element_by_xpath('//*[@id="kota_pertama_umumkan"]').send_keys(kota)
                self.driver.find_element_by_xpath('//*[@id="keterangan"]').send_keys(keterangan)

                self.driver.find_element_by_xpath('//*[@id="file_ciptaan"]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileCiptaan/"+str(fileciptaan)+".pdf")

                self.driver.find_element_by_xpath('//*[@id="ktp"]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileCiptaan/"+str(fileciptaan)+".pdf")

                self.driver.find_element_by_xpath('//*[@id="file_pernyataan"]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileCiptaan/"+str(fileciptaan)+".pdf")

                self.driver.find_element_by_xpath('//*[@id="file_pengalihan"]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileCiptaan/"+str(fileciptaan)+".pdf")

                self.driver.find_element_by_xpath('//*[@id="team1"]/div[2]/div/input').send_keys("alamat")

                self.driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div/div[1]/div/div[2]/form/button').click()

                        # haki = driver.find_element_by_xpath('//*[@id="haki"]/a')
                        # haki.click()

        # pengajuan = driver.find_element_by_xpath('//*[@id="hakcipta"]/a')
        # pengajuan.click()

                #exec(open("./Haki-otomatis-master/main.py").read()) 

                #driver = webdriver.Chrome()
                #driver.get('https://e-hakcipta.dgip.go.id/login')

                #username = driver.find_element_by_name('username')
                #username.send_keys('awangga@poltekpos.ac.id')

                #password = driver.find_element_by_name('password')
                #password.send_keys('sayaakuirollyituganteng')

                #btn = driver.find_element_by_xpath('//*[@id="login-form"]/button')
                #btn.click()

      
    def web(self):
        self.driver.get('https://e-hakcipta.dgip.go.id/login')
        sleep(1)
        self.driver.find_element_by_name('username').send_keys("awangga@poltekpos.ac.id")
        sleep(1)
        self.driver.find_element_by_name('password').send_keys('sayaakuirollyituganteng')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
        

    def permohonan_baru(self):
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/div/ul/li[1]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/div/ul/li[1]/ul/li[1]').click()
        sleep(2)
        self.driver.find_elements_by_class_name('close')[-1].click()
        sleep(2)
        self.driver.find_elements_by_class_name('select2-selection__rendered')[0].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-results__option')[1].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-selection__rendered')[1].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-results__option')[1].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-selection__rendered')[2].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-results__option')[4].click()
        sleep(1)

        date = self.driver.find_element_by_xpath('//*[@id="createform"]/div[1]/div[2]/div/div[6]/div/div/input[1]')

        date.click()
        
        for i in range(len(date.get_attribute('value'))):
            date.send_keys(Keys.BACKSPACE)

        date.send_keys(self.date, Keys.ENTER)

        #sleep(1)
        #self.driver.find_element_by_name('announced_city').send_keys("Bandung")

    def data_pencipta(self):
        # self.permohonan_baru()
        # self.driver.get('https://e-hakcipta.dgip.go.id/index.php/register/hakcipta')
        # sleep(2)
        # self.driver.find_elements_by_class_name('close')[-1].click()
        # sleep(2)
        for x in range (self.people):

            self.driver.find_element_by_xpath('//*[@id="createform"]/div[3]/div[1]/div[2]/a').click()
            sleep(1)
            self.driver.find_element_by_name("name").send_keys(self.name[x])
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[3]/div/textarea').send_keys(self.address[x])
            sleep(1)
            self.driver.find_element_by_name('city').send_keys(self.city[x])
            sleep(1)
            self.driver.find_element_by_name('zip_code').send_keys(self.zip_code[x])
            sleep(1)
            
            self.driver.find_element_by_name('province').click()
            sleep(1)
            if self.province[x] == "jawa barat" :
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[11]').click()
                sleep(1)
            elif self.province[x] == "bali":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[2]').click()
                sleep(1)
            elif self.province[x] == "bangka belitung":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[3]').click()
                sleep(1)
            elif self.province[x] == "banten":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[4]').click()
                sleep(1)
            elif self.province[x] == "bengkulu":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[5]').click()
                sleep(1)
            elif self.province[x] == "di aceh":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[6]').click()
                sleep(1)
            elif self.province[x] == "di yogyakarta":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[7]').click()
                sleep(1)
            elif self.province[x] == "dki jakarta":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[8]').click()
                sleep(1)
            elif self.province[x] == "gorontalo":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[9]').click()
                sleep(1)
            elif self.province[x] == "jambi":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[10]').click()
                sleep(1)
            elif self.province[x] == "jawa tengah":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[12]').click()
                sleep(1)
            elif self.province[x] == "jawa timur":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[13]').click()
                sleep(1)
            elif self.province[x] == "kalimantan barat":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[14]').click()
                sleep(1)
            elif self.province[x] == "kalimantan selatan":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[15]').click()
                sleep(1)
            elif self.province[x] == "kalimantan tengah":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[16]').click()
                sleep(1)
            elif self.province[x] == "kalimantan timur":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[17]').click()
                sleep(1)
            elif self.province[x] == "kalimantan utara":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[18]').click()
                sleep(1)
            elif self.province[x] == "kepulauan riau":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[19]').click()
                sleep(1)
            elif self.province[x] == "lampung":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[20]').click()
                sleep(1)
            elif self.province[x] == "maluku":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[21]').click()
                sleep(1)
            elif self.province[x] == "maluku utara":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[22]').click()
                sleep(2)
            elif self.province[x] == "nusa tenggara barat":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[23]').click()
                sleep(1)
            elif self.province[x] == "nusa tenggara timur":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[24]').click()
                sleep(1)
            elif self.province[x] == "papua":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[25]').click()
                sleep(1)
            elif self.province[x] == "papua barat":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[26]').click()
                sleep(1)
            elif self.province[x] == "riau":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[27]').click()
                sleep(1)
            elif self.province[x] == "sulawesi barat":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[28]').click()
                sleep(1)
            elif self.province[x] == "sulawesi selatan":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[29]').click()
                sleep(1)
            elif self.province[x] == "sulawesi tengah":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[30]').click()
                sleep(1)
            elif self.province[x] == "sulawesi tenggara":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[31]').click()
                sleep(1)    
            elif self.province[x] == "sulawesi utara":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[32]').click()
                sleep(1)
            elif self.province[x] == "sumatera barat":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[33]').click()
                sleep(1)
            elif self.province[x] == "sumatera selatan":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[34]').click()
                sleep(1)
            elif self.province[x] == "sumatera utara":
                self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[35]').click()
                sleep(1)
            else :
                print("Kota tidak ditemukan !!!!")
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[9]/input').click()
            sleep(5)

    def pemegang_hak_cipta(self):
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[4]/div[1]/div[2]/a').click()
        sleep(1)
        self.driver.find_element_by_name('name').send_keys('Politeknik Pos Indonesia')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holder"]/div[3]/div/textarea').send_keys('Jalan Sariasih No.54, Sarijadi, Sukasari, Kota Bandung, Jawa Barat 40151')
        sleep(1)
        self.driver.find_element_by_name('city').send_keys('Bandung')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holder"]/div[5]/div/label/span').click()
        sleep(1)
        self.driver.find_element_by_name('zip_code').send_keys('40151')
        sleep(1)
        self.driver.find_element_by_name('province').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holder"]/div[8]/div/select/option[11]').click()
        sleep(1)
        self.driver.find_element_by_name('email').send_keys('humas@poltekpos.ac.id')
        sleep(1)
        self.driver.find_element_by_name('phone_number').send_keys('(022) 2009562')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holder"]/div[11]/input').click()
        sleep(5)

    def lampiran(self):

        rows=XLUtils.getRowCount(self.path,'Sheet1')

        count = 0

        for r in range(2,rows+1):
            judul=XLUtils.readData(self.path,"Sheet1",r,1)
            uraian=XLUtils.readData(self.path,"Sheet1",r,2)
            #tanggal=XLUtils.readData(self.path,"Sheet1",r,3)
            #negara=XLUtils.readData(self.path,"Sheet1",r,4)
            kota=XLUtils.readData(self.path,"Sheet1",r,5)
            #keterangan=XLUtils.readData(self.path,"Sheet1",r,6)
            fileciptaan=XLUtils.readData(self.path,"Sheet1",r,7)
            ktp=XLUtils.readData(self.path,"Sheet1",r,8)
            pernyataan=XLUtils.readData(self.path,"Sheet1",r,9)
            pengalihan=XLUtils.readData(self.path,"Sheet1",r,10)
            #alamat=XLUtils.readData(self.path,"Sheet1",r,11)
            #suratkuasa=XLUtils.readData(self.path,"Sheet1",r,12)
            umkm=XLUtils.readData(self.path,"Sheet1",r,13)
            aktahukum=XLUtils.readData(self.path,"Sheet1",r,14)
            npwp=XLUtils.readData(self.path,"Sheet1",r,15)

            if judul:
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[1]/div[2]/div/div[4]/div/input').send_keys(judul)
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[1]/div[2]/div/div[5]/div/textarea').send_keys(uraian)
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[1]/div[2]/div/div[8]/div/input').send_keys(kota)
                #SURAT KUASA   
                #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[1]/div/div/singleupload/span[1]/input[1]').send_keys(str(rootPath) + "/Haki-otomatis-master/FileCiptaan/"+str(fileciptaan)+".pdf")
                #ciptaan
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[7]/div/div/multipleupload/span[1]/input[1]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileCiptaan/"+str(fileciptaan)+".pdf")
                #ktp
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[4]/div/div/singleupload/span[1]/input[1]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileKTP/"+str(ktp)+".pdf")
                #pernyataan
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[6]/div/div/singleupload/span[1]/input[1]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FilePernyataan/"+str(pernyataan)+".pdf")    
                #pengalihan
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[8]/div/div/singleupload/span[1]/input[1]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FilePengalihan/"+str(pengalihan)+".pdf")
                #surat umkm
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[2]/div/div/singleupload/span[1]/input[1]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileUMKM/"+str(umkm)+".pdf")
                # salinan akta hukum
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[3]/div/div/singleupload/span[1]/input[1]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileBadanHukum/"+str(aktahukum)+".pdf")
                #npwp
                self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[5]/div/div/singleupload/span[1]/input[1]').send_keys(os.getcwd()+"/SeleniumAPTIMAS/FileNPWP/"+str(npwp)+".pdf")
                

                self.driver.find_element_by_xpath('//*[@id="createform"]/div[6]/div[1]/input').click()
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="disclaimer"]/div[2]/div/div/label/span[3]').click()
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="disclaimer"]/div[3]/button').click()
                

        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[3]/div/div/singleupload/span[1]').click()        
        #path = r"C:/Innal/Poltekpos/IRC"
        #nameFile = filePath + ".pdf"
        #result = os.path.join(path, nameFile)
        #pdf = os.path.abspath('C:\Innal\Poltekpos\IRC\ST Tim Sentra KI Poltekpos.pdf')
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[3]/div/div/singleupload/span[1]').send_keys(pdf)
        #sleep(15)
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[5]/div/div/singleupload/span[1]').click()
        #sleep(15)
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[7]/div/div/multipleupload/span[1]').click()
        #sleep(15)
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[4]/div/div/singleupload/span[1]').click()
        #sleep(15)
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[6]/div/div/singleupload/span[1]').click()
        #sleep(15)
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[8]/div/div/singleupload/span[1]').click()
        #sleep(15)
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[6]/div[1]/input').click()
        #sleep(1)





    def status(self):
        self.driver.execute_script("window.open('https://aptimas.poltekpos.ac.id/login');")
        self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[1]/input').send_keys('0410118609')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('lppm.poltekpos.ac.id')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="haki"]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/aside/div/section/ul[2]/li[4]/ul/li[2]/a').click()
        sleep(2)
        rows=XLUtils.getRowCount(self.path,'Sheet1')

        count = 0

        for r in range(2,rows+1):
            judul=XLUtils.readData(self.path,"Sheet1",r,1)

            if judul:
                self.driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div/div/div/div[2]/div[1]/div[4]/form/div/input').send_keys(judul)
                self.driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div/div/div/div[2]/div[1]/div[4]/form/div/span/button').click()
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="formbulk"]/table/tbody/tr[2]/td[6]/a[1]').click()
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="jenis_haki"]').click()
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="jenis_haki"]/option[4]').click()
                sleep(2)
                self.driver.find_element_by_name('submit').click()

    def billing(self):
        #self.driver.switch_to_window(self.driver.window_handles[0])
        #sleep(1)
        self.driver.execute_script("window.open('https://e-hakcipta.dgip.go.id/login');")
        self.driver.switch_to_window(self.driver.window_handles[2])
        sleep(15)
        self.driver.find_element_by_name('username').send_keys("awangga@poltekpos.ac.id")
        sleep(40)
        self.driver.find_element_by_name('password').send_keys('sayaakuirollyituganteng')
        sleep(40)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/div/ul/li[1]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/div/ul/li[1]/ul/li[2]/a').click()
        #self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/div/ul/li[1]').click()
        sleep(1)
        rows=XLUtils.getRowCount(self.path,'Sheet1')

        count = 0

        for r in range(2,rows+1):
            judul=XLUtils.readData(self.path,"Sheet1",r,1)

            if judul:
                self.driver.find_element_by_xpath('//*[@id="searchbar"]').send_keys(judul)
                self.driver.find_element_by_xpath('//*[@id="searchbar"]').send_keys(Keys.ENTER)
                sleep(2)        
                self.driver.find_element_by_xpath('//*[@id="sample_1"]/tbody/tr[1]/td[2]/a').click()
                sleep(2)
                #status = self.driver.find_element_by_xpath('//*[@id="detail"]/div[1]/div[2]/div/div[13]/div/div/span').text
                billing = self.driver.find_element_by_xpath('//*[@id="detail"]/div/div[2]/div/div[14]/div/div/span').text
                sleep(2)
                print("ini billing codenyaa", billing)