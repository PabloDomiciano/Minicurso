from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def run_selenium_demo():
    # Obter o caminho absoluto para o arquivo HTML de exemplo
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(current_dir, 'web_app_example.html')
    file_url = f'file://{html_file_path}'

    # Configurar o WebDriver (usando Chrome, certifique-se de ter o chromedriver instalado e no PATH)
    # Para este exemplo, vamos usar o Chrome em modo headless para execução no ambiente sandbox
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        print(f"Abrindo a página: {file_url}")
        driver.get(file_url)
        print("Página aberta com sucesso.")

        # 1. Teste de interação básica: Digitar nome e saudar
        print("\n--- Teste de Interação Básica ---")
        name_input = driver.find_element(By.ID, 'name-input')
        greet_button = driver.find_element(By.ID, 'greet-button')

        name_input.send_keys('Aluno Teste')
        greet_button.click()

        # Esperar a mensagem de saudação aparecer
        greeting_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'greeting-message'))
        )
        print(f"Mensagem de saudação: {greeting_message.text}")
        assert 'Olá, Aluno Teste!' in greeting_message.text
        print("Teste de saudação bem-sucedido.")

        # 2. Teste de renderização de componentes dinâmicos
        print("\n--- Teste de Renderização de Componentes Dinâmicos ---")
        toggle_button = driver.find_element(By.ID, 'toggle-content-button')
        toggle_button.click()

        # Esperar o conteúdo dinâmico aparecer
        dynamic_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'dynamic-content'))
        )
        print(f"Conteúdo dinâmico: {dynamic_content.text}")
        assert 'Este conteúdo apareceu dinamicamente!' in dynamic_content.text
        print("Conteúdo dinâmico visível. Teste de renderização bem-sucedido.")

        # Clicar novamente para esconder o conteúdo
        toggle_button.click()
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, 'dynamic-content'))
        )
        print("Conteúdo dinâmico escondido.")

        print("\nTodos os testes de demonstração foram executados com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro durante a execução do Selenium: {e}")
    finally:
        driver.quit()
        print("Navegador fechado.")

if __name__ == '__main__':
    run_selenium_demo()

