#!/usr/bin/env bash
# scripts/run_robot.sh
#
# Run KalyNow Robot Framework tests.
#
# Usage:
#   bash scripts/run_robot.sh            # run all web tests (default)
#   bash scripts/run_robot.sh web        # run web tests
#   bash scripts/run_robot.sh mobile     # run mobile tests
#   bash scripts/run_robot.sh all        # run web + mobile tests
#
# Environment variables (set in .env or export before running):
#   WEB_URL      Frontend web app URL     (default: http://localhost:3000)
#   BROWSER      Selenium browser         (default: chrome)
#   APPIUM_URL   Appium server URL        (default: http://localhost:4723/wd/hub)

set -euo pipefail

# Load .env if present
if [ -f .env ]; then
  # shellcheck disable=SC1091
  set -a
  source .env
  set +a
fi

WEB_URL="${WEB_URL:-http://localhost:3000}"
BROWSER="${BROWSER:-chrome}"
APPIUM_URL="${APPIUM_URL:-http://localhost:4723/wd/hub}"

TARGET="${1:-web}"

ROBOT_VARS=(
  --variable "WEB_URL:${WEB_URL}"
  --variable "BROWSER:${BROWSER}"
  --variable "APPIUM_URL:${APPIUM_URL}"
)

run_web() {
  echo "Running web tests (browser: ${BROWSER}, url: ${WEB_URL})..."
  robot "${ROBOT_VARS[@]}" robot-tests/tests/web
}

run_mobile() {
  echo "Running mobile tests (Appium: ${APPIUM_URL})..."
  robot "${ROBOT_VARS[@]}" robot-tests/tests/mobile
}

case "$TARGET" in
  web)
    run_web
    ;;
  mobile)
    run_mobile
    ;;
  all)
    run_web
    run_mobile
    ;;
  *)
    echo "Unknown target: ${TARGET}. Use: web | mobile | all"
    exit 1
    ;;
esac
