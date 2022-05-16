from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

def probar_formulario(respuestas):
    driver.get("https://URL-TO-POST-HERE")

    #INPUTS TYPE TEXT BY ID
    # RESPUESTAS[0] COLOUMN 0 OF CVS...
    elem = driver.find_element_by_id("account_name").send_keys(respuestas[0])
    elem = driver.find_element_by_id("account_lastname").send_keys(respuestas[1])
    elem = driver.find_element_by_id("account_cuil").send_keys(respuestas[2])
    elem = driver.find_element_by_id("account_tel").send_keys(respuestas[3])
    elem = driver.find_element_by_id("account_email").send_keys(respuestas[4])
    elem = driver.find_element_by_id("account_univ").send_keys(respuestas[5])
    elem = driver.find_element_by_id("account_tit").send_keys(respuestas[6])
    elem = driver.find_element_by_id("account_post").send_keys(respuestas[7])
    # INPUT BY NAME KEY
    driver.find_element_by_xpath("//input[@name='account_birthdate']").send_keys(respuestas[8])
    
    
    el = driver.find_element_by_id('account_prov')
    for option in el.find_elements_by_tag_name('option'):
        if option.text == respuestas[9]:
            option.click() # select() in earlier versions of webdriver
            break
    driver.find_element_by_xpath("//input[@name='account_sexo' and @value='Masculino']").click()
    #postgrado si o no, acomodar
    driver.find_element_by_xpath("//input[@name='inlineRadioOptions' and @value='option2']").click()
    elem = driver.find_element_by_id("termCond").click()
    elem = driver.find_element_by_xpath("//button[@type='submit']").submit()
    sleep(2)

driver = webdriver.Chrome()
driver.maximize_window()

with open('LINK-TO-CSV-WHIT-ANSWERS.csv', newline='') as File:  
    reader = csv.reader(File)
    next(reader)
    for row in reader:
        probar_formulario(row)

driver.close()

