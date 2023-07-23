# Similarity Search Service with Django

This is a Django web application that allows to create Items, and search similarities (cosine similarity) between Items.description fields. by using REST API

after launching application you can use tools lik a Postman, python requests,cURL, to make http requests. API dosc/endpoints available on http://127.0.0.1:8000/api/schema/docs/

+ +Docker, Postgres


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mrhetsko/similarities_search.git
   ```
2. Move to "sservice" directory:
   ```bash
   cd similarity_search
   ```

3. Create virtual environment:
   ```bash
   python3 -m venv venv --upgrade-deps
   ```
   
4. Activate virtual environment:
    ```bash
    venv/Scripts/activate.ps1
   or
   source venv/bin/activate  on Unix

   
5. Install requirements:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
6. Take care about database configuration in ```base/settings.py```. If you want tu use default sqlite3- uncomment it in settings.py and comment postgresql.


7. Migrations
   ```bash
   python3 manage.py makemigrations
   ```

8. Migrate
   ```bash
   python3 manage.py migrate```
   
8. Run development server 
   ```bash
   python3 manage.py runserver
   ```
### Now application available on your localhost: default - http://127.0.0.1:8000


## Using Docker:

1. Clone the repository:

   ```bash
   git clone https://github.com/Mrhetsko/similarities_search.git
   ```
2. Move to sservice directory:
   ```bash
   cd similarity_search

3. Build & launch:
   ```bash
   docker-compose up -d
   ```



### Now application available on your localhost: default - localhost:8000 or 127.0.0.1:8000