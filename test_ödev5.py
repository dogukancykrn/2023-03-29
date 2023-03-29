from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
from time import sleep 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
from pathlib import Path
from datetime import date







class TestCasesler():
 def setup_method(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    URL ="https://www.saucedemo.com/"
    self.driver.get(URL)
    self.driver.maximize_window()
    self.folderPath = str(date.today())
    Path(f"{self.folderPath}").mkdir(exist_ok=True)
    self.vars = {}
  
 def teardown_method(self):
    self.driver.quit()
 

 
 def testlogin (self) :
     
     Username =self.driver.find_element(By.ID,"user-name")
     Username.send_keys("")
     password = self.driver.find_element(By.ID,"password")
     password.send_keys("")
     loginButton =self.driver.find_element(By.XPATH,"//*[@id='login-button']")
     loginButton.click()
     errormessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
     self.driver.save_screenshot(f"{self.folderPath}/test-login.png")
     assert errormessage.text == "Epic sadface: Username is required" 
 
 @pytest.mark.parametrize("Username",[("naber"),("abcde"),("1111")])    
 def testcases1(self,Username) :
     
     username_input =self.driver.find_element(By.ID,"user-name")
     username_input.send_keys(Username)
     loginButton =self.driver.find_element(By.XPATH,"//*[@id='login-button']")
     loginButton.click()
     errormessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
     self.driver.save_screenshot(f"{self.folderPath}/test-cases1.png")
     assert errormessage.text == "Epic sadface: Password is required" 

  
 def testcases2(self):
       
        Username = self.driver.find_element(By.ID,"user-name")
        Username.send_keys("locked_out_user")
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        errormessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-cases2.png")
        assert errormessage.text == "Epic sadface: Sorry, this user has been locked out."    

 def test_xICON (self) :
        
        Username = self.driver.find_element(By.ID,"user-name")
        Username.send_keys("")
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("")
        loginButton =self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        ICON = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        ICON.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-xICON.png")  
        assert True 
 
  
        

 def testurunler(self):
        
        Username = self.driver.find_element(By.ID,"user-name")
        Username.send_keys("standard_user")
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        url2 ="https://www.saucedemo.com/inventory.html"
        self.driver.get(url2)
        listOfUrun = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Swag Labs sitesinde şu anda {len(listOfUrun)} adet ürün vardır.")
        self.driver.save_screenshot(f"{self.folderPath}/test-urunler.png")  
        assert len(listOfUrun) == 6
 
 
 @pytest.mark.parametrize("username,password",[("standard_user","abcdef"),("kullaniciadi","secret_sauce"),("besiktas","sergenyalcin")])     
 def testnomatch(self,username,password):
        Usernameinput = self.driver.find_element(By.ID,"user-name")
        Usernameinput.send_keys(username)
        passwordinput= self.driver.find_element(By.ID,"password")
        passwordinput.send_keys(password)
        loginButton = self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        errormessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-nomatch.png")
        assert errormessage.text == "Epic sadface: Username and password do not match any user in this service"    
      
 
 def testAddItem(self):
        Username = self.driver.find_element(By.ID,"user-name")
        Username.send_keys("standard_user")
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        url2 ="https://www.saucedemo.com/inventory.html"
        self.driver.get(url2)

        Item1 = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        Item1.click()
        Item2 = self.driver.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt")
        Item2.click()

        carticon = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
        carticon.click()
        
        checkoutButton = self.driver.find_element(By.ID,"checkout")
        checkoutButton.click()
        
        firstNameInput = self.driver.find_element(By.XPATH,"//*[@id='first-name']")
        firstNameInput.send_keys("Doğukan")
        lastNameInput = self.driver.find_element(By.ID,"last-name")
        lastNameInput.send_keys("Çaykiran")
        postalCodeInput = self.driver.find_element(By.ID,"postal-code")
        postalCodeInput.send_keys("12345")
        countineButton = self.driver.find_element(By.ID,"continue")
        countineButton.click()

        finishButton = self.driver.find_element(By.ID,"finish")
        finishButton.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-Item.png")
        assert True


 def testZamanAsimi(self):
        Username = self.driver.find_element(By.ID,"user-name")
        Username.send_keys("standard_user")
        password = self.driver.find_element(By.ID,"password")
        password.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()

        url2 ="https://www.saucedemo.com/inventory.html"
        self.driver.get(url2)
        self.driver.implicitly_wait(5) 
        Item1 = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        Item1.click()

        
        carticon = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")
        carticon.click()
        #normalde bu süreyi daha uzun süre tutyordum fakat beklememek için 5sn tuttum
        try:
         sleep(5)  
        except TimeoutError:
         element_present = EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Total:') and contains(@class, 'cart-total-price')]"))
         WebDriverWait(self.driver, 5).until(element_present)
         print("İşleminize uzun zamandır devam etmediğiniz için ana sayfaya yönlendiiriliyorsunuz!")
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-zaman-asimi.png")
        assert True