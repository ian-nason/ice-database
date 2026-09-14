#!/usr/bin/env bash
# Download the Deportation Data Project ICE releases used by build_database.py.
# Links come from https://deportationdata.org/data/ice.html (box.com shared files);
# update them here when DDP posts a new release.
set -uo pipefail
cd "$(dirname "$0")/.."
RAW=data/raw

# Latest cumulative release: 2022-10-01 through 2026-08-06 (posted 2026-08-21)
LATEST=(
  https://ucla.box.com/shared/static/jh4rar1ifbczhuj3c2fack6etsxco4mk.zip
  https://ucla.box.com/shared/static/867c2ituyijy15insi5kqxjkjn2tnpip.zip
  https://ucla.box.com/shared/static/bonhlxvjur3jf2k84cl0yi8rdidefm8t.zip
  https://ucla.box.com/shared/static/li3eje734jhnktgag0pz2vtksbyvbeei.zip
  https://ucla.box.com/shared/static/rihbivpt54zek3z3xtlax41ypjml2rs0.zip
)
# ACLU linked data, 2011-10-01 through 2023-09-30 (release_2023)
LINKED=(
  https://ucla.box.com/shared/static/3i6xhnd5cig3qacy5phxvw9cmy7a71k1.zip
  https://ucla.box.com/shared/static/gjfcedj3ne4d6l6rt5sv0t6yfao18jzp.zip
  https://ucla.box.com/shared/static/hanv0cqbvxole910mo63z9uy40cwwi9t.zip
  https://ucla.box.com/shared/static/x6jxz982onabumgfx0dwnd39b27ggoqz.zip
)

fetch_all() {
  local dir=$1; shift
  mkdir -p "$dir"
  local i=0
  for u in "$@"; do
    i=$((i+1))
    local f="$dir/part_$i.zip"
    if [[ -s "$f" ]]; then echo "have $f"; continue; fi
    echo "GET $u -> $f"
    curl -L --retry 5 --retry-delay 10 -sS -o "$f.part" "$u" && mv "$f.part" "$f" || { echo "FAILED $u"; rm -f "$f.part"; return 1; }
    ls -la "$f"
  done
  for f in "$dir"/part_*.zip; do
    echo "unzip $f"; unzip -o -q "$f" -d "$dir" || { echo "UNZIP FAILED $f"; file "$f"; return 1; }
  done
  find "$dir" -type f ! -name 'part_*.zip' | sort
}

fetch_all "$RAW/release_2026_08" "${LATEST[@]}" || exit 1
fetch_all "$RAW/release_2023"    "${LINKED[@]}" || exit 1
echo "ICE DOWNLOADS DONE"
