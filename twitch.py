from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument('disable-notifications')
# options.add_argument('headless')

class Twitch:

	def __init__(self):

		self.URL = 'https://www.twitch.tv/videos/312787044'

		self.driver = webdriver.Chrome('webdriver/chromedriver', chrome_options=options)

		self.chat = []


	def get(self):

		self.driver.get(self.URL)

		try:
			WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mature-link'))).click()
		except:
			pass

		try:
			settings = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#default-player > div > div.hover-display.pl-hover-transition-out > div > div.pl-controls-bottom.pl-flex.qa-controls-bottom > div.player-buttons-right > div.pl-flex > button > span > span.pl-settings-icon')))
		except:
			print('cannot click settings!')

		try:
			total_time = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#default-player > div > div.hover-display.pl-hover-transition-out > div > div.pl-controls-bottom.pl-flex.qa-controls-bottom > div.player-seek > div.player-seek__time-container > span.player-seek__time.player-seek__time--total'))).text
			print(f'total time: {total_time}')
		except:
			print('can\'t find total time of this video')

		try:
			comment_list = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > div.right-column.tw-flex-shrink-0.tw-full-height.tw-relative > div > div > div > div.tw-full-height.tw-overflow-hidden.tw-relative > div > div > ul')))
		except:
			print('no comment list!')

		while True:
			for c in self.driver.find_elements_by_css_selector('#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > div.right-column.tw-flex-shrink-0.tw-full-height.tw-relative > div > div > div > div.tw-full-height.tw-overflow-hidden.tw-relative > div > div > ul > li'):
				t = c.text.strip()
				if t and (t not in self.chat):
					self.chat.append(t)
					print(self.chat[-1])
			time.sleep(5)

			try:
				time_now = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#default-player > div > div.hover-display.pl-hover-transition-out > div > div.pl-controls-bottom.pl-flex.qa-controls-bottom > div.player-seek > div.player-slider.js-player-slider'))).get_attribute('aria-valuenow')
				print(f'time now: {time_now}')
			except:
				print('can\'t find total time of this video')

if __name__ == '__main__':

	t = Twitch().get()
		
			

		