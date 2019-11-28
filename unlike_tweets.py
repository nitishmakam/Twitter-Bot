from selenium import webdriver
import time
import configparser
import os

driver = webdriver.Chrome()

class Twitter:
	domain_name = "https://twitter.com"

	config = None
	cfg_fname = 'config.ini'

	username = ''
	password = ''

	def config_init(self, cfg_fname):
		curr_dir = os.getcwd()
		cfg_fpath = os.path.join(curr_dir,cfg_fname)
	
		if not os.path.exists(cfg_fpath):
			print("Config path doesn't exist")
			sys.exit(1)

		self.config = configparser.ConfigParser()
		self.config.read(cfg_fpath)

	def logout(self):
		time.sleep(10)
		driver.close()
	
	def unlike_tweets(self):
		driver.get("{}/{}/likes".format(self.domain_name,self.username))
			
		for j in range(1,10):
			driver.get("{}/{}/likes".format(self.domain_name,self.username))
			time.sleep(5)
			for i in range(1,10):
				try:
					k=3
					path = "/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[{pos}]/div/article/div/div[2]/div[2]/div[{sec}]/div[3]/div/div/div[1]".format(pos=i,sec=k)
					print("1-"+path)
					like1=driver.find_element_by_xpath(path)
					like1.click()
					time.sleep(2)
					print("Trying first - "+(j*10+i))
				except Exception:
					print("Caught exception")
					time.sleep(1)
        
					try:    
						k=4
						path="/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[{pos}]/div/article/div/div[2]/div[2]/div[{sec}]/div[3]/div/div/div[1]".format(pos=i,sec=k)
						print("2-"+path)
						like2=driver.find_element_by_xpath(path)
						like2.click()
						print("Trying second - " +(j*10+i))
						time.sleep(2)
					except Exception:
						print("Caught exception 2")
						time.sleep(1)

	def login_app(self,username,password):				
		driver.get(self.domain_name)
		login = driver.find_element_by_link_text("Log In")
		login.click()

		usernameField=element=driver.find_element_by_css_selector("div#page-container > div > div > form > fieldset > div > input")
		usernameField.send_keys(username)

		passwordField=driver.find_element_by_css_selector("div#page-container > div > div > form > fieldset > div:nth-of-type(2) > input")
		passwordField.send_keys(password)

		login=driver.find_element_by_tag_name("button")
		login.click()

	def execute(self):
		
		#Config init
		self.config_init(self.cfg_fname)

		#Load credentials
		self.username = self.config.get("twitter","username")
		self.password = self.config.get("twitter","password")

		self.login_app(self.username,self.password)
		self.unlike_tweets()
		self.logout()	

if __name__ == '__main__':
	obj = Twitter()
	obj.execute()
	
