# MICRO-VIDEOS

Micro serviço do admin de gerenciamento de vídeos

## Instalação e execução

### Subir o projeto com docker

```bash
docker-compose up --build     # cria e sobe um novo container
docker-compose up -d          # sobe um container e deixa o terminal livre
```

### Acessar o volume do projeto

```bash
docker-compose exec app bash
```

### Remote container (vscode)

Caso tenha instalado a instenção do vscode, remote container, a instalação e execução do projeto pode ser feita através dela ao invés de subir manualmente o ambiente no docker.

# Executar os testes:

De dentro do container, executar o comando:

```bash
python -m unittest <caminho_do_teste>
# exemplo:
# python -m unittest category.domain.tests.test_entities
```
