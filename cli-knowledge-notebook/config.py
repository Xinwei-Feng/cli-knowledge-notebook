import os

DB_CONFIG = {
    "host": os.getenv("NB_HOST", "localhost"),
    "user": os.getenv("NB_USER", "root"),
    "password": os.getenv("NB_PASSWORD", ""),
    "database": os.getenv("NB_DATABASE", "notebook"),
    "charset": "utf8mb4"
}
