import os
from PIL import Image

files_to_compress = [
    "apartment-charger.webp",
    "best-home-chargers.webp",
    "ev-depreciation-chart.webp",
    "ev-insurance-cost.webp",
    "ev-maintenance-vs-gas.webp",
    "hardwired-vs-plug-in.webp",
    "hidden-costs-evs.webp",
    "install-charger-cost.webp"
]

folder = "public/images/guides"
target_width = 800

for fname in files_to_compress:
    path = os.path.join(folder, fname)
    if os.path.exists(path):
        img = Image.open(path)
        ratio = target_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((target_width, new_height), Image.LANCZOS)
        img.save(path, "WEBP", quality=80, method=4)
        new_size = os.path.getsize(path)
        print(f"{fname}: {new_size/1024:.1f} KB ({img.width}x{img.height})")
    else:
        print(f"NOT FOUND: {fname}")
