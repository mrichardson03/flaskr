#!/usr/bin/env bash

SCRIPT_BASE="$(cd "$(dirname "$0")" && pwd)"
ROOT=${SCRIPT_BASE}/..

set -e

poetry build

# Set version in charts/flaskr/Chart.yaml
grep -E '^version: ".+"$' "$ROOT/charts/flaskr/Chart.yaml" >/dev/null
sed -i.bak -E "s/^version: \".+\"$/version: \"$NEW_VERSION\"/" "$ROOT/charts/flaskr/Chart.yaml" && rm "$ROOT/charts/flaskr/Chart.yaml.bak"

grep -E '^appVersion: ".+"$' "$ROOT/charts/flaskr/Chart.yaml" >/dev/null
sed -i.bak -E "s/^appVersion: \".+\"$/appVersion: \"$NEW_VERSION\"/" "$ROOT/charts/flaskr/Chart.yaml" && rm "$ROOT/charts/flaskr/Chart.yaml.bak"
