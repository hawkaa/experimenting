import logging
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import List
from requests import get


@dataclass(frozen=True)
class Metric:
    type: str
    sensor: str
    value: float
    battery: int


def get_metrics(url: str) -> List[Metric]:
    obj = get(url).json()

    metrics = []

    for sensor in obj.values():
        if sensor["type"] == "ZHATemperature":
            metrics.append(
                Metric(
                    "temperature",
                    sensor["name"],
                    sensor["state"]["temperature"] / 100.0,
                    sensor["config"]["battery"],
                )
            )
        elif sensor["type"] == "ZHAPressure":
            metrics.append(
                Metric(
                    "pressure",
                    sensor["name"],
                    sensor["state"]["pressure"],
                    sensor["config"]["battery"],
                )
            )
        elif sensor["type"] == "ZHAHumidity":
            metrics.append(
                Metric(
                    "humidity",
                    sensor["name"],
                    sensor["state"]["humidity"],
                    sensor["config"]["battery"],
                )
            )
    return metrics


def handler_factory(url: str, api_key: str):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/metrics":
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                metrics = get_metrics(f"http://{url}/api/{api_key}/sensors")
                for metric in metrics:
                    self.wfile.write(
                        (
                            "deconz_"
                            + metric.type
                            + '{name="'
                            + metric.sensor
                            + '"} '
                            + str(metric.value)
                            + "\n"
                        ).encode()
                    )
                    self.wfile.write(
                        (
                            "deconz_battery"
                            + '{name="'
                            + metric.sensor
                            + '",type="'
                            + metric.type
                            + '"} '
                            + str(metric.battery)
                            + "\n"
                        ).encode()
                    )
            else:
                self.send_response(404)
                self.end_headers()

    return Handler


def run_server(deconz_url: str, deconz_api_key: str, port: int) -> None:
    logging.info("Starting server on port %s", port)
    httpd = HTTPServer(("", port), handler_factory(deconz_url, deconz_api_key))
    httpd.serve_forever()
