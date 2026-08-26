# 🧟‍♂️ GitHub Zombie Survival Graph

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

<br>

<div align="center">
  <img src="zombie-graph.svg" alt="GitHub Zombie Survival Graph" />
</div>

---

<h2 id="english">🇬🇧 English</h2>

Transform your standard GitHub contribution graph into a post-apocalyptic tactical survival system! This GitHub Action generates a dynamic SVG showing your survival streak, eliminated zombies (commits), and tactical rank based on your daily GitHub activity.

### 🎯 The Goal & Mechanics
Survive the apocalypse by writing code! Every day, a deterministic number of zombies attacks your sector. You must make enough GitHub commits to eliminate them.
* **Cleared:** Your Commits >= Zombies. Sector secured!
* **Invaded:** Your Commits < Zombies. The sector is overrun.
* **Survival Streak:** If you make **0 commits** in a day, your active "Survival Day" streak resets to 0. Don't break the chain!
* **🖥️ UI Features:** Terminal aesthetics, a local radar, live cam, and a terminal-style XP loading bar.

### ⚔️ Difficulty Levels
Control how many zombies spawn each day with the `difficulty` input:

| Value | Zombies per Day | Description |
|-------|----------------|-------------|
| `easy` | 1 – 2 | For casual coders |
| `normal` | 1 – 4 | Default — balanced challenge |
| `hard` | 3 – 6 | You'd better commit daily |
| `nightmare` | 5 – 10 | Extreme pressure. No rest. |

### 🎨 Themes
Customize the look of your SVG with the `theme` input:

| Value | Style |
|-------|-------|
| `classic` | The original pre-theming colors (neon green, dark background, crimson red) |
| `cyberpunk` | Same neon-green cyberpunk palette — independently customizable |
| `fallout` | Pip-Boy amber/orange on deep black |
| `resident_evil` | Umbrella Corp — white text, deep red danger colors |

### 🚀 How to Use

**1. Create the Workflow**
Create a new file in your repository at `.github/workflows/zombie-graph.yml` and add the following code:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main # Updates the graph every time you push code
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 Oyunun Amacı ve Mekanikler
Kod yazarak kıyametten sağ çıkın! Her gün, bölgenize belirli sayıda zombi saldırır. Onları yok etmek için yeterli sayıda GitHub commit'i atmalısınız.
* **Temizlendi (Cleared):** Commit >= Zombi. Bölge güvende!
* **İstila Edildi (Invaded):** Commit < Zombi. Bölge ele geçirildi.
* **Hayatta Kalma Serisi (Streak):** Bir gün boyunca hiç commit atmazsanız (0 commit), "Survival Day" seriniz 0'a sıfırlanır. Zinciri kırmayın!
* **🖥️ Arayüz Özellikleri:** Terminal estetiği, yerel radar, canlı kamera ve terminal tarzı XP yükleme çubuğu.

### ⚔️ Zorluk Seviyeleri
Her gün kaç zombinin saldıracağını `difficulty` parametresiyle belirleyin:

| Değer | Günlük Zombi | Açıklama |
|-------|-------------|----------|
| `easy` | 1 – 2 | Rahat bir tempo |
| `normal` | 1 – 4 | Varsayılan — dengeli zorluk |
| `hard` | 3 – 6 | Her gün commit atmak zorundasın |
| `nightmare` | 5 – 10 | Aşırı baskı. Dinlenme yok. |

### 🎨 Temalar
SVG'nin görünümünü `theme` parametresiyle özelleştirin:

| Değer | Stil |
|-------|------|
| `classic` | Orijinal eski renkler (neon yeşil, koyu arka plan, kırmızı tehlike) |
| `cyberpunk` | Aynı neon-yeşil siberpunk paleti — bağımsız özelleştirilebilir |
| `fallout` | Pip-Boy amber/turuncu, çok koyu arka plan |
| `resident_evil` | Umbrella Corp — beyaz metin, derin kırmızı tehlike renkleri |

