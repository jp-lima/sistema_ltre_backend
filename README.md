# LTRE Backend

Backend da aplicação **LTRE**, construído com [FastAPI](https://fastapi.tiangolo.com/) e Python 3.14+. Fornece API REST para autenticação de usuários e cálculos científicos (inicialmente modelos de adsorção), com persistência assíncrona em PostgreSQL via SQLAlchemy.

---

## ✨ Tecnologias

- **[FastAPI](https://fastapi.tiangolo.com/)** — framework web moderno e assíncrono
- **[Pydantic](https://docs.pydantic.dev/) / pydantic-settings** — validação de dados e configuração
- **[SQLAlchemy 2.0](https://www.sqlalchemy.org/) (asyncio)** — ORM assíncrono
- **[asyncpg](https://magicstack.github.io/asyncpg/)** — driver PostgreSQL assíncrono
- **[Alembic](https://alembic.sqlalchemy.org/)** — migrações de banco de dados
- **[Passlib + bcrypt](https://passlib.readthedocs.io/)** — hash de senhas
- **[PyJWT](https://pyjwt.readthedocs.io/)** — tokens JWT
- **[SymPy](https://www.sympy.org/)** — computação simbólica/cálculos
- **[uv](https://docs.astral.sh/uv/)** — gerenciamento de dependências e ambiente virtual

---

## 📁 Estrutura do Projeto

```
.
├── alembic/                    # Configuração e versões de migrações
│   ├── env.py
│   └── versions/
│       └── 001_create_users_table.py
├── src/
│   ├── app.py                  # Aplicação FastAPI e rotas principais
│   ├── config.py               # Configurações via variáveis de ambiente
│   ├── database.py             # Engine, sessão e base do SQLAlchemy
│   ├── auth/                   # Módulo de autenticação
│   │   ├── models.py           # Modelo User
│   │   ├── routes.py           # Endpoints de autenticação
│   │   ├── schema.py           # Schemas Pydantic
│   │   ├── security.py         # JWT, hash de senha e cookies
│   │   └── services.py         # Lógica de registro/login
│   ├── calculations/           # Módulo de cálculos científicos
│   │   └── adsorption/         # Cálculos de adsorção (em desenvolvimento)
│   │       ├── routes.py
│   │       ├── schemas.py
│   │       └── services.py
│   └── ltre_backend/           # Pacote principal
├── .env                        # Variáveis de ambiente (não versionado)
├── .env.example                # Exemplo de variáveis de ambiente
├── alembic.ini                 # Configuração do Alembic
├── pyproject.toml              # Metadados e dependências do projeto
└── uv.lock                     # Lock de dependências do uv
```

---

## ⚙️ Pré-requisitos

- Python >= 3.14
- [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado
- Banco de dados PostgreSQL acessível (local, Docker ou serviço como Supabase)

---

## 🚀 Instalação

Clone o repositório e instale as dependências com o `uv`:

```bash
uv sync
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

---

## 🔑 Configuração

Copie o arquivo de exemplo e ajuste as variáveis de ambiente:

```bash
cp .env.example .env
```

Edite o `.env`:

```env
DATABASE_URL=postgresql+asyncpg://usuario:senha@host:5432/banco
SECRET_KEY=sua-chave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ Em produção, use uma `SECRET_KEY` forte e configure `secure=True` no cookie de autenticação (`src/auth/security.py`).

---

## 🗄️ Banco de Dados e Migrações

O projeto utiliza Alembic para controle de versão do esquema do banco. Para aplicar as migrações:

```bash
alembic upgrade head
```

Para gerar uma nova migração após alterar os modelos:

```bash
alembic revision --autogenerate -m "descrição da mudança"
```

---

## ▶️ Executando a Aplicação

### Modo de desenvolvimento (com recarga automática)

```bash
uv run fastapi dev src/app.py
```

### Modo de produção

```bash
uv run uvicorn app:app --app-dir src --host 0.0.0.0 --port 8000
```

A documentação interativa estará disponível em:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 🔒 Autenticação

A autenticação é baseada em **JWT** armazenado em cookie `HttpOnly` chamado `access_token`.

### Endpoints disponíveis

| Método | Endpoint         | Descrição                              |
|--------|------------------|----------------------------------------|
| POST   | `/auth/register` | Cadastra um novo usuário               |
| POST   | `/auth/login`    | Realiza login e define o cookie JWT    |
| POST   | `/auth/logout`   | Remove o cookie de autenticação        |
| GET    | `/auth/me`       | Retorna os dados do usuário logado     |

### Exemplo de registro

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "João Silva",
    "email": "joao@email.com",
    "password": "senha123"
  }'
```

---

## 🧪 Testes

> Em breve. Atualmente o projeto não possui suite de testes configurada. Contribuições são bem-vindas!

---

## 📝 Licença

Este projeto é privado e foi desenvolvido por [jota](mailto:jpbrasil763@gmail.com).

---

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou novos cálculos científicos.
