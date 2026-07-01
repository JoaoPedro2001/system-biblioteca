# system-biblioteca
(Projeto de desenvolvimento web 2 cujo objetivo original era criação de um sistema em arquitetura MVC que rode localmente, e que agora foi expandido para aplicação em nuvem)

O projeto system-biblioteca consiste em um sistema de gerenciamento de biblioteca criado em Arquitetura MVC e utilizando o paradigma arquitetural de Microsservicos, cujo objetivo é a organização dos dados referentes ao funcionamento da biblioteca em que é aplicado, permitindo o registro, armazenamento a manipulação de dados referentes aos bibliotecários que nela trabalham, os livros que se encontram disponíveis, os emprestimos realizados, e os leitores cadastrados para os emprestimos de livros. 

## Tecnologias utlizadas
* VS Code: Ambiente de desenvolvimento utilizado no desenvolvimento do projeto;
* PostgreSQL: Sistema de gerenciamento de banco de dados utlizado para a criação do banco e manipulação dos dados nele armazaenados;
* SQLAlchemy: Biblioteca Python utilizada para trabalhar com bancos de dados por meio de linguagem python, sendo usada na criação do banco de dados e suas tabelas (tables), além da interação das demais partes do sistema com o bancod de dados;
* Flask: Microframework web para Python usado no desenvolimento de aplicações web e APIs, sendo utilizada no back-end do projeto para o estabelecimento das rotas que o sistema usa para integarir com o banco de dados, além de também ter sido utilizado para a definição de rodas das telas do front-end, permitindo que a página inicial (index.html) seja aberta por meio do link localhost gerado ao ativar o sistema;
* Bootsrap: Framework front-end baseado em HTML, CSS e JavaScript usado para criar interfaces web responsivas e modernas, tendo sido aplicado no front-end deste projeto para a criação das telas que permitem a interação com as operações CRUD de manipulação de dados no banco;
* Docker: O Docker é uma plataforma de conteinerização que permite empacotar uma aplicação e todas as suas dependências, como bibliotecas, arquivos de configuração, entre outros, em um único "contêiner", sendo implementado neste Projeto para realizar o isolamento dos microsserviços projetados, além de ser utilizado na aplicação do frontend e na implementação de cache, atuando em conjunto com o Redis;
* PyJWT: O PyJWT é uma biblioteca Python utilizada para codificar e decodificar JSON Web Tokens, um padrão de comunicação compacto e seguro o qual pode ser usado para troca de informações sensíveis para fins de validação em sistemas, sendo utilizado no projeto para a aplicação do sistema de autenticação presente no login; 
* bcrypt: O bcrypt é uma biblioteca usada para realizar atividades de criptografia e hashing de senhas. Baseada em um algoritmo criptográfico de mesmo nome, ele é aplicado no projeto como medida de segurança para a proteção de senhas salvas no banco, sendo utilizado nos serviços de cadastro e atualização de senhas para bibliotecários e nos sistemas de povoamento do banco com dados iniciais;
* Redis: O Redis é um armazenamento de estrutura de dados em memória o qual é usado principalmente em banco de dados, message broker, e cache, sendo utilizado no projeto para a implementação deste ultimo em conjunto com o docker. O cache gerado com o redis é aplicado nas operações crud refentens ao armazenamento de dados de livros; 
* Linguagems de programação:
  * Python: Utilizado no banco de dados em conjunto com SQLAlquemy e back-end em conjunto com o Flask;
  * HTML, CSS e JavaScript: utlizados Front-end, sendo facilitados pelo uso do Bootstrap.

## Estrutura dos microsserviços

O sistema do projeto de biblioteca foi reestruturado para o paradigma arquitetural de microsserviços. Devido a isso, ele se apresenta com uma nova estrutura organizacional, focada em três pastas principais, as quais interagem com containers do docker para manterem seu conteúdo independentes dentre sí, com cada microsservico contendo seu próprio banco de dados independente. tais pastas também possuem uma estrutura MVC interna, armazenam os códigos referentes a criação de tabelas e povoamento de dados iniciais dos próprios bancos de dados, e abriagam os códigos de serviço referentes as operações CRUD do sistema. As pastas de microsseviço são dividas em:

* auth_service: Responsável por abrigar o banco de dados referente aos bibliotecários, assim como o sistema de autenticação do projeto e os serviços;
* catalog_service: Responsável pelo armazenameto de dados referentes a livros e leitores cadastrados no sistema;
* loans_service: Responsável por armazenar os dados referentes aos emprestimos realizados com o sistema, assim como os códigos das operações CRUD responsáveis por tais emprestimos.

## Regras de negócio

