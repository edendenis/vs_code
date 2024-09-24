#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `VS Code` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `VS Code` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install/usae the `VS Code` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `VS Code (Visual Studio Code)`
# 
# O `Visual Studio Code`, comumente conhecido como VS Code, é um editor de código-fonte altamente popular e amplamente utilizado por desenvolvedores de software em todo o mundo. Desenvolvido pela Microsoft, o VS Code é uma ferramenta altamente personalizável e extensível, que oferece suporte a uma ampla variedade de linguagens de programação e _frameworks_. Sua interface simples e intuitiva, juntamente com recursos poderosos, como realce de sintaxe, depuração integrada, controle de versão e uma vasta coleção de extensões disponíveis na sua loja, tornam-no uma escolha preferida para muitos programadores que buscam eficiência e produtividade em seus projetos de desenvolvimento de _software_.
# 
# ### `Linting`
# 
# O `Linting` é o processo de análise estática de código-fonte para identificar problemas, erros de sintaxe, e más práticas de programação antes da execução do programa. Ferramentas de linting, conhecidas como _linters_, verificam o código em busca de inconsistências, padrões de estilo e potenciais _bugs_, ajudando os desenvolvedores a manterem a qualidade e legibilidade do código. Esse recurso é especialmente valioso em equipes de desenvolvimento, pois promove a conformidade com diretrizes de codificação e reduz a probabilidade de erros em produção, resultando em um código mais robusto e fácil de manter.
# 

# ## 1. Como configurar/instalar/usar o `VS Code` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `VS Code` no `Linux Ubuntu`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 3. **Navegue até o diretório onde o arquivo `.deb` está localizado:** Use o comando cd para navegar até o diretório onde o arquivo `.deb` está localizado. Por exemplo, se o arquivo `.deb` estiver na sua pasta `Downloads`, você pode usar o seguinte comando: `cd ~/Downloads`
# 
# 4. Instale o arquivo `.deb`: Use o comando `dpkg` para instalar o arquivo `.deb`. Substitua "`<nome_do_arquivo>.deb`" pelo nome real do arquivo `.deb` que você deseja instalar: `sudo dpkg -i code_1.82.2-1694671812_amd64.deb`
# 
#     Você precisará fornecer sua senha de administrador (`sudo`) para continuar.
# 
# 5. Resolva as dependências (se necessário): Às vezes, a instalação do arquivo `.deb` pode gerar erros devido a dependências ausentes. Se isso acontecer, você pode usar o seguinte comando para tentar resolver as dependências: `sudo apt install -f`
# 
# O comando acima tentará instalar automaticamente as dependências necessárias para o pacote `.deb` que você está instalando.
# 
# 6. **Verifique a instalação:** Após a conclusão do processo, verifique se o programa ou pacote foi instalado corretamente. Você pode fazer isso procurando o aplicativo no menu de aplicativos ou executando-o a partir do terminal com o comando: `code`
# 
# Isso deve permitir que você instale um arquivo `.deb` no seu sistema Ubuntu. Lembre-se de que os arquivos .deb são pacotes de software específicos para distribuições baseadas no Debian, como o Ubuntu, e geralmente são seguros de usar, especialmente se você os obtiver de fontes confiáveis. No entanto, sempre esteja ciente da origem dos arquivos .deb que você baixa e evite fontes não confiáveis para garantir a segurança do seu sistema.
# 

# ## 1.1 Código completo para configurar/instalar/usar o `VS Code` no `Linux Ubuntu` 
# 
# Para configurar/instalar/usar o `VS Code` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÂO há.
#     ```

