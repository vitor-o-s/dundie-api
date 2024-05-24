#!/usr/bin/bash

# Start environment with docker compose
DUNDIE_DB=dundie_test docker compose up -d

# wait 5 seconds
sleep 5

# Ensure database is clean
docker compose exec api dundie reset-db -f
docker compose exec api alembic stamp base

# run migrations
docker compose exec api alembic upgrade head

# run tests
# for some reason I still dont know some commands need explicit user param
docker compose exec --user "$(id -u):$(id -g)" api pytest -v -l --tb=short --maxfail=1 tests/

# Stop environment
docker compose down
