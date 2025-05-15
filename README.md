# Como configurar/instalar/usar o `VS Code` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `VS Code` no `Linux Ubuntu`.

## _Abstract_

_In this document are contained the main commands and settings to set up/install/usae the `VS Code` on `Linux Ubuntu`._

## Descrição [2]

### `VS Code (VS Code)`

O `VS Code`, comumente conhecido como `VS Code`, é um editor de código-fonte altamente popular e amplamente utilizado por desenvolvedores de software em todo o mundo. Desenvolvido pela Microsoft, o `VS Code` é uma ferramenta altamente personalizável e extensível, que oferece suporte a uma ampla variedade de linguagens de programação e _frameworks_. Sua interface simples e intuitiva, juntamente com recursos poderosos, como realce de sintaxe, depuração integrada, controle de versão e uma vasta coleção de extensões disponíveis na sua loja, tornam-no uma escolha preferida para muitos programadores que buscam eficiência e produtividade em seus projetos de desenvolvimento de _software_.

### `Linting`

O `Linting` é o processo de análise estática de código-fonte para identificar problemas, erros de sintaxe, e más práticas de programação antes da execução do programa. Ferramentas de linting, conhecidas como _linters_, verificam o código em busca de inconsistências, padrões de estilo e potenciais _bugs_, ajudando os desenvolvedores a manterem a qualidade e legibilidade do código. Esse recurso é especialmente valioso em equipes de desenvolvimento, pois promove a conformidade com diretrizes de codificação e reduz a probabilidade de erros em produção, resultando em um código mais robusto e fácil de manter.

### `PyLance`

O `PyLance` é uma extensão para o `VS Code` que oferece suporte avançado ao `Python`, proporcionando uma experiência de codificação mais eficiente. Baseado no `Pyright`, um servidor de linguagem desenvolvido pela `Microsoft`, o `PyLance` fornece recursos como autocompletar (_IntelliSense_), verificação de tipos estática, navegação de código e documentação _inline_, ajudando os desenvolvedores a escrever código mais preciso e sem erros. Ele é amplamente utilizado para melhorar a produtividade ao trabalhar com projetos `Python`, oferecendo ferramentas poderosas de análise e sugestões em tempo real.


## 1. Como configurar/instalar/usar o `VS Code` no `Linux Ubuntu` [1]

Para configurar/instalar/usar o `VS Code` no `Linux Ubuntu`, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`


2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
    
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
    
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    
    ```bash
    sudo apt full-upgrade -y
    ```

3. **Navegue até o diretório onde o arquivo `.deb` está localizado:** Use o comando cd para navegar até o diretório onde o arquivo `.deb` está localizado. Por exemplo, se o arquivo `.deb` estiver na sua pasta `Downloads`, você pode usar o seguinte comando:

    ```bash
    cd ~/Downloads
    ```

4. Instale o arquivo `.deb`: Use o comando `dpkg` para instalar o arquivo `.deb`. Substitua "`<nome_do_arquivo>.deb`" pelo nome real do arquivo `.deb` que você deseja instalar:
    
    ```bash
    sudo dpkg -i code_1.82.2-1694671812_amd64.deb
    ```

    Você precisará fornecer sua senha de administrador (`sudo`) para continuar.

5. Resolva as dependências (se necessário): Às vezes, a instalação do arquivo `.deb` pode gerar erros devido a dependências ausentes. Se isso acontecer, você pode usar o seguinte comando para tentar resolver as dependências:

    ```bash
    sudo apt install -f
    ```

O comando acima tentará instalar automaticamente as dependências necessárias para o pacote `.deb` que você está instalando.

6. **Verifique a instalação:** Após a conclusão do processo, verifique se o programa ou pacote foi instalado corretamente. Você pode fazer isso procurando o aplicativo no menu de aplicativos ou executando-o a partir do terminal com o comando:

    ```bash
    code
    ```

Isso deve permitir que você instale um arquivo `.deb` no seu sistema Ubuntu. Lembre-se de que os arquivos .deb são pacotes de software específicos para distribuições baseadas no Debian, como o Ubuntu, e geralmente são seguros de usar, especialmente se você os obtiver de fontes confiáveis. No entanto, sempre esteja ciente da origem dos arquivos .deb que você baixa e evite fontes não confiáveis para garantir a segurança do seu sistema.


## 1.1 Código completo para configurar/instalar/usar o `VS Code` no `Linux Ubuntu` 

Para configurar/instalar/usar o `VS Code` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```

