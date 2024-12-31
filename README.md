# Note API

This is a simple Note API built with Python. It allows users to create, read, update, and delete notes.

## Features

- Create a new note
- Retrieve all notes
- Retrieve a single note by ID
- Update a note by ID
- Delete a note by ID

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aakinlalu/note-api.git
    ```
2. Navigate to the project directory:
    ```bash
    cd note-api
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    fastapi dev
    ```
2. The API will be available at `http://127.0.0.1:8000`.

## Endpoints

- `GET /notes` - Retrieve all notes
- `GET /notes/<id>` - Retrieve a single note by ID
- `POST /notes` - Create a new note
- `PUT /notes/<id>` - Update a note by ID
- `DELETE /notes/<id>` - Delete a note by ID

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [yourname@example.com](mailto:yourname@example.com).
