from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv


driver = webdriver.Chrome('chromedriver.exe') 



def probar_formulario(respuestas):
    driver.get("")

    #INPUTS TYPE TEXT BY ID
    # RESPUESTAS[0] COLOUMN 0 OF CVS...
    #firstname
    elem = driver.find_element_by_id("first-name").send_keys(respuestas[0])
    #lastname
    elem = driver.find_element_by_id("mat-input-4").send_keys(respuestas[1])
    #email
    elem = driver.find_element_by_id("mat-input-5").send_keys(respuestas[2])
    #pass
    elem = driver.find_element_by_id("mat-input-6").send_keys(respuestas[3])
    #pass again
    elem = driver.find_element_by_id("mat-input-7").send_keys(respuestas[4])
    #code
    elem = driver.find_element_by_id("mat-input-8").send_keys(respuestas[5])
    #submit button
    elem = driver.find_element_by_xpath("//button[@type='submit']").submit()
    sleep(2)

driver = webdriver.Chrome()
driver.maximize_window()

with open('answers.csv', newline='') as File:  
    reader = csv.reader(File)
    next(reader)
    for row in reader:
        probar_formulario(row)

driver.close()

