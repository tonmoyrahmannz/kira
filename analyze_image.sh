#!/bin/bash
# Run image analysis
IMAGE="/Users/tonmoyrahman/.hermes/image_cache/img_0522ad00dfc4.jpg"

echo "=== file info ==="
file "$IMAGE"

echo ""
echo "=== sips image properties ==="
sips --getProperty all "$IMAGE" 2>&1

echo ""
echo "=== Trying python3 with PIL if available ==="
python3 -c "
from PIL import Image
img = Image.open('$IMAGE')
print(f'Size: {img.size[0]}x{img.size[1]}')
print(f'Mode: {img.mode}')
print(f'Format: {img.format}')
" 2>&1 || echo "PIL not available"

echo ""
echo "=== md5 hash ==="
md5 -q "$IMAGE"
