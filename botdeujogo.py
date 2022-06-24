from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
import requests

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(15)

def bot():
	try:
			#Pega Bolinha Verde
		
		bolinha = driver.find_element_by_class_name('aumms1qt')
		bolinha = driver.find_elements_by_class_name('aumms1qt')
		clica_bolinha = bolinha[-1]
		acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
		acao_bolinha.move_to_element_with_offset(clica_bolinha, 0,-20)
		acao_bolinha.click()
		acao_bolinha.perform()
		acao_bolinha.click()
		acao_bolinha.perform()
			#PEGA O TELEFONE DO CLIENTE
		telefone_cliente = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
		telefone_final = telefone_cliente.text
		print(telefone_final)
			#pega a mensagem do cliente
		todas_as_msg = driver.find_elements_by_class_name('_1Gy50')
		todas_as_msg_texto = [e.text for e in todas_as_msg]
		msg = todas_as_msg_texto[-1]
		print(msg)

		#responder a mensagem
		
		#processar
		if msg == '1':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'Criar sua conta no site da Deu Jogo é muito simples:{os.linesep} *1°- acesse https://deujogo.bet/registro*.{os.linesep}  2°- Preencha todos os campos. {os.linesep} 3° - Crie sua conta. {os.linesep} 4°- Se o registro foi bem sucedido, você receberá um e-mail com o link para ativar sua conta (verifique o spam){os.linesep} 5°- *aproveite as maiores cotações do Brasil.*'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
		elif msg == '2':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'Você pode efetuar depósitos via Pix, Transferência bancária ou boleto pela plataforma Pay4Fun. {os.linesep} *Acesse: deujogo.bet* para realizar um depósito agora mesmo. {os.linesep}'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()	
		elif msg == '3':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f'Para retirar dinheiro da sua conta, tudo o que você tem que fazer é ir em *Saque*, digitar o valor e a resposta da Pergunta de Segurança. {os.linesep} Um código único de retirada será gerado. copie o código e cole na página da Pay4Fun. {os.linesep} Em seguida, selecione o método que deseja receber e preencha os seu dados solicitados. {os.linesep} *Acesse: deujogo.bet* para sacar seu saldo disponível agora mesmo.'
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
		elif msg == '4':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('*acesse: https://deujogo.bet/ajuda?tema=reglamento* para acessar o regulamento', Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
		elif msg == '5':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f'Aguarde, em alguns minutos que você será atendido. {os.linesep}_(horário de atendimento: das 8:00 às 18:00)_'
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
				#Mandar mensagem para atendente

			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('Atender', Keys.ENTER)
			campo_de_texto.send_keys(telefone_final, Keys.ENTER)

			

		elif msg == '6':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'*Jogos adiados, cancelados ou remarcados:*  Se um evento de apostas for adiado, cancelado ou não começar na data e hora indicadas na oferta de apostas, por qualquer motivo, e recomeçar ou começar dentro de 72 horas da data e hora de início exibidas, a aposta é válida para esse evento (e acumuladores incluindo ele). Caso um evento de apostas não seja retomado dentro de 72 horas da data de início exibida, as apostas relevantes serão anuladas. Em caso de suspensão ou cancelamento de um evento selecionado dentro de uma aposta combinada: a aposta é "devolvida" com um preço final de 1,00, afetando diretamente o preço final da aposta combinada, mas não sua validade.  {os.linesep} *Jogos abandonados*: Como regra geral, qualquer aposta em um evento cujo resultado seja determinável no momento da suspensão de uma competição esportiva, será considerada válida.'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()

		elif msg == '7':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'*Acesse: https://deujogo.bet/ajuda?tema=seguridad*'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()

		elif msg == '8':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'*Acesse: https://deujogo.bet/recuperar-senha* {os.linesep}Em seguida, digite o seu E-mail e clique em "Recuperação de senha"'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()	


		elif msg == '9':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f'Acesse a *página de usuário* (canto superior direito) em seguida, clique em *"configurações"*, depois mais um clique em *"Mudar pergunta"*, após aceitar, você reberá um e-mail para cadastrar sua nova pergunta de segurança.'
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()

		elif msg == '10':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f"""Bônus de primeiro depósito:
*• Até R$ 1.000,00* • O bônus credita o valor do prêmio • bônus não pode ser usado duas vezes na mesma partida • Ele também não pode ser sacado, apenas utilizado pra apostar (você saca a premiação) • pode ser usado em E-sports(esportes eletrônicos) • não pode encerrar aposta

{os.linesep}
mercados aceitos: 1x2, ao vivo, handicap ou margem vencedora, 1 gol, resultado exato, intervalo/final do jogo, 1x2 e ambas as equipes para marcar, números exatos de gols
{os.linesep}
Mercados não aceitos: empate devolve aposta, total (+1.5 gols e etc), ambos marcam, dupla hipótese, parte mais produtiva, ímpar/par'"""
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()	
				


		elif msg == 'Cadastro':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'Criar sua conta no site da Deu Jogo é muito simples:{os.linesep} *1°- acesse o site deujogo.bet*.{os.linesep}  2°- Selecione o botão *"Cadastre-se!"* e preencha todos os campos. Este formulário está localizado no menu de login (canto superior direito). {os.linesep} 3° - Crie sua conta. {os.linesep} 4°- Se o registro foi bem sucedido, você receberá um e-mail com o link para ativar sua conta (verifique o spam){os.linesep} 5°- *aproveite as maiores cotações do Brasil.*'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()

		elif msg == 'Deposito':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'Você pode efetuar depósitos via Pix, Transferência bancária ou boleto pela plataforma Pay4Fun. {os.linesep} Clique em saldo e depois vá em "depositar". Clique na plataforma Pay4Fun Go, em seguida, preencha o valor e o e seu E-mail. Na próxima página, digite o seu cpf e clique em prosseguir. Agora escolha o método de depósito e aproveite! {os.linsesp}*Acesse: deujogo.bet* para realizar um depósito agora mesmo.'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
				#Mandar mensagem para atendente

			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('Atender', Keys.ENTER)
			campo_de_texto.send_keys(telefone_final, Keys.ENTER)

		elif msg == 'Depósito':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'Você pode efetuar depósitos via Pix, Transferência bancária ou boleto pela plataforma Pay4Fun. {os.linesep} *Acesse: deujogo.bet* para realizar um depósito agora mesmo.'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
				#Mandar mensagem para atendente

			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('Atender', Keys.ENTER)
			campo_de_texto.send_keys(telefone_final, Keys.ENTER)

		elif msg == 'Como faço deposito':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'Você pode efetuar depósitos via Pix, Transferência bancária ou boleto pela plataforma Pay4Fun. {os.linesep} *Acesse: deujogo.bet* para realizar um depósito agora mesmo.'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
				#Mandar mensagem para atendente

			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('Atender', Keys.ENTER)
			campo_de_texto.send_keys(telefone_final, Keys.ENTER)

		elif msg == 'Como faço depósito':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'Você pode efetuar depósitos via Pix, Transferência bancária ou boleto pela plataforma Pay4Fun. {os.linesep} *Acesse: deujogo.bet* para realizar um depósito agora mesmo.'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
				#Mandar mensagem para atendente

			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('Atender', Keys.ENTER)
			campo_de_texto.send_keys(telefone_final, Keys.ENTER)

		elif msg == 'Como faço depósito?':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'Você pode efetuar depósitos via Pix, Transferência bancária ou boleto pela plataforma Pay4Fun. {os.linesep} *Acesse: deujogo.bet* para realizar um depósito agora mesmo.'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
						

		elif msg == 'Saque':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f'Para retirar dinheiro de sua conta: {os.linesep} tudo o que você tem que fazer é ir para "Saque", digitar a quantia e a resposta da Pergunta Secreta. {os.linesep} Um código único de retirada será gerado. copie o código e cole na página da Pay4Fun, {os.linesep} em seguida, selecione o método que deseja receber com os seu dados solicitados. {os.linesep} *Acesse: deujogo.bet* para sacar seu saldo disponível agora mesmo.'
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()

		elif msg == 'Como faço saque':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f'Para retirar dinheiro de sua conta: {os.linesep} tudo o que você tem que fazer é ir para "Saque", digitar a quantia e a resposta da Pergunta Secreta. {os.linesep} Um código único de retirada será gerado. copie o código e cole na página da Pay4Fun, {os.linesep} em seguida, selecione o método que deseja receber com os seu dados solicitados. {os.linesep} *Acesse: deujogo.bet* para sacar seu saldo disponível agora mesmo.'
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()

		elif msg == 'Como faço saque?':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f'Para retirar dinheiro de sua conta: {os.linesep} tudo o que você tem que fazer é ir para "Saque", digitar a quantia e a resposta da Pergunta Secreta. {os.linesep} Um código único de retirada será gerado. copie o código e cole na página da Pay4Fun, {os.linesep} em seguida, selecione o método que deseja receber com os seu dados solicitados. {os.linesep} *Acesse: deujogo.bet* para sacar seu saldo disponível agora mesmo.'
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()	


		elif msg == 'Regulamento':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('*acesse: https://deujogo.bet/ayuda?tema=reglamento* para acessar o regulamento', Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()

		elif msg == 'Atendimento':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('Aguarde, dentro de alguns minutos que você será atendido...', Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
			#Mandar mensagem para atendente
			
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			campo_de_texto.send_keys('Atender', Keys.ENTER)
			campo_de_texto.send_keys(telefone_final, Keys.ENTER)


		elif msg == 'jogo adiado':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'*Jogos adiados, cancelados ou remarcados:*  Se um evento de apostas for adiado, cancelado ou não começar na data e hora indicadas na oferta de apostas, por qualquer motivo, e recomeçar ou começar dentro de 72 horas da data e hora de início exibidas, a aposta é válida para esse evento (e acumuladores incluindo ele). Caso um evento de apostas não seja retomado dentro de 72 horas da data de início exibida, as apostas relevantes serão anuladas. Caso de suspensão ou cancelamento de um evento selecionado dentro de uma aposta combinada: a aposta é "devolvida" com um preço final de 1,00, afetando diretamente o preço final da aposta combinada, mas não sua validade.  {os.linesep} *Jogos abandonados*: Como regra geral, qualquer aposta em um evento cujo resultado seja determiinável no momento da suspensão de uma competição esportiva, será considerada válida.'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()

		elif msg == 'jogo remarcado':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			texto_modificado = f'*Jogos adiados, cancelados ou remarcados:*  Se um evento de apostas for adiado, cancelado ou não começar na data e hora indicadas na oferta de apostas, por qualquer motivo, e recomeçar ou começar dentro de 72 horas da data e hora de início exibidas, a aposta é válida para esse evento (e acumuladores incluindo ele). Caso um evento de apostas não seja retomado dentro de 72 horas da data de início exibida, as apostas relevantes serão anuladas. Caso de suspensão ou cancelamento de um evento selecionado dentro de uma aposta combinada: a aposta é "devolvida" com um preço final de 1,00, afetando diretamente o preço final da aposta combinada, mas não sua validade.  {os.linesep} *Jogos abandonados*: Como regra geral, qualquer aposta em um evento cujo resultado seja determiinável no momento da suspensão de uma competição esportiva, será considerada válida.'
			time.sleep(3)
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()	
		elif msg == 'Bônus':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f"""Bônus de primeiro depósito:
*• Até R$ 1.000,00* • O bônus credita o valor do prêmio • bônus não pode ser usado duas vezes na mesma partida • Ele também não pode ser sacado, apenas utilizado pra apostar (você saca a premiação) • pode ser usado em E-sports(esportes eletrônicos) • não pode encerrar aposta

{os.linesep}
mercados aceitos: 1x2, ao vivo, handicap ou margem vencedora, 1 gol, resultado exato, intervalo/final do jogo, 1x2 e ambas as equipes para marcar, números exatos de gols
{os.linesep}
Mercados não aceitos: empate devolve aposta, total (+1.5 gols e etc), ambos marcam, dupla hipótese, parte mais produtiva, ímpar/par'"""
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()	
		elif msg == 'Como funciona o bônus':
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f"""Bônus de primeiro depósito:
*• Até R$ 1.000,00* • O bônus credita o valor do prêmio • bônus não pode ser usado duas vezes na mesma partida • Ele também não pode ser sacado, apenas utilizado pra apostar (você saca a premiação) • pode ser usado em E-sports(esportes eletrônicos) • não pode encerrar aposta

{os.linesep}
*mercados aceitos:* 1x2, ao vivo, handicap ou margem vencedora, 1 gol, resultado exato, intervalo/final do jogo, 1x2 e ambas as equipes para marcar, números exatos de gols
{os.linesep}
*Mercados não aceitos:* empate devolve aposta, total (+1.5 gols e etc), ambos marcam, dupla hipótese, parte mais produtiva, ímpar/par'"""
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
							#VOLTAR PARA O CONTATO PADRÃO

			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()						


		else:
			campo_de_texto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
			campo_de_texto.click()
			time.sleep(3)
			texto_modificado = f'Bem-vindo ao atendimento da Deu Jogo. *Como posso ajudar você hoje?*{os.linesep} [1] - Como fazer o meu cadastro no site da Deu Jogo? {os.linesep} [2] - Como faço depósito?{os.linesep} [3] - Como faço saque? {os.linesep} [4] - Regulamento  {os.linesep}[5] - Falar com um atendente{os.linesep} [6] - Jogos cancelados ou adiados{os.linesep}[7] - Dúvidas frequentes - Central de ajuda {os.linesep}[8] - Esqueci minha senha {os.linesep}[9] - Recuperar pergunta de segurança para saque {os.linesep}[10] - Bônus'
			campo_de_texto.send_keys(texto_modificado, Keys.ENTER)
				#VOLTAR PARA O CONTATO PADRÃO
			contato_padrao = driver.find_element_by_class_name('_2XH9R')
			acao_contato = webdriver.common.action_chains.ActionChains(driver)
			acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
			acao_contato.click()
			acao_contato.perform()
			acao_contato.click()
			acao_contato.perform()
#_3OvU8
#_3dulN  - etiqueta de mensagem (funciona)
#Zu0md
#_1i_wG
#i0jNr
#HONz8
#_1pJ9J _2XH9R - pegar apenas o final do pino
#_2XH9R icone pino mensagem fixada - funcionando atualmente
	except:
		print('buscando novas mensagens')
		time.sleep(3)
while True:
	bot()