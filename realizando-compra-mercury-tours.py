from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

class testeClaro():
    def __init__(self):
        # Acesse o link: http://www.newtours.demoaut.com/
        try:
            self.url = 'http://www.newtours.demoaut.com/'
            self.titulo = 'Welcome: Mercury Tours'
            self.drive = webdriver.Firefox()
            self.drive.get(self.url)
            assert self.url == self.drive.current_url
            self.drive.implicitly_wait(30)
            assert self.titulo == self.drive.title

        except Exception as e:
            print(e)

    def validandoPaginaInicial(self):
        titulo = 'Welcome: Mercury Tours'
        assert titulo == self.drive.title


    def acessarLogin(self):
        try:
            # USUARIO E SENHA
            self.username = ''
            self.password = ''
            # INSERINDO AS INFORMAÇÕES NOS CAMPOS NECESSARIOS E INDO PARA A PRÓXIMA PÁGINA
            self.drive.find_element_by_name('userName').click()
            self.drive.find_element_by_name('userName').send_keys(self.username)
            self.drive.find_element_by_name('password').click()
            self.drive.find_element_by_name('password').send_keys(self.password)
            self.drive.find_element_by_name('login').click()

        except Exception as e:
            print(e)

    def inserindoInformacoes(self):
        # PEDINDO PARA O BROWSER AGUARDAR CASO O CARREGAMENTO LEVE UM TEMPO
        self.drive.implicitly_wait(30)
        ## SELECIONANDO A IDA
        # SELECIONANDO O LONDON
        select = Select(self.drive.find_element_by_name('fromPort'))
        select.select_by_visible_text('London')
        # SELECIONANDO DECEMBER
        select = Select(self.drive.find_element_by_name('fromMonth'))
        select.select_by_value('12')
        # SELECIONANDO O DIA
        select = Select(self.drive.find_element_by_name('fromDay'))
        select.select_by_index('20')
        ## SELECIONANDO O RETORNO
        # SELECIONANDO O OCTOBER
        select = Select(self.drive.find_element_by_name('toMonth'))
        select.select_by_value('10')
        # SELECIONANDO O DIA
        select = Select(self.drive.find_element_by_name('toDay'))
        select.select_by_index('21')
        # SELECIONANDO A FIRST CLASS
        self.drive.find_element_by_xpath(
            '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[2]').click()
        # SELECIONANDO AIRLINES
        select = Select(self.drive.find_element_by_name('airline'))
        select.select_by_visible_text('Blue Skies Airlines')
        sleep(1)
        # CLICANDO EM CONTINUAR
        self.drive.find_element_by_name('findFlights').click()
        sleep(1)

    def escolhendoVoo(self):
        # PEDINDO PARA O BROWSER AGUARDAR CASO O CARREGAMENTO LEVE UM TEMPO
        self.drive.implicitly_wait(30)
        # CONFIRMANDO SE O TITULO DA PÁGINA CORRESPONDE A PÁGINA ATUAL
        assert 'Select a Flight: Mercury Tours' == self.drive.title
        # SELECIONANDO O VOO DE IDA
        self.drive.find_element_by_xpath(
            '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[5]/td[1]/input').click()
        sleep(1)
        # SELECIONANDO O VOO DE VOLTA
        self.drive.find_element_by_xpath(
            '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[5]/td[1]/input').click()
        sleep(1)
        # CLICANDO EM CONTINUAR
        self.drive.find_element_by_name('reserveFlights').click()
        sleep(1)

    def conferindoVoos(self):
        # CONFERINDO O VOO DE IDA
        self.flightGoing = self.drive.find_element_by_css_selector(
            'body > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(3) > td.data_left > font > b').text
        assert self.flightGoing == 'Blue Skies Airlines 361'
        # CONFERINDO O VOO DE VOLTA
        self.flightReturn = self.drive.find_element_by_css_selector(
            'body > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td.data_left > font > font > font:nth-child(1) > b').text
        assert self.flightReturn == 'Blue Skies Airlines 631'
        # INSERINDO O FIRST NAME
        self.drive.find_element_by_name('passFirst0').send_keys('Teste')
        # INSERINDO O LAST NAME
        self.drive.find_element_by_name('passLast0').send_keys('Nextel')
        # INSERINDO O NUMBER
        self.drive.find_element_by_name('creditnumber').send_keys('118989038904')
        # CLICANDO EM SECURE PURCHASE
        self.drive.find_element_by_name('buyFlights').click()

    def confirmandoOVoo(self):
        # CONFIRMADO O VOO
        self.drive.implicitly_wait(10)
        self.flightConfirmation = self.drive.find_element_by_class_name('frame_header_info').text
        assert self.drive.title == 'Flight Confirmation: Mercury Tours'
        assert self.drive.current_url == 'http://newtours.demoaut.com/mercurypurchase2.php'
        assert 'flight confirmation' in self.flightConfirmation.lower()

    def logout(self):
        self.drive.quit()


claro = testeClaro()
claro.acessarLogin()
claro.inserindoInformacoes()
claro.escolhendoVoo()
claro.conferindoVoos()
claro.confirmandoOVoo()
claro.logout()



