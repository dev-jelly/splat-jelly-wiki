#!/bin/bash
# Helper script to archive raw markdown sources from URLs
# Usage: ./archive-source.sh <URL> <FILENAME>

URL=$1
FILENAME=$2
SAVE_PATH=".sisyphus/raw_sources/$FILENAME"

echo "Archiving $URL to $SAVE_PATH..."
# We use curl to fetch and pandoc or similar if available, but here just raw html/text is fine
# Since we need markdown, we'll try to get it via webfetch in the main loop
# This script is a placeholder for the logging part
