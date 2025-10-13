# Tutorial Prático: Construindo e Executando Testes Automatizados e de Acessibilidade

Este tutorial guiará você através da criação e execução de testes automatizados com Selenium e testes de acessibilidade com `axe-selenium-python` em uma aplicação web de exemplo.

## Pré-requisitos

Certifique-se de ter o seguinte instalado em seu ambiente:

*   **Python 3.x**
*   **pip** (gerenciador de pacotes do Python)
*   **Google Chrome** (ou outro navegador compatível com Selenium)
*   **ChromeDriver** (ou o driver correspondente ao seu navegador, compatível com a versão do seu navegador e adicionado ao PATH do sistema)

## Configuração do Ambiente

1.  **Crie um diretório para o projeto** e navegue até ele no terminal:
    ```bash
    mkdir minicurso_testes
    cd minicurso_testes
    ```

2.  **Crie os arquivos da aplicação de exemplo e dos scripts de teste**:
    *   Salve o conteúdo do `web_app_example.html` em um arquivo chamado `web_app_example.html` dentro do diretório `minicurso_testes`.
    *   Salve o conteúdo do `selenium_demo.py` em um arquivo chamado `selenium_demo.py`.
    *   Salve o conteúdo do `accessibility_demo.py` em um arquivo chamado `accessibility_demo.py`.

3.  **Instale as bibliotecas Python necessárias**:
    ```bash
    pip install selenium axe-selenium-python
    ```

## Parte 1: Testes Automatizados com Selenium

Nesta parte, você executará e entenderá o script `selenium_demo.py`, que demonstra interações básicas com a aplicação de exemplo.

1.  **Abra o arquivo `selenium_demo.py`** em seu editor de código. Analise o código para entender como ele:
    *   Inicializa o WebDriver do Chrome (em modo headless).
    *   Navega para o arquivo `web_app_example.html`.
    *   Localiza elementos por ID (`name-input`, `greet-button`, `greeting-message`).
    *   Digita texto e clica em botões.
    *   Utiliza `WebDriverWait` e `expected_conditions` para esperar que elementos dinâmicos apareçam ou desapareçam, simulando a renderização de componentes.
    *   Verifica o texto das mensagens para validar o comportamento.

2.  **Execute o script de demonstração do Selenium**:
    ```bash
    python selenium_demo.py
    ```

3.  **Observe a saída no terminal**. Você verá as mensagens indicando as etapas do teste e a validação dos elementos. Se tudo estiver configurado corretamente, o teste deve passar sem erros.

4.  **Experimente modificar o script `selenium_demo.py`**:
    *   Altere o nome digitado no campo de entrada.
    *   Remova a espera explícita (`WebDriverWait`) para o conteúdo dinâmico e observe se o teste falha, demonstrando a importância da sincronização em aplicações com renderização de componentes.

## Parte 2: Testes de Acessibilidade com axe-selenium-python

Nesta parte, você executará o script `accessibility_demo.py` para analisar a acessibilidade da aplicação de exemplo.

1.  **Abra o arquivo `accessibility_demo.py`** em seu editor de código. Analise o código para entender como ele:
    *   Inicializa o WebDriver do Chrome (em modo headless).
    *   Navega para o arquivo `web_app_example.html`.
    *   Injeta e executa o `axe-core` na página.
    *   Salva os resultados da análise em um arquivo JSON (`accessibility_results.json`).
    *   Processa e exibe as violações encontradas no terminal.

2.  **Execute o script de demonstração de acessibilidade**:
    ```bash
    python accessibility_demo.py
    ```

3.  **Observe a saída no terminal**. O script identificará algumas violações de acessibilidade na `web_app_example.html` (por exemplo, contraste de cores insuficiente nos botões, falta de um `main` landmark). Isso demonstra como o `axe-core` pode rapidamente apontar problemas comuns de acessibilidade.

4.  **Examine o arquivo `accessibility_results.json`**. Este arquivo contém um relatório detalhado de todas as violações, incluindo a descrição do problema, o impacto e os elementos HTML afetados.

5.  **Desafio (Opcional)**: Tente corrigir as violações de acessibilidade na `web_app_example.html` e execute o `accessibility_demo.py` novamente para ver se as violações foram resolvidas. Por exemplo, você pode ajustar as cores dos botões para ter um contraste maior ou adicionar um elemento `<main>` para envolver o conteúdo principal.

## Conclusão

Ao completar este tutorial, você terá uma compreensão prática de como utilizar Selenium para automatizar interações em aplicações web e como `axe-selenium-python` pode ser usado para identificar problemas de acessibilidade. Essas ferramentas são fundamentais para garantir a qualidade e a inclusão em seus projetos de desenvolvimento web.
