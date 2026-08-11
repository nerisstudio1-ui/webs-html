#!/usr/bin/env bash
# Empaqueta el tema hijo en un .zip listo para
# WordPress > Apariencia > Temas > Anadir nuevo > Subir tema.
#
# Uso: ./tools/build-theme.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/wordpress/themes/blomstra-child"
OUT="$ROOT/dist/blomstra-child.zip"

if [ ! -f "$SRC/style.css" ]; then
  echo "No encuentro $SRC/style.css" >&2
  exit 1
fi

if ! command -v zip >/dev/null 2>&1; then
  echo "Falta el comando 'zip'. Instalalo (apt install zip / brew install zip)." >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT")"
rm -f "$OUT"

# WordPress espera que el zip contenga la CARPETA del tema, no sus archivos
# sueltos, de ahi que se comprima desde el directorio padre.
( cd "$SRC/.." && zip -rq "$OUT" "blomstra-child" -x '.*' -x '*/.*' )

echo "Tema generado: $OUT"
echo "Subelo en: Apariencia > Temas > Anadir nuevo > Subir tema"
