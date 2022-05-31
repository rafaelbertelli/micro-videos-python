# MICRO-VIDEOS

Micro serviço do admin de gerenciamento de vídeos

## Dependências

O projeto pode ser rodado apontando para a máquina local (não recomendado) ou para o ambiente Docker, que pode ser rodado manualmente através de seus comandos ou através do **VSCode Remote Container** (recomendado)

### VSCode

- [VSCode](https://code.visualstudio.com/Download)
- [Kit de extensões Remote Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

### Docker

- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Local

- [Python 3.10](https://www.python.org/)
- [PDM](https://pdm.fming.dev/)

## Instalação e execução do projeto

Caso necessário, dê permissão para o caminho:

```bash
chmod +x .docker/entrypoint.sh
```

## Execução do projeto

Preferencialmente, opte por rodar o projeto através do **VSCode Remote Container**.

### Remote container

```bash
[F1]
> Remote-Containers: Reopen in Container                # abre o projeto em um container existente
> Remote-Containers: Rebuild Container Without Cache    # abre o projeto em um container recriado
```

### Docker (manualmente)

```bash
docker-compose up -d          # abre o projeto em um container existente
docker-compose up --build     # abre o projeto em um container recriado
```

### Local (manualmente)

```bash
pdm install
```

### Acessar o container do projeto

```bash
docker-compose exec app bash
```

## Execução dos testes

Os testes podem ser executados via **interface do VSCode** ou linha de comando

```bash
python -m pytest <caminho_do_teste>
# python -m pytest category.tests.unit.domain.test_unit_entities
```
