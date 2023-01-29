from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import codecs
# import mysql.connector
from csv import writer

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="scrape"
# )
# cursor = mydb.cursor()
# f= open("new.txt","a+")
driver.get("https://sankoudesign.com/")
page = driver.find_element(By.ID, "pagenav")
firstnum = 1
lastnum = 2
product_url= ""
product_image_url = ""
product_name = ""
for k in range(firstnum, lastnum):
    if k==1:
        wait = WebDriverWait(driver , 10)
        wait.until(EC.url_to_be("https://sankoudesign.com/"))
        for i in driver.find_elements(By.TAG_NAME, "figure"):
            j = i.find_element(By.TAG_NAME, "a")
            print (j.get_attribute("href"))
            # f.write(j.get_attribute("href")+"\n")
            product_url = j.get_attribute("href")
            for k in j.find_elements(By.TAG_NAME,"img"):
                print (k.get_attribute("src"))
                product_image_url = k.get_attribute("src")
                product_name = k.get_attribute("alt")
                print(product_name)
                # f.write(k.get_attribute("src")+"\n")
            # sql = "INSERT INTO product_list(product_name, product_url, product_image_url, product_price, product_info, category_name) VALUES (%s, %s, %s, %s, %s, %s)"
            # val = (str(product_name), str(product_url), str(product_image_url), "100円", str(product_name), "categoryname")
            # cursor.execute(sql, val)
            # mydb.commit()
            pro_list = list((product_url,product_name , "body", "vendor", "Apparel & Accessories > Clothing", "product type", "Tags", "TRUE", "Color", "Black", "Size", "Large", "", "","Variant SKU", "5125", "shopify", "Inventory Qty", "deny", "manual", "9.99", "9.99", "FALSE","TRUE ", " ", product_image_url, "1", product_name, "FALSE", "Our awesome T-shirt in 70 characters or less", "A great description of your products in 320 characters or less", "Apparel & Accessories > Clothing", "Unisex", "Adult", "7X8ABC910", "T-shirts", "cotton, pre-shrunk", "used", "FALSE", "", "", "", "", "", "", "g", "", "", "", "","archived"))
            with open('pro.csv', 'a', encoding='utf-8',newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(pro_list)
                f_object.close()
    elif k>1:
        wait = WebDriverWait(driver , 10)
        url = "https://sankoudesign.com/page/"+str(k)
        driver.get(url)
        
        for i in driver.find_elements(By.TAG_NAME, "figure"):
            
            j = i.find_element(By.TAG_NAME, "a")
            print (j.get_attribute("href"))
            # f.write(j.get_attribute("href")+"\n")
            product_url = j.get_attribute("href")
            for k in j.find_elements(By.TAG_NAME,"img"):
                print (k.get_attribute("src"))
                product_image_url = k.get_attribute("src")
                product_name = k.get_attribute("alt")
                # f.write(k.get_attribute("src")+"\n")
            pro_list = list((product_url,product_name , "body", "vendor", "category", "product type", "Tags", "TRUE", "Color", "Black", "Size", "Large", "", "","Variant SKU", "5125", "shopify", "Inventory Qty", "Inventory Policy", "joans-fulfillment", "9.99", "9.99", "FALSE","TRUE ", " ", product_image_url, "1", product_name, "FALSE", "Our awesome T-shirt in 70 characters or less", "A great description of your products in 320 characters or less", "Apparel & Accessories > Clothing", "Unisex", "Adult", "7X8ABC910", "T-shirts", "cotton, pre-shrunk", "used", "FALSE", "", "", "", "", "", "", "g", "", "", "", "", "archived"))
            with open('pro.csv', 'a', encoding='utf-8',newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(pro_list)
                f_object.close()
            # sql = "INSERT INTO product_list(product_name, product_url, product_image_url, product_price, product_info, category_name) VALUES (%s, %s, %s, %s, %s, %s)"
            # val =  (str(product_name), str(product_url), str(product_image_url), "100円", str(product_name), "categoryname")
            # cursor.execute(sql, val)
            # mydb.commit()      
# content = figure.text
# mydb.close()
get_url = driver.current_url


# f.close()
print("The current url is:"+str(get_url))

