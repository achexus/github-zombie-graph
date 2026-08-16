<div align="center">
  <a href="#english">🇬🇧 English</a> • 
  <a href="#turkce">🇹🇷 Türkçe</a> • 
  <a href="#espanol">🇪🇸 Español</a> • 
  <a href="#deutsch">🇩🇪 Deutsch</a>
</div>

---
# 🧟‍♂️ GitHub Zombie Survival Graph

<div align="center">
  <img src="zombie-graph.svg" alt="GitHub Zombie Survival Graph" />
</div>

<br>

<div align="center">
  <a href="#english">🇬🇧 English</a> • 
  <a href="#turkce">🇹🇷 Türkçe</a>
</div>

---

<h2 id="english">🇬🇧 English</h2>

Transform your standard GitHub contribution graph into a post-apocalyptic tactical survival system! This GitHub Action generates a dynamic SVG showing your survival streak, eliminated zombies (commits), and tactical rank based on your daily GitHub activity.

### 🚀 How to Use

**1. Create the Workflow**
Create a new file in your repository at `.github/workflows/zombie-graph.yml` and add the following code:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *" # Runs automatically every midnight
  workflow_dispatch: # Allows manual trigger

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Update GitHub Zombie Survival Graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Important Note:** Ensure your repository allows Actions to read and write. Go to **Settings > Actions > General**, scroll down to **Workflow permissions**, and select **"Read and write permissions"**.

**2. Update your README**
Add the generated SVG to your profile's `README.md`:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="turkce">🇹🇷 Türkçe</h2>

Klasik GitHub katkı grafiğinizi kıyamet sonrası taktiksel bir hayatta kalma sistemine dönüştürün! Bu GitHub Action, günlük GitHub aktivitenize dayanarak hayatta kalma serinizi, yok edilen zombileri (commit'ler) ve taktiksel rütbenizi gösteren dinamik bir SVG oluşturur.

### 🚀 Nasıl Kullanılır?

**1. Workflow Dosyasını Oluşturun**
Deponuzda `.github/workflows/zombie-graph.yml` yolunda yeni bir dosya oluşturun ve aşağıdaki kodu ekleyin:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *" # Her gece yarısı otomatik çalışır
  workflow_dispatch: # Manuel tetiklemeye izin verir

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Zombie Survival Graph
        uses: achexus/github-zombie-graph@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Update GitHub Zombie Survival Graph"
          file_pattern: zombie-graph.svg
```

> **⚠️ Önemli Not:** Deponuzun Action'lar için okuma ve yazma iznine sahip olduğundan emin olun. **Settings > Actions > General** sekmesine gidin, en alttaki **Workflow permissions** kısmından **"Read and write permissions"** seçeneğini işaretleyip kaydedin.

**2. README Dosyanızı Güncelleyin**
Oluşturulan SVG dosyasını profilinizin `README.md` dosyasına ekleyin:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```
