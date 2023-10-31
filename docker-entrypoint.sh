#!/bin/sh

set -e

exec /venv/bin/python3 -m flask run --host=0.0.0.0
