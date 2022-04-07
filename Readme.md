# Cidade API

## Installation

Para rodar o projeto será necessário as seguintes tecnologias:
* docker
* python

### Se você estiver no linux basta rodar
```sh
make run
```
Com isso irá subir seu projeto com docker no localhost

### Se você estiver no windowns basta rodar
```sh
docker-compose up -d
```
Com isso irá subir seu projeto com docker no localhost

## Testes

Para rodar os testes será necessário subir o banco postgres no docker, caso ele não esteja inicializado e depois rodar os testes :

### Se você estiver no linux basta rodar
```sh
make run-postgres

make check
```

### Se você estiver no windowns basta rodar
```sh
docker start city-api-postgres 2>/dev/null || docker run --name city-api-postgres -p 5432:5432 -e POSTGRES_PASSWORD='postgres' -d postgres:10-alpine

pytest -vv -x --cov=apps
```
