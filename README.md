# An example of setting up a RESTful Pyramid Web Server that communicates with a MySQL database

## Usage

1) Clone this repo (obviously :)!)
2) Run the following command to build the containers and start up both web server and database containers:

    ```bash
    docker compose up --build
    ```

3) In a new terminal window, open an interactive bash shell, initialize the database, and close the shell:

    ---
    > **Note:** This step is no longer needed if using the init-db.sql file.
    ---

    ```bash
    docker exec -it 140a-rest-server bash
    python init-db.py
    exit
    ```

4) Point your browser to one of the two defined routes (might be localhost on some machines):

    ```0.0.0.0:6543/students``` or ```0.0.0.0:6543/student/[some-id]```
