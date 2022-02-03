# An example of setting up a RESTful Pyramid Web Server that communicates with a MySQL database

## Usage Instructions

### Native Usage

---

1) Install MySQL Server on your computer
2) Run init-db.sql to create the database (in the database folder)

    ```bash
    mysql -u root -p
    source init-db.sql
    exit
    ```

3) Install the Python dependencies from requirements.txt

    ```bash
    pip3 install -r requirements.txt
    ```

4) Source the environment variables into your path

   ```bash
   source credentials.env
   ```

   > NOTE: Windows users, I'm sorry your life is always harder. Please follow this guide to read environment variables into your path: <https://bennett4.medium.com/windows-alternative-to-source-env-for-setting-environment-variables-606be2a6d3e1>

5) Run the server

    ```bash
    python3 server.py
    ```

6) Point your browser to the webserver routes (might be ```http://localhost``` on some machines):

    * GET / Route: ```http://0.0.0.0```
    * GET /actors Route: ```http://0.0.0.0/actors```
    * GET /actor/[actor-id] Route: ```http://0.0.0.0/actor/[actor-id]```

### Docker-based Usage

---
0) Create database credentials:
    ```bash
    echo "MYSQL_HOST=" > credentials.env
    echo "MYSQL_USER=" >> credentials.env
    echo "MYSQL_PASSWORD=" >> credentials.env
    echo "MYSQL_DATABASE=" >> credentials.env
    ```

1) Run the following command to build the containers and start up both web server and database containers:

    ```bash
    docker compose up --build
    ```

2) In a new terminal window, open an interactive shell into the web server container and start the web server:

    ```bash
    docker exec -it 140-web-server bash
    python server.py
    ```

3) Point your browser to the webserver routes (might be ```http://localhost``` on some machines):

    * GET / Route: ```http://0.0.0.0```
    * GET /actors Route: ```http://0.0.0.0/actors```
    * GET /actor/[actor-id] Route: ```http://0.0.0.0/actor/[actor-id]```
