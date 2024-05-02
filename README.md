# Leader (Projeto em andamento)
## API Leader - Documentação
Este projeto consiste em uma API desenvolvida com Django e Django Rest Framework para gerenciar produtos e carrinhos de compras em um sistema de comércio.

### Configuração do Ambiente

#### Pré-requisitos
Certifique-se de ter o Python e o pip instalados em sua máquina.

### Instalação do Ambiente Virtual
#### 1. Clone este repositório:

:~$ git clone https://github.com/HelderMenegatti/Leader

#### 2. Clone este repositório:

:~$ cd Leader/api_leader_v2/

#### 3. Crie um ambiente virtual utilizando o virtualenv:

:~$ virtualenv virtualenv

#### 4. Ative o ambiente virtual:

:~$ source virtualenv/bin/activate

### Instalação das Dependências

Dentro do ambiente virtual, instale as dependências do projeto utilizando o pip:

:~$ pip install -r requirements.txt

### Configuração do Arquivo .env

#### 1. Copie o arquivo .env.example para .env:

:~$ cp .env.example .env

#### 2. Edite o arquivo .env com as configurações necessárias, como as credenciais do banco de dados PostgreSQL.

#### 3. Realize as migrações:

:~$ python manage.py migrete

### Utilização da API
#### Execução do Servidor
Para iniciar o servidor local, execute o seguinte comando:

:~$ python manage.py runserver

O servidor estará disponível em http://localhost:8000/.

### Endpoints Disponíveis até o presente momento

/api/products/: Endpoint para visualização, criação, edição e exclusão de produtos.

/api/carts/: Endpoint para visualização, criação, edição e exclusão de carrinhos de compras.

/api/cart-items/: Endpoint para visualização, criação, edição e exclusão de itens do carrinhos de compras.
