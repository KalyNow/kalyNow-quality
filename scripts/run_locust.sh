#!/usr/bin/env bash
# scripts/run_locust.sh
#
# Run KalyNow Locust load tests.
#
# Usage:
#   bash scripts/run_locust.sh                  # interactive web UI
#   bash scripts/run_locust.sh --headless        # headless mode with defaults
#
# Environment variables (set in .env or export before running):
#   BASE_URL          Backend API base URL  (default: http://localhost:8000)
#   LOCUST_USERS      Number of users       (default: 10)
#   LOCUST_SPAWN_RATE Spawn rate per second (default: 2)
#   LOCUST_RUN_TIME   Run duration          (default: 60s)

set -euo pipefail

# Load .env if present
if [ -f .env ]; then
  # shellcheck disable=SC1091
  set -a
  source .env
  set +a
fi

BASE_URL="${BASE_URL:-http://localhost:8000}"
LOCUST_USERS="${LOCUST_USERS:-10}"
LOCUST_SPAWN_RATE="${LOCUST_SPAWN_RATE:-2}"
LOCUST_RUN_TIME="${LOCUST_RUN_TIME:-60s}"

HEADLESS=false
if [[ "${1:-}" == "--headless" ]]; then
  HEADLESS=true
fi

LOCUST_CMD=(
  locust
  -f load-tests/locustfile.py
  --host="${BASE_URL}"
)

if [ "$HEADLESS" = true ]; then
  LOCUST_CMD+=(
    --headless
    --users="${LOCUST_USERS}"
    --spawn-rate="${LOCUST_SPAWN_RATE}"
    --run-time="${LOCUST_RUN_TIME}"
  )
  echo "Running Locust in headless mode..."
  echo "  Host:       ${BASE_URL}"
  echo "  Users:      ${LOCUST_USERS}"
  echo "  Spawn rate: ${LOCUST_SPAWN_RATE}/s"
  echo "  Run time:   ${LOCUST_RUN_TIME}"
else
  echo "Starting Locust web UI..."
  echo "  Host: ${BASE_URL}"
  echo "  Open http://localhost:8089 in your browser to start the test."
fi

"${LOCUST_CMD[@]}"
