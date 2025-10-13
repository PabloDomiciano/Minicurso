from selenium import webdriver
from selenium.webdriver.common.by import By
from axe_selenium_python import Axe
import time
import os
import json

def run_accessibility_demo():
    # Obter o caminho absoluto para o arquivo HTML de exemplo
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(current_dir, 'web_app_example.html')
    file_url = f'file://{html_file_path}'

    # Configurar o WebDriver (usando Chrome em modo headless)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        print(f"Abrindo a página para teste de acessibilidade: {file_url}")
        driver.get(file_url)
        print("Página aberta com sucesso.")

        # Injetar e executar o Axe
        axe = Axe(driver)
        axe.inject()
        print("Executando análise de acessibilidade com Axe...")
        results = axe.run()

        # Salvar os resultados em um arquivo JSON
        output_file = 'accessibility_results.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print(f"Resultados da análise de acessibilidade salvos em {output_file}")

        # Processar e exibir os resultados (apenas algumas informações para demonstração)
        violations = results['violations']
        if violations:
            print(f"\n--- Violações de Acessibilidade Encontradas ({len(violations)}) ---")
            for i, violation in enumerate(violations):
                print(f"{i+1}. ID: {violation['id']}")
                print(f"   Descrição: {violation['description']}")
                print(f"   Ajuda: {violation['help']}")
                print(f"   Impacto: {violation['impact']}")
                print("   Elementos afetados:")
                for node in violation['nodes']:
                    print(f"     - HTML: {node['html']}")
                    print(f"       Mensagem: {node['failureSummary']}")
                print("--------------------------------------------------")
        else:
            print("\nNenhuma violação de acessibilidade encontrada. Bom trabalho!")

    except Exception as e:
        print(f"Ocorreu um erro durante a execução do teste de acessibilidade: {e}")
    finally:
        driver.quit()
        print("Navegador fechado.")

if __name__ == '__main__':
    run_accessibility_demo()

