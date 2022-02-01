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

4) Run the server

    ```bash
    python3 server.py
    ```

5) Point your browser to the webserver routes (might be ```http://localhost``` on some machines):

    * GET / Route: ```http://0.0.0.0```
    * GET /actors Route: ```http://0.0.0.0/actors```
    * GET /actor/[actor-id] Route: ```http://0.0.0.0/actor/[actor-id]```

### Docker-based Usage

---

1) Run the following command to build the containers and start up both web server and database containers:

    ```bash
    docker compose up --build
    ```

2) In a new terminal window, open an interactive shell into the web server container and start the web server:

    ```bash
    docker exec -it 140a-web-server bash
    python server.py
    ```

3) Point your browser to the webserver routes (might be ```http://localhost``` on some machines):

    * GET / Route: ```http://0.0.0.0```
    * GET /actors Route: ```http://0.0.0.0/actors```
    * GET /actor/[actor-id] Route: ```http://0.0.0.0/actor/[actor-id]```
