from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class EHaki(object):cd.
    def __init__(self, title, description, date, name, address, city, zip_code, province, people):
        self.driver = webdriver.Chrome()
        self.title = title
        self.description = description
        self.date = date 
        self.name = name 
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.province = province
        self.people = people
        
    
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
        self.driver.find_element_by_name('title').send_keys(self.title)
        sleep(1)
        self.driver.find_elements_by_name('description')[1].send_keys(self.description)
        sleep(1)
        date = self.driver.find_element_by_xpath('//*[@id="createform"]/div[1]/div[2]/div/div[6]/div/div/input[1]')

        date.click()
        
        for i in range(len(date.get_attribute('value'))):
            date.send_keys(Keys.BACKSPACE)

        date.send_keys(self.date, Keys.ENTER)

        sleep(1)
        self.driver.find_element_by_name('announced_city').send_keys("Bandung")

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
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[3]/div/div/singleupload/span[1]').click()        
        #path = r"C:/Innal/Poltekpos/IRC"
        #nameFile = filePath + ".pdf"
        #result = os.path.join(path, nameFile)
        #pdf = os.path.abspath('C:\Innal\Poltekpos\IRC\ST Tim Sentra KI Poltekpos.pdf')
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[3]/div/div/singleupload/span[1]').send_keys(pdf)
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[5]/div/div/singleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[7]/div/div/multipleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[4]/div/div/singleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[6]/div/div/singleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[8]/div/div/singleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[6]/div[1]/input').click()
        sleep(1)