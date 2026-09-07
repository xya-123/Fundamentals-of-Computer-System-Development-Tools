#!/usr/bin/env bash
set -euo pipefail

url="http://127.0.0.1:8000/packages.json"

{
  echo "# Active Package Report"
  echo
  echo "| name | version | downloads |"
  echo "|---|---|---:|"

  curl -fsS "$url" |
    jq -r '
      [.[] | select(.status == "active" and .downloads >= 100)]
      | sort_by([-.downloads, .name])
      | .[]
      | "| \(.name) | \(.version) | \(.downloads) |"
    '
} > summary.md