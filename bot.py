from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')
time.sleep(15)

def bot():
	try:
		bolinha = driver.find_element_by_class_name('_l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt')	
		bolinha = driver.find_elements_by_class_name('_l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt')
		clica_bolinha = bolinha[-1]
		acao_bolinha = webdriver.common.action_chains.ActionChain(driver)
		acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
		acao_bolinha.click()
		acao_bolinha.perform()
		acao_bolinha.click()
		acao_bolinha.perform()


	except:
		print('buscando novas mensagens')
		time.sleep(3)
while True:
	bot()
