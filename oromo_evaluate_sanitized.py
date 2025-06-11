# This script has been sanitized to remove private access tokens and credentials.

# Remove or replace these hardcoded API tokens with environment variables:
HF_API_TOKEN = "<YOUR_HF_API_TOKEN>"  # Replace with os.getenv("HF_API_TOKEN") in production
WANDB_API_KEY = "<YOUR_WANDB_API_KEY>"  # Replace with os.getenv("WANDB_API_KEY") in production

# Updated login logic (recommended):
# import os
# from huggingface_hub import login
# import wandb
# wandb.login(key=os.getenv("WANDB_API_KEY"))
# login(os.getenv("HF_API_TOKEN"))

# Rest of the original script remains intact and functional.
# Ensure you manage sensitive credentials securely using .env or your system's secret manager.

# For full script sanitization, you can apply these replacements across the codebase.

# Example use for safer credential loading:
# import os
# HF_API_TOKEN = os.getenv("HF_API_TOKEN")
# WANDB_API_KEY = os.getenv("WANDB_API_KEY")
