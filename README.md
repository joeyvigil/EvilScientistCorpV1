# Evil Scientist FASTAPI app 
This is a simple FASTAPI application that simulates an evil scientist's laboratory. The app provides endpoints to create, read, update, and delete experiments.

## Run instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/joeyvigil/EvilScientistCorpV1
    ```
2. Open terminal in base directory on vs code

3. Install the required dependencies:
    ```bash
    pip install fastapi
    pip install uvicorn
    ```
4. Start the FASTAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```
    to close the server, press `CTRL + C` in the terminal.

5. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.