FROM python:3.10-slim-bullseye
RUN pip install requests
COPY main.py main.py
COPY deconz_prometheus_exporter/ deconz_prometheus_exporter/
CMD ["python", "main.py"]