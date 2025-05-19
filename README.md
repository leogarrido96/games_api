# Games API

This project is a RESTful API for managing a collection of games. It allows users to create, read, update, and delete game records. The API is designed for easy integration with frontend applications or other services.

## Features

- List all games
- Retrieve details of a specific game
- Add new games
- Update existing games
- Delete games

## Technologies Used

- Python
- Django REST Framework
- /PostgreSQL/ (Next step)
- Docker (Next step)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/games_api.git
    cd games_api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables (if needed). You can copy the example file and edit it:
    ```bash
    cp .env.example .env
    ```
    Update the `.env` file with your database credentials and other settings.

5. Run database migrations (if applicable):
    ```bash
    alembic upgrade head
    ```
    Or use your framework's migration tool.

6. Start the development server:
    ```bash
    uvicorn main:app --reload
    ```
    Adjust the command if using Flask or Django.

## Usage

Once the server is running, you can access the API at `http://localhost:8000` (or the port you configured).

- Test endpoints using [Postman](https://www.postman.com/) or [curl](https://curl.se/).
- API documentation is available at `/docs` (Swagger UI) and `/redoc` (ReDoc) if using FastAPI.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License.
