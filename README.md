# crud-cliente

Este é um projeto em python acerca de desenvolvimento web utilizando a biblioteca django do Python. Nele foi criado um login básico, um model e o crud do cliente.

## Criando e executando o ambiente virtual

Já com o python instalado:

No mesmo local onde está a pasta "projeto" deve ser criado o ambiente virtual, para isso vamos instalar a biblioteca virtualvenv:

'python -m venv venv'

Com o ambiente criado, para ativá-lo vamos usar:

`.\venv\Scripts\activate`

## Instalando os requerimentos

Após isso, para instalar as extensões que serão utlizadas no ambiente virtual:

`cd projeto`

`pip install -r requirements.txt`

## Criando usuário

Após isso, iremos criar um superusuário para ter acesso ao sistema:

`python manage.py createsuperuser`

## Rodando a máquina

Com tudo feito, para rodar a máquina:

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

Após isso, basta copiar o endereço criado e colar no navegador.

