from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import PyPDF2
import requests
import time
import subprocess
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Automação:
    def __init__(self):
        self.caminho = "C:\\Users\\Usuário\\Downloads\\curriculos_atual\\"
        self.caminhoTotal = None
        self.index = 1
        
        
    def PegarFileNomeDaPasta(self):
        for arquivo in os.listdir(self.caminho):
            if arquivo.lower().endswith('.pdf'):
                self.caminhoTotal = self.caminho+arquivo
                self.ler_pdf()
                 
        
    def ler_pdf(self):
        try:
            with open(self.caminhoTotal, 'rb') as arquivo:
                leitor = PyPDF2.PdfReader(arquivo)
                texto = leitor.pages[0].extract_text()
                print(texto)
                self.mandarTexto(texto)
            
        except Exception as e:
            print(f"Erro ao ler PDF: {e}")
            
 
    

    def PreenchendoForm(self, nome, email, telefone):
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            
            sucesso = False
            
            try:
                driver.get('https://cevolu.com.br/adicionar-curriculo')
                print(driver.title)
                radio_button = driver.find_element(By.XPATH, '//*[@id="autorizacaoSim"]')
                radio_button.click()
                inputNome = driver.find_element(By.XPATH, '//*[@id="name"]')
                inputNome.send_keys(nome)
                inputTelefone = driver.find_element(By.XPATH, '//*[@id="cellphone"]')
                inputTelefone.send_keys(telefone)
                inputEmail = driver.find_element(By.XPATH, '//*[@id="email"]')
                inputEmail.send_keys(email)
            
                selecioneVaga = driver.find_element(By.XPATH, '//*[@id="react-select-2-input"]')
                selecioneVaga.click()
                selecioneVaga.send_keys("Geral")
                selecioneVaga.send_keys(Keys.TAB )
                time.sleep(5)
            
                curriculo = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/input')
                curriculo.send_keys(self.caminhoTotal)
                time.sleep(5)
                button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button').click()
                time.sleep(10)
                sucesso = True
                
            except Exception as e:
                print(f"Erro preencher formulario: {e}")
                
            finally:
                driver.quit()
                
               
                        
            
    
    def mandarTexto(self, curriculo):
        url = 'https://api.cevolu.com.br/api/BuscarDadosPessoais'
        dados = {
            "texto": curriculo
        }
        response = requests.post(url, json=dados)
        print(response)
        print(response.text)
        texto = response.json()
        lista = texto[0].split(",")  
        self.PreenchendoForm(lista[0],lista[1],lista[2])


    def renomearArquivo(self): 
        novo_nome = f"{self.index}.pdf"
        caminho_arquivo_novo = os.path.join(self.caminho, novo_nome)

        try:
            os.rename(self.caminhoTotal, caminho_arquivo_novo)
            print(f"Arquivo renomeado para: {novo_nome}")
        except Exception as e:
            print(f"Erro ao renomear {self.caminhoTotal}: {e}")
        finally:
            self.index += 1
           
    
    
    
if __name__ == "__main__":
    auto = Automação()
    auto.PegarFileNomeDaPasta()
    
    