### 🚀 Nasıl Kullanılır?

**1. Workflow Dosyasını Oluşturun**
Deponuzda `.github/workflows/zombie-graph.yml` yolunda yeni bir dosya oluşturun ve aşağıdaki kodu ekleyin:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main # Her kod gönderdiğinizde grafiği günceller
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 El Objetivo y Mecánicas
¡Sobrevive al apocalipsis escribiendo código! Cada día, un número de zombis ataca tu sector. Debes hacer suficientes commits para eliminarlos.
* **Despejado (Cleared):** Commits >= Zombis. ¡Sector asegurado!
* **Invadido (Invaded):** Commits < Zombis. El sector ha sido invadido.
* **Racha (Streak):** Si haces **0 commits** en un día, tu racha de "Survival Day" se reinicia a 0. ¡No rompas la cadena!
* **🖥️ Interfaz:** Estética de terminal, radar local, cámara en vivo y barra de XP de terminal.

### ⚔️ Niveles de Dificultad
Controla cuántos zombis aparecen cada día con el parámetro `difficulty`:

| Valor | Zombis por Día | Descripción |
|-------|---------------|-------------|
| `easy` | 1 – 2 | Para programadores casuales |
| `normal` | 1 – 4 | Predeterminado — desafío equilibrado |
| `hard` | 3 – 6 | Mejor que hagas commits a diario |
| `nightmare` | 5 – 10 | Presión extrema. Sin descanso. |

### 🎨 Temas
Personaliza el aspecto de tu SVG con el parámetro `theme`:

| Valor | Estilo |
|-------|--------|
| `classic` | Los colores originales (verde neón, fondo oscuro, rojo carmesí) |
| `cyberpunk` | La misma paleta neón-verde — personalizable de forma independiente |
| `fallout` | Ámbar/naranja Pip-Boy sobre negro profundo |
| `resident_evil` | Umbrella Corp — texto blanco, colores de peligro rojo intenso |

### 🚀 Cómo Utilizar

**1. Crear el Flujo de Trabajo (Workflow)**
Crea un nuevo archivo en tu repositorio en `.github/workflows/zombie-graph.yml` y añade el siguiente código:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 Das Ziel & Mechanik
Überlebe die Apokalypse, indem du Code schreibst! Jeden Tag greifen Zombies deinen Sektor an. Du musst genug Commits machen, um sie zu eliminieren.
* **Geräumt (Cleared):** Commits >= Zombies. Sektor gesichert!
* **Überrannt (Invaded):** Commits < Zombies. Der Sektor wird überrannt.
* **Überlebensserie (Streak):** Wenn du an einem Tag **0 Commits** machst, wird deine "Survival Day"-Serie auf 0 zurückgesetzt. Brich die Kette nicht!
* **🖥️ UI-Funktionen:** Terminal-Ästhetik, lokales Radar, Live-Kamera und Terminal-XP-Leiste.

### ⚔️ Schwierigkeitsgrade
Steuere mit dem Parameter `difficulty`, wie viele Zombies täglich spawnen:

| Wert | Zombies pro Tag | Beschreibung |
|------|----------------|--------------|
| `easy` | 1 – 2 | Für gelegentliche Programmierer |
| `normal` | 1 – 4 | Standard — ausgewogene Herausforderung |
| `hard` | 3 – 6 | Du solltest täglich committen |
| `nightmare` | 5 – 10 | Extremer Druck. Keine Ruhe. |

### 🎨 Themes
Passe das Aussehen deiner SVG mit dem Parameter `theme` an:

| Wert | Stil |
|------|------|
| `classic` | Die originalen Farben (Neongrün, dunkler Hintergrund, Dunkelrot) |
| `cyberpunk` | Dieselbe Neongrün-Palette — unabhängig anpassbar |
| `fallout` | Pip-Boy Bernstein/Orange auf tiefem Schwarz |
| `resident_evil` | Umbrella Corp — weißer Text, tiefrote Gefahrenfarben |