# ## 2. Configurar a variável de ambiente no `VS Code`
# 
# Para configurar o `VS Code` para informar ao sistema operacional que você está em modo de depuração e definir a variável de ambiente `DEBUG_MODE`, você pode seguir os seguintes passos:
# 
# ### 2.1 Configurar a variável de ambiente no `VS Code`
# 
# 1. **Abra seu projeto no `VS Code`**: Certifique-se de que seu projeto esteja aberto no `VS Code`.
# 
# 2. **Crie ou edite o arquivo `launch.json`**:
# 
#     2.1 O arquivo `launch.json` é usado para configurar o comportamento da depuração no `VS Code`. Se você não tiver um arquivo `launch.json`, você pode criar um.
# 
#     2.2 Para criar ou abrir o `launch.json`, vá para a aba `Run and Debug` (`Ctrl+Shift+D`) e clique no _link_ `create a launch.json file` ou `add configuration`.
# 
# 3. **Adicione a configuração da variável de ambiente**: No arquivo `launch.json`, adicione uma configuração para a variável de ambiente `DEBUG_MODE`. Aqui está um exemplo de configuração que define a variável de ambiente `DEBUG_MODE` para `True` durante a depuração:
# 
# ```
# {
#     "version": "0.2.0",
#     "configurations": [
#         {
#             "name": "Python: Current File",
#             "type": "debugpy",
#             "request": "launch",
#             "program": "${file}",
#             "console": "integratedTerminal",
#             "env": {
#                 "DEBUG_MODE": "True"
#             }
#         }
#     ]
# }
# ```
# 
# 4. **Salvar e iniciar a depuração**: Salve as alterações no arquivo `launch.json`. Inicie a depuração clicando no botão de execução de depuração (ícone de triângulo verde) na aba `Run and Debug` ou pressionando `F5`.
# 

# ### 2.2 Localização do arquivo `launch.json`
# 
# o arquivo `launch.json` é armazenado em uma pasta específica dentro do seu projeto no `VS Code`. Ele faz parte da configuração do seu ambiente de depuração. Aqui estão detalhes sobre onde você pode encontrar e como ele é organizado:
# 
# 1. **Localização**:
# 
#     1.1 O arquivo `launch.json` é armazenado na pasta `.vscode` no diretório raiz do seu projeto. Esta pasta é criada automaticamente pelo `VS Code` quando você adiciona configurações de depuração pela primeira vez.
# 
#     1.2 O caminho completo seria algo como: `/caminho/para/seu/projeto/.vscode/launch.json`
# 
#     1.2 Você pode copiar o arquivo para a pasta do seu projeto, execute o comando: `sudo cp /home/edenedfsls/Documents/Downloads/unix/ubuntu/ide/vs_code/vs_code/docs/.vscode/launch.json /caminho/para/seu/projeto/.vscode/` 

# ### 2.3 Código `Python` para verificar a variável de ambiente
# 
# Dentro do seu código `Python`, você pode verificar se a variável `DEBUG_MODE` está definida corretamente assim:
# 
# ```
# import os
# 
# # Verificar a variável de ambiente DEBUG_MODE
# debug_mode = os.getenv("DEBUG_MODE") == "True"
# 
# if debug_mode:
#     print("Modo de depuração ativado.")
# else:
#     print("Modo de depuração não ativado.")
# ```
# 
# **Dicas adicionais**
# 
# - **Ambientes de desenvolvimento e testes**: Certifique-se de que o `VS Code` e o seu ambiente `Python` estejam configurados corretamente para usar o ambiente virtual ou a configuração desejada.
# 
# - **Recarregar o `VS Code`**: Às vezes, é útil reiniciar o `VS Code` para garantir que todas as configurações e variáveis de ambiente sejam aplicadas corretamente.
# 
# Seguindo esses passos, você deverá ser capaz de configurar o `VS Code` para informar ao sistema operacional que você está em modo de depuração e definir a variável `DEBUG_MODE` conforme necessário.

# ## 3. Configurar o `PEP 8` no `VS Code`
# 
#     Antes de configurar o `PEP 8` no `VS Code` é recomendável conhecer as opções de arquivo `settings.json`, como segue:
# 

