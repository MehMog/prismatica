
# Prismatica

Prismatica is a FastAPI project with HTMX to explore and view HDR images in AVIF format. This project allows you to list all the photos stored in the `static/images` directory and view them in a browser.

## Features

- List all AVIF images in the `static/images` directory
- View selected images with HTMX
- Responsive design to fit images to the height of the browser

## Project Structure

```
prismatica/
├── Dockerfile
├── README.md
├── main.py
├── poetry.lock
├── pyproject.toml
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   │   └── your-image.avif
│   └── js/
│       └── script.js
└── templates/
    ├── index.html
    └── view_image.html
```

## Installation

### Prerequisites

- Python 3.10 or higher
- Poetry
- Docker

### Steps

1. **Clone the repository:**

```sh
git clone https://github.com/yourusername/prismatica.git
cd prismatica
```

2. **Install dependencies using Poetry:**

```sh
poetry install
```

3. **Run the application locally:**

```sh
poetry run uvicorn main:app --reload
```

4. **Open your browser and go to `http://localhost:8000` to view the application.**

## Docker

### Build the Docker image:

```sh
docker build -t prismatica-app .
```

### Run the Docker container:

```sh
docker run -d -p 8000:8000 --name prismatica-container prismatica-app
```

### Verify the application is running:

Open your browser and go to `http://localhost:8000` to see your FastAPI application running inside the Docker container.

## Usage

- Place your AVIF images in the `static/images/` directory.
- Open the application in your browser.
- Click on an image name to view the image.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [HTMX](https://htmx.org/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

Feel free to customize the `README.md` file further to suit your project's needs.