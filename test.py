import simple_selenium

tistory = simple_selenium.browser()
naver = simple_selenium.browser()
kakao = simple_selenium.browser()

if __name__ == '__main__':
    kakao.open("https://kakao.com")
    kakao.xpath()