# system-biblioteca
(Projeto de desenvolvimento web 2 cujo objetivo a criação de um sistema em arquitetura MVC que rode localmente)

O projeto system-biblioteca consiste em um sistema de gerenciamento de biblioteca criado em Arquitetura MVC e utilizando o paradigma arquitetural de Microsservicos, cujo objetivo é a organização dos dados referentes ao funcionamento da biblioteca em que é aplicado, permitindo o registro, armazenamento a manipulação de dados referentes aos bibliotecários que nela trabalham, os livros que se encontram disponíveis, os emprestimos realizados, e os leitores cadastrados para os emprestimos de livros. 

## Tecnologias utlizadas
* VS Code: Ambiente de desenvolvimento utilizado no desenvolvimento do projeto;
* SQLite3: Sistema de gerenciamento de banco de dados utlizado para a criação do banco e manipulação dos dados nele armazaenados;
* SQLAlchemy: Biblioteca Python utilizada para trabalhar com bancos de dados por meio de linguagem python, sendo usada na criação do banco de dados e suas tabelas (tables), além da interação das demais partes do sistema com o bancod de dados;
* Flask: Microframework web para Python usado no desenvolimento de aplicações web e APIs, sendo utilizada no back-end do projeto para o estabelecimento das rotas que o sistema usa para integarir com o banco de dados, além de também ter sido utilizado para a definição de rodas das telas do front-end, permitindo que a página inicial (index.html) seja aberta por meio do link localhost gerado ao ativar o sistema;
* Bootsrap: Framework front-end baseado em HTML, CSS e JavaScript usado para criar interfaces web responsivas e modernas, tendo sido aplicado no front-end deste projeto para a criação das telas que permitem a interação com as operações CRUD de manipulação de dados no banco;
* Linguagems de programação:
  * Python: Utilizado no banco de dados em conjunto com SQLAlquemy e back-end em conjunto com o Flask;
  * HTML, CSS e JavaScript: utlizados Front-end, sendo facilitados pelo uso do Bootstrap.

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

### Banco de dados

Primeiro, verifique se seu dispositivo possui SQLite3 instalado, Caso não, instale-o com o seguinte comando de terminal caso esteja em sistema Linux:

```bash
sudo apt install sqlite3
```

Em caso de estar usando Windows, use o site oficial do SQLite para baixar um instalador em arquivo .zip (https://sqlite.org/download.html).

Com o ambiente virtual ativado, insira o código abaixo no terminal para criar o banco de dados, sendo gerada uma pasta "data", a qual armazenara o arquivo biblioteca_db.db, sendo este o arquivo de banco de dados gerado com o SQLite3:

```bash
python create_tables.py
```

Após isso, insira no terminal o comando abaixo para popular o banco de dados com os dados iniciais padrão (Você pode usar este comando novamente caso queirar que os dados do banco voltem a um estado padrâo):

```bash
python seed.py
```
### Rodar código

Após criar e popular o banco de dados, voçê pode rodar o sistema por meio do código abaixo, inserindo-o no terminal:

```bash
python run.py
```

Com este código rodando, será geado no terminal um link Localhost (http://127.0.0.1:5000) o qual você pode usar em seu navegador para acessar o sistema por meio do front-end em página web local a qual está conectada ao banco de dados por meio do Flask.

Para fazer com que o run.py pare de rodar, voce pode utilizar ctrl + c no terminal para finalizar a seção.

### Tutorial do front-end