2. Digite o seguinte comando e pressione `Enter`:

    ```
    NÂO há.
    ```

## 2. Configurar a variável de ambiente no `VS Code`

Para configurar o `VS Code` para informar ao sistema operacional que você está em modo de depuração e definir a variável de ambiente `DEBUG_MODE`, você pode seguir os seguintes passos:

### 2.1 Configurar a variável de ambiente no `VS Code`

1. **Abra seu projeto no `VS Code`**: Certifique-se de que seu projeto esteja aberto no `VS Code`.

2. **Crie ou edite o arquivo `launch.json`**:

    2.1 O arquivo `launch.json` é usado para configurar o comportamento da depuração no `VS Code`. Se você não tiver um arquivo `launch.json`, você pode criar um.

    2.2 Para criar ou abrir o `launch.json`, vá para a aba `Run and Debug` (`Ctrl+Shift+D`) e clique no _link_ `create a launch.json file` ou `add configuration`.

3. **Adicione a configuração da variável de ambiente**: No arquivo `launch.json`, adicione uma configuração para a variável de ambiente `DEBUG_MODE`. Aqui está um exemplo de configuração que define a variável de ambiente `DEBUG_MODE` para `True` durante a depuração:

    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "debugpy",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "env": {
                    "DEBUG_MODE": "True"
                }
            }
        ]
    }
    ```

4. **Salvar e iniciar a depuração**: Salve as alterações no arquivo `launch.json`. Inicie a depuração clicando no botão de execução de depuração (ícone de triângulo verde) na aba `Run and Debug` ou pressionando `F5`.


### 2.2 Localização do arquivo `launch.json`

o arquivo `launch.json` é armazenado em uma pasta específica dentro do seu projeto no `VS Code`. Ele faz parte da configuração do seu ambiente de depuração. Aqui estão detalhes sobre onde você pode encontrar e como ele é organizado:

1. **Localização**:

    1.1 O arquivo `launch.json` é armazenado na pasta `.vscode` no diretório raiz do seu projeto. Esta pasta é criada automaticamente pelo `VS Code` quando você adiciona configurações de depuração pela primeira vez.

    1.2 O caminho completo seria algo como: `/caminho/para/seu/projeto/.vscode/launch.json`

    1.2 Você pode copiar o arquivo para a pasta do seu projeto, execute o comando:
    
    ```bash
    sudo cp /home/edenedfsls/Documents/Downloads/unix/ubuntu/ide/vs_code/vs_code/docs/.vscode/launch.json /caminho/para/seu/projeto/.vscode/
    ``` 

### 2.3 Código `Python` para verificar a variável de ambiente

Dentro do seu código `Python`, você pode verificar se a variável `DEBUG_MODE` está definida corretamente assim:

```python
import os

# Verificar a variável de ambiente DEBUG_MODE
debug_mode = os.getenv("DEBUG_MODE") == "True"

if debug_mode:
    print("Modo de depuração ativado.")
else:
    print("Modo de depuração não ativado.")