### 🚀 Verwendung

**1. Workflow Erstellen**
Erstelle eine neue Datei in deinem Repository unter `.github/workflows/zombie-graph.yml` und füge den folgenden Code hinzu:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 L'Objectif et Mécaniques
Survivez à l'apocalypse en écrivant du code ! Chaque jour, des zombies attaquent votre secteur. Vous devez faire suffisamment de commits pour les éliminer.
* **Sécurisé (Cleared) :** Commits >= Zombies. Secteur sécurisé !
* **Envahi (Invaded) :** Commits < Zombies. Le secteur est envahi.
* **Série de survie (Streak) :** Si vous faites **0 commit** en un jour, votre série "Survival Day" retombe à 0. Ne brisez pas la chaîne !
* **🖥️ Interface :** Esthétique de terminal, radar local, caméra en direct et barre d'XP style terminal.

### ⚔️ Niveaux de Difficulté
Contrôlez le nombre de zombies par jour avec le paramètre `difficulty` :

| Valeur | Zombies par Jour | Description |
|--------|-----------------|-------------|
| `easy` | 1 – 2 | Pour les codeurs occasionnels |
| `normal` | 1 – 4 | Par défaut — défi équilibré |
| `hard` | 3 – 6 | Mieux vaut commiter chaque jour |
| `nightmare` | 5 – 10 | Pression extrême. Pas de repos. |

### 🎨 Thèmes
Personnalisez l'apparence de votre SVG avec le paramètre `theme` :

| Valeur | Style |
|--------|-------|
| `classic` | Les couleurs d'origine (vert néon, fond sombre, rouge cramoisi) |
| `cyberpunk` | La même palette néon-vert — personnalisable indépendamment |
| `fallout` | Ambre/orange Pip-Boy sur noir profond |
| `resident_evil` | Umbrella Corp — texte blanc, rouge danger intense |

### 🚀 Comment l'utiliser

**1. Créer le Workflow**
Créez un nouveau fichier dans votre dépôt à l'emplacement `.github/workflows/zombie-graph.yml` et ajoutez le code suivant :

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 L'Obiettivo e Meccaniche
Sopravvivi all'apocalisse scrivendo codice! Ogni giorno, degli zombie attaccano il tuo settore. Devi fare abbastanza commit per eliminarli.
* **Liberato (Cleared):** Commit >= Zombie. Settore sicuro!
* **Invaso (Invaded):** Commit < Zombie. Il settore è invaso.
* **Serie (Streak):** Se fai **0 commit** in un giorno, la tua serie "Survival Day" si azzera. Non spezzare la catena!
* **🖥️ Interfaccia:** Estetica terminale, radar locale, live cam e barra XP da terminale.

### ⚔️ Livelli di Difficoltà
Controlla quanti zombie appaiono ogni giorno con il parametro `difficulty`:

| Valore | Zombie al Giorno | Descrizione |
|--------|-----------------|-------------|
| `easy` | 1 – 2 | Per programmatori occasionali |
| `normal` | 1 – 4 | Predefinito — sfida equilibrata |
| `hard` | 3 – 6 | Meglio fare commit ogni giorno |
| `nightmare` | 5 – 10 | Pressione estrema. Nessuna tregua. |

### 🎨 Temi
Personalizza l'aspetto del tuo SVG con il parametro `theme`:

| Valore | Stile |
|--------|-------|
| `classic` | I colori originali (verde neon, sfondo scuro, rosso cremisi) |
| `cyberpunk` | La stessa palette neon-verde — personalizzabile indipendentemente |
| `fallout` | Ambra/arancio Pip-Boy su nero profondo |
| `resident_evil` | Umbrella Corp — testo bianco, colori pericolo rosso intenso |

### 🚀 Come Usarlo

