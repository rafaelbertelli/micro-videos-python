# MICRO-VIDEOS

Micro serviço do admin de gerenciamento de vídeos

## Dependências

O projeto pode ser rodado apontando para a máquina local (não recomendado) ou para o ambiente Docker, que pode ser rodado manualmente através de seus comandos ou através do **VSCode Remote Container** (recomendado)

### Docker

-   [Docker](https://docs.docker.com/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

### VSCode

-   [VSCode](https://code.visualstudio.com/Download)
-   [Kit de extensões Remote Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

## Instalação e execução do projeto

Caso necessário, dê as seguintes permisssões:

```bash
chmod +x .docker/entrypoint.sh
```

## Execução do projeto

Preferencialmente, opte por rodar o projeto através do **VSCode Remote Container**.

### Remote container

```vscode
[F1]
> Remote-Containers: Rebuild Container Without Cache
```

### Subir o projeto com docker

```bash
docker-compose up --build     # cria e sobe um novo container
docker-compose up -d          # sobe um container e deixa o terminal livre
```

### Acessar o container do projeto

```bash
docker-compose exec app bash
```

## Execução dos testes

De dentro do container, executar o comando:

```bash
python -m unittest <caminho_do_teste>
# python -m unittest category.tests.unit.domain.test_unit_entities
```
