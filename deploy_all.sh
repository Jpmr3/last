#!/usr/bin/env bash
set -e
echo "==> Starting UltimateKit pro automated deploy..."
# 1) Deploy to Vercel (requires VERCEL_TOKEN)
if command -v vercel >/dev/null 2>&1; then
  echo "Vercel CLI found."
else
  echo "Installing Vercel CLI..."
  npm i -g vercel
fi
echo "Deploying to Vercel... (will ask for auth if not configured)"
vercel --prod --confirm || true
# 2) Create product in Gumroad
echo "Creating product on Gumroad via script..."
python3 scripts/create_gumroad_product.py "./UltimateKit_pro_Pack_Ultimate_500_Prompts_Bilingue.pdf" || true
# 3) Setup Mailchimp audience/automation
echo "Setting up Mailchimp (may require plan)..."
python3 scripts/setup_mailchimp.py || true
# 4) Post socials via Buffer (optional)
echo "Posting launch messages to Buffer-connected profiles..."
python3 scripts/post_socials.py || true
echo "==> Deploy script finished. Check the console output for links and results."
