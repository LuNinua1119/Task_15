import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#ვებ-გვერდზე შესვლისას აუცილებელია ყოველჯერზე ხელით ცავერიოთ, როცა მოგვთხოვს Change your passwords, თორე ტესტირება არ იმუშავებს
class SauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.get(
            "https://www.saucedemo.com/"
        )

        self.driver.maximize_window()

    def test_locked_out_user(self):
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        time.sleep(2)

        username.send_keys("locked_out_user")

        time.sleep(2)

        password.send_keys("secret_sauce")

        time.sleep(2)

        login_button.click()

        time.sleep(5)

        error = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        print(error.text)

        self.assertIn(
            "locked out",
            error.text
        )

    def test_performance_glitch_user(self):
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username.send_keys("performance_glitch_user")
        password.send_keys("secret_sauce")

        login_button.click()

        time.sleep(5)

        if "inventory" in self.driver.current_url:
            menu_button = self.driver.find_element(By.ID,"react-burger-menu-btn"
)
            menu_button.click()

            time.sleep(2)

            logout_button = self.driver.find_element(By.ID,"logout_sidebar_link")

            logout_button.click()

        else:
            error = self.driver.find_element(By.CSS_SELECTOR,"[data-test='error']")

            print(error.text)


    def test_problem_user(self):
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        time.sleep(2)

        username.send_keys("problem_user")

        time.sleep(2)

        password.send_keys("secret_sauce")

        login_button.click()

        time.sleep(5)


        if "inventory" in self.driver.current_url:
            first_item = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

            second_item = self.driver.find_element(By.ID,  "add-to-cart-sauce-labs-bike-light")

            time.sleep(2)

            first_item.click()


            time.sleep(2)

            second_item.click()

            cart = self.driver.find_element(By.ID, "shopping_cart_container")

            cart.click()

            time.sleep(2)
            remove_first_item = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")

            remove_second_item = self.driver.find_element(By.ID, "remove-sauce-labs-bike-light")

            time.sleep(2)
            remove_first_item.click()

            time.sleep(2)
            remove_second_item.click()

            meny_button = self.driver.find_element(By.ID, "react-burger-menu-btn" )

            time.sleep(2)
            meny_button.click()

            logout_button = self.driver.find_element(By.ID, "logout_sidebar_link")

            time.sleep(2)
            logout_button.click()

        else:
            error = self.driver.find_element( By.CSS_SELECTOR, "[data-test='error']")

            print(error.text)


    def test_standard_user(self):
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        if "inventory" in self.driver.current_url:
            first_item = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")

            second_item = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")

            first_item.click()
            second_item.click()

            time.sleep(5)

            remove_first = self.driver.find_element(By.ID,"remove-sauce-labs-backpack")

            remove_first.click()

            product = self.driver.find_element(By.ID,"item_0_title_link")

            product.click()

            time.sleep(5)

            self.driver.back()

            sort = Select(self.driver.find_element(By.CLASS_NAME,"product_sort_container"))

            sort.select_by_value("hilo")

            facebook = self.driver.find_element(By.CLASS_NAME,"social_facebook")

            facebook.click()

            time.sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[0])

            linkedin = self.driver.find_element(By.CLASS_NAME,"social_linkedin")

            linkedin.click()

            time.sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[0])

            menu_button = self.driver.find_element(By.ID,"react-burger-menu-btn")

            menu_button.click()

            time.sleep(2)

            logout_button = self.driver.find_element( By.ID,"logout_sidebar_link")

            logout_button.click()

        else:
            error = self.driver.find_element(By.CSS_SELECTOR,"[data-test='error']")

            print(error.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()