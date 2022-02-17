import time

from PageObject import Poisk
'''Заполните переменные '''
name = 'Petya'
lastname = 'Petrov'
phone = '+77078555478'
email = 'Test12345@gmail.com'
kommentar = 'Привет я рыбалка, Хочу работать у вас, и изучать Питон'


def test_1(browser):
    '''Перейдем на сайт'''
    obratnaya_svyaz = Poisk(browser)
    obratnaya_svyaz.go_to_site()
    time.sleep(2)

    '''нажмем на кнопку Обратная связь'''
    obratnaya_svyaz.Poisk_Obratnaya_svyaz()
    time.sleep(0.5)
    '''Заполним поле имя'''
    obratnaya_svyaz.Name(name)
    time.sleep(2)
    '''Заполним поле Фамилия'''
    obratnaya_svyaz.Lastname(lastname)
    time.sleep(2)
    '''Заполним поле телефон'''
    obratnaya_svyaz.Phone(phone)
    time.sleep(2)
    '''Заполним поле Почта'''
    obratnaya_svyaz.Email(email)
    time.sleep(2)
    '''Заполним поле Коментарий'''
    obratnaya_svyaz.Komment(kommentar)
    time.sleep(2)
    '''Нажмем кнопку отправить'''
    obratnaya_svyaz.Otpravit_Knopka()
    time.sleep(2)


    assert obratnaya_svyaz.Uvedomlenie_OK() == 'Спасибо, ваше сообщение отправлено.'

    time.sleep(5)
    #Ожидаем 5 секунд и делается проверка на сообщение