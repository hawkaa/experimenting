import logging
import os
from deconz_prometheus_exporter import run_server


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    port = int(os.environ.get("PORT", 8080))

    deconz_api_key = os.environ.get("DECONZ_API_KEY")
    if deconz_api_key is None or deconz_api_key == "":
        logging.error("No DECONZ_API_KEY provided")
        exit(1)

    deconz_url = os.environ.get("DECONZ_URL")
    if deconz_url is None or deconz_url == "":
        logging.error("No DECONZ_URL provided")
        exit(1)

    run_server(deconz_url, deconz_api_key, port)
