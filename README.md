import urllib.request
from weasyprint import HTML, CSS

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    @page {
        size: A4;
        margin: 15mm 15mm;
        background-color: #0d1117;
    }
    
    *, *::before, *::after {
        box-sizing: border-box;
    }
    
    body {
        margin: 0;
        padding: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #0d1117;
        color: #c9d1d9;
        font-size: 11pt;
        line-height: 1.6;
    }
    
    h1 {
        color: #39ff14;
        text-align: center;
        font-size: 24pt;
        margin-top: 20mm;
        margin-bottom: 5mm;
        text-transform: uppercase;
        border-bottom: 2px solid #39ff14;
        padding-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        color: #8b949e;
        font-size: 14pt;
        margin-bottom: 20mm;
    }
    
    h2 {
        color: #39ff14;
        font-size: 16pt;
        border-left: 4px solid #39ff14;
        padding-left: 10px;
        margin-top: 30px;
        margin-bottom: 15px;
        page-break-after: avoid;
    }
    
    h3 {
        color: #58a6ff;
        font-size: 13pt;
        margin-top: 20px;
        margin-bottom: 10px;
        page-break-after: avoid;
    }
    
    p {
        margin-bottom: 15px;
    }
    
    .code-block {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 12px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 9.5pt;
        color: #e6edf3;
        white-space: pre;
        overflow-x: hidden;
        page-break-inside: avoid;
        margin-bottom: 15px;
    }
    
    .warning {
        background-color: rgba(210, 153, 34, 0.15);
        border-left: 4px solid #d29922;
        padding: 12px 15px;
        margin: 15px 0;
        border-radius: 0 6px 6px 0;
        page-break-inside: avoid;
    }
    
    .warning strong {
        color: #d29922;
    }
    
    .index-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 20px;
        margin-bottom: 40px;
    }
    
    .index-box h3 {
        margin-top: 0;
        border-bottom: 1px solid #30363d;
        padding-bottom: 10px;
    }
    
    .lang-item {
        display: inline-block;
        width: 48%;
        margin-bottom: 8px;
        font-weight: bold;
    }
    
    .section-divider {
        border: 0;
        height: 1px;
        background-color: #30363d;
        margin: 40px 0;
    }
    
    .keyword { color: #ff7b72; }
    .string { color: #a5d6ff; }
    .comment { color: #8b949e; font-style: italic; }
    .variable { color: #79c0ff; }
    
</style>
</head>
<body>

    <h1>GitHub Zombie Survival Graph</h1>
    <div class="subtitle">Multi-Lingual README Documentation Setup Guide (10 Languages)</div>
    
    <div class="index-box">
        <h3>Supported Languages</h3>
        <div style="display: block;">
            <span class="lang-item">🇬🇧 English (EN)</span>
            <span class="lang-item">🇹🇷 Türkçe (TR)</span>
            <span class="lang-item">🇪🇸 Español (ES)</span>
            <span class="lang-item">🇩🇪 Deutsch (DE)</span>
            <span class="lang-item">🇫🇷 Français (FR)</span>
            <span class="lang-item">🇮🇹 Italiano (IT)</span>
            <span class="lang-item">🇵🇹 Português (PT)</span>
            <span class="lang-item">🇷🇺 Русский (RU)</span>
            <span class="lang-item">🇳🇱 Nederlands (NL)</span>
            <span class="lang-item">🇵🇱 Polski (PL)</span>
        </div>
    </div>
    
    <p>Copy the code blocks below for the languages you want to support in your repository's <code>README.md</code>. You can create a table of contents in your README that anchors to each language section.</p>
    
    <hr class="section-divider">
"""

languages_data = [
    {
        "flag": "🇬🇧",
        "lang": "English",
        "desc": "Transform your standard GitHub contribution graph into a post-apocalyptic tactical survival system! This GitHub Action generates a dynamic SVG showing your survival streak, eliminated zombies (commits), and tactical rank based on your daily GitHub activity.",
        "how_to": "🚀 How to Use",
        "step1": "1. Create the Workflow",
        "step1_desc": "Create a new file in your repository at <code>.github/workflows/zombie-graph.yml</code> and add the following code:",
        "warning_title": "⚠️ Important Note",
        "warning_desc": "Ensure your repository allows Actions to read and write. Go to <strong>Settings > Actions > General</strong>, scroll down to <strong>Workflow permissions</strong>, and select <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. Update your README",
        "step2_desc": "Add the generated SVG to your profile's <code>README.md</code>:"
    },
    {
        "flag": "🇹🇷",
        "lang": "Türkçe",
        "desc": "Klasik GitHub katkı grafiğinizi kıyamet sonrası taktiksel bir hayatta kalma sistemine dönüştürün! Bu GitHub Action, günlük GitHub aktivitenize dayanarak hayatta kalma serinizi, yok edilen zombileri (commit'ler) ve taktiksel rütbenizi gösteren dinamik bir SVG oluşturur.",
        "how_to": "🚀 Nasıl Kullanılır?",
        "step1": "1. Workflow Dosyasını Oluşturun",
        "step1_desc": "Deponuzda <code>.github/workflows/zombie-graph.yml</code> yolunda yeni bir dosya oluşturun ve aşağıdaki kodu ekleyin:",
        "warning_title": "⚠️ Önemli Not",
        "warning_desc": "Deponuzun Action'lar için okuma ve yazma iznine sahip olduğundan emin olun. <strong>Settings > Actions > General</strong> sekmesine gidin, en alttaki <strong>Workflow permissions</strong> kısmından <strong>\"Read and write permissions\"</strong> seçeneğini işaretleyip kaydedin.",
        "step2": "2. README Dosyanızı Güncelleyin",
        "step2_desc": "Oluşturulan SVG dosyasını profilinizin <code>README.md</code> dosyasına ekleyin:"
    },
    {
        "flag": "🇪🇸",
        "lang": "Español",
        "desc": "¡Transforma tu gráfico de contribuciones de GitHub estándar en un sistema táctico de supervivencia post-apocalíptico! Esta GitHub Action genera un SVG dinámico que muestra tu racha de supervivencia, zombis eliminados (commits) y rango táctico.",
        "how_to": "🚀 Cómo Utilizar",
        "step1": "1. Crear el Flujo de Trabajo (Workflow)",
        "step1_desc": "Crea un nuevo archivo en tu repositorio en <code>.github/workflows/zombie-graph.yml</code> y añade el siguiente código:",
        "warning_title": "⚠️ Nota Importante",
        "warning_desc": "Asegúrate de que tu repositorio permite a las Actions leer y escribir. Ve a <strong>Settings > Actions > General</strong>, desplázate hasta <strong>Workflow permissions</strong> y selecciona <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. Actualizar el README",
        "step2_desc": "Añade el SVG generado al <code>README.md</code> de tu perfil:"
    },
    {
        "flag": "🇩🇪",
        "lang": "Deutsch",
        "desc": "Verwandle dein standardmäßiges GitHub-Beitragsdiagramm in ein postapokalyptisches taktisches Überlebenssystem! Diese GitHub Action generiert eine dynamische SVG, die deine Überlebenssträhne, eliminierte Zombies (Commits) und deinen taktischen Rang anzeigt.",
        "how_to": "🚀 Verwendung",
        "step1": "1. Workflow Erstellen",
        "step1_desc": "Erstelle eine neue Datei in deinem Repository unter <code>.github/workflows/zombie-graph.yml</code> und füge den folgenden Code hinzu:",
        "warning_title": "⚠️ Wichtiger Hinweis",
        "warning_desc": "Stelle sicher, dass dein Repository Lese- und Schreibrechte für Actions erlaubt. Gehe zu <strong>Settings > Actions > General</strong>, scrolle zu <strong>Workflow permissions</strong> und wähle <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. README Aktualisieren",
        "step2_desc": "Füge die generierte SVG-Datei zur <code>README.md</code> deines Profils hinzu:"
    },
    {
        "flag": "🇫🇷",
        "lang": "Français",
        "desc": "Transformez votre graphique de contributions GitHub standard en un système de survie tactique post-apocalyptique ! Cette GitHub Action génère un SVG dynamique affichant votre série de survie, les zombies éliminés (commits) et votre rang tactique.",
        "how_to": "🚀 Comment l'utiliser",
        "step1": "1. Créer le Workflow",
        "step1_desc": "Créez un nouveau fichier dans votre dépôt à l'emplacement <code>.github/workflows/zombie-graph.yml</code> et ajoutez le code suivant :",
        "warning_title": "⚠️ Remarque Importante",
        "warning_desc": "Assurez-vous que votre dépôt autorise les Actions à lire et écrire. Allez dans <strong>Settings > Actions > General</strong>, descendez jusqu'à <strong>Workflow permissions</strong>, et sélectionnez <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. Mettre à jour votre README",
        "step2_desc": "Ajoutez le SVG généré au <code>README.md</code> de votre profil :"
    },
    {
        "flag": "🇮🇹",
        "lang": "Italiano",
        "desc": "Trasforma il tuo grafico standard dei contributi di GitHub in un sistema tattico di sopravvivenza post-apocalittico! Questa GitHub Action genera un SVG dinamico che mostra la tua serie di sopravvivenza, gli zombie eliminati (commit) e il tuo grado tattico.",
        "how_to": "🚀 Come Usarlo",
        "step1": "1. Creare il Workflow",
        "step1_desc": "Crea un nuovo file nel tuo repository in <code>.github/workflows/zombie-graph.yml</code> e aggiungi il seguente codice:",
        "warning_title": "⚠️ Nota Importante",
        "warning_desc": "Assicurati che il tuo repository consenta alle Action di leggere e scrivere. Vai su <strong>Settings > Actions > General</strong>, scorri fino a <strong>Workflow permissions</strong> e seleziona <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. Aggiornare il README",
        "step2_desc": "Aggiungi l'SVG generato al <code>README.md</code> del tuo profilo:"
    },
    {
        "flag": "🇵🇹",
        "lang": "Português",
        "desc": "Transforme seu gráfico de contribuições padrão do GitHub em um sistema tático de sobrevivência pós-apocalíptico! Esta GitHub Action gera um SVG dinâmico mostrando sua sequência de sobrevivência, zumbis eliminados (commits) e rank tático.",
        "how_to": "🚀 Como Usar",
        "step1": "1. Criar o Workflow",
        "step1_desc": "Crie um novo arquivo no seu repositório em <code>.github/workflows/zombie-graph.yml</code> e adicione o seguinte código:",
        "warning_title": "⚠️ Nota Importante",
        "warning_desc": "Certifique-se de que seu repositório permite que as Actions leiam e escrevam. Vá para <strong>Settings > Actions > General</strong>, role até <strong>Workflow permissions</strong> e selecione <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. Atualizar o README",
        "step2_desc": "Adicione o SVG gerado ao <code>README.md</code> do seu perfil:"
    },
    {
        "flag": "🇷🇺",
        "lang": "Русский",
        "desc": "Превратите ваш стандартный график активности GitHub в постапокалиптическую тактическую систему выживания! Этот GitHub Action создает динамический SVG, показывающий вашу серию выживания, уничтоженных зомби (коммиты) и тактический ранг.",
        "how_to": "🚀 Как Использовать",
        "step1": "1. Создайте рабочий процесс (Workflow)",
        "step1_desc": "Создайте новый файл в вашем репозитории по пути <code>.github/workflows/zombie-graph.yml</code> и добавьте следующий код:",
        "warning_title": "⚠️ Важное Примечание",
        "warning_desc": "Убедитесь, что ваш репозиторий разрешает Actions чтение и запись. Перейдите в <strong>Settings > Actions > General</strong>, прокрутите до <strong>Workflow permissions</strong> и выберите <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. Обновите ваш README",
        "step2_desc": "Добавьте сгенерированный SVG в <code>README.md</code> вашего профиля:"
    },
    {
        "flag": "🇳🇱",
        "lang": "Nederlands",
        "desc": "Transformeer je standaard GitHub bijdragegrafiek in een post-apocalyptisch tactisch overlevingssysteem! Deze GitHub Action genereert een dynamische SVG die je overlevingsreeks, geëlimineerde zombies (commits) en tactische rang toont.",
        "how_to": "🚀 Hoe te Gebruiken",
        "step1": "1. Maak de Workflow aan",
        "step1_desc": "Maak een nieuw bestand in je repository op <code>.github/workflows/zombie-graph.yml</code> en voeg de volgende code toe:",
        "warning_title": "⚠️ Belangrijke Opmerking",
        "warning_desc": "Zorg ervoor dat je repository Actions toestaat om te lezen en schrijven. Ga naar <strong>Settings > Actions > General</strong>, scrol naar <strong>Workflow permissions</strong> en selecteer <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. Werk je README bij",
        "step2_desc": "Voeg de gegenereerde SVG toe aan de <code>README.md</code> van je profiel:"
    },
    {
        "flag": "🇵🇱",
        "lang": "Polski",
        "desc": "Przekształć swój standardowy wykres aktywności GitHub w postapokaliptyczny system taktycznego przetrwania! Ta akcja GitHub generuje dynamiczny SVG pokazujący Twoją serię przetrwania, wyeliminowane zombie (commity) i rangę taktyczną.",
        "how_to": "🚀 Jak Używać",
        "step1": "1. Utwórz Workflow",
        "step1_desc": "Utwórz nowy plik w swoim repozytorium pod adresem <code>.github/workflows/zombie-graph.yml</code> i dodaj następujący kod:",
        "warning_title": "⚠️ Ważna Uwaga",
        "warning_desc": "Upewnij się, że Twoje repozytorium zezwala Actions na odczyt i zapis. Przejdź do <strong>Settings > Actions > General</strong>, przewiń do <strong>Workflow permissions</strong> i wybierz <strong>\"Read and write permissions\"</strong>.",
        "step2": "2. Zaktualizuj README",
        "step2_desc": "Dodaj wygenerowany plik SVG do <code>README.md</code> w swoim profilu:"
    }
]

yaml_code = """<span class="keyword">name</span>: GitHub Zombie Survival Graph

<span class="keyword">on</span>:
  <span class="keyword">schedule</span>:
    - <span class="keyword">cron</span>: <span class="string">"0 0 * * *"</span> <span class="comment"># Runs automatically every midnight</span>
  <span class="keyword">workflow_dispatch</span>: <span class="comment"># Allows manual trigger</span>

<span class="keyword">jobs</span>:
  <span class="keyword">build</span>:
    <span class="keyword">runs-on</span>: ubuntu-latest
    <span class="keyword">permissions</span>:
      <span class="keyword">contents</span>: write

    <span class="keyword">steps</span>:
      - <span class="keyword">name</span>: Checkout Repository
        <span class="keyword">uses</span>: actions/checkout@v4

      - <span class="keyword">name</span>: Generate Zombie Survival Graph
        <span class="keyword">uses</span>: achexus/github-zombie-graph@main
        <span class="keyword">with</span>:
          <span class="keyword">github_token</span>: <span class="variable">${{ secrets.GITHUB_TOKEN }}</span>

      - <span class="keyword">name</span>: Commit and Push the generated SVG
        <span class="keyword">uses</span>: stefanzweifel/git-auto-commit-action@v5
        <span class="keyword">with</span>:
          <span class="keyword">commit_message</span>: <span class="string">"Update GitHub Zombie Survival Graph"</span>
          <span class="keyword">file_pattern</span>: zombie-graph.svg
"""

html_code = """&lt;div align=<span class="string">"center"</span>&gt;
  &lt;img src=<span class="string">"zombie-graph.svg"</span> alt=<span class="string">"My Zombie Survival Status"</span> /&gt;
&lt;/div&gt;"""

for item in languages_data:
    html_content += f"""
    <h2 id="{item['lang'].lower()}">{item['flag']} {item['lang']}</h2>
    <p>{item['desc']}</p>
    
    <h3>{item['how_to']}</h3>
    
    <p><strong>{item['step1']}</strong></p>
    <p>{item['step1_desc']}</p>
    
    <div class="code-block">{yaml_code}</div>
    
    <div class="warning">
        <strong>{item['warning_title']}:</strong> {item['warning_desc']}
    </div>
    
    <p><strong>{item['step2']}</strong></p>
    <p>{item['step2_desc']}</p>
    
    <div class="code-block">{html_code}</div>
    
    <hr class="section-divider">
    """

html_content += """
</body>
</html>
"""

with open("readme_template.html", "w", encoding="utf-8") as f:
    f.write(html_content)

HTML("readme_template.html").write_pdf("zombie_graph_readme_10_languages.pdf")
print("[file-tag: zombie_graph_readme_10_languages.pdf]")
