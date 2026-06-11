#!/bin/bash
# Stáhne 11 velkých fotek z Google Drive (8–12 MB) které se nepodařilo stáhnout přes MCP.
# Spusť v Terminálu: bash download_large_photos.sh
# Vyžaduje: gdown (nainstalováno na tomto Macu)

GDOWN="/Users/krystofsobotka/Library/Python/3.9/bin/gdown"
OUT="/Users/krystofsobotka/Desktop/U Cerhů/U cerhů 1/assets/images"

declare -A FILES=(
  ["1ehMk95GIaQHjOfBkbq53YHhhk02PS8fl"]="img-6805.jpg"
  ["13ODB4GgNbYRxJ_A3ssS85rp1e8On8Aqx"]="img-6804.jpg"
  ["1zYvb9WLZwOcLiQksdXdinhto-EkWmtVg"]="img-6808.jpg"
  ["1wLATslfhR_IaXDGzalKvmmjb8bkK81uv"]="img-6758.jpg"
  ["1eZjf6NLUOWooQCoKJSYWqIBG6aJjIy8R"]="img-6743.jpg"
  ["1rno84nmi9OEGrj_yfCKeihae9pxCnuWR"]="nase-svatba-u-cerhu-148.jpg"
  ["1p3KnOA1XepV6j3kmEMRN8TK9ERpAP6nk"]="nase-svatba-u-cerhu-24.jpg"
  ["1yjw3R6t86Wxa3TXl6oIKKsJlw61Ha21W"]="nase-svatba-u-cerhu-43.jpg"
  ["14fldg6ZMttr8ey5ZrounoC1lYi_-kQO7"]="nase-svatba-u-cerhu-31.jpg"
  ["1Vuck4-Z3FDCW05_2N3DsKnyb4SFyCmeI"]="nase-svatba-u-cerhu-29.jpg"
  ["1KVQQeZqCaAz_pxHbXOi7MjBy7HUsYJGA"]="nase-svatba-u-cerhu-3.jpg"
)

for ID in "${!FILES[@]}"; do
  NAME="${FILES[$ID]}"
  TARGET="$OUT/$NAME"
  if [ -f "$TARGET" ]; then
    echo "SKIP (exists): $NAME"
    continue
  fi
  echo "Downloading $NAME ..."
  "$GDOWN" "https://drive.google.com/uc?id=$ID" -O "$TARGET" 2>&1
  if [ -f "$TARGET" ]; then
    echo "  OK: $NAME ($(du -sh "$TARGET" | cut -f1))"
  else
    echo "  FAILED: $NAME — stáhni ručně z Drive a ulož do assets/images/$NAME"
  fi
done

echo ""
echo "Hotovo. Zkontroluj výsledky výše."
