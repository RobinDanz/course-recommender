# Usage

## Docker container

1. Locate terminal in `course-recommender/recommender-server/`

2. Launch the containers:

`docker-compose up --build -d`

## Mixing local and Docker container

In this setup the api will run locally and the database will run in Docker containers.

1. Locate terminal in `course-recommender/recommender-server/`

2. Create a python virtual environnment

`python3 -m venv .venv`

3. Activate the virtual environnment

`source .env/bin/activate`

4. Install dependencies

`pip install -r requirements.txt`

5. Launch the containers (run them all once to apply database migrations)

`docker-compose up --build -d`

6. Stop the `api` container

`docker container stop api`

7. Run the API locally (form the /src/ folder)

`uvicorn main:app --reload`

## Access
API Swagger URL: http://127.0.0.1:8000/docs

Adminer URL: http://127.0.0.1:8080/

# Migrations

The database migrations are handled with Alembic. 

## Create migration:
### When creating a new model: 
1. Create the model in `models` folder
2. Import the created model in the `migrations/env.py` file
    
    ```python
    # Models
    from models.user import User
    from models.course import Course  # Newly created model
    ```
3. Generate and apply the migration as explained in the next section

### Generate the migration
After any modification in one of the registered models, run the following command to create a migration file:

`alembic revision --autogenerate -m "message"`

This command will generate a file in the `migrations/versions` folder. The file will be named after the following pattern: `id_message.py`

## Apply migrations
In order to update the database to the last migration, run the following command: 

`alembic update head`

## Additional Information
### Use case
When running the server in Docker containers it is not needed to manually create the database and apply the migration. It is only required when using a local database.


### Official documentation
This section is only a condensed tutorial to get an up-to-date database. For more informations about Alembic refer to [the offical tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html).




