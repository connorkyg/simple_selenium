from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import subprocess


class browser:
    subprocess.Popen(
        r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')  # 디버거 크롬 구동
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={USER_AGENT}')
    options.add_argument("lang=dko_KR")
    path = r"D:/Development/Python/Coupang Partners/utils/chromedriver.exe"
    driver = webdriver.Chrome(service=Service(path), options=options)

    def __init__(self):
        print("browser class __init__")
        return

    def open(self, url):
        self.driver.get(url)

    def xpath(self, locate):
        self.driver.find_element(By.XPATH, locate)

    def class_name(self, locate):
        self.driver.find_element(By.CLASS_NAME, locate)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("browser class __exit__")
        self.driver.quit()
