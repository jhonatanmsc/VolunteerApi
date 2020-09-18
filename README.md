# VolunteerApi

neste projeto usei as tecnologias:
- fastapi (microframework python)
- postgres
- docker
- docker compose
- sqlalchemy
- alembic

para rodar o projeto vc precisará de docker e docker compose instalado em sua maquina

comandos para iniciar:
```bash
$ cp app/.env.example app/.env
$ docker-compose build
$ docker-compose up -d
```

e pronto se tudo tiver dado certo você poderá acessar a tela do swagger para testar os endpoints :D, para isso basta acessar localhost:8000/docs
