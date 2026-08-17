# 🧟‍♂️ GitHub Zombie Survival Graph

<div align="center">
  <img src="zombie-graph.svg" alt="GitHub Zombie Survival Graph" />
</div>

<br>

<div align="center">
  <table>
    <tr>
      <td align="center"><a href="#english">🇬🇧 English</a></td>
      <td align="center"><a href="#turkce">🇹🇷 Türkçe</a></td>
      <td align="center"><a href="#espanol">🇪🇸 Español</a></td>
      <td align="center"><a href="#deutsch">🇩🇪 Deutsch</a></td>
      <td align="center"><a href="#francais">🇫🇷 Français</a></td>
    </tr>
    <tr>
      <td align="center"><a href="#italiano">🇮🇹 Italiano</a></td>
      <td align="center"><a href="#portugues">🇵🇹 Português</a></td>
      <td align="center"><a href="#русский">🇷🇺 Русский</a></td>
      <td align="center"><a href="#nederlands">🇳🇱 Nederlands</a></td>
      <td align="center"><a href="#polski">🇵🇱 Polski</a></td>
    </tr>
  </table>
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

---

<h2 id="espanol">🇪🇸 Español</h2>

¡Transforma tu gráfico de contribuciones de GitHub estándar en un sistema táctico de supervivencia post-apocalíptico! Esta GitHub Action genera un SVG dinámico que muestra tu racha de supervivencia, zombis eliminados (commits) y rango táctico.

### 🚀 Cómo Utilizar

**1. Crear el Flujo de Trabajo (Workflow)**
Crea un nuevo archivo en tu repositorio en `.github/workflows/zombie-graph.yml` y añade el siguiente código:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

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

> **⚠️ Nota Importante:** Asegúrate de que tu repositorio permite a las Actions leer y escribir. Ve a **Settings > Actions > General**, desplázate hasta **Workflow permissions** y selecciona **"Read and write permissions"**.

**2. Actualizar el README**
Añade el SVG generado al `README.md` de tu perfil:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="deutsch">🇩🇪 Deutsch</h2>

Verwandle dein standardmäßiges GitHub-Beitragsdiagramm in ein postapokalyptisches taktisches Überlebenssystem! Diese GitHub Action generiert eine dynamische SVG, die deine Überlebenssträhne, eliminierte Zombies (Commits) und deinen taktischen Rang anzeigt.

### 🚀 Verwendung

**1. Workflow Erstellen**
Erstelle eine neue Datei in deinem Repository unter `.github/workflows/zombie-graph.yml` und füge den folgenden Code hinzu:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

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

> **⚠️ Wichtiger Hinweis:** Stelle sicher, dass dein Repository Lese- und Schreibrechte für Actions erlaubt. Gehe zu **Settings > Actions > General**, scrolle zu **Workflow permissions** und wähle **"Read and write permissions"**.

**2. README Aktualisieren**
Füge die generierte SVG-Datei zur `README.md` deines Profils hinzu:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="francais">🇫🇷 Français</h2>

Transformez votre graphique de contributions GitHub standard en un système de survie tactique post-apocalyptique ! Cette GitHub Action génère un SVG dynamique affichant votre série de survie, les zombies éliminés (commits) et votre rang tactique.

### 🚀 Comment l'utiliser

**1. Créer le Workflow**
Créez un nouveau fichier dans votre dépôt à l'emplacement `.github/workflows/zombie-graph.yml` et ajoutez le code suivant :

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

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

> **⚠️ Remarque Importante :** Assurez-vous que votre dépôt autorise les Actions à lire et écrire. Allez dans **Settings > Actions > General**, descendez jusqu'à **Workflow permissions**, et sélectionnez **"Read and write permissions"**.

**2. Mettre à jour votre README**
Ajoutez le SVG généré au `README.md` de votre profil :

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="italiano">🇮🇹 Italiano</h2>

Trasforma il tuo grafico standard dei contributi di GitHub in un sistema tattico di sopravvivenza post-apocalittico! Questa GitHub Action genera un SVG dinamico che mostra la tua serie di sopravvivenza, gli zombie eliminati (commit) e il tuo grado tattico.

