import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "database": os.getenv("DB_NAME", "agenda"),
    "user": os.getenv("DB_USER", "username"),
    "password": os.getenv("DB_PASSWORD", "password")
}
