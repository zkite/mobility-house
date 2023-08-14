import os

import arrow

APP_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(APP_DIR, "files")
FILE_NAME = f"output_{int(arrow.utcnow().timestamp())}.txt"
FILE_PATH = os.path.join(FILES_DIR, FILE_NAME)

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", "5672")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")

AMQP_URL = (
    f"amqp://{RABBITMQ_PASS}:{RABBITMQ_USER}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"
)

DATETIME_FORMAT = "YYYY-MM-DD HH:mm:ss"
QUEUE_NAME = "exchange_queue"
