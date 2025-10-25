UltimateKit pro - AUTOMATION PACKAGE (Ultra minimal interaction)

WHAT'S INSIDE
- index.html (landing page)
- UltimateKit_pro_Pack_Ultimate_500_Prompts_Bilingue.pdf (product placeholder)
- deploy_all.sh (orchestrator)
- scripts/
  - create_gumroad_product.py
  - setup_mailchimp.py
  - post_socials.py
- .github/auto_deploy.yml (CI pipeline)
- launch_kit/ (social and email copy)

PREREQS (one-time)
- Python3 and pip
- Node and npm
- Vercel CLI (npm i -g vercel)
- GitHub account (optional: for CI)
- Accounts/APIs: Gumroad, Mailchimp, Buffer, Vercel

SETUP (quick)
1) Unzip the package and cd into folder.
2) Export your API keys (or add as GitHub Secrets):
   export VERCEL_TOKEN="your_vercel_token"
   export GUMROAD_ACCESS_TOKEN="your_gumroad_token"
   export MAILCHIMP_API_KEY="your_mailchimp_key"
   export BUFFER_ACCESS_TOKEN="your_buffer_token"
3) Make deploy script executable: chmod +x deploy_all.sh
4) Run: ./deploy_all.sh
   - Follow console outputs. Scripts may require manual confirmation in rare cases.

SECURITY NOTE
- Keep your API keys private. Use GitHub Secrets for CI to avoid exposing keys in logs.
- This package assumes APIs accept programmatic product creation/upload; if some API blocks upload, script prints product_id for manual attach via dashboard.

If you want, I can now:
- (A) Create a GitHub repo with these files and give you the exact one-click import steps for Vercel.
- (B) Keep it local and you run the deploy_all.sh command.
Reply with 'GITHUB' to create the repo structure instructions, or 'LOCAL' to proceed locally.
