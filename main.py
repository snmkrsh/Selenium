# Dosyanın ismini selenium.py yapma, bu hataya sebep verir.
# Selenium, Test otomasyon imkanı sunar.
# Manuel yaptıktan sonra selenium ile otomotize ederiz.
# Bir testin otomotize edilebilmesi için manuel olarak önce testin tamamlanması gerekir.
# html locators; elementlerin konumunu belirlemek lazım ki selenium onla iletişime geçebilsin.
# https://chromedriver.chromium.org/downloads   -- chrome driver



from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait  # ilgili driverı bekletmek için
from selenium.webdriver.support import expected_conditions  # istenen koşullar

from selenium.webdriver.common.action_chains import ActionChains

def a(time,by,path): 
 WebDriverWait(driver, time).until(expected_conditions.visibility_of_element_located((by, path)))

driver = webdriver.Chrome()
driver.get("https://www.etiya.com")
driver.maximize_window() #Chrome ekranını büyük ekran yapar.


# WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "lang_select"))) 
# class name'i x olan yapı görünene kadar maksimun 5 saniye bekle.
#a(10000,By.ID,"x")
# languageSelector = driver.find_element(By.ID,"x") # bu satırda ki id si x olan elementi bul selectore ata.

a(10000,By.CLASS_NAME,"lang-select")
languageSelector = driver.find_element(By.CLASS_NAME, "lang-select")
languageSelector.click()

a(10000,By.XPATH,"//*[@id='etiya']/header/div/div[2]/div[1]/div[2]/div[1]/a")
turkishLangugae = driver.find_element(By.XPATH, "//*[@id='etiya']/header/div/div[2]/div[1]/div[2]/div[1]/a")
turkishLangugae.click()

a(10000,By.ID,"search-btn")
searchBtn = driver.find_element(By.ID, "search-btn")
searchBtn.click()

a(10000,By.ID,"search-input")
searchInput = driver.find_element(By.ID, "search-input")
searchInput.send_keys("merhaba")

a(10000,By.XPATH,"//*[@id='search-box']/form/div/button")
searchIcon = driver.find_element(By.XPATH, "//*[@id='search-box']/form/div/button")
searchIcon.click()

a(10000,By.XPATH,"//*[@id='etiya']/header/div/div[1]/a/img")
backEtiya = driver.find_element(By.XPATH,"//*[@id='etiya']/header/div/div[1]/a/img")
backEtiya.click()

a(10000,By.XPATH,'//*[@id="nav-icon"]')
clickMenu = driver.find_element(By.XPATH,'//*[@id="nav-icon"]')
clickMenu.click()

a(10000,By.XPATH,'//*[@id="menu-container"]/ul/li[8]/a')
clickContact = driver.find_element(By.XPATH,'//*[@id="menu-container"]/ul/li[8]/a')
clickContact.click()

driver.get("https://www.etiya.com")

a(10000,By.XPATH,"//*[@id='home-sosial']/a[1]/i")
goLinkedln = driver.find_element(By.XPATH, "//*[@id='home-sosial']/a[1]/i")
goLinkedln.click()


a(10000,By.XPATH,"//*[@id='home-sosial']/a[2]/i")
goTwitter = driver.find_element(By.XPATH, "//*[@id='home-sosial']/a[2]/i")
goTwitter.click()


a(10000,By.XPATH,"//*[@id='home-sosial']/a[4]/i")
goYoutube = driver.find_element(By.XPATH, "//*[@id='home-sosial']/a[4]/i")
goYoutube.click()


# Action Chains
#3driver.get("https://www.etiya.com")
#button = driver.find_element(By.XPATH,"//*[@id='home-leadform']/div[1]/div[1]/span[4]")
#actionChain = ActionChains(driver)
#actionChain.move_to_element(button)
#actionChain.click()
#actionChain.perform()


sleep(5000)