# src/utils/logger.py
import logging
import os

# Pastikan folder logs/ ada
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "system.log")

# Konfigurasi dasar logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # bisa diubah ke DEBUG jika mau lebih detail
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(msg: str) -> None:
    """Catat log level INFO."""
    logging.info(msg)

def log_warning(msg: str) -> None:
    """Catat log level WARNING."""
    logging.warning(msg)

def log_error(msg: str) -> None:
    """Catat log level ERROR."""
    logging.error(msg)