O sistema do projeto também possui em seu código um conjunto de regras de negócio, um conjunto de diretrizes implementadas em código as quais determinam o comportamento do sistema com relação a certas interações que nele podem ocorrer. Tais regras são:

### Regras de emprestimo (Loans):

* Regra 1 - Não permitir empréstimo de livro indisponível

* Regra 2 - Atualizar status do livro automaticamente

* Regra 3 - Não permitir exclusão de empréstimo ativo

### Regras de catálogo (Catalog):

* Regra 1 - Não permitir exclusão de livro emprestado

* Regra 2 - Não permitir exclusão de leitor com empréstimos ativos

* Regra 3 - Não permitir duplicidade de leitores cadastrados (duplicação de email)

### Regras de autenticação (Auth):

* Regra 1 - Não permitir duplicidade de bibliotecarios cadastrados (duplicação de email)

## Como configurar

Após baixar o código do sistema em seu ambiente de desenvolvimeto, deve-se preparar o ambiente virtual venv, o qual já vem inserido no Python. O venv possui duas formas de preparo dependendo se está sendo utilizado um sistema Linux ou Python. Abaixo, encontram-se as instruçoes para ambos (O desenvolvimento do projeto foi feito em sistema Linux Mint):

### Linux

No seu ambiente, abra o terminal e certifiquisse de que está interagindo com a pasta do sistema (system-biblioteca). Em seguida, insira no terminal:

```bash
python3 -m venv .venv
```

Após isso, insira o código abaixo para ativar o ambiente virtual venv, devendo aparecer (venv) escrito em seu terminal quando for ativado:

```bash
source .venv/bin/activate
```
### Windows

No seu ambiente, abra o terminal e certifiquisse de que está interagindo com a pasta do sistema (system-biblioteca). Em seguida, insira no terminal:

```CMD
python -m venv .venv
```

Após isso, insira o código abaixo para ativar o ambiente virtual venv, devendo aparecer (venv) escrito em seu terminal quando for ativado:

```CMD
.venv\Scripts\activate.bat
```

### Destivar venv

Em ambos os casos, você pode desativar o venv usando o seguinte comando no terminal:

```bash
deactivate
```

### Requirements

Este sistema opera contendo um conjunto de arquivos requirements.txt dentro das pastas de microsserviços os quais contem listas de extensões necessarias para rodar o seu respectivo microsseviço no sistema. Devido a forma como estas pastas foram confirguradas para rodar com o docker, elas não quererem instalação manual, com as extensões presentes sendo automaticamente aplicadas quando o docker é ativado. A instalação do docker é um processo que vária de acordo diversos elementos do sistema em que se deseja implementar, devido a isso, deve-se buscar informações sobre sua instalação em sua página oficial referente a implementação em sistemas:

<https://docs.docker.com/desktop/>

Com o docker instalado, você deve fazer com que ele inicie rodando o seguinte comando na raiz do projeto, por meio do terminal:

```bash
docker compose up --build -d
```

Além disso, para poder aplicar o banco de dados do sistema, é necessário instalar o PostgreSQL, que de forma similar ao docker, possui processos de instalação distintos de acordo com o sistema que se esteja trabalhando. devido a issso, deve-se buscar amis informações para a sua instalação em sua página oficial:

<https://www.postgresql.org/download/>

### Banco de dados

Devido a estrutura de microsserviços, o banco de dados do projeto consiste em diferentes bancos os quais existem de forma independente em cada microsserviço interagindo entre si por meio das aplicações de serviço e as regras de negócio que neles são aplicadas. Tais bancos de dados são gerenciados com o uso PosgreSQL o qual é aplicado em conjundo com o docker para gerar suas tabelas e povoa-las. Para aplicar as tabelas dos bancos de dados do projeto, deve-se  prineiro inicializar o docker e após isso, aplciar os seguintes comandos na raíz do terminal:

```bash
docker compose exec auth_service python create_tables.py

docker compose exec catalog_service python create_tables.py

docker compose exec loans_service python create_tables.py
```
Após isso, para povoar as tabelas geradas, aplica-se os seguintes comandos:

```bash
docker compose exec auth_service python seed.py

docker compose exec catalog_service python seed.py
```

Percebe-se que não há comnando para povar as tabelas referentas a loans_service, isso é intencional, pois o banco deste microsserviço é responsável pelos registros de emprestimos de livros, e por padrão, se iniciam vazíos no sistema.

### Rodar código

Após criar e popular o banco de dados, voçê pode utilizar o sistema, o qual começa a rodar de forma automática no momento em que voçe inicia o docker.

Para acessar o sitema do projeto, utilize o link Localhost (http://127.0.0.1:8080) o qual você pode usar em seu navegador para acessar o sistema por meio do front-end em página web local a qual está conectada ao banco de dados por meio do Flask.

Para fazer com que o sistema pare de rodar, voce pode o comando abaixo no terminal para finalizar a seção.

```bash
docker compose down
```

### Tutorial do front-end

Ao acessar o front-end por meio do link localhost, você verá uma tela inicial a qual apresenta um sisteam de login do sistema. Para acessá-lo, deve-se informar o e-mail de usuário e sua respectiva senha. Para fins de primeiro acesso, pode-se utilizar o acesso do administrador:

* E-mail: admin@biblioteca.com
* senha: admin123

Ao preencher corretamente o e-mail e senha, clique em entrar para obter acesso ao sistema e sua primeira tela.

#### Menu

A tela inicial do sistema após a realização fo login. A tela de menu contem quatro botões principais, os quais o levarão para a pagina de visualização das tabelas correspondentes e que também contem as opções de interação das operações CRUD com o banco de dados. A tela de menu também possui um quinto botão no canto superiro esquerdo nomeado logout, o qual pode ser usado para retornar a página de login. Com relação aos botões principais, eles são:

* Livros;
* Leitores;
* Bibliotecários;
* Empréstimos;

#### Livros

Na página de livros voccê possui a tela de visualização dos livros, na qual você pode ver os livros cadastrados no banco de dados. Abaixo se encontram botões de interação, permitindo operações CRUD com o banco.

* Novo Livro abre uma página para a inserção de dados para uma nova instância da entidade livro;
* Ao selecionar uma das instâncias por meio das caixas de seleção (Selecionar), você obtem acesso a Editar Livro e Remover Livro:
 * Editar Livro puxa os dados da instância selacionada e permite que você os altere;
 * Remover Livro apaga a instância selecionada da do banco de dados.
* O botão Voltar retorna a tela inicial;

#### Leitores


Na página de leitores voccê possui a tela de visualização dos leitores, na qual você pode ver os leitores cadastrados no banco de dados. Abaixo se encontram botões de interação, permitindo operações CRUD com o banco.

* Novo Leitor abre uma página para a inserção de dados para uma nova instância da entidade leitor;
* Ao selecionar uma das instâncias por meio das caixas de seleção (Selecionar), você obtem acesso a Editar Leitor e Remover Leitor:
 * Editar Leitor puxa os dados da instância selacionada e permite que você os altere;
 * Remover Leitor apaga a instância selecionada da do banco de dados.
* O botão Voltar retorna a tela inicial;

#### Bibliotecários

Na página de bibliotecários voccê possui a tela de visualização dos bibliotecários, na qual você pode ver os bibliotecários cadastrados no banco de dados. Abaixo se encontram botões de interação, permitindo operações CRUD com o banco.

* Novo Bibliotecário abre uma página para a inserção de dados para uma nova instância da entidade leitor. Diferente dos anteriores, Novo Bibliotecário possui campos "Senha" e "Confirmar Senha" as quais o dado preenchido deve ser o mesmo caso o contrário, o sistema não aceita a nova instância;
* Ao selecionar uma das instâncias por meio das caixas de seleção (Selecionar), você obtem acesso a Editar Bibliotecário e Remover Bibliotecário:
 * Editar Bibliotecário puxa os dados da instância selacionada e permite que você os altere. Os campos  "Senha" e "Confirmar Senha" em Editar Bbiliotecário funcionam da mesma maneira que em Novo Bibliotecário, porém você pode optar por deixar os dois campos em branco para manter a senha já cadastrada;
 * Remover Bibliotecário apaga a instância selecionada da do banco de dados.
* O botão Voltar retorna a tela inicial;

#### Empréstimos

Na página de empréstimos voccê possui a tela de visualização dos empréstimos, na qual você pode ver os empréstimos cadastrados no banco de dados. Abaixo se encontram botões de interação, permitindo operações CRUD com o banco.

* Novo Empréstimo abre uma página para a inserção de dados para uma nova instância da entidade leitor. Diferente dos anteriores, os campos de Novo Empréstimo não são livres, mas possuem opções pré-determinadas baseadas no  conteúdo das tabelas de livro, leitor e bibliotecário, permitindo definir qual livro está sendo emprestado, qual leitor está recebendo o livro e qual biliotecário fez o empréstimo;
* Ao selecionar uma das instâncias por meio das caixas de seleção (Selecionar), você obtem acesso a Editar Empréstimo e Remover Empréstimo:
 * Editar Empréstimo puxa os dados da instância selacionada e permite que você os altere. Diferente dos anteriores, Editar Empréstimo póssui uma caixa de seleção "Renovar empréstimo (+7 dias)", a qual irá automaticamente adicionar mais uma semana a data de devolução;
 * Remover Empréstimo apaga a instância selecionada da do banco de dados.
* O botão Voltar retorna a tela inicial;
 