**1. Creare il Workflow**
Crea un nuovo file nel tuo repository in `.github/workflows/zombie-graph.yml` e aggiungi il seguente codice:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 O Objetivo e Mecânicas
Sobreviva ao apocalipse escrevendo código! Todos os dias, zumbis atacam seu setor. Você deve fazer commits suficientes para eliminá-los.
* **Livre (Cleared):** Commits >= Zumbis. Setor seguro!
* **Invadido (Invaded):** Commits < Zumbis. O setor foi invadido.
* **Sequência (Streak):** Se você fizer **0 commits** em um dia, sua sequência de "Survival Day" zera. Não quebre a corrente!
* **🖥️ Interface:** Estética de terminal, radar local, câmera ao vivo e barra de XP de terminal.

### ⚔️ Níveis de Dificuldade
Controle quantos zumbis aparecem por dia com o parâmetro `difficulty`:

| Valor | Zumbis por Dia | Descrição |
|-------|---------------|-----------|
| `easy` | 1 – 2 | Para programadores casuais |
| `normal` | 1 – 4 | Padrão — desafio equilibrado |
| `hard` | 3 – 6 | Melhor fazer commits todo dia |
| `nightmare` | 5 – 10 | Pressão extrema. Sem descanso. |

### 🎨 Temas
Personalize a aparência do seu SVG com o parâmetro `theme`:

| Valor | Estilo |
|-------|--------|
| `classic` | As cores originais (verde neon, fundo escuro, vermelho carmesim) |
| `cyberpunk` | A mesma paleta neon-verde — personalizável de forma independente |
| `fallout` | Âmbar/laranja Pip-Boy sobre preto profundo |
| `resident_evil` | Umbrella Corp — texto branco, cores de perigo vermelho intenso |

### 🚀 Como Usar

**1. Criar o Workflow**
Crie um novo arquivo no seu repositório em `.github/workflows/zombie-graph.yml` e adicione o seguinte código:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 Цель и Механика
Выживите в апокалипсисе, создавая код! Каждый день зомби атакуют ваш сектор. Сделайте достаточно коммитов, чтобы уничтожить их.
* **Очищено (Cleared):** Коммиты >= Зомби. Сектор в безопасности!
* **Захвачено (Invaded):** Коммиты < Зомби. Сектор захвачен.
* **Серия выживания (Streak):** Если вы сделаете **0 коммитов** за день, ваша серия "Survival Day" сбросится до 0. Не прерывайте цепь!
* **🖥️ Интерфейс:** Эстетика терминала, локальный радар, прямая трансляция и шкала XP в стиле терминала.

### ⚔️ Уровни Сложности
Управляйте количеством зомби в день с помощью параметра `difficulty`:

| Значение | Зомби в День | Описание |
|----------|-------------|----------|
| `easy` | 1 – 2 | Для любителей |
| `normal` | 1 – 4 | По умолчанию — сбалансированное испытание |
| `hard` | 3 – 6 | Лучше делайте коммиты ежедневно |
| `nightmare` | 5 – 10 | Экстремальное давление. Без отдыха. |

### 🎨 Темы
Настройте внешний вид SVG с помощью параметра `theme`:

| Значение | Стиль |
|----------|-------|
| `classic` | Оригинальные цвета (неоновый зелёный, тёмный фон, тёмно-красный) |
| `cyberpunk` | Та же неоново-зелёная палитра — независимо настраиваемая |
| `fallout` | Янтарный/оранжевый Pip-Boy на глубоком чёрном |
| `resident_evil` | Umbrella Corp — белый текст, насыщенный красный для опасности |

### 🚀 Как Использовать

**1. Создайте рабочий процесс (Workflow)**
Создайте новый файл в вашем репозитории по пути `.github/workflows/zombie-graph.yml` и добавьте следующий код:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 Het Doel & Mechanica
Overleef de apocalyps door code te schrijven! Elke dag vallen zombies je sector aan. Je moet genoeg commits maken om ze te elimineren.
* **Gevrijwaard (Cleared):** Commits >= Zombies. Sector veilig!
* **Overspoeld (Invaded):** Commits < Zombies. De sector is overspoeld.
* **Overlevingsreeks (Streak):** Als je **0 commits** op een dag maakt, wordt je "Survival Day"-reeks gereset naar 0. Verbreek de ketting niet!
* **🖥️ Interface:** Terminal esthetiek, lokale radar, live cam en terminal-stijl XP balk.

