# Windows
  
Modulo para trabalhar com a configuração do Windows  

*Read this in other languages: [English](Manual_Windows.md), [Português](Manual_Windows.pr.md), [Español](Manual_Windows.es.md)*
  
![banner](imgs/Banner_Windows.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Obter resolução de tela
  
Retorna a resolução atual da tela principal para uma variável do Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a uma variável|Variável onde o resultado será salvo|Variable|

### Obter todas as resoluções
  
Retorna todas as resoluções de tela permitidas na tela principal
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a uma variável|Variável onde o resultado será salvo|Variable|

### Alterar resolução
  
Altera a resolução da tela principal para a indicada. Deve ser uma resolução permitida pelo sistema
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Resolução|Resolução da tela (largura,altura)|800,600|

### Obter nome do usuário
  
Retorna o nome do usuário atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a uma variável|Variável onde o resultado será salvo|Variable|

### Bloquear tela
  
Bloqueia a tela do Windows
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

### Estou logado?
  
Verifica se o usuário atual está logado e não está bloqueada a tela
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Assign result to a variable|Variável onde o resultado será salvo|Variable|

### Maximizar janela
  
Maximiza uma janela por título
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título|Título da janela para maximizar|Título da janela|

### Restaurar janela
  
Restaura uma janela por título
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título|Título da janela para restaurar|Título da janela|

### Minimizar janela
  
Minimizar uma janela por título
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título|Título da janela para minimizar|Título da janela|

### Listar janelas abertas
  
Lista as janelas abertas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Salvar em|Variável onde o resultado será salvo|Variável|
|Deseja os handles?|Marque se deseja obter os handles das janelas|False|
|Filter|Word to find in the title of the windows|Find word|

### Traga janela para frente
  
Traga uma janela para frente
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título|Título da janela para trazer para frente|Título da janela|

### Encontrar janela
  
Encontre uma janela por título
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título|Título da janela para buscar|Título da janela|
|Salvar em|Variável onde o resultado será salvo|Variável|

### Obter estado do serviço
  
Obter estado do serviço
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Title||Titulo del servicio|
|Salvar resultado em variável|Variável onde o resultado será salvo|Variável|

### Iniciar serviço
  
Este comando inicia um serviço do Windows. Rocketbot.exe deve ser executado como administrador para executar este comando.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título|Título do serviço a iniciar|Título do serviço|
|Atribuir resultado à variável|Variável onde o resultado será salvo|Variável|

### Parar serviço
  
Este comando para um serviço do Windows. Rocketbot.exe deve ser executado como administrador para executar este comando.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título|Título do serviço a parar|Título do serviço|
|Atribuir resultado à variável|Variável onde o resultado será salvo|Variável|

### Mover e redimensionar janela
  
Muda a posição e dimensões de uma janela obtida por título
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Título||Título|
|Coordenadas (x, y)|Coordenadas da janela no desktop|0,0|
|Dimensão (Largura, Altura)|Dimensões da janela|0,0|