### 🚀 Come Usarlo

**1. Creare il Workflow**
Crea un nuovo file nel tuo repository in `.github/workflows/zombie-graph.yml` e aggiungi il seguente codice:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

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

> **⚠️ Nota Importante:** Assicurati che il tuo repository consenta alle Action di leggere e scrivere. Vai su **Settings > Actions > General**, scorri fino a **Workflow permissions** e seleziona **"Read and write permissions"**.

**2. Aggiornare il README**
Aggiungi l'SVG generato al `README.md` del tuo profilo:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="portugues">🇵🇹 Português</h2>

Transforme seu gráfico de contribuições padrão do GitHub em um sistema tático de sobrevivência pós-apocalíptico! Esta GitHub Action gera um SVG dinâmico mostrando sua sequência de sobrevivência, zumbis eliminados (commits) e rank tático.

### 🚀 Como Usar

**1. Criar o Workflow**
Crie um novo arquivo no seu repositório em `.github/workflows/zombie-graph.yml` e adicione o seguinte código:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

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

> **⚠️ Nota Importante:** Certifique-se de que seu repositório permite que as Actions leiam e escrevam. Vá para **Settings > Actions > General**, role até **Workflow permissions** e selecione **"Read and write permissions"**.

**2. Atualizar o README**
Adicione o SVG gerado ao `README.md` do seu perfil:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="русский">🇷🇺 Русский</h2>

Превратите ваш стандартный график активности GitHub в постапокалиптическую тактическую систему выживания! Этот GitHub Action создает динамический SVG, показывающий вашу серию выживания, уничтоженных зомби (коммиты) и тактический ранг.

### 🚀 Как Использовать

**1. Создайте рабочий процесс (Workflow)**
Создайте новый файл в вашем репозитории по пути `.github/workflows/zombie-graph.yml` и добавьте следующий код:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

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

> **⚠️ Важное Примечание:** Убедитесь, что ваш репозиторий разрешает Actions чтение и запись. Перейдите в **Settings > Actions > General**, прокрутите до **Workflow permissions** и выберите **"Read and write permissions"**.

**2. Обновите ваш README**
Добавьте сгенерированный SVG в `README.md` вашего профиля:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="nederlands">🇳🇱 Nederlands</h2>

Transformeer je standaard GitHub bijdragegrafiek in een post-apocalyptisch tactisch overlevingssysteem! Deze GitHub Action genereert een dynamische SVG die je overlevingsreeks, geëlimineerde zombies (commits) en tactische rang toont.

### 🚀 Hoe te Gebruiken

**1. Maak de Workflow aan**
Maak een nieuw bestand in je repository op `.github/workflows/zombie-graph.yml` en voeg de volgende code toe:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

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

> **⚠️ Belangrijke Opmerking:** Zorg ervoor dat je repository Actions toestaat om te lezen en schrijven. Ga naar **Settings > Actions > General**, scrol naar **Workflow permissions** en selecteer **"Read and write permissions"**.

**2. Werk je README bij**
Voeg de gegenereerde SVG toe aan de `README.md` van je profiel:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```

---

<h2 id="polski">🇵🇱 Polski</h2>

Przekształć swój standardowy wykres aktywności GitHub w postapokaliptyczny system taktycznego przetrwania! Ta akcja GitHub generuje dynamiczny SVG pokazujący Twoją serię przetrwania, wyeliminowane zombie (commity) i rangę taktyczną.

### 🚀 Jak Używać

**1. Utwórz Workflow**
Utwórz nowy plik w swoim repozytorium pod adresem `.github/workflows/zombie-graph.yml` i dodaj następujący kod:

```yaml
name: GitHub Zombie Survival Graph

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: 

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

> **⚠️ Ważna Uwaga:** Upewnij się, że Twoje repozytorium zezwala Actions na odczyt i zapis. Przejdź do **Settings > Actions > General**, przewiń do **Workflow permissions** i wybierz **"Read and write permissions"**.

**2. Zaktualizuj README**
Dodaj wygenerowany plik SVG do `README.md` w swoim profilu:

```html
<div align="center">
  <img src="zombie-graph.svg" alt="My Zombie Survival Status" />
</div>
```