# ### 3.1 Opções de arquivo `settings.json`
# 
#     Há três opções para editar o settings.json. Vou explicar quando usar cada uma delas:
# 
# * **Preferences: `Open User Settings (JSON)`**:
# 
#     * **Uso**: Essa opção é usada para definir configurações globais que serão aplicadas a todas as instâncias e projetos do `VS Code` no seu ambiente de usuário.
# 
#     * **Quando usar**: Se você quer que o PEP 8 seja aplicado em todos os projetos Python que você abrir no `VS Code`, faça a alteração aqui.
# 
# * **Preferences: `Open Default Settings (JSON)`**:
# 
#     * **Uso**: Este arquivo contém as configurações padrão do `VS Code`, mas não é recomendável fazer alterações diretamente neste arquivo. Ele serve mais como referência para ver as configurações padrão.
# 
#     * **Quando usar**: Não faça modificações aqui.
# 
# * **Preferences: `Open Workspace Settings (JSON)`**:
# 
#     * **Uso**: Este arquivo armazena configurações específicas para o _workspace_ ou pasta de projeto atual. As configurações que você fizer aqui só serão aplicadas ao projeto aberto no momento.
# 
#     * **Quando usar**: Use esta opção se você quer que as configurações de `PEP 8` sejam aplicadas apenas ao projeto atual e não a todos os projetos.
# 
# **Qual opção escolher?**
# 
# * **Se você quer aplicar as configurações do PEP 8 para todos os projetos no VS Code**: Escolha `Preferences: Open User Settings (JSON)`.
# 
# * **Se você quer aplicar as configurações apenas para o projeto atual**: Escolha `Preferences: Open Workspace Settings (JSON)`.
# 
# Normalmente, a opção mais usada é `Open User Settings (JSON)`, pois assim o comportamento será consistente em todos os projetos que você abrir.

# ### 3.2 Configurar o(s) _linters_ (`flake8` ou `pylint`) no `VS Code`
# 
# Para garantir que o `VS Code` considere o `PEP 8` (o guia de estilo para Python) ao editar seus códigos, você pode configurar algumas extensões e ajustes nas configurações do editor. Aqui estão os passos para configurar isso:
# 
# 1. **Instalar `flake8` e/ou `pylint`**:
# 
#     1.1 Você pode instalar um _linter_ específico. O `flake8` é uma boa escolha, pois é leve e fácil de usar. Você pode instalá-lo usando `pip`:
# 
#     ```
#     pip install flake8
#     ```
# 
#     1.2 Para instalar o `pylint`, use:
# 
#     ```
#     pip install pylint
#     ```
# 
# 2. **Configurar o(s) _linters_ (`flake8` e/ou `pylint`) no `VS Code`**: Você pode adicionar diretamente ao seu arquivo de configuração `settings.json`:
# 
# ```
# {
#     "python.linting.enabled": true,
#     "python.linting.flake8Enabled": true,
#     "python.linting.pylintEnabled": false  // ou true, dependendo do que você preferir
# }
# ```
# 
# 3. **Configurar o Formatação de Código**:
# 
#     3.1 Para formatar seu código automaticamente de acordo com o PEP 8 ao salvar, você pode usar o `autopep8` ou `black`. Para instalar o `autopep8`, execute:
# 
#     ```
#     pip install autopep8
#     ```
# 
#     3.2 Para configurar a formatação automática ao salvar, adicione ao seu `settings.json`:
# 
#     ```
#     {
#         "python.formatting.provider": "autopep8",
#         "editor.formatOnSave": true
#     }
#     ```
# 
# 4. **Verificar o Código**: Após configurar tudo, abra um arquivo `Python` e você deve ver as sugestões e avisos do _linter_ em relação ao estilo do `PEP 8`. Você também pode formatar seu código com a tecla de atalho (`Shift+Alt+F` ou `Ctrl+Shift+I`).
# 
# **Conclusão**
# 
# Com essas configurações, o `VS Code` considerará o `PEP 8` ao editar códigos `Python`, ajudando a manter um estilo de código consistente e legível. Essas ferramentas não apenas ajudam a detectar problemas de estilo, mas também promovem boas práticas de codificação.

# ## Referências
# 
# [1] OPENAI. ***Instalar arquivo .sh no ubuntu.*** Disponível em: <https://chat.openai.com/c/073320a8-7cc5-4590-9da0-d2bcc7093c88> (texto adaptado). Acessado em: 17/10/2023 16:05.
# 
# [2] OPENAI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 14/11/2023 09:33.
# 
