**Gabarito**

1.  b) Garantir a qualidade, funcionalidade e estabilidade da aplicação de forma repetitiva e consistente.

2.  Instabilidade dos testes (flakiness) refere-se a testes que falham intermitentemente sem uma causa aparente, mesmo quando o código da aplicação não foi alterado. Fatores que podem causá-la incluem tempos de carregamento de página variáveis, animações, elementos que não estão visíveis ou interativos no momento da execução, e problemas de sincronização em aplicações com renderização dinâmica de componentes.

3.  `WebDriverWait` e `expected_conditions` são cruciais para lidar com a natureza assíncrona das aplicações web modernas. Eles permitem que o Selenium espere por uma condição específica (como um elemento estar visível, clicável ou presente no DOM) antes de tentar interagir com ele. Isso evita falhas de teste causadas por elementos que ainda não foram renderizados ou estão em transição, garantindo a estabilidade e confiabilidade dos testes.

4.  b) Integrar o motor de regras `axe-core` com Selenium para identificar violações de acessibilidade.

5.  Na demonstração, foram observadas violações de `color-contrast` (contraste de cores insuficiente) e `landmark-one-main` (falta de um `main` landmark na página) e `region` (conteúdo não contido por landmarks).

6.  É importante realizar testes de acessibilidade para garantir que as aplicações web sejam utilizáveis por pessoas com diversas deficiências (visuais, auditivas, motoras, cognitivas), promovendo a inclusão digital, cumprindo requisitos legais (como a WCAG) e éticos, e ampliando o público-alvo da aplicação.

7.  A automação de testes de acessibilidade é excelente para identificar problemas técnicos e estruturais, mas não é suficiente para avaliar aspectos subjetivos ou contextuais da acessibilidade. Por exemplo, a clareza do texto, a usabilidade para usuários com deficiências cognitivas, a ordem lógica de navegação para leitores de tela (que pode não ser detectada por ferramentas automáticas se o DOM estiver tecnicamente correto, mas semanticamente confuso), ou a adequação de descrições alternativas para imagens complexas, geralmente exigem avaliação manual por especialistas ou usuários reais.

8.  Salvar os resultados em um arquivo JSON permite que os dados da análise de acessibilidade sejam facilmente processados, armazenados, versionados e integrados a outras ferramentas ou pipelines de CI/CD. Facilita a geração de relatórios personalizados, a comparação de resultados ao longo do tempo e a automação da criação de tickets para correção de defeitos.

9.  Uma causa comum é a falta de sincronização, ou seja, o Selenium tentou encontrar o elemento antes que ele estivesse totalmente carregado ou visível na página (especialmente em aplicações com renderização dinâmica). A solução seria adicionar uma espera explícita (`WebDriverWait`) para garantir que o elemento esteja presente e interativo antes de tentar localizá-lo.

10. Em um TCC, os conhecimentos podem ser aplicados para: 
    *   **Desenvolvimento de uma Aplicação Web**: Integrar testes automatizados com Selenium para garantir a funcionalidade e testes de acessibilidade com `axe-selenium-python` como parte do processo de desenvolvimento, demonstrando a preocupação com a qualidade e inclusão desde o início do projeto.
    *   **Estudo Comparativo**: Realizar um estudo comparativo entre diferentes ferramentas de automação de testes ou de acessibilidade, analisando sua eficácia, facilidade de uso e cobertura para um cenário específico de TCC.
    *   **Melhoria de Acessibilidade**: Desenvolver um projeto focado na melhoria da acessibilidade de um site existente (ou de um protótipo), utilizando as ferramentas para identificar problemas e implementando as correções, documentando o processo e os resultados obtidos.
