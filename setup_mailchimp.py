#!/usr/bin/env python3
import os, sys, requests, json
API_KEY = os.getenv("MAILCHIMP_API_KEY")
if not API_KEY:
    print("MAILCHIMP_API_KEY not found. Exiting setup_mailchimp.py")
    sys.exit(1)
server = API_KEY.split('-')[-1]
base = f"https://{server}.api.mailchimp.com/3.0"
auth = ("anystring", API_KEY)
print("Creating Mailchimp audience (list)...")
list_data = {
  "name": "UltimateKit pro buyers",
  "contact": {
    "company": "UltimateKit pro",
    "address1": "Online",
    "city": "Remote",
    "state": "Remote",
    "zip": "00000",
    "country": "US"
  },
  "permission_reminder": "You are receiving this because you purchased UltimateKit pro.",
  "campaign_defaults": {
    "from_name": "UltimateKit pro",
    "from_email": "support@ultimatekitpro.example",
    "subject": "Thanks for purchasing UltimateKit pro",
    "language": "en"
  },
  "email_type_option": False
}
r = requests.post(base + "/lists", auth=auth, json=list_data)
print("Mailchimp response:", r.status_code, r.text)
print("NOTE: Mailchimp automation creation may need manual steps depending on your plan.")
