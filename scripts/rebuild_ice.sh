#!/usr/bin/env bash
# rebuild_ice.sh — Manual-trigger rebuild of the ICE enforcement database
#
# Assumes data is already in data/raw/release_2023/ and data/raw/release_2025/
# (xlsx files from the Deportation Data Project FOIA releases).
#
# Usage:
#   ./scripts/rebuild_ice.sh
#   HF_TOKEN=hf_xxx ./scripts/rebuild_ice.sh   # also upload to HF
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

LOG_DIR="$PROJECT_DIR/logs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/rebuild_$(date +%Y%m%d_%H%M%S).log"

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

log "=== ICE Database Rebuild ==="
log "Project dir: $PROJECT_DIR"

# Check data exists
if [ ! -d "data/raw/release_2023" ] && [ ! -d "data/raw/release_2025" ]; then
    log "ERROR: No release directories found in data/raw/"
    log "Place xlsx files in data/raw/release_2023/ and/or data/raw/release_2025/"
    exit 1
fi

# Build
log "Building database..."
uv run python build_database.py --output ice.duckdb 2>&1 | tee -a "$LOG"

DB_SIZE=$(du -h ice.duckdb | cut -f1)
log "Database built: $DB_SIZE"

# Upload to HF if token is set
if [ -n "${HF_TOKEN:-}" ]; then
    log "Uploading to Hugging Face..."
    uv run python publish_to_hf.py --token "$HF_TOKEN" 2>&1 | tee -a "$LOG"
    log "Upload complete"
else
    log "No HF_TOKEN set — skipping upload"
    log "To upload: HF_TOKEN=hf_xxx ./scripts/rebuild_ice.sh"
fi

log "=== Done ==="
log "Log: $LOG"
