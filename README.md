# Evil Scientist FASTAPI app 
This is a simple FASTAPI application that simulates an evil scientist's laboratory. The app provides endpoints to create, read, update, and delete experiments.

## Run instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/joeyvigil/EvilScientistCorpV1
    ```
2. CD into the project directory:
    ```bash
    cd EvilScientistCorporation
    ```

3. Install the required dependencies:
    ```bash
    pip install fastapi
    pip install uvicorn
    ```
4. Start the FASTAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```