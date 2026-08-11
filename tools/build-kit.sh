#!/usr/bin/env bash
# Empaqueta elementor-kit/ en un .zip listo para
# WordPress > Elementor > Herramientas > Importar/Exportar kit > Importar kit.
#
# Uso: ./tools/build-kit.sh [nombre-salida]

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/elementor-kit"
OUT="$ROOT/dist/${1:-blomstra-kit}.zip"

if [ ! -f "$SRC/manifest.json" ]; then
  echo "No encuentro $SRC/manifest.json" >&2
  exit 1
fi

if ! command -v zip >/dev/null 2>&1; then
  echo "Falta el comando 'zip'. Instalalo (apt install zip / brew install zip)." >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT")"
rm -f "$OUT"

# El zip debe tener manifest.json en la RAIZ, no dentro de una carpeta.
( cd "$SRC" && zip -rq "$OUT" . -x '.*' -x '*/.*' )

echo "Kit generado: $OUT"
echo "Importalo en: Elementor > Herramientas > Importar/Exportar kit > Importar kit"
