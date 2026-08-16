<div align="center">

# 🧟 GitHub Zombie Survival Graph

Transform your GitHub contribution graph into a post-apocalyptic tactical survival system!

[English](#-english) | [Türkçe](#-türkçe) | [Español](#-español) | [Français](#-français) | [Deutsch](#-deutsch) | [Italiano](#-italiano) | [Português](#-português) | [Русский](#-русский) | [中文](#-中文) | [日本語](#-日本語)

</div>

---

## 🇺🇸 English

### How to Add This to Your Profile?

1. Go to your GitHub profile repository (the repository named exactly like your username).
2. Create or open `.github/workflows/zombie-graph.yml` and paste the following workflow:

```yaml
name: Generate Zombie Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
        
      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          game_start_date: "2026-08-15"
          
      - name: Commit and Push SVG
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add zombie-graph.svg
          git commit -m "update: Daily Zombie Survival Intel" || echo "No changes to commit"
          git push