### ⚔️ Moeilijkheidsgraden
Bepaal hoeveel zombies er dagelijks spawnen met de parameter `difficulty`:

| Waarde | Zombies per Dag | Beschrijving |
|--------|----------------|--------------|
| `easy` | 1 – 2 | Voor casual programmeurs |
| `normal` | 1 – 4 | Standaard — evenwichtige uitdaging |
| `hard` | 3 – 6 | Beter dagelijks committen |
| `nightmare` | 5 – 10 | Extreme druk. Geen rust. |

### 🎨 Thema's
Pas het uiterlijk van je SVG aan met de parameter `theme`:

| Waarde | Stijl |
|--------|-------|
| `classic` | De originele kleuren (neongroen, donkere achtergrond, donkerrood) |
| `cyberpunk` | Dezelfde neongroene paletten — onafhankelijk aanpasbaar |
| `fallout` | Pip-Boy amber/oranje op diep zwart |
| `resident_evil` | Umbrella Corp — witte tekst, dieprode gevaarskleur |

### 🚀 Hoe te Gebruiken

**1. Maak de Workflow aan**
Maak een nieuw bestand in je repository op `.github/workflows/zombie-graph.yml` en voeg de volgende code toe:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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

### 🎯 Cel i Mechanika
Przetrwaj apokalipsę pisząc kod! Codziennie zombie atakują twój sektor. Musisz zrobić wystarczająco dużo commitów, aby ich wyeliminować.
* **Oczyszczono (Cleared):** Commity >= Zombie. Sektor bezpieczny!
* **Zajęto (Invaded):** Commity < Zombie. Sektor został zajęty.
* **Seria przetrwania (Streak):** Jeśli w ciągu dnia zrobisz **0 commitów**, twoja seria "Survival Day" zresetuje się do 0. Nie przerywaj łańcucha!
* **🖥️ Interfejs:** Estetyka terminala, lokalny radar, kamera na żywo i pasek XP w stylu terminala.

### ⚔️ Poziomy Trudności
Kontroluj liczbę zombie pojawiających się każdego dnia za pomocą parametru `difficulty`:

| Wartość | Zombie na Dzień | Opis |
|---------|----------------|------|
| `easy` | 1 – 2 | Dla okazjonalnych programistów |
| `normal` | 1 – 4 | Domyślny — zrównoważone wyzwanie |
| `hard` | 3 – 6 | Lepiej commitować codziennie |
| `nightmare` | 5 – 10 | Ekstremalna presja. Bez odpoczynku. |

### 🎨 Motywy
Dostosuj wygląd swojego SVG za pomocą parametru `theme`:

| Wartość | Styl |
|---------|------|
| `classic` | Oryginalne kolory (neonowa zieleń, ciemne tło, ciemnoczerwony) |
| `cyberpunk` | Ta sama paleta neonowej zieleni — niezależnie konfigurowalna |
| `fallout` | Bursztynowy/pomarańczowy Pip-Boy na głębokiej czerni |
| `resident_evil` | Umbrella Corp — biały tekst, głęboka czerwień dla zagrożenia |

### 🚀 Jak Używać

**1. Utwórz Workflow**
Utwórz nowy plik w swoim repozytorium pod adresem `.github/workflows/zombie-graph.yml` i dodaj następujący kod:

```yaml
name: GitHub Zombie Survival Graph

on:
  push:
    branches:
      - main
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
        uses: achexus/github-zombie-graph@v1.2.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          difficulty: normal      # easy | normal | hard | nightmare
          theme: cyberpunk        # classic | cyberpunk | fallout | resident_evil

      - name: Commit and Push the generated SVG
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update zombie survival graph"
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
