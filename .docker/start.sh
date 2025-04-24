#!/usr/bin/env bash
set -eux

docker compose -f compose.yml up -d --force-recreate --remove-orphans
echo "Installation of the plugin reloader"
docker exec -t qgis sh -c "qgis_setup.sh reloader"
echo "Containers are running"
