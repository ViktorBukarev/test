import time

from BasePage import BasePage
from selenium.webdriver.common.by import By

class ZooSeacrhLocators:
                                       # '''Здесь мы указываем список перемнных Xpath'''#

    obratnaya_svyaz = (By.XPATH, "//div[@class='shop_menuone_top_right']/div")
    poisk_polei_mane = (By.XPATH, "/html/body/div[3]//input[@name='name']")
    poisk_polei_lastname = (By.XPATH, "/html/body/div[3]//input[@name='lastname']")
    poisk_polei_phone = (By.XPATH, "/html/body/div[3]//input[@name='phone']")
    poisk_polei_email = (By.XPATH, "/html/body/div[3]//input[@name='email']")
    poisk_polei_kommentariy = (By.XPATH, "/html/body/div[3]//textarea[@class='b24-form-control']")
    knopka_otpravit = (By.XPATH, "/html/body/div[3]//div[@class='b24-form-btn-block']/button[@type='submit']")
    uvedomlenie_ob_otpravke = (By.XPATH, "//div[3]/div[2]/div[1]/div[2]//*[contains(text(),'Спасибо, ваше сообщение отправлено')]")



class Poisk(BasePage):

    '''Из списка элементов, выбираем обратная связь. И нажимаем на кнопку'''
    def Poisk_Obratnaya_svyaz(self):
        zooshoptest =self.find_elements(ZooSeacrhLocators.obratnaya_svyaz)
        for e in zooshoptest:
            print(e.text)
            if (e.text =='Обратная связь'):
                e.click()
                break

    '''Кликаем на кнопку отправить'''
    def Otpravit_Knopka(self):
        Otpravit =self.find_element(ZooSeacrhLocators.knopka_otpravit).click()

        '''Ищем поле ввода Имя, очищаем и вводим данные '''
    def Name(self, name):
        Name = self.find_element(ZooSeacrhLocators.poisk_polei_mane).clear()
        Name = self.find_element(ZooSeacrhLocators.poisk_polei_mane).send_keys(name)

        '''Ищем поле ввода Фамилия, очищаем и вводим данные'''
    def Lastname(self, lastname):
        Lastname = self.find_element(ZooSeacrhLocators.poisk_polei_lastname).clear()
        Lastname = self.find_element(ZooSeacrhLocators.poisk_polei_lastname).send_keys(lastname)


        '''Ищем поле ввода телефона , очищаем и вводим значения'''
    def Phone(self, phone):
        Phone = self.find_element(ZooSeacrhLocators.poisk_polei_phone).clear()
        Phone = self.find_element(ZooSeacrhLocators.poisk_polei_phone).send_keys(phone)


        '''Ищем поле ввода коментария, очищаем и вводим текст'''
    def Komment(self, kommentar):
        Komment = self.find_element(ZooSeacrhLocators.poisk_polei_kommentariy).clear()
        Komment = self.find_element(ZooSeacrhLocators.poisk_polei_kommentariy).send_keys(kommentar)


        '''Ищем поле ввода почты, очищаем и вводим данные'''
    def Email(self, email):
        Email = self.find_element(ZooSeacrhLocators.poisk_polei_email).clear()
        Emailmail = self.find_element(ZooSeacrhLocators.poisk_polei_email).send_keys(email)

        '''Считываем полученое уведомление об успешном отправке формы'''
    def Uvedomlenie_OK(self):
        messeg = self.find_elements(ZooSeacrhLocators.uvedomlenie_ob_otpravke)
        m = [el.text for el in messeg]
        print("проверим, что получили в переменную M:", m)
        return "".join(m)






