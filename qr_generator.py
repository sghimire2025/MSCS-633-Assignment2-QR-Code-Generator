# qr_generator.py
from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse

import qrcode
from qrcode.constants import ERROR_CORRECT_M

# --- Fixed settings for the assignment ---
URL_TO_ENCODE = "https://www.bioxsystems.com/"
OUTPUT_PATH = Path("sample_output/qr_bioxsystems.png")

# Tunable QR appearance
BOX_SIZE = 10          # pixels per module
BORDER = 4             # modules
FILL_COLOR = "black"
BACK_COLOR = "white"

def _is_valid_http_url(url: str) -> bool:
    p = urlparse(url)
    return p.scheme in {"http", "https"} and bool(p.netloc)

def _build_qr(url: str) -> qrcode.image.pil.PilImage:
    qr = qrcode.QRCode(
        version=None,                     # auto size
        error_correction=ERROR_CORRECT_M, # ~15% EC
        box_size=BOX_SIZE,
        border=BORDER,
    )
    qr.add_data(url, optimize=20)
    qr.make(fit=True)
    return qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)

def main() -> None:
    if not _is_valid_http_url(URL_TO_ENCODE):
        raise SystemExit("Configured URL is not a valid http(s) URL.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img = _build_qr(URL_TO_ENCODE)
    img.save(OUTPUT_PATH)
    print(f"QR code for {URL_TO_ENCODE} saved to {OUTPUT_PATH.resolve()}")

if __name__ == "__main__":
    main()
