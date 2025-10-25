#!/usr/bin/env python3
import os, sys, requests, json
TOKEN = os.getenv("BUFFER_ACCESS_TOKEN")
if not TOKEN:
    print("BUFFER_ACCESS_TOKEN not found. Exiting post_socials.py")
    sys.exit(1)
text_es = "🚀 LANZAMIENTO: UltimateKit pro - Pack Ultimate 500 Prompts para ChatGPT (ES/EN). Oferta lanzamiento $29 [TU_LINK_GUMROAD]"
text_en = "🚀 LAUNCH: UltimateKit pro - 500 Prompts for ChatGPT (ES/EN). Launch price $29 [YOUR_GUMROAD_LINK]"
print("Fetching Buffer profiles...")
r = requests.get("https://api.bufferapp.com/1/profiles.json", params={'access_token': TOKEN})
if r.status_code != 200:
    print("Failed to get profiles:", r.status_code, r.text)
else:
    profiles = r.json() or []
    for p in profiles:
        pid = p.get('id')
        payload = {'profile_ids[]': pid, 'text': text_es}
        res = requests.post("https://api.bufferapp.com/1/updates/create.json", params={'access_token':TOKEN}, data=payload)
        print("Posted to profile", pid, "status:", res.status_code)
print("Done posting (check Buffer dashboard).")
