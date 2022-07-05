
---

# ToDo-List - Back-End - Python <a name="boas-vindas-ao-repositório-todo-list"></a>

---

# Sumário

- [ToDo-List - Back-End - Python](#boas-vindas-ao-repositório-todo-list)
- [O que foi desenvolvido](#o-que-foi-desenvolvido)
- [Conexão com o Banco](#conexao-db)
  - [Conexão local](#conexao-local)
- [Para testar o projeto](#testar-o-projeto)
  - [Rodar API Local](#via-local)
  - [Rodar API por docker](#via-docker)
- [Endpoint's](#endpoint)
  - [Para criar Tarefa POST](#task-post)
  - [Para buscar Tarefas GET](#task-get)
  - [Para atualizar Tarefa por ID PUT](#task-put)
  - [Para deletar Tarefa por ID DELETE](#task-delte)
- [Protótipo](#prototipo)

---

## O que foi desenvolvido: <a name="o-que-foi-desenvolvido"></a>

  Foi desenvolvido um back-end para um sistema de registro de tarefas em Python com framework Flask

  As tarefas são inseridas em um banco de dados **MongoDB** sendo possível modelar os dados através do **pymongo**

  É possível:
   - Inserir Tarefas
   - Remover Tarefas
   - Atualizar Tarefas

---

### Conexão com o Banco: <a name="conexao-db"></a>

#### Conexão local <a name="conexao-local"></a>

**⚠️ IMPORTANTE! ⚠️**

Para conexão local é necessário ter instalado localmente o **MongoDB**

Essa API utiliza as seguintes variáveis de ambiente:

```sh
FLASK_APP=app/app.py
FLASK_ENV=development
MONGO_URI="mongodb://localhost:27017/db"
```

---

## Para testar o projeto: <a name="testar-o-projeto"></a>

1. Clone o repositório:
  * `https://github.com/Thiago-FR/teste-python-salutho.git`.
  * Entre na pasta do repositório que você acabou de clonar

### Rodar API por docker <a name="via-docker"></a>

1. API via Docker [**É Necessário ter o docker-compose v1.29 instalado!**]
  * `docker-compose up -d --build`

2. Ao final da containerização você pode checar o container **app_backend** :
  * `docker ps`

3. Para descer os container basta rodar:
  * `docker-compose down --remove-orphans`


### Rodar API Local <a name="via-local"></a>

2. Instalar as dependências:
  * `python3 -m pip install --upgrade pip`
  * `python3 -m venv .venv && source .venv/bin/activate`
  * `python3 -m pip install -r requirements.txt`

3. Iniciar servidor:
  * `flask run`

Obs: Este projeto utiliza variável de ambiente veja a sessação - [Conexão com o Banco](#conexao-db)

---

## Endpoint's <a name="endpoint"></a>

### Para criar Tarefa POST <a name="task-post"></a>

* Endpoint: `/api/todo-list`

Body
```json
  { 
    "task": "Teste",
    "status": "Pendente",
    "responsible": "Teste"
  }
 ```

Reponse
```json
  {
    "id": 1,
    "task": "Teste",
    "date": "2022-05-13T18:09:08.859Z",
    "status": "Pendente",
    "responsible": "Teste"
  },
```
---

### Para buscar Tarefas GET <a name="task-get"></a>

* Endpoint: `/api/todo-list`

```json
  [
    {
      "id": 1,
      "task": "Teste",
      "date": "2022-05-13T18:09:08.859Z",
      "status": "Pendente",
      "responsible": "Teste"
    },
    ...
  ]
```
---

### Para atualizar Tarefa por ID PUT <a name="task-put"></a>

* Endpoint: `/api/todo-list/<id>`

Body
```json
  {
    "task": "Teste",
    "status": "Pronto",
    "responsible": "Teste"
  }
```
---

### Para deletar Tarefa por ID DELETE <a name="task-delete"></a>

* Endpoint: `/api/todo-list/<id>`

---

## Protótipo <a name="prototipo"></a>
![Prototipo]()
---
