#!/usr/bin/env python3
"""Processes MCP Google Drive download temp files and saves decoded JPEGs."""
import json, base64, glob, os, sys

TOOL_RESULTS_DIR = os.path.expanduser(
    "~/.claude/projects/-Users-krystofsobotka-Desktop-U-Cerh--U-cerh--1/"
    "b935707f-7dad-4ce8-8aad-df0c0ccf72c1/tool-results"
)
OUT_DIR = os.path.join(os.path.dirname(__file__), "assets", "images")

ID_TO_NAME = {
    "1G0s_aPnJNHLRPhbUvQX1oLuMrPL5H9Qo": "img-6857.jpg",
    "1NyNs_X-NNUBqubIwzZTBhap3wkk0la5X": "img-6856.jpg",
    "1Ld5MErgsHH8x8cbes58CQgT4cQf-mNxp": "img-6835.jpg",
    "1aWEonnPB-XxhzyYuUyCznFsZIOVlHGdz": "img-6826.jpg",
    "13O-Tgth_RVwUdXf7aCZrO0B7irRurJDD": "img-6836.jpg",
    "1witf5XUuxs9tsQrpvZDzYiJ76zyN0j_7": "img-6829.jpg",
    "1V85ZP0Ye0pF6LxMNMXbmRMvkTG84iBHb": "img-6828.jpg",
    "1Uu8Vj3dnh6pJTQvpPcmTSSy_bWIzvI-k": "img-6827.jpg",
    "1DFoBmYRjQjt-ok5AciHb4yyxpV8VsacV": "img-6824.jpg",
    "1ehMk95GIaQHjOfBkbq53YHhhk02PS8fl": "img-6805.jpg",
    "13ODB4GgNbYRxJ_A3ssS85rp1e8On8Aqx": "img-6804.jpg",
    "1zYvb9WLZwOcLiQksdXdinhto-EkWmtVg": "img-6808.jpg",
    "1Qd7tIWEnJ-whjBXVC78TJpoB32UclqEW": "img-6806.jpg",
    "1wLATslfhR_IaXDGzalKvmmjb8bkK81uv": "img-6758.jpg",
    "1eZjf6NLUOWooQCoKJSYWqIBG6aJjIy8R": "img-6743.jpg",
    "1rvaQGDUW2iC5tbOMcNIOxsJNKeAkOvcJ": "img-6744.jpg",
    "1HaU8ig6G60m8RY0Z6ZfMB6cyb9QaJ1Bi": "img-6605.jpg",
    "1NSMvfMS4UpQQ-CcDIiTxchILPL2-lKKK": "img-6581.jpg",
    "171Q5nZ-5rU9kVIOXoYyiRSzU_JnTloM7": "img-6584.jpg",
    "19QQg3HpflbZ5SsMeG0k4Q3mTgwzxMTbD": "img-6572.jpg",
    "1MgcdACSn-gq86xF5ElKHxA1lKSy-mrB-": "img-6583.jpg",
    "1Ntsaz17yoiZcrAgyfvIBuun5wkd-hWcE": "img-6579.jpg",
    "1gjfBbSqOtWqr0p33c8GCqCP6ZIwT7Ihe": "img-6599.jpg",
    "1uhL0sncventPYhjq0OKlogExRFI7Lb8S": "img-6574.jpg",
    "17iaCKyd1je7i3ksbA0MbvXL9ImEh4T0R": "img-6577.jpg",
    "1zfHPMMHHZo-lLaAa3mYR9Qj0kyWNWMoa": "img-6576.jpg",
    "1k_OqyC_wNUN1NDYBxuKSZpWa_FFKTMz4": "img-6595.jpg",
    "1wXsILmaXHUCVQLjS7wYxx1Grw0LpPDTi": "img-6573.jpg",
    "1yA7ZK84NTNBWcSbYMrs-QnGvHR3wqDVT": "img-6580.jpg",
    "1LT5dMNRwNVcCoqhIglpXWeuM2BQBpxlf": "img-6575.jpg",
    "1CaItLBckqgim95LxWc11mEJy4BulJwIB": "img-6571.jpg",
    "1XYGGKuJa5k-1DsK2NHCMIAOnEL1xOkVF": "img-6570.jpg",
    "1CcJbjJWqOieJbN4wonQUl4JpImrwceCT": "img-6516.jpg",
    "1ohayohqSwHRE3Ts3LiEF7ZCTJHw47uS9": "img-6513.jpg",
    "1zJPQT6vAFRBLXyTLgDOrR1OWnqZE0dcX": "img-6522.jpg",
    "1IjVJ8isffu_6p71xkFih7PeM8FeynLh7": "img-9124.jpg",
    "1rno84nmi9OEGrj_yfCKeihae9pxCnuWR": "nase-svatba-u-cerhu-148.jpg",
    "1p3KnOA1XepV6j3kmEMRN8TK9ERpAP6nk": "nase-svatba-u-cerhu-24.jpg",
    "1yjw3R6t86Wxa3TXl6oIKKsJlw61Ha21W": "nase-svatba-u-cerhu-43.jpg",
    "14fldg6ZMttr8ey5ZrounoC1lYi_-kQO7": "nase-svatba-u-cerhu-31.jpg",
    "1Vuck4-Z3FDCW05_2N3DsKnyb4SFyCmeI": "nase-svatba-u-cerhu-29.jpg",
    "1KVQQeZqCaAz_pxHbXOi7MjBy7HUsYJGA": "nase-svatba-u-cerhu-3.jpg",
    "1MH3EPjmCfp9ldf023pfxKh6918CEg2s6": "img-5285.jpg",
}

saved = skipped = errors = 0
import glob as _glob
patterns = [
    os.path.join(TOOL_RESULTS_DIR, "mcp-claude_ai_Google_Drive-download_file_content-*.txt"),
    os.path.join(TOOL_RESULTS_DIR, "toolu_*.txt"),
]
all_files = []
for p in patterns:
    all_files.extend(_glob.glob(p))
pattern = None  # replaced by all_files list below
for fpath in all_files:
    try:
        with open(fpath) as f:
            data = json.load(f)
        file_id = data.get("id", "")
        target = ID_TO_NAME.get(file_id)
        if not target:
            continue
        out_path = os.path.join(OUT_DIR, target)
        if os.path.exists(out_path):
            skipped += 1
            continue
        img_bytes = base64.b64decode(data["content"])
        with open(out_path, "wb") as f:
            f.write(img_bytes)
        print(f"  saved {target} ({len(img_bytes)//1024} KB)")
        saved += 1
    except Exception as e:
        print(f"  ERROR {fpath}: {e}", file=sys.stderr)
        errors += 1

print(f"\nDone: {saved} saved, {skipped} skipped, {errors} errors")
