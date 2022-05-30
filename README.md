# MICRO-VIDEOS

Micro serviço do admin de gerenciamento de vídeos

## Dependências

-   [Docker](https://docs.docker.com/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

## Instalação e execução do projeto

Caso necessário, dê as seguintes permisssões:

```bash
chmod +x .docker/entrypoint.sh
```

### Subir o projeto com docker

```bash
docker-compose up --build     # cria e sobe um novo container
docker-compose up -d          # sobe um container e deixa o terminal livre
```

### Acessar o volume do projeto

```bash
docker-compose exec app bash    # ou
docker-compose exec app zsh
```

### Remote container (vscode)

Caso tenha instalado a instenção do vscode, remote container, a instalação e execução do projeto pode ser feita através dela ao invés de subir manualmente o ambiente no docker.

## Execução dos testes

De dentro do container, executar o comando:

```bash
python -m unittest <caminho_do_teste>
# exemplo:
# python -m unittest category.tests.unit.domain.test_unit_entities
```
