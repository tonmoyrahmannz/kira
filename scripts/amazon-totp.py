#!/usr/bin/env python3
"""Generate current Amazon TOTP 6-digit code from stored secret."""
import os
import sys
import hmac
import hashlib
import struct
import base64
import time

# Load secret from env or fallback
secret_b32 = os.environ.get("AMAZON_TOTP_SECRET")
if not secret_b32:
    # Read from env file
    env_file = os.path.expanduser("~/Kira/secrets/homeassistant.env")
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                if line.startswith("AMAZON_TOTP_SECRET="):
                    secret_b32 = line.strip().split("=", 1)[1]
                    break

if not secret_b32:
    print("ERROR: AMAZON_TOTP_SECRET not found", file=sys.stderr)
    sys.exit(1)

# Clean spaces
secret_b32 = secret_b32.replace(" ", "")

# Pad if needed
padding = 8 - (len(secret_b32) % 8)
if padding != 8:
    secret_b32 += "=" * padding

key = base64.b32decode(secret_b32.upper())

# Generate TOTP (standard 30s interval)
interval = int(time.time()) // 30
msg = struct.pack(">Q", interval)
digest = hmac.new(key, msg, hashlib.sha1).digest()
offset = digest[-1] & 0x0F
code = (struct.unpack(">I", digest[offset:offset+4])[0] & 0x7FFFFFFF) % 1000000

print(f"Amazon TOTP: {code:06d}")