```

**Dicas adicionais**

- **Ambientes de desenvolvimento e testes**: Certifique-se de que o `VS Code` e o seu ambiente `Python` estejam configurados corretamente para usar o ambiente virtual ou a configuração desejada.

- **Recarregar o `VS Code`**: Às vezes, é útil reiniciar o `VS Code` para garantir que todas as configurações e variáveis de ambiente sejam aplicadas corretamente.

Seguindo esses passos, você deverá ser capaz de configurar o `VS Code` para informar ao sistema operacional que você está em modo de depuração e definir a variável `DEBUG_MODE` conforme necessário.

## 3. Configurar o `PEP 8` no `VS Code`

Antes de configurar o `PEP 8` no `VS Code` é recomendável conhecer as opções de arquivo `settings.json`, como segue:


### 3.1 Opções de arquivo `settings.json`

Há três opções para editar o `settings.json`. Vou explicar quando usar cada uma delas:

* **Preferences: `Open User Settings (JSON)`**:

    * **Uso**: Essa opção é usada para definir configurações globais que serão aplicadas a todas as instâncias e projetos do `VS Code` no seu ambiente de usuário.

    * **Quando usar**: Se você quer que o `PEP 8` seja aplicado em todos os projetos `Python` que você abrir no `VS Code`, faça a alteração aqui.

* **Preferences: `Open Default Settings (JSON)`**:

    * **Uso**: Este arquivo contém as configurações padrão do `VS Code`, mas não é recomendável fazer alterações diretamente neste arquivo. Ele serve mais como referência para ver as configurações padrão.

    * **Quando usar**: Não faça modificações aqui.

* **Preferences: `Open Workspace Settings (JSON)`**:

    * **Uso**: Este arquivo armazena configurações específicas para o _workspace_ ou pasta de projeto atual. As configurações que você fizer aqui só serão aplicadas ao projeto aberto no momento.

    * **Quando usar**: Use esta opção se você quer que as configurações de `PEP 8` sejam aplicadas apenas ao projeto atual e não a todos os projetos.

**Qual opção escolher?**

* **Se você quer aplicar as configurações do PEP 8 para todos os projetos no VS Code**: Escolha `Preferences: Open User Settings (JSON)`.

* **Se você quer aplicar as configurações apenas para o projeto atual**: Escolha `Preferences: Open Workspace Settings (JSON)`.

Normalmente, a opção mais usada é `Open User Settings (JSON)`, pois assim o comportamento será consistente em todos os projetos que você abrir.

### 3.2 Configurar o(s) _linters_ (`flake8` ou `pylint`) no `VS Code`

Para garantir que o `VS Code` considere o `PEP 8` (o guia de estilo para Python) ao editar seus códigos, você pode configurar algumas extensões e ajustes nas configurações do editor. Aqui estão os passos para configurar isso:

1. **Instalar `pylint` e/ou `flake8`**:

    1.1 Para instalar o `pylint`, use:

    ```
    pip install pylint
    ```

    1.2 Você pode instalar um _linter_ específico. O `flake8` é uma boa escolha, pois é leve e fácil de usar. Você pode instalá-lo usando `pip`:

    ```
    pip install flake8
    ```

2. **Configurar o(s) _linters_ (`pylint` e/ou `flake8`) no `VS Code`**: Você pode adicionar diretamente ao seu arquivo de configuração `settings.json`:

    ```json
    {
        "python.linting.enabled": true,
        "python.linting.flake8Enabled": true,
        "python.linting.pylintEnabled": false  // ou true, dependendo do que você preferir
    }
    ```

3. **Configurar o Formatação de Código**:

    3.1 Para formatar seu código automaticamente de acordo com o PEP 8 ao salvar, você pode usar o `autopep8` ou `black`. Para instalar o `autopep8`, execute:

    ```bash
    pip install autopep8
    ```

    3.2 Para configurar a formatação automática ao salvar, adicione ao seu `settings.json`:

    ```json
    {
        "python.formatting.provider": "autopep8",
        "editor.formatOnSave": true
    }
    ```

4. **Verificar o Código**: Após configurar tudo, abra um arquivo `Python` e você deve ver as sugestões e avisos do _linter_ em relação ao estilo do `PEP 8`. Você também pode formatar seu código com a tecla de atalho (`Shift+Alt+F` ou `Ctrl+Shift+I`).

**Conclusão**

Com essas configurações, o `VS Code` considerará o `PEP 8` ao editar códigos `Python`, ajudando a manter um estilo de código consistente e legível. Essas ferramentas não apenas ajudam a detectar problemas de estilo, mas também promovem boas práticas de codificação.

### 3.3 Como configurar o limite visual de caracteres no `VS Code`

1. **Editar o `settings.json`**: Você pode adicionar a seguinte configuração:

    ```json
    {
        // outras configurações...
        "editor.rulers": [100],
        "editor.wordWrap": "on"  // opcional: quebra de linha automática
    }
    ```

    Se quiser usar `79` em vez de `100`, basta trocar `"editor.rulers": [100]` por `"editor.rulers": [79]`. Se quiser os dois, use:

    ```json
    "editor.rulers": [79, 100]
    ```

O `VS Code` mostrará uma linha vertical cinza (ou da cor do seu tema) na coluna especificada. Isso não bloqueia a digitação além do limite, mas ajuda visualmente a manter o padrão.


## 4. Extensões

### 4.1 Extensões recomendadas

| Extensão                                      | Descrição |
|-----------------------------------------------|-----------|
| `ambar.live-code`                             | Extensão para executar e depurar código ao vivo no VS Code. |
| `docker.docker`                               | Suporte para o Docker no VS Code, facilitando a criação, execução e gerenciamento de contêineres. |
| `github.copilot`                              | Assistente de IA da GitHub que sugere trechos de código para aumentar a produtividade. |
| `github.copilot-chat`                         | Extensão do GitHub Copilot que permite a interação por chat para sugestões de código. |
| `gitlab.gitlab-workflow`                      | Ferramentas para integração com GitLab e fluxo de trabalho direto no VS Code. |
| `james-yu.latex-workshop`                     | Extensão para facilitar a edição de documentos LaTeX no VS Code, com visualização de PDF. |
| `mathematic.vscode-pdf`                       | Visualizador de PDF integrado no VS Code, ideal para visualizar documentos matemáticos. |
| `mathworks.language-matlab`                   | Suporte para o desenvolvimento em MATLAB, incluindo destaque de sintaxe e execução de código. |
| `mechatroner.rainbow-csv`                     | Ferramenta para visualizar e editar arquivos CSV com formatação colorida no VS Code. |
| `ms-azuretools.vscode-docker`                 | Extensão que facilita o gerenciamento de contêineres Docker diretamente no VS Code. |
| `ms-ceintl.vscode-language-pack-pt-br`        | Pacote de idioma para o VS Code em português do Brasil. |
| `ms-dotnettools.vscode-dotnet-runtime`        | Suporte ao .NET Runtime no VS Code para desenvolvimento com C# e outros frameworks .NET. |
| `ms-python.debugpy`                           | Ferramenta para depuração de código Python no VS Code. |
| `ms-python.isort`                             | Extensão para organizar automaticamente importações em código Python. |
| `ms-python.python`                            | Extensão oficial do Python para o VS Code, oferecendo recursos como execução, depuração e linting. |
| `ms-python.vscode-pylance`                    | Extensão para autocompletar e análise de tipo no Python, baseada no PyLance. |
| `ms-toolsai.datawrangler`                    | Ferramenta para manipulação e análise de dados diretamente no VS Code. |
| `ms-toolsai.jupyter`                          | Suporte ao Jupyter Notebooks no VS Code, para trabalhar com notebooks interativos de Python. |
| `ms-toolsai.jupyter-keymap`                   | Mapeamento de teclas específico para trabalhar com Jupyter Notebooks no VS Code. |
| `ms-toolsai.jupyter-renderers`                | Extensão para renderizar saídas de células em Jupyter Notebooks no VS Code. |
| `ms-toolsai.vscode-jupyter-cell-tags`         | Permite adicionar tags às células de Jupyter Notebooks no VS Code para melhorar a organização. |
| `ms-toolsai.vscode-jupyter-slideshow`         | Ferramenta para criar apresentações interativas com Jupyter Notebooks no VS Code. |
| `ms-vscode-remote.remote-containers`          | Suporte para desenvolvimento remoto em contêineres Docker no VS Code. |
| `ms-vscode-remote.remote-wsl`                 | Suporte ao Windows Subsystem for Linux (WSL) para desenvolvimento em ambientes Linux no Windows. |
| `ms-vscode.cmake-tools`                       | Ferramenta para suporte ao CMake, permitindo configurar e compilar projetos no VS Code. |
| `ms-vscode.cpptools`                          | Extensão que oferece suporte completo ao desenvolvimento em C++, incluindo depuração e IntelliSense. |
| `ms-vscode.cpptools-extension-pack`          | Pacote de extensões para melhorar a experiência de desenvolvimento em C++ no VS Code. |
| `ms-vscode.cpptools-themes`                   | Temas personalizados para a interface de desenvolvimento em C++ no VS Code. |
| `ms-vscode.makefile-tools`                    | Ferramenta para suportar projetos que utilizam Makefiles, permitindo compilação e execução de tarefas. |
| `ms-vscode.powershell`                        | Extensão para trabalhar com o PowerShell diretamente no VS Code, com destaque de sintaxe e depuração. |
| `ms-vsliveshare.vsliveshare`                  | Permite a colaboração em tempo real com outros desenvolvedores dentro do VS Code, compartilhando o ambiente de trabalho. |
| `oracle.sql-developer`                       | Extensão para desenvolvimento de SQL e interação com bancos de dados Oracle no VS Code. |
| `paulosilva.vsc-octave-debugger`              | Ferramenta para depuração de código em Octave diretamente no VS Code. |
| `redhat.java`                                 | Suporte para desenvolvimento em Java no VS Code, incluindo ferramentas de construção e depuração. |
| `redhat.vscode-xml`                           | Extensão para trabalhar com arquivos XML no VS Code, oferecendo validação e formatação. |
| `toasty-technologies.octave`                  | Suporte para desenvolvimento em Octave no VS Code, com destaque de sintaxe e depuração. |
| `twxs.cmake`                                  | Extensão para facilitar o uso de CMake no VS Code, permitindo criar e configurar projetos C++ facilmente. |
| `visualstudioexptteam.intellicode-api-usage-examples` | Exemplos de uso da API IntelliCode, proporcionando sugestões de código baseadas em inteligência artificial. |
| `visualstudioexptteam.vscodeintellicode`      | Extensão que oferece sugestões inteligentes de código, melhorando a produtividade com IA. |
| `vscjava.vscode-gradle`                       | Suporte completo para projetos Gradle em Java no VS Code, com construção e depuração. |
| `vscjava.vscode-java-debug`                   | Extensão para depuração de código Java no VS Code, integrando com o processo de desenvolvimento. |
| `vscjava.vscode-java-dependency`              | Ferramenta para gerenciar dependências em projetos Java no VS Code. |
| `vscjava.vscode-java-pack`                    | Pacote de ferramentas essenciais para desenvolvimento Java no VS Code, incluindo depuração e execução. |
| `vscjava.vscode-java-test`                    | Extensão que facilita a execução e a depuração de testes em projetos Java no VS Code. |
| `vscjava.vscode-maven`                        | Suporte ao Apache Maven para gerenciamento de dependências e construção de projetos Java no VS Code. |


### 4.2 Instalar uma extensão

Para instalar uma extensão no `VS Code`, siga os passos abaixo:

1. **Abrir o VS Code**:

    1.1 Inicie o `VS Code` no seu computador.

2. **Acessar a Visualização de Extensões**:

    2.1 Clique no ícone de Extensões na barra lateral esquerda ou pressione `Ctrl+Shift+X` para abrir a visualização de extensões.

3. **Pesquisar a Extensão**:

    2.2 No campo de pesquisa que aparece no topo da barra lateral de extensões, digite o nome da extensão que você deseja instalar (por exemplo, `Python`, `C++`, `GitLab` etc.).

4. **Selecionar e Instalar a Extensão**:

    4.1 Após encontrar a extensão desejada na lista de resultados, clique nela para abrir a página de detalhes.

    4.2 Clique no botão `Instalar` para adicionar a extensão ao seu ambiente de desenvolvimento.

5. **Configurar a Extensão (se necessário)**:

    5.1 Algumas extensões podem exigir configurações adicionais. Para fazer isso, você pode acessar as configurações do `VS Code` (`File > Preferences > Settings ou Ctrl+,`) e procurar pela extensão instalada para ajustar suas opções conforme necessário.

6. **Reiniciar o `VS Code` (se necessário)**:

    6.1 Embora a maioria das extensões seja ativada automaticamente, em alguns casos, pode ser necessário reiniciar o `VS Code` para que todas as funcionalidades da extensão sejam corretamente carregadas.

Após esses passos, a extensão estará pronta para uso no seu `VS Code`!

### 4.3 Consultar extensões instaladas através de linha de comando

1. Você pode verificar as extensões instaladas no `VS Code` através da linha de comando. Para isso, use o seguinte comando no `Terminal Emulator` do `VS Code`:

    ```bash
    code --list-extensions
    ```

    Esse comando vai listar todas as extensões instaladas no seu `VS Code`. Caso queira obter mais detalhes sobre uma extensão específica, como sua versão, você pode adicionar o parâmetro `--show-versions`:

    ```bash
    code --list-extensions --show-versions
    ```
    
    Isso mostrará todas as extensões junto com suas versões atuais.


### 5. Habilitar o `PyLance`

Para habilitar o `PyLance` no `VS Code`, siga os passos abaixo:

1. **Instalar a Extensão `PyLance`**:

    1.1 Abra o `VS Code`.

    1.2 Vá até a visualização de extensões clicando no ícone de quadrado no menu lateral esquerdo ou pressione: `Ctrl+Shift+X`.

    1.3 No campo de pesquisa, digite `PyLance`.

    1.4 Clique na extensão `PyLance` da `Microsoft` e depois clique em Instalar.

2. **Configurar o `PyLance` como o servidor de linguagem `Python`**:

    2.1 Após a instalação, `PyLance` será ativado automaticamente, mas você pode verificar ou alterar a configuração manualmente.

    2.2 Abra a configuração do `VS Code` clicando em `File > Preferences > Settings` ou pressionando `Ctrl+,`.

    2.3 Na barra de pesquisa de configurações, digite `python.languageServer`.

    2.4 No campo de configuração que aparecer, altere o valor para `Pylance` (se não estiver configurado automaticamente).

3. **Reinicie o `VS Code`**:

    3.1 Para garantir que as configurações sejam aplicadas corretamente, reinicie o `VS Code`.

Com isso, o `PyLance` estará ativado e você poderá aproveitar os recursos avançados como autocompletar, análise de tipos estática, navegação de código e outros recursos de produtividade no seu projeto `Python`.


## 6. Atalhos para visualizar objetos

Essa funcionalidade é separada em algumas ferramentas, e depende da linguagem que você está usando (ex: `Python`, `C#`, `JavaScript` etc.). Para `Python`, por exemplo, e para outras linguagens também, você tem:

| Recurso                        | O que faz                                                                 | Como acessar                                              |
|-------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------|
| **Ir para Definição**         | Vai para onde a função/objeto/classe está definido                        | `F12`, `Ctrl+Clique` ou clique com o botão direito do mouse e escolha a opção `"Go to Definition"`              |
| **Procurar Simbologia**       | Lista todas funções, classes, variáveis do projeto                        | `Ctrl+T`                                                  |
| **Exibir Esquema do Arquivo** | Mostra todas funções/classe/variáveis dentro do arquivo atual             | `Ctrl+Shift+O`                                            |
| **Pesquisar na Árvore de Símbolos** | Pesquisa em todo o projeto                                          | `Ctrl+P`, depois digite `#nome`                           |
| **IntelliSense**              | Autocompleta e sugere funções, propriedades, métodos                      | `Ctrl+Espaço` (ou automático conforme digita)             |
| **Extensões específicas**     | Instalar extensões como *Python*, *Pylance*, *IntelliCode*, etc.          | Pela aba de extensões no `VS Code` (`Ctrl+Shift+X`)         |


## Referências

[1] OPENAI. ***Instalar arquivo .sh no ubuntu.*** Disponível em: <https://chat.openai.com/c/073320a8-7cc5-4590-9da0-d2bcc7093c88> (texto adaptado). Acessado em: 17/10/2023 16:05.

[2] OPENAI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 14/11/2023 09:33.

