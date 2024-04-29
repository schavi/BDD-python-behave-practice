

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.general_page import GeneralPage



class Ecosia(GeneralPage):

    def __init__(self, chosen_browser):
        super().__init__(url='https://ecosia.org/',chosen_browser=chosen_browser)
        self.wait = WebDriverWait(self.browser, 5)

    

    def main_search_input(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//input[@type='search']")

    def main_search_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//button[@type='submit']")
    

    def result_images_tab_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@data-test-id='search-navigation-images']/a")

    def result_news_tab_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@data-test-id='search-navigation-news']/a")
    
    def result_videos_tab_button(self) -> WebElement:
        return self.browser.find_element(By.XPATH, "//div[@data-test-id='search-navigation-videos']/a")


    def result_all_links(self) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@data-test-id='result-link']")))
    
    def result_images_articles(self) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@data-test-id='images-result']")))
