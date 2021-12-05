# Deconz Prometheus Exporter

Repository for a custom python DeConz exporter, and a docker-compose file for a full monitoring
setup with prometheus and grafana.

## Hacking

Running:

```sh
DECONZ_API_KEY=... DECONZ_URL=... poetry run python main.py
```

Building and pushing docker image:

```sh
docker build . -t deconz-prometheus-exporter
docker tag deconz-prometheus-exporter hakonamdal/deconz-prometheus-exporter
docker push hakonamdal/deconz-prometheus-exporter
```

Running docker:

```sh
docker run -e DECONZ_API_KEY=... -e DECONZ_URL=... -p 8080:8080 hakonamdal/deconz-prometheus-exporter
```

## Running the exporter, prometheus, and grafana

Modify environment variables in `docker-compose.yml` to match your environment.

Start the servers with:

```sh
docker-compose up
```
