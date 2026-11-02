#!/usr/bin/env bash
# Upscale and grade one generated image into src/photos/<name>.jpg.
#
# The image generator hands back a small thumbnail, so this does the work that
# makes it survive at video scale: a Lanczos upscale, a light unsharp pass to
# put some edge back, and a touch of grain so it reads as a soft film frame
# rather than a stretched JPEG.
#
#   tools/grade_photo.sh <source-image> <name> [width]

set -euo pipefail

src=${1:?source image required}
name=${2:?output name required}
width=${3:-980}

root=$(cd "$(dirname "$0")/.." && pwd)
out="$root/src/photos/$name.jpg"
mkdir -p "$root/src/photos"

ffmpeg_bin=${FFMPEG:-}
if [ -z "$ffmpeg_bin" ]; then
  for candidate in /usr/bin/ffmpeg /usr/local/bin/ffmpeg; do
    [ -x "$candidate" ] && ffmpeg_bin=$candidate && break
  done
fi
if [ -z "$ffmpeg_bin" ]; then
  ffmpeg_bin=$(ls /usr/local/lib/python*/site-packages/imageio_ffmpeg/binaries/ffmpeg-* \
               /usr/local/lib/python*/dist-packages/imageio_ffmpeg/binaries/ffmpeg-* 2>/dev/null | head -1)
fi
[ -n "$ffmpeg_bin" ] || { echo "no ffmpeg found; set FFMPEG" >&2; exit 1; }

"$ffmpeg_bin" -hide_banner -loglevel error -i "$src" \
  -vf "scale=${width}:-1:flags=lanczos,unsharp=5:5:0.8:3:3:0.4,noise=alls=7:allf=t+u" \
  -frames:v 1 -q:v 3 -y "$out"

echo "$out  ($(du -h "$out" | cut -f1))"
