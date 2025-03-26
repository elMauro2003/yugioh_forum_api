# Yugioh Forum API project

## Previous knowledge
<!-- UL -->
1. [Git](https://github.com/)
2. [Python](https://www.python.org/)
3. [Fastapi](https://fastapi.tiangolo.com/)

## Getting started

Follow the steps below to install the app in your corresponding environment

## Download the repository via git

```
# Clone git repo in your path
git clone https://github.com/elMauro2003/yugioh_forum_api.git
      
```

## Development environment 

Create your virtual env 

```
Example:
python -m venv env    
```
Linux Run env
```
source env/bin/activate
```

Windows Run env
```
env\Scripts\activate
```


## Install the project requirements

>Run next comand 
```
pip install -r requirements.txt
```

## Configure .env file with environment variables


Create your .env and configure it if you use production environment. 

Run db.sqlite3 by default

```
DATABASE_URL = <''>    # default sqlite:///./test.db in postgres case 'postgresql://user:password@host:port/database_name'
ALLOWED_HOSTS = <example.com, example2.com >  # default '*'

```


## Run server

```python
uvicorn main:app --reload
```


## Generate migration:

```cmd
alembic revision  -m "init"
```

## Apply migration:

```cmd
alembic upgrade head
```