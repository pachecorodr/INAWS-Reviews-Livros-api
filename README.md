# INAWS-Reviews-Livros-api

## Descrição
O projeto **Reviews-Livros** é uma aplicação onde qualquer usuário pode adicionar livros e avaliá-los 

O projeto está sendo utilizado nas disciplinas de **Interface Homem-Máquina** e **Infraestrutura em Nuvem com AWS**.

### Autores
- [@pachecorodr](https://github.com/pachecorodr)

## Variáveis de Ambiente
Para rodar esse projeto localmente, você precisará adicionar as seguintes variáveis de ambiente no seu arquivo `.env`:

- `POSTGRES_H`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `POSTGRES_PORT`

## Rodando Localmente

### 1. Clone o projeto
```bash
git clone https://github.com/pachecorodr/INAWS-Reviews-Livros-api.git 
```
### 2. Entre no diretório do projeto
```bash
cd INAWS-Reviews-Livros-api
```
### 3. Construa uma imagem a partir do docker-compose.yaml
```bash
docker-compose -f docker/docker-compose.yaml -p backend_inaws_reviews_livros up --build
```
## Rodando as migrações do banco de dados

### 1. Após subir os containers, aplique as migrações para garantir que o banco esteja atualizado
```bash
docker exec -it backend_dose_certa-backend-1 alembic upgrade head
```
### 2. Caso precise criar uma nova migração ao modificar os modelos:
```bash
docker exec -it backend_inaws_reviews_livros-backend-1 alembic revision --autogenerate -m "descrição da migração"
docker exec -it backend_inaws_reviews_livros-backend-1 alembic upgrade head
```

## Documentação da API 
A API possui documentação gerada pelo Swagger. Após construir a imagem no Docker, acesse a documentação em:

http://localhost:8000/docs

## Relacionado 

Segue a API do projeto: https://github.com/pachecorodr/INAWS-Reviews-Livros
