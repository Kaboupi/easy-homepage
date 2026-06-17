import os
import sys

from dotenv import load_dotenv
from loguru import logger

load_dotenv(override=True)

logger.remove()
logger.add(sys.stderr, level="INFO")


# TODO: Implement TLS connections
def print_homepage_link(tls: bool = False) -> None:
    prefix: str = "https" if tls else "http"

    host: str = os.environ.get("HOMELAB_ADDRESS", "127.0.0.1")
    domain: str = os.environ.get("HOMELAB_DOMAIN", "my.home.lab")
    port: str = os.environ.get("HOMEPAGE_PORT", "3030")

    host_full = f"{prefix}://{host}:{port}/"
    domain_full = f"{prefix}://{domain}:{port}/"

    logger.info("")
    logger.info("You can visit your Homepage by following these links:")
    logger.success(f"==> {host_full}")
    logger.success(f"==> {domain_full}")
