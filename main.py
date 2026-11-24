#!/usr/bin/env python3
"""Entry for make.fun's "Worst AI Advice: The 48-Hour Tight Line Open".

Writes one line of the worst advice an AI assistant could confidently give
to /output/entry.txt (140 characters or fewer).
"""

import os

ENTRY = (
    "Missed your flight? Just book the next one for yesterday - most "
    "airlines honor tickets from the past, and it shows initiative."
)

assert len(ENTRY) <= 140, len(ENTRY)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
print(ENTRY)
