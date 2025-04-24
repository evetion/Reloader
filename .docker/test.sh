#!/usr/bin/env bash
set -eux
docker compose -f compose.yml up -d --force-recreate --remove-orphans
docker exec -t qgis sh -c "qgis_setup.sh reloader"
docker exec -t qgis sh -c "cd /tests_directory && xvfb-run -a qgis_testrunner.sh reloader.tests"
exit_code=$?
docker compose -f compose.yml kill
docker compose -f compose.yml rm -f
exit $exit_code
