#!/usr/bin/env python3
import os, sys, requests, json
TOKEN = os.getenv("GUMROAD_ACCESS_TOKEN")
if not TOKEN:
    print("GUMROAD_ACCESS_TOKEN not found. Exiting create_gumroad_product.py")
    sys.exit(1)
file_path = sys.argv[1] if len(sys.argv)>1 else "./UltimateKit_pro_Pack_Ultimate_500_Prompts_Bilingue.pdf"
print("Uploading file to Gumroad (this may require the Gumroad API to support file uploads)...")
# Gumroad has a limited public API for uploads; if this fails, script will print product_id for manual attach.
upload_url = "https://api.gumroad.com/v2/files"
with open(file_path, "rb") as fh:
    files = {'file': fh}
    data = {'access_token': TOKEN}
    r = requests.post(upload_url, files=files, data=data)
if r.status_code != 200:
    print("Upload response:", r.status_code, r.text)
else:
    print("Upload response OK. Response:", r.text)
# Create product
product_url = "https://api.gumroad.com/v2/products"
payload = {
    'access_token': TOKEN,
    'name': 'UltimateKit pro - Pack Ultimate 500 Prompts',
    'price': 2900,
    'description': '500 professional prompts for ChatGPT (ES/EN). Instant delivery.',
    'requires_shipping': False,
    'publish': True
}
r2 = requests.post(product_url, data=payload)
print("Create product response:", r2.status_code, r2.text)
try:
    info = r2.json()
    pid = info.get('product', {}).get('id') or info.get('id')
    print("Product ID:", pid)
    short = info.get('product', {}).get('short_url') or info.get('public_url') or f"https://gumroad.com/l/{pid}"
    print("Possible public link:", short)
except Exception as e:
    print("Could not parse product creation response:", e)
