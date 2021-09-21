from selenium import webdriver

navegador = webdriver.Chrome()

#entrar no site -  no get vc coloca o link do site
navegador.get("http://127.0.0.1:8000/")

#entrar em criar conta
navegador.find_element_by_xpath('/html/body/div[1]/div[2]/a[2]').click()

#preencher as informações de cadastro -

navegador.find_element_by_xpath('//*[@id="id_username"]').send_keys('Teste')
navegador.find_element_by_xpath('//*[@id="id_email"]').send_keys('irianyjisunger@gmail.com')
navegador.find_element_by_xpath('//*[@id="id_password1"]').send_keys('testejisung123456')
navegador.find_element_by_xpath('//*[@id="id_password2"]').send_keys('testejisung123456')


#clicar no botao de cadastro - pega o nome que vc deu ao botao
navegador.find_element_by_xpath('//*[@id="logar"]').click()

#preencher as informaçoes após criar conta
navegador.find_element_by_xpath('//*[@id="id_username"]').send_keys('irianyjisunger@gmail.com')
navegador.find_element_by_xpath('//*[@id="id_password"]').send_keys('testejisung123456')

#clicar no botao de entrar na conta - pega o nome que vc deu ao botao
navegador.find_element_by_xpath('//*[@id="logar"]').click()