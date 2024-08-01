from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from core.utils import get_driver


class CostumerTestCase(TestCase):
    def test_signin(self):
        driver = get_driver()
        driver.get("http://localhost:8000/signin/")

        username_element = driver.find_element(By.NAME, "username")
        password_element = driver.find_element(By.ID, "id_password")

        username_element.clear()
        username_element.send_keys("admin")
        password_element.clear()
        password_element.send_keys("admin")
        password_element.send_keys(Keys.RETURN)
        sleep(2)
        assert "Вы успешно авторизовались!" in driver.page_source
        sleep(2)
        driver.close()


    def test_searchbar(self):
        driver = get_driver()
        driver.get("http://localhost:8000/")

        searchbar_element = driver.find_element(By.NAME, "keyword")

        searchbar_element.clear()
        searchbar_element.send_keys("Электроника")
        sleep(2)
        searchbar_element.send_keys(Keys.RETURN)
        sleep(2)
        driver.close()


class AddTestCase(TestCase):
    def test_add_new(self):
        driver = get_driver()
        driver.get("http://127.0.0.1:8000/new-create/")

        title_element = driver.find_element(By.NAME, "new_title")
        article_element = driver.find_element(By.NAME, "new_article")
        button_element = driver.find_element(By.NAME, "add-new")

        title_element.clear()
        title_element.send_keys("title")
        article_element.clear()
        article_element.send_keys("article")
        sleep(3)
        button_element.click()
        sleep(3)
        driver.close()

    def test_add_product(self):
        driver = get_driver()
        driver.get("http://127.0.0.1:8000/product-create/")

        name_elem = driver.find_element(By.NAME, "name")
        description_elem = driver.find_element(By.NAME, "description")
        price_elem = driver.find_element(By.NAME, "price")
        qty_elem = driver.find_element(By.NAME, "qty")
        image_elem = driver.find_element(By.NAME, "image")
        button_elem = driver.find_element(By.NAME, "add-product")

        name_elem.clear()
        name_elem.send_keys("Selenium")
        description_elem.clear()
        description_elem.send_keys("Written by Selenium")
        price_elem.clear()
        price_elem.send_keys("666")
        qty_elem.clear()
        qty_elem.send_keys("666")
        image_elem.send_keys(r"media\selenium-logo.png")
        sleep(3)
        button_elem.click()
        sleep(3)
        driver.close()

    def test_add_profile(self):
        driver = get_driver()
        driver.get("http://127.0.0.1:8000/profile-create/")

        user_select = Select(driver.find_element(By.NAME, "user"))
        bio_elem = driver.find_element(By.NAME, "bio")
        sociallink_elem = driver.find_element(By.NAME, "social_link")
        phonenumber_elem = driver.find_element(By.NAME, "phone_number")
        photo_elem = driver.find_element(By.NAME, "photo")
        button_elem = driver.find_element(By.NAME, "add-profile")


        user_select.select_by_value('6')
        bio_elem.clear()
        bio_elem.send_keys("Written by Selenium")
        sociallink_elem.clear()
        sociallink_elem.send_keys("https://www.selenium.dev/")
        phonenumber_elem.clear()
        phonenumber_elem.send_keys("0555555555")
        photo_elem.send_keys(r"media\selenium-logo.png")
        sleep(3)
        button_elem.click()
        sleep(3)
        driver.close()